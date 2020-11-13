import numpy as np 
import pandas as pd
import networkx as nx
import matplotlib as mpl        
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM


plt.close('all')

# extend of Bronholm in Geodetic Coordinates
extent = [14.65, 15.2, 54.97, 55.31]


fig = plt.figure(figsize=[6, 6])

# plot open street map data
request = OSM()
ax = plt.axes(projection=request.crs)
ax.set_extent(extent)
ax.add_image(request, 10)  # zoom level 10

grid = pd.DataFrame(columns=["Long", "Lat", "Type", "Color", "Size"])
grid.loc["nodeA"] = [15, 55.1, "60kV Station", "Orange", 9]
grid.loc["nodeB"] = [14.7, 55.2, "60kV Station", "Orange", 9]

grid_conn = pd.DataFrame(columns=["conn1", "conn2"])
grid_conn = grid_conn.append({"conn1":"nodeA", "conn2":"nodeB"}, ignore_index=True)

EV = pd.DataFrame(columns=["Long", "Lat", "Type", "Color", "Size", "grid", "time"])
EV.loc["EV_1"] = [15.1, 55.15, "Car", "Blue", 9, "nodeA", 0]
EV.loc["EV_2"] = [14.9, 55.2, "Car", "Blue", 9, "nodeA",  0]
EV.loc["EV_3"] = [14.75, 55.1, "Car", "Blue", 9, "nodeB",  0]

plt.plot(grid["Long"].to_numpy(), grid["Lat"].to_numpy(), 
         transform=ccrs.PlateCarree(), marker="o", color="Orange", 
         markersize=9, linestyle='')

for index, row in grid_conn.iterrows():
    long, lat = grid.loc[[row["conn1"], row["conn2"]], ["Long", "Lat"]].to_numpy().T
    plt.plot(long, lat, transform=ccrs.PlateCarree(), marker="", color="Orange")
    
for index, row in EV.iterrows():
    longEV, latEV = row[["Long", "Lat"]].to_numpy()
    longGrid, latGrid = grid.loc[row["grid"], ["Long", "Lat"]].to_numpy()
    plt.plot(np.array([longEV, longGrid]),
             np.array([latEV, latGrid]),
             transform=ccrs.PlateCarree(),
             marker="", color="blue"
             )
    
plt.plot(EV["Long"].to_numpy(), EV["Lat"].to_numpy(), 
         transform=ccrs.PlateCarree(), marker="o", color="Blue", 
         markersize=9, linestyle='')


#plt.show()


