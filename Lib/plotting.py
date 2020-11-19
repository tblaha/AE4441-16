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
    def __init__(self):
        
        # characteristics
        self.extent = [14.65, 15.2, 54.97, 55.31]
        self.zoomlevel = 10
        self.figsize = [12, 9]
        
        # make basic figure size
        self.fig = plt.figure(figsize=self.figsize)
        
        # get and plot the Open Streetmap data
        request = OSM()
        self.ax = plt.axes(projection=request.crs)
        self.ax.set_extent(self.extent)
        self.ax.add_image(request, self.zoomlevel)  # zoom level 10
        
    
    
    def plot_series(self, grid, grid_conn, outpath, fnamebase):
        self.grid = grid
        
        self._add_grid()
        
        
        k_array = np.unique(grid_conn["time"])
        with io.get_writer(outpath+"/"+fnamebase+".gif", 
                           mode='I', 
                           duration=1.5
                           ) as writer:
            
            for k in k_array:
                # add the meat of the plot
                self._add_links(grid_conn.loc[grid_conn["time"] == k, :])
                
                filename = outpath + "/" + fnamebase + '_' + str(k) + '.eps'
                plt.savefig(filename, 
                            format='eps', 
                            )
                
                writer.append_data(io.imread(filename, format='eps'))
                
                
                # clean the plot up so that only the OSM and the grid nodes remain
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
        
        x, y = grid.loc[grid_conn["conn1"], ["Long", "Lat"]].to_numpy().T
        xpu, ypv = grid.loc[grid_conn["conn2"], ["Long", "Lat"]].to_numpy().T
        
        
        idx_flip = 1-(grid_conn["Load"] >= 0).to_numpy()
        
        for i, b in enumerate(idx_flip):
            if b:
                (x[i], y[i], xpu[i], ypv[i]) = (xpu[i], ypv[i], x[i], y[i])
        
        u = xpu - x
        v = ypv - y
        
        phi = np.arctan2(v, u)
        sf = 1 + 0.78*(np.sin(phi))**(1.8)
        
        
        pload = 100 * (np.abs(grid_conn["Load"]) / grid_conn["Cap"]).to_numpy()
        
        
        # colorbar
        self.cmap = plt.cm.jet
        self.norm = mpl.colors.Normalize(vmin=0, vmax=max(110, np.max(pload)))
        
        self.grid_quivers = self.ax.quiver(x,
                                           y,
                                           u*sf,
                                           v*sf,
                                           pload,
                                           angles='xy',
                                           scale_units='xy',
                                           scale=8.98*1e-6,
                                           linewidth=1,
                                           transform=ccrs.PlateCarree(), 
                                           cmap=self.cmap,
                                           norm=self.norm,
                                           )
        self.cb = plt.colorbar(self.grid_quivers)
        self.cb.set_label("% Load")
        
        
        
    def _clean_plot(self):
        self.cb.remove()
        self.grid_quivers.remove()

        

    def __del__(self):
        import matplotlib.pyplot as plt   #bbbbeunfix
        plt.close(self.fig)
        





