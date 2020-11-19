import numpy as np 
import pandas as pd
from Lib import plotting as pt

grid = pd.DataFrame(columns=["Long", "Lat", "Type", "Color", "Size"])
grid = grid.astype({"Long": float, 
                    "Lat": float, 
                    "Type": str, 
                    "Color": str, 
                    "Size": float,
                    })
grid.loc["nodeA"] = [15, 55.1, "60kV Station", "Orange", 50]
grid.loc["nodeB"] = [14.7, 55.2, "60kV Station", "Orange", 50]
grid.loc["nodeC"] = [15.1, 55.2, "60kV Station", "Orange", 50]

grid_conn = pd.DataFrame(columns=["conn1", "conn2", "Cap", "time", "Load"])
grid_conn = grid_conn.astype({"conn1": str, 
                              "conn2": str, 
                              "Cap": float, 
                              "time": int, 
                              "Load": float,
                              })

grid_conn.loc[1] = ["nodeA", "nodeB", 100, 0, 70]
grid_conn.loc[2] = ["nodeA", "nodeC", 100, 0, 110]
grid_conn.loc[3] = ["nodeB", "nodeC", 100, 0, -70]
grid_conn.loc[4] = ["nodeA", "nodeB", 100, 1, 0]
grid_conn.loc[5] = ["nodeA", "nodeC", 100, 1, 50]
grid_conn.loc[6] = ["nodeB", "nodeC", 100, 1, -35]
grid_conn.loc[7] = ["nodeA", "nodeB", 100, 2, 105]
grid_conn.loc[8] = ["nodeA", "nodeC", 100, 2, 97]
grid_conn.loc[9] = ["nodeB", "nodeC", 100, 2, -98]


outpath = "./plots/"
fnamebase = "test"

c=pt.netgif()
c.plot_series(grid, grid_conn, outpath, fnamebase)




# for index, row in EV.iterrows():
#     longEV, latEV = row[["Long", "Lat"]].to_numpy()
#     longGrid, latGrid = grid.loc[row["grid"], ["Long", "Lat"]].to_numpy()
#     plt.plot(np.array([longEV, longGrid]),
#              np.array([latEV, latGrid]),
#              transform=ccrs.PlateCarree(),
#              marker="", color="blue"
#              )
    
# plt.plot(EV["Long"].to_numpy(), EV["Lat"].to_numpy(), 
#          transform=ccrs.PlateCarree(), marker="o", color="Blue", 
#          markersize=9, linestyle='')



