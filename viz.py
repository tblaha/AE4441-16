import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Lib.cars import car_stat, cars_data, grid
from Lib import plotting as pt

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

grid_conn.loc[1] = ["Ronne", "Nexo", 100, 0, 70]
grid_conn.loc[2] = ["Ronne", "Tejn", 100, 0, 110]
grid_conn.loc[3] = ["Nexo", "Tejn", 100, 0, -70]
grid_conn.loc[4] = ["Ronne", "Nexo", 100, 1, 0]
grid_conn.loc[5] = ["Ronne", "Tejn", 100, 1, 50]
grid_conn.loc[6] = ["Nexo", "Tejn", 100, 1, -35]
grid_conn.loc[7] = ["Ronne", "Nexo", 100, 2, 105]
grid_conn.loc[8] = ["Ronne", "Tejn", 100, 2, 97]
grid_conn.loc[9] = ["Nexo", "Tejn", 100, 2, 98]

cars_data["Color"] = "Blue"
cars_data["Size"] = 30

outpath = "./plots/"
fnamebase = "test"

c=pt.netgif([14.65, 15.2, 54.97, 55.31], 10)
# c=pt.netgif([14.65, 14.75, 55.175, 55.225], 13)
c.plot_series(grid, grid_conn, cars_data, outpath, fnamebase)

plt.close("all")

