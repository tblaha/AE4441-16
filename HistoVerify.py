#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:10:24 2020

@author: tblaha
"""

import matplotlib.pyplot as plt

#%% Driven distance + Battery size


fig4, ax4 = plt.subplots(1,1,figsize=(10, 6))
ax4.scatter(np.arange(0, 150, 5),
            np.cumsum(np.array([4,7,12,11,11,9,10,6,5,3,4,2,3,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0]))/100,
            label="Driven Distance",
            color="blue",
            )
ax4.hist([cars[i].s_day for i in range(len(cars))],
         bins=35,
         density=True,
         cumulative=True,
         histtype='step',
         color="blue",
         lw=2,
         )


ax4.scatter([32,39.2,47.5,52,64.7],
            np.cumsum(np.array([16,12,28,32,12]))/100,
            label="Battery Size",
            color="orange",
            )
ax4.hist([cars[i].E_bat for i in range(len(cars))],
         bins=15,
         density=True,
         cumulative=True,
         histtype='step',
         color="orange",
         lw=2,
         )

ax4.scatter([190,255,280,315,320],
            np.cumsum(np.array([16,12,12,32,28]))/100,
            label="Range",
            color="green",
            )
ax4.hist([a.E_bat/a.E_eff for a in cars],
         bins=15,
         density=True,
         cumulative=True,
         histtype='step',
         color="green",
         lw=2,
         )

plt.legend(loc="lower right", fontsize=14)
ax4.set_xlim(right=350)
#ax4.grid()
ax4.set_xlabel("Distance, Bat Size, Range", fontsize=16)
ax4.set_ylabel("Cumulative Distribution", fontsize=16)
plt.show()