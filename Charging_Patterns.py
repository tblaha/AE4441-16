#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:04:58 2020

@author: tblaha
"""

from matplotlib import pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as hac
import seaborn as sns
import numpy as np

# from complex import cars_data, cars

a=cars_data.groupby(["CarId", "Time"])["Load"].sum().unstack(level=0)

boolarr=a.apply(lambda x: sum(abs(x))) > 1e-6

ts_usable = a.loc[:, boolarr]

Z=hac.linkage(ts_usable.T, method='ward', metric='euclidean')
#Z=hac.linkage(ts_usable.T, method='average', metric='correlation')
#Z=hac.linkage(ts_usable.T, method='centroid', metric='euclidean')

#%%
figD = plt.figure(figsize=(8, 5))
plt.title('Truncated Hierarchical Clustering Dendrogram')
plt.xlabel('Cars', fontsize=22)
plt.ylabel('Euclidean Distance', fontsize=18)
hac.dendrogram(
    Z,
    #leaf_rotation=0.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
    truncate_mode='level',
    p=5,
    color_threshold=200,
)
plt.title("")
#figD.axes[0].set_xticks([])
plt.show()

#%%


results = hac.fcluster(Z, 3, criterion='maxclust')
clusters = np.unique(results)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
fig2, ax2 = plt.subplots(1, 1, figsize=(8, 6))
fig3, ax3 = plt.subplots(1, 1, figsize=(8, 6))

cluster_attribs = pd.DataFrame()

lss = ["-", "--", "-.", ":", "-"]
ts_reset = ts_usable.stack(level=-1).reset_index()
for i in np.unique(results):
    boolarr = np.in1d(ts_reset["CarId"], np.where(results==i))
    sns.lineplot(ax=ax,
                 x=ts_reset.loc[boolarr, "Time"],
                 y=ts_reset.loc[boolarr, 0],
                 ci="quantile",
                 lw=2,
                 ls=lss[i-1],
                 label="Cluster "+str(i)+", Members: "+str(sum(results==i)),
                 )
    sns.lineplot(ax=ax,
                 x=ts_reset.loc[boolarr, "Time"],
                 y=ts_reset.loc[boolarr, 0],
                 ci=95,
                 lw=0,
                 err_style='bars',
                 ls=lss[i-1],
                 label=None,
                 )
    attrb = cars_data.loc[np.in1d(cars_data["CarId"],
                                np.where(results==i)
                                )
                        ].groupby(["Time", "Car Type"])["CarId"].size().loc[0]
    cluster_attribs.loc[i, attrb.index] \
        = attrb
    
    E_start = np.array([
        cars[ts_usable.columns[np.where(results==i)][j]].E_state
        for j in range(sum(results==i))
        ])
    
    E_bat = np.array([
        cars[ts_usable.columns[np.where(results==i)][j]].E_bat
        for j in range(sum(results==i))
        ])
    
    E_bat = (E_start + ts_usable.iloc[:, np.where(results==i)[0]].cumsum()) / E_bat * 100
    E_bat_stack = E_bat.copy().stack(level=-1).reset_index()
    
    sns.lineplot(ax=ax3,
                  x=E_bat_stack["Time"],
                  y=E_bat_stack[0],
                  ci='quantile',
                  estimator='mean',
                  #n_boot=len(E_bat_stack[0]),
                  err_style="band",
                  lw=2,
                  ls=lss[i-1],
                  label="Cluster "+str(i)+", Members: "+str(sum(results==i)),
                  )
    sns.lineplot(ax=ax3,
                  x=E_bat_stack["Time"],
                  y=E_bat_stack[0],
                  ci=95,
                  estimator='mean',
                  #n_boot=len(E_bat_stack[0]),
                  err_style="bars",
                  lw=0,
                  ls=lss[i-1],
                  label=None,
                  )
    
    


cluster_attribs.plot(kind='bar', stacked=True, ax=ax2)
ax2.set_xlabel("Cluster #", fontsize=16)
ax2.set_ylabel("# of cars", fontsize=16)
ax2.legend(fontsize=14)


ct = cars_data.loc[cars_data["CarId"] == 0, "Charger type"].to_numpy()
cp = cars_data.loc[cars_data["CarId"] == 0, "Charger Power"].to_numpy()
r = np.arange(cfg.K)
first_non_home = r[ct != ct[0]][0]
last_non_home  = r[ct != ct[0]][-1]

aprops=dict(arrowstyle='<->', mutation_scale=20)
xy_s = [cfg.t[0],
        cfg.t[first_non_home-1],
        cfg.t[last_non_home],
        cfg.t[-1]
        ]
texts = ["Home", "Work", "Home"]

for axis, y_coord in zip([ax, ax3], [4, 30]):

    for i in range(len(xy_s)-1):
        axis.annotate(text='',
                     xytext=(xy_s[i],y_coord),
                     xy=(xy_s[i+1],y_coord),
                     arrowprops=aprops,
                     )
        axis.annotate(text=texts[i],
                     xy=(0,0),
                     xytext=(0.5*xy_s[i]+0.5*xy_s[i+1],
                             y_coord*1.075),
                     ha='center',
                     fontsize=14,
                     )
    
    #ax.set_ylim(bottom=-10, top=6)
    axis.set_xlim(left=0, right=24)
    
    axis.set_xlabel("Time [h]", fontsize=16)
    axis.grid()
    axis.legend(loc="lower left", fontsize=14)



ax.set_ylabel("Charging Power [kW]", fontsize=16)
ax3.set_ylabel("Battery Energy [%]", fontsize=16)
ax3.set_ylim(bottom=0, top=100)
