import numpy as np

import pandas as pd
from Lib import plotting as pt
import matplotlib.pyplot as plt 

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

grid_conn = pd.DataFrame(columns=["conn1",
                                  "conn2", 
                                  "Cap",
                                  "time",
                                  "Load"]
                         )
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


EV = pd.DataFrame(columns=["Long", 
                           "Lat", 
                           "Type", 
                           "Color", 
                           "Size", 
                           "Cap",
                           "time", 
                           "grid", 
                           "Load", 
                           ])
EV = EV.astype({"Long": float, 
                "Lat": float,
                "Type": str,
                "Color": str,
                "Size": float,
                "Cap": float,
                "time": int,
                "grid": str,
                "Load": float,
                })

EV.loc["EV_1_0"] = [15.10, 55.15, "Car", "Blue", 30, 11, 0, "nodeA", 5]
EV.loc["EV_2_0"] = [14.90, 55.22, "Car", "Blue", 30, 11, 0, "nodeA", 0]
EV.loc["EV_3_0"] = [14.75, 55.10, "Car", "Blue", 30, 11, 0, "nodeB", -11]
EV.loc["EV_1_1"] = [15.10, 55.15, "Car", "Blue", 30, 11, 1, "nodeA", -5]
EV.loc["EV_2_1"] = [14.90, 55.22, "Car", "Blue", 30, 11, 1, "nodeA", 0]
EV.loc["EV_3_1"] = [14.75, 55.10, "Car", "Blue", 30, 11, 1, "nodeB", 11]
EV.loc["EV_1_2"] = [15.10, 55.15, "Car", "Blue", 30, 11, 2, "nodeA", 0]
EV.loc["EV_2_2"] = [14.90, 55.22, "Car", "Blue", 30, 11, 2, "nodeA", 5]
EV.loc["EV_3_2"] = [14.75, 55.10, "Car", "Blue", 30, 11, 2, "nodeB", 9]



outpath = "./plots/"
fnamebase = "test"

c=pt.netgif([14.65, 15.2, 54.97, 55.31], 10)
# c=pt.netgif([14.65, 14.75, 55.175, 55.225], 13)
c.plot_series(grid, grid_conn, EV, outpath, fnamebase)

plt.close("all")




# for index, row in EV.iterrows():
#     longEV, latEV = row[["Long", "Lat"]].to_numpy()
#     longGrid, latGrid = grid.loc[row["grid"], ["Long", "Lat"]].to_numpy()
#     plt.plot(np.array([longEV, longGrid]),
#               np.array([latEV, latGrid]),
#               transform=ccrs.PlateCarree(),
#               marker="", color="blue"
#               )
    
# plt.plot(EV["Long"].to_numpy(), EV["Lat"].to_numpy(), 
#          transform=ccrs.PlateCarree(), marker="o", color="Blue", 
#          markersize=9, linestyle='')



