#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:19:54 2020

@author: tblaha
"""

import pandas as pd
import numpy as np
import imageio as io
 
import matplotlib as mpl
import matplotlib.pyplot as plt 
import matplotlib.animation as ani

import cartopy.crs as ccrs
from cartopy.io.img_tiles import GoogleTiles

from Lib import SimConfig as cfg


class netgif():
    def __init__(self, extend, zoom):
        
        # characteristics
        self.extent = extend
        self.zoomlevel = zoom
        self.figsize = [12, 9]
        
        # make basic figure size
        self.fig = plt.figure(figsize=self.figsize)
        
        # get and plot the Open Streetmap data
        request = GoogleTiles()
        self.ax = plt.axes(projection=request.crs)
        self.ax.set_extent(self.extent)
        self.ax.add_image(request, self.zoomlevel)  # zoom level 10
        
    
    
    def plot_series(self, grid, grid_links, cars_data, pp_data, cons_data, outpath, fnamebase):
        self.grid = grid
        
        # colormapping
        self.cmap = plt.cm.jet
        self.norm = mpl.colors.Normalize(vmin=-110, vmax=110)
        
        # add grid
        self._add_grid()
        
        # max capacity for each car and powerplant when aggregated over the day
        car_caps = cars_data.groupby(["CarId"])["Cap"].max()
        pp_caps  = pp_data.groupby(["Name"])["Cap"].max()
        
        # iterate over discrete times k
        # k_array = np.unique(grid_links["Time"])
        k_array = np.arange(cfg.K)
        times = np.zeros(cfg.K+1)
        times[1:] = np.cumsum(cfg.dt)
        times2 = np.roll(times, -1)
        with io.get_writer(outpath+"/"+fnamebase+".gif", # this sets up the gif
                           mode='I', 
                           duration=1.5
                           ) as writer:
            
            for j in k_array:
                
                # add the meat of the plot
                self._add_links(grid_links.loc[grid_links["Time"] == j, :])
                self._add_cars(cars_data.loc[cars_data["Time"] == j, :],
                               car_caps)
                self._add_pp(pp_data.loc[pp_data["Time"] == j, :],
                             pp_caps)
                self._add_cons(cons_data.loc[cons_data["Time"] == j, :])
                
                # make colorbar
                self.cb = plt.colorbar(self.grid_quivers)
                self.cb.set_label("% Load", fontsize=16)
                
                # make legend
                self._make_legend(grid, grid_links, cars_data, pp_data, cons_data)
                
                # make title
                plt.title("Network at " + str(times[j]) 
                                 + "h to " + str(times2[j]) + "h",
                          fontsize=18)
                
                
                # save file as png graphics
                filename = outpath + "/" + fnamebase + '_' + str(j) + '.png'
                plt.savefig(filename, 
                            format='png', 
                            )
                
                # open again as image and append it to the gif
                writer.append_data(io.imread(filename, format='png'))
                
                # clean the plot up so that only the OSM and the grid nodes 
                # remain
                self._clean_plot()
        
    def _make_legend(self):
        # official matplotlib beun to get custom legends...
        # https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/custom_legends.html
        custom_lines = [
            mpl.lines.Line2D([0], [0],
                             marker="*",
                             markersize=15,
                             linestyle="",
                             linewidth=1,
                             color="Purple",
                             # edgecolor="black",
                             label="Consumers"
                             )
            ]
        
        # add cars as tiny dots!
        self.legend = self.fig.legend(handles=custom_lines)
        
            
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
        assert((np.abs(load) <= cap+1e-2).all())
        pload = np.zeros(len(load))
        cap_pos = cap > 0
        pload[cap_pos] = [100*p/c for (p, c) in zip(load[cap_pos], cap[cap_pos])]
        
        
        return x1, y1, u, v, pload
    
        
        
    def _add_links(self, grid_links):
        
        grid = self.grid
        
        x1, y1 = grid.loc[grid_links["conn1"], ["Long", "Lat"]].to_numpy().T
        x2, y2 = grid.loc[grid_links["conn2"], ["Long", "Lat"]].to_numpy().T
        cap = grid_links["Cap"].to_numpy()
        load = grid_links["Load"].to_numpy()
        
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
    
    
    
    def _add_cars(self, EV, caps):
        
        grid = self.grid
        
        x1, y1 = grid.loc[EV["GridConn"], ["Long", "Lat"]].to_numpy().T
        x2, y2 = EV[["Long", "Lat"]].to_numpy().T
        cap = caps[EV["CarId"]].to_numpy()
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
                                           width=0.0025,
                                           headwidth=10,
                                           headlength=14,
                                           transform=ccrs.PlateCarree(), 
                                           cmap=self.cmap,
                                           norm=self.norm,
                                           )
        
        
        
    def _add_pp(self, pp_data, caps):
        
        grid = self.grid
        
        x1, y1 = pp_data[["Long", "Lat"]].to_numpy().T       
        x2, y2 = grid.loc[pp_data["GridConn"], ["Long", "Lat"]].to_numpy().T

        cap = caps[pp_data["Name"]].to_numpy()
        load = pp_data["Load"].to_numpy()
        
        x, y, u, v, pload = self._process_arrows(x1, y1, x2, y2, cap, load)
        
        self.pp_scatter = \
            self.ax.scatter(pp_data["Long"].to_numpy(), 
                            pp_data["Lat"].to_numpy(), 
                            s=pp_data["Size"].to_numpy(),
                            c=pp_data["Color"],
                            transform=ccrs.PlateCarree(), 
                            marker="s",
                            linewidths=1,
                            edgecolors="black"
                            )
        
        self.pp_quivers   = self.ax.quiver(x,
                                           y,
                                           u,
                                           v,
                                           pload,
                                           angles='xy',
                                           scale_units='xy',
                                           scale=8.98*1e-6,
                                           width=0.005,
                                           linewidth=0.5,
                                           transform=ccrs.PlateCarree(), 
                                           cmap=self.cmap,
                                           norm=self.norm,
                                           )
        
    def _add_cons(self, cons_data):
        
        grid = self.grid
        
        x1, y1 = grid.loc[cons_data["GridConn"], ["Long", "Lat"]].to_numpy().T
        x2, y2 = cons_data[["Long", "Lat"]].to_numpy().T
        
        peak = cons_data["Peak"].to_numpy()
        load = cons_data["Load"].to_numpy()
        
        x, y, u, v, pload = self._process_arrows(x1, y1, x2, y2, peak, load)
        
        self.cons_scatter = \
            self.ax.scatter(cons_data["Long"].to_numpy(), 
                            cons_data["Lat"].to_numpy(), 
                            s=cons_data["Size"].to_numpy(),
                            c=cons_data["Color"],
                            transform=ccrs.PlateCarree(), 
                            marker="*",
                            linewidths=1,
                            edgecolors="black"
                            )
        
        self.cons_quivers = self.ax.quiver(x,
                                           y,
                                           u,
                                           v,
                                           pload,
                                           angles='xy',
                                           scale_units='xy',
                                           scale=8.98*1e-6,
                                           width=0.005,
                                           linewidth=0.5,
                                           transform=ccrs.PlateCarree(), 
                                           cmap=self.cmap,
                                           norm=self.norm,
                                           )
        
    def _clean_plot(self):
        self.cb.remove()
        self.grid_quivers.remove()
        self.car_quivers.remove()
        self.pp_scatter.remove()
        self.pp_quivers.remove()
        self.cons_scatter.remove()
        self.cons_quivers.remove()
        self.legend.remove()

        

    def __del__(self):
        import matplotlib.pyplot as plt   #bbbbeunfix
        plt.close(self.fig)
        





