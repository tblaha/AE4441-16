\ Model Advanced Model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  8 P_Biomass_0 + 8 P_Biomass_1 + 8 P_Biomass_2 + 8 P_WindWest_0
   + 8 P_WindWest_1 + 8 P_WindWest_2 + 16 P_Cable_0 + 16 P_Cable_1
   + 16 P_Cable_2 + 8 P_SolarWest_0 + 8 P_SolarWest_1 + 8 P_SolarWest_2
Subject To
 C_Pub_0_0: X_0_0 - 41 Y_0_0_0 - 41 Y_0_0_1 - 22 Y_0_0_2 - 7.4 Y_0_0_3
   <= 0
 C_Plb_0_0: X_0_0 + 41 Y_0_0_0 + 41 Y_0_0_1 + 22 Y_0_0_2 + 7.4 Y_0_0_3
   >= 0
 C_OOOMa_0_0: Y_0_0_3 = 1
 C_OOOMb_0_0: Y_0_0_0 + Y_0_0_1 + Y_0_0_2 = 0
 C_Pub_0_1: X_0_1 - 41 Y_0_1_0 - 41 Y_0_1_1 - 22 Y_0_1_2 - 7.4 Y_0_1_3
   <= 0
 C_Plb_0_1: X_0_1 + 41 Y_0_1_0 + 41 Y_0_1_1 + 22 Y_0_1_2 + 7.4 Y_0_1_3
   >= 0
 C_OOOM_0_1: Y_0_1_0 + Y_0_1_1 + Y_0_1_2 + Y_0_1_3 = 0
 C_Pub_0_2: X_0_2 - 41 Y_0_2_0 - 41 Y_0_2_1 - 22 Y_0_2_2 - 7.4 Y_0_2_3
   <= 0
 C_Plb_0_2: X_0_2 + 41 Y_0_2_0 + 41 Y_0_2_1 + 22 Y_0_2_2 + 7.4 Y_0_2_3
   >= 0
 C_OOOMa_0_2: Y_0_2_3 = 1
 C_OOOMb_0_2: Y_0_2_0 + Y_0_2_1 + Y_0_2_2 = 0
 C_Enet_0: 8 X_0_0 + 8 X_0_1 + 8 X_0_2 >= 3.301587301587301
 C_Elb_0_0: 8 X_0_0 >= -20.8
 C_Eub_0_0: 8 X_0_0 <= 20.8
 C_Elb_0_1: 8 X_0_0 + 8 X_0_1 >= -20.8
 C_Eub_0_1: 8 X_0_0 + 8 X_0_1 <= 20.8
 C_Pub_1_0: X_1_0 - 41 Y_1_0_0 - 41 Y_1_0_1 - 22 Y_1_0_2 - 7.4 Y_1_0_3
   <= 0
 C_Plb_1_0: X_1_0 + 41 Y_1_0_0 + 41 Y_1_0_1 + 22 Y_1_0_2 + 7.4 Y_1_0_3
   >= 0
 C_OOOMa_1_0: Y_1_0_3 = 1
 C_OOOMb_1_0: Y_1_0_0 + Y_1_0_1 + Y_1_0_2 = 0
 C_Pub_1_1: X_1_1 - 41 Y_1_1_0 - 41 Y_1_1_1 - 22 Y_1_1_2 - 7.4 Y_1_1_3
   <= 0
 C_Plb_1_1: X_1_1 + 41 Y_1_1_0 + 41 Y_1_1_1 + 22 Y_1_1_2 + 7.4 Y_1_1_3
   >= 0
 C_OOOM_1_1: Y_1_1_0 + Y_1_1_1 + Y_1_1_2 + Y_1_1_3 <= 1
 C_Pub_1_2: X_1_2 - 41 Y_1_2_0 - 41 Y_1_2_1 - 22 Y_1_2_2 - 7.4 Y_1_2_3
   <= 0
 C_Plb_1_2: X_1_2 + 41 Y_1_2_0 + 41 Y_1_2_1 + 22 Y_1_2_2 + 7.4 Y_1_2_3
   >= 0
 C_OOOMa_1_2: Y_1_2_3 = 1
 C_OOOMb_1_2: Y_1_2_0 + Y_1_2_1 + Y_1_2_2 = 0
 C_Enet_1: 8 X_1_0 + 8 X_1_1 + 8 X_1_2 >= 0
 C_Elb_1_0: 8 X_1_0 >= -20.8
 C_Eub_1_0: 8 X_1_0 <= 20.8
 C_Elb_1_1: 8 X_1_0 + 8 X_1_1 >= -20.8
 C_Eub_1_1: 8 X_1_0 + 8 X_1_1 <= 20.8
 C_Pub_2_0: X_2_0 - 105 Y_2_0_0 - 45 Y_2_0_1 - 11 Y_2_0_2 - 7.4 Y_2_0_3
   <= 0
 C_Plb_2_0: X_2_0 + 105 Y_2_0_0 + 45 Y_2_0_1 + 11 Y_2_0_2 + 7.4 Y_2_0_3
   >= 0
 C_OOOM_2_0: Y_2_0_0 + Y_2_0_1 + Y_2_0_2 + Y_2_0_3 = 0
 C_Pub_2_1: X_2_1 - 105 Y_2_1_0 - 45 Y_2_1_1 - 11 Y_2_1_2 - 7.4 Y_2_1_3
   <= 0
 C_Plb_2_1: X_2_1 + 105 Y_2_1_0 + 45 Y_2_1_1 + 11 Y_2_1_2 + 7.4 Y_2_1_3
   >= 0
 C_OOOM_2_1: Y_2_1_0 + Y_2_1_1 + Y_2_1_2 + Y_2_1_3 <= 1
 C_Pub_2_2: X_2_2 - 105 Y_2_2_0 - 45 Y_2_2_1 - 11 Y_2_2_2 - 7.4 Y_2_2_3
   <= 0
 C_Plb_2_2: X_2_2 + 105 Y_2_2_0 + 45 Y_2_2_1 + 11 Y_2_2_2 + 7.4 Y_2_2_3
   >= 0
 C_OOOM_2_2: Y_2_2_0 + Y_2_2_1 + Y_2_2_2 + Y_2_2_3 = 0
 C_Enet_2: 8 X_2_0 + 8 X_2_1 + 8 X_2_2 >= 4.453125
 C_Elb_2_0: 8 X_2_0 >= -19
 C_Eub_2_0: 8 X_2_0 <= 19
 C_Elb_2_1: 8 X_2_0 + 8 X_2_1 >= -19
 C_Eub_2_1: 8 X_2_0 + 8 X_2_1 <= 19
 C_numCh_1_0: Y_1_1_0 + Y_2_1_0 <= 1
 C_numCh_1_1: Y_1_1_1 + Y_2_1_1 <= 1
 C_numCh_1_2: Y_1_1_2 + Y_2_1_2 <= 1
 C_numCh_1_3: Y_1_1_3 + Y_2_1_3 <= 1
 C_nodal_Ronne_0: - X_0_0 - X_1_0 - X_2_0 + P_Biomass_0 + P_WindWest_0
   + P_Cable_0 + P_SolarWest_0 = 21440.6779661017
 C_nodal_Ronne_1: - X_0_1 - X_1_1 - X_2_1 + P_Biomass_1 + P_WindWest_1
   + P_Cable_1 + P_SolarWest_1 = 32161.01694915254
 C_nodal_Ronne_2: - X_0_2 - X_1_2 - X_2_2 + P_Biomass_2 + P_WindWest_2
   + P_Cable_2 + P_SolarWest_2 = 32288.13559322034
Bounds
 X_0_0 free
 X_0_1 free
 X_0_2 free
 X_1_0 free
 X_1_1 free
 X_1_2 free
 X_2_0 free
 X_2_1 free
 X_2_2 free
 P_Biomass_0 <= 15000
 P_Biomass_1 <= 15000
 P_Biomass_2 <= 15000
 P_WindWest_0 <= 19049.45002093224
 P_WindWest_1 <= 13490.8325190203
 P_WindWest_2 <= 20000
 -30000 <= P_Cable_0 <= 30000
 -30000 <= P_Cable_1 <= 30000
 -30000 <= P_Cable_2 <= 30000
 P_SolarWest_0 = 0
 P_SolarWest_1 <= 5000
 P_SolarWest_2 = 0
Binaries
 Y_0_0_0 Y_0_0_1 Y_0_0_2 Y_0_0_3 Y_0_1_0 Y_0_1_1 Y_0_1_2 Y_0_1_3 Y_0_2_0
 Y_0_2_1 Y_0_2_2 Y_0_2_3 Y_1_0_0 Y_1_0_1 Y_1_0_2 Y_1_0_3 Y_1_1_0 Y_1_1_1
 Y_1_1_2 Y_1_1_3 Y_1_2_0 Y_1_2_1 Y_1_2_2 Y_1_2_3 Y_2_0_0 Y_2_0_1 Y_2_0_2
 Y_2_0_3 Y_2_1_0 Y_2_1_1 Y_2_1_2 Y_2_1_3 Y_2_2_0 Y_2_2_1 Y_2_2_2 Y_2_2_3
End
