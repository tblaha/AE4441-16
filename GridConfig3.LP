\ Model Advanced Model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  1e-06 L+_0-Ronne-Nexo_0 + 1e-06 L-_0-Ronne-Nexo_0
   + 1e-06 L+_0-Ronne-Nexo_1 + 1e-06 L-_0-Ronne-Nexo_1
   + 1e-06 L+_0-Ronne-Nexo_2 + 1e-06 L-_0-Ronne-Nexo_2
   + 1e-06 L+_1-Ronne-Tejn_0 + 1e-06 L-_1-Ronne-Tejn_0
   + 1e-06 L+_1-Ronne-Tejn_1 + 1e-06 L-_1-Ronne-Tejn_1
   + 1e-06 L+_1-Ronne-Tejn_2 + 1e-06 L-_1-Ronne-Tejn_2
   + 1e-06 L+_2-Nexo-Tejn_0 + 1e-06 L-_2-Nexo-Tejn_0
   + 1e-06 L+_2-Nexo-Tejn_1 + 1e-06 L-_2-Nexo-Tejn_1
   + 1e-06 L+_2-Nexo-Tejn_2 + 1e-06 L-_2-Nexo-Tejn_2 + 8 P_Biomass_0
   + 8 P_Biomass_1 + 8 P_Biomass_2 + 8 P_WindWest_0 + 8 P_WindWest_1
   + 8 P_WindWest_2 + 8 P_WindNorth_0 + 8 P_WindNorth_1 + 8 P_WindNorth_2
   + 8 P_WindEast_0 + 8 P_WindEast_1 + 8 P_WindEast_2 + 8 P_SolarWest_0
   + 8 P_SolarWest_1 + 8 P_SolarWest_2 + 8 P_SolarNorth_0
   + 8 P_SolarNorth_1 + 8 P_SolarNorth_2 + 8 P_SolarEast_0
   + 8 P_SolarEast_1 + 8 P_SolarEast_2 + 16 P_Cable_0 + 16 P_Cable_1
   + 16 P_Cable_2
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
 C_numCh_0_0: <= 1
 C_numCh_1_0: Y_1_1_0 + Y_2_1_0 <= 1
 C_numCh_2_0: <= 1
 C_numCh_0_1: <= 1
 C_numCh_1_1: Y_1_1_1 + Y_2_1_1 <= 1
 C_numCh_2_1: <= 1
 C_numCh_0_2: <= 1
 C_numCh_1_2: Y_1_1_2 + Y_2_1_2 <= 1
 C_numCh_2_2: <= 1
 C_numCh_0_3: <= 1
 C_numCh_1_3: Y_1_1_3 + Y_2_1_3 <= 1
 C_numCh_2_3: <= 1
 C_nodal_Ronne_0: - X_0_0 - L+_0-Ronne-Nexo_0 + L-_0-Ronne-Nexo_0
   - L+_1-Ronne-Tejn_0 + L-_1-Ronne-Tejn_0 + P_Biomass_0 + P_WindWest_0
   + P_SolarWest_0 + P_Cable_0 = 12864.40677966102
 C_nodal_Ronne_1: - X_0_1 - L+_0-Ronne-Nexo_1 + L-_0-Ronne-Nexo_1
   - L+_1-Ronne-Tejn_1 + L-_1-Ronne-Tejn_1 + P_Biomass_1 + P_WindWest_1
   + P_SolarWest_1 + P_Cable_1 = 19296.61016949153
 C_nodal_Ronne_2: - X_0_2 - L+_0-Ronne-Nexo_2 + L-_0-Ronne-Nexo_2
   - L+_1-Ronne-Tejn_2 + L-_1-Ronne-Tejn_2 + P_Biomass_2 + P_WindWest_2
   + P_SolarWest_2 + P_Cable_2 = 19372.8813559322
 C_nodal_Nexo_0: - X_1_0 + L+_0-Ronne-Nexo_0 - L-_0-Ronne-Nexo_0
   - L+_2-Nexo-Tejn_0 + L-_2-Nexo-Tejn_0 + P_WindEast_0 + P_SolarEast_0
   = 4288.13559322034
 C_nodal_Nexo_1: - X_1_1 + L+_0-Ronne-Nexo_1 - L-_0-Ronne-Nexo_1
   - L+_2-Nexo-Tejn_1 + L-_2-Nexo-Tejn_1 + P_WindEast_1 + P_SolarEast_1
   = 6432.203389830509
 C_nodal_Nexo_2: - X_1_2 + L+_0-Ronne-Nexo_2 - L-_0-Ronne-Nexo_2
   - L+_2-Nexo-Tejn_2 + L-_2-Nexo-Tejn_2 + P_WindEast_2 + P_SolarEast_2
   = 6457.627118644068
 C_nodal_Tejn_0: - X_2_0 + L+_1-Ronne-Tejn_0 - L-_1-Ronne-Tejn_0
   + L+_2-Nexo-Tejn_0 - L-_2-Nexo-Tejn_0 + P_WindNorth_0 + P_SolarNorth_0
   = 4288.13559322034
 C_nodal_Tejn_1: - X_2_1 + L+_1-Ronne-Tejn_1 - L-_1-Ronne-Tejn_1
   + L+_2-Nexo-Tejn_1 - L-_2-Nexo-Tejn_1 + P_WindNorth_1 + P_SolarNorth_1
   = 6432.203389830509
 C_nodal_Tejn_2: - X_2_2 + L+_1-Ronne-Tejn_2 - L-_1-Ronne-Tejn_2
   + L+_2-Nexo-Tejn_2 - L-_2-Nexo-Tejn_2 + P_WindNorth_2 + P_SolarNorth_2
   = 6457.627118644068
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
 L+_0-Ronne-Nexo_0 <= 100000
 L-_0-Ronne-Nexo_0 <= 100000
 L+_0-Ronne-Nexo_1 <= 100000
 L-_0-Ronne-Nexo_1 <= 100000
 L+_0-Ronne-Nexo_2 <= 100000
 L-_0-Ronne-Nexo_2 <= 100000
 L+_1-Ronne-Tejn_0 <= 100000
 L-_1-Ronne-Tejn_0 <= 100000
 L+_1-Ronne-Tejn_1 <= 100000
 L-_1-Ronne-Tejn_1 <= 100000
 L+_1-Ronne-Tejn_2 <= 100000
 L-_1-Ronne-Tejn_2 <= 100000
 L+_2-Nexo-Tejn_0 <= 100000
 L-_2-Nexo-Tejn_0 <= 100000
 L+_2-Nexo-Tejn_1 <= 100000
 L-_2-Nexo-Tejn_1 <= 100000
 L+_2-Nexo-Tejn_2 <= 100000
 L-_2-Nexo-Tejn_2 <= 100000
 P_Biomass_0 <= 15000
 P_Biomass_1 <= 15000
 P_Biomass_2 <= 15000
 P_WindWest_0 <= 6349.816673644081
 P_WindWest_1 <= 4496.944173006766
 P_WindWest_2 <= 6666.666666666667
 P_WindNorth_0 <= 6349.816673644081
 P_WindNorth_1 <= 4496.944173006766
 P_WindNorth_2 <= 6666.666666666667
 P_WindEast_0 <= 6349.816673644081
 P_WindEast_1 <= 4496.944173006766
 P_WindEast_2 <= 6666.666666666667
 P_SolarWest_0 = 0
 P_SolarWest_1 <= 1666.666666666667
 P_SolarWest_2 = 0
 P_SolarNorth_0 = 0
 P_SolarNorth_1 <= 1666.666666666667
 P_SolarNorth_2 = 0
 P_SolarEast_0 = 0
 P_SolarEast_1 <= 1666.666666666667
 P_SolarEast_2 = 0
 -30000 <= P_Cable_0 <= 30000
 -30000 <= P_Cable_1 <= 30000
 -30000 <= P_Cable_2 <= 30000
Binaries
 Y_0_0_0 Y_0_0_1 Y_0_0_2 Y_0_0_3 Y_0_1_0 Y_0_1_1 Y_0_1_2 Y_0_1_3 Y_0_2_0
 Y_0_2_1 Y_0_2_2 Y_0_2_3 Y_1_0_0 Y_1_0_1 Y_1_0_2 Y_1_0_3 Y_1_1_0 Y_1_1_1
 Y_1_1_2 Y_1_1_3 Y_1_2_0 Y_1_2_1 Y_1_2_2 Y_1_2_3 Y_2_0_0 Y_2_0_1 Y_2_0_2
 Y_2_0_3 Y_2_1_0 Y_2_1_1 Y_2_1_2 Y_2_1_3 Y_2_2_0 Y_2_2_1 Y_2_2_2 Y_2_2_3
End
