#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:19:54 2020

@author: tblaha
"""

#% reset python workspace
from IPython import get_ipython
get_ipython().magic('reset -sf')

import pandas as pd
import numpy as np
import imageio as io
 
import matplotlib as mpl
import matplotlib.pyplot as plt 
import matplotlib.animation as ani

import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM


class netgif():
    def __init__(self, extend, zoom):
        
        # characteristics
        self.extent = extend
        self.zoomlevel = zoom
        self.figsize = [12, 9]
        
        # make basic figure size
        self.fig = plt.figure(figsize=self.figsize)
        
        # get and plot the Open Streetmap data
        request = OSM()
        self.ax = plt.axes(projection=request.crs)
        self.ax.set_extent(self.extent)
        self.ax.add_image(request, self.zoomlevel)  # zoom level 10
        
    
    
    def plot_series(self, grid, grid_conn, EVs, outpath, fnamebase):
        self.grid = grid
        
        
        # colormapping
        self.cmap = plt.cm.jet
        self.norm = mpl.colors.Normalize(vmin=0, vmax=110)
        
        # add grid
        self._add_grid()
        
        # iterate over discrete times k
        k_array = np.unique(grid_conn["time"])
        with io.get_writer(outpath+"/"+fnamebase+".gif", # this sets up the gif
                           mode='I', 
                           duration=1.5
                           ) as writer:
            
            for k in k_array:
                
                # add the meat of the plot
                self._add_links(grid_conn.loc[grid_conn["time"] == k, :])
                self._add_cars(EVs.loc[EVs["time"] == k, :])
                
                # make colorbar
                self.cb = plt.colorbar(self.grid_quivers)
                self.cb.set_label("% Load")
                
                # save file as png graphics
                filename = outpath + "/" + fnamebase + '_' + str(k) + '.png'
                plt.savefig(filename, 
                            format='png', 
                            )
                
                # open again as image and append it to the gif
                writer.append_data(io.imread(filename, format='png'))
                
                # clean the plot up so that only the OSM and the grid nodes 
                # remain
                self._clean_plot()
        
        
            
    def _add_grid(self):
        
        grid = self.grid
        
        self.grid_scatter = \
            self.ax.scatter(grid["Long"].to_numpy(), 
                            grid["Lat"].to_numpy(), 
                            s=grid["Size"].to_numpy(),
                            c=grid["Color"],
                            transform=ccrs.PlateCarree(), 
                            marker="o",
                            linewidths=1,
                            edgecolors="black"
                            )
    
        
        
    def _add_links(self, grid_conn):
        
        grid = self.grid
        
        x1, y1 = grid.loc[grid_conn["conn1"], ["Long", "Lat"]].to_numpy().T
        x2, y2 = grid.loc[grid_conn["conn2"], ["Long", "Lat"]].to_numpy().T
        cap = grid_conn["Cap"].to_numpy()
        load = grid_conn["Load"].to_numpy()
        
        x, y, u, v, pload = self._process_arrows(x1, y1, x2, y2, cap, load)
        
        self.grid_quivers = self.ax.quiver(x,
                                           y,
                                           u,
                                           v,
                                           pload,
                                           angles='xy',
                                           scale_units='xy',
                                           scale=8.98*1e-6,
                                           width=0.005,
                                           linewidth=1,
                                           transform=ccrs.PlateCarree(), 
                                           cmap=self.cmap,
                                           norm=self.norm,
                                           )
        
        
    def _process_arrows(self, x1, y1, x2, y2, cap, load):
        
        idx_flip = 1 - (load >= 0).astype(int)
        
        # flip destination/source of arrow based on sign of the load 
        for i, b in enumerate(idx_flip):
            if b:
                (x1[i], y1[i], x2[i], y2[i]) = (x2[i], y2[i], x1[i], y1[i])
        
        # vector coordinates
        u = x2 - x1
        v = y2 - y1
        
        # scale vectors according to some reverse engineering of the shitty 
        # cartopy interface
        phi = np.arctan2(v, u)
        sf = 1 + 0.78*(np.sin(abs(phi)))**(1.8) # scaling factor
        (u, v) = (u * sf, v * sf) 
        
        # percentage load of the link for the colormap:
        pload = 100 * (np.abs(load) / cap)
        
        return x1, y1, u, v, pload
    
    
        
    def _add_cars(self, EV):
        
        grid = self.grid
        
        x1, y1 = grid.loc[EV["GridNode"], ["Long", "Lat"]].to_numpy().T
        x2, y2 = EV[["Long", "Lat"]].to_numpy().T
        cap = EV["Cap"].to_numpy()
        load = EV["Load"].to_numpy()
        
        x, y, u, v, pload = self._process_arrows(x1, y1, x2, y2, cap, load)
        
        self.car_quivers  = self.ax.quiver(x,
                                           y,
                                           u,
                                           v,
                                           pload,
                                           angles='xy',
                                           scale_units='xy',
                                           scale=8.98*1e-6,
                                           linestyle="--",
                                           edgecolor="k",
                                           facecolor='none',
                                           linewidth=1,
                                           width=0.002,
                                           headwidth=10,
                                           headlength=14,
                                           transform=ccrs.PlateCarree(), 
                                           cmap=self.cmap,
                                           norm=self.norm,
                                           )
        
        
        
    def _clean_plot(self):
        self.cb.remove()
        self.grid_quivers.remove()
        self.car_quivers.remove()

        

    def __del__(self):
        import matplotlib.pyplot as plt   #bbbbeunfix
        plt.close(self.fig)
        





