\ Model Advanced Model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  1e-06 Dxp_0_0 + 1e-06 Dxn_0_0 + 1e-06 Dxp_0_1 + 1e-06 Dxn_0_1
   + 1e-06 Dxp_1_0 + 1e-06 Dxn_1_0 + 1e-06 Dxp_1_1 + 1e-06 Dxn_1_1
   + 1e-06 Dxp_2_0 + 1e-06 Dxn_2_0 + 1e-06 Dxp_2_1 + 1e-06 Dxn_2_1
   + 1e-06 Lp_0-Ronne-Nexo_0 + 1e-06 Ln_0-Ronne-Nexo_0
   + 1e-06 Lp_0-Ronne-Nexo_1 + 1e-06 Ln_0-Ronne-Nexo_1
   + 1e-06 Lp_0-Ronne-Nexo_2 + 1e-06 Ln_0-Ronne-Nexo_2
   + 1e-06 Lp_0-Ronne-Nexo_3 + 1e-06 Ln_0-Ronne-Nexo_3
   + 1e-06 Lp_1-Ronne-Tejn_0 + 1e-06 Ln_1-Ronne-Tejn_0
   + 1e-06 Lp_1-Ronne-Tejn_1 + 1e-06 Ln_1-Ronne-Tejn_1
   + 1e-06 Lp_1-Ronne-Tejn_2 + 1e-06 Ln_1-Ronne-Tejn_2
   + 1e-06 Lp_1-Ronne-Tejn_3 + 1e-06 Ln_1-Ronne-Tejn_3
   + 1e-06 Lp_2-Nexo-Tejn_0 + 1e-06 Ln_2-Nexo-Tejn_0
   + 1e-06 Lp_2-Nexo-Tejn_1 + 1e-06 Ln_2-Nexo-Tejn_1
   + 1e-06 Lp_2-Nexo-Tejn_2 + 1e-06 Ln_2-Nexo-Tejn_2
   + 1e-06 Lp_2-Nexo-Tejn_3 + 1e-06 Ln_2-Nexo-Tejn_3 + 6 P_Biomass_0
   + 6 P_Biomass_1 + 6 P_Biomass_2 + 6 P_Biomass_3 + 6 P_WindWest_0
   + 6 P_WindWest_1 + 6 P_WindWest_2 + 6 P_WindWest_3 + 6 P_WindNorth_0
   + 6 P_WindNorth_1 + 6 P_WindNorth_2 + 6 P_WindNorth_3 + 6 P_WindEast_0
   + 6 P_WindEast_1 + 6 P_WindEast_2 + 6 P_WindEast_3 + 6 P_SolarWest_0
   + 6 P_SolarWest_1 + 6 P_SolarWest_2 + 6 P_SolarWest_3 + 6 P_SolarNorth_0
   + 6 P_SolarNorth_1 + 6 P_SolarNorth_2 + 6 P_SolarNorth_3
   + 6 P_SolarEast_0 + 6 P_SolarEast_1 + 6 P_SolarEast_2 + 6 P_SolarEast_3
   + 12 P_Cable_0 + 12 P_Cable_1 + 12 P_Cable_2 + 12 P_Cable_3
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
 C_OOOM_0_2: Y_0_2_0 + Y_0_2_1 + Y_0_2_2 + Y_0_2_3 <= 1
 C_Pub_0_3: X_0_3 - 41 Y_0_3_0 - 41 Y_0_3_1 - 22 Y_0_3_2 - 7.4 Y_0_3_3
   <= 0
 C_Plb_0_3: X_0_3 + 41 Y_0_3_0 + 41 Y_0_3_1 + 22 Y_0_3_2 + 7.4 Y_0_3_3
   >= 0
 C_OOOMa_0_3: Y_0_3_3 = 1
 C_OOOMb_0_3: Y_0_3_0 + Y_0_3_1 + Y_0_3_2 = 0
 C_Enet_0: 6 X_0_0 + 6 X_0_1 + 6 X_0_2 + 6 X_0_3 >= 3.301587301587301
 C_Elb_0_0: 6 X_0_0 >= -20.8
 C_Eub_0_0: 6 X_0_0 <= 20.8
 C_Elb_0_1: 6 X_0_0 + 6 X_0_1 >= -20.8
 C_Eub_0_1: 6 X_0_0 + 6 X_0_1 <= 20.8
 C_Elb_0_2: 6 X_0_0 + 6 X_0_1 + 6 X_0_2 >= -20.8
 C_Eub_0_2: 6 X_0_0 + 6 X_0_1 + 6 X_0_2 <= 20.8
 C_Dxp_0_1: - X_0_0 - Dxp_0_0 + X_0_2 <= 0
 C_Dxn_0_1: X_0_0 - Dxn_0_0 - X_0_2 <= 0
 C_Dxp_0_2: - X_0_1 - Dxp_0_1 + X_0_3 <= 0
 C_Dxn_0_2: X_0_1 - Dxn_0_1 - X_0_3 <= 0
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
 C_OOOM_1_2: Y_1_2_0 + Y_1_2_1 + Y_1_2_2 + Y_1_2_3 = 0
 C_Pub_1_3: X_1_3 - 41 Y_1_3_0 - 41 Y_1_3_1 - 22 Y_1_3_2 - 7.4 Y_1_3_3
   <= 0
 C_Plb_1_3: X_1_3 + 41 Y_1_3_0 + 41 Y_1_3_1 + 22 Y_1_3_2 + 7.4 Y_1_3_3
   >= 0
 C_OOOMa_1_3: Y_1_3_3 = 1
 C_OOOMb_1_3: Y_1_3_0 + Y_1_3_1 + Y_1_3_2 = 0
 C_Enet_1: 6 X_1_0 + 6 X_1_1 + 6 X_1_2 + 6 X_1_3 >= 0
 C_Elb_1_0: 6 X_1_0 >= -20.8
 C_Eub_1_0: 6 X_1_0 <= 20.8
 C_Elb_1_1: 6 X_1_0 + 6 X_1_1 >= -20.8
 C_Eub_1_1: 6 X_1_0 + 6 X_1_1 <= 20.8
 C_Elb_1_2: 6 X_1_0 + 6 X_1_1 + 6 X_1_2 >= -20.8
 C_Eub_1_2: 6 X_1_0 + 6 X_1_1 + 6 X_1_2 <= 20.8
 C_Dxp_1_1: - X_1_0 - Dxp_1_0 + X_1_2 <= 0
 C_Dxn_1_1: X_1_0 - Dxn_1_0 - X_1_2 <= 0
 C_Dxp_1_2: - X_1_1 - Dxp_1_1 + X_1_3 <= 0
 C_Dxn_1_2: X_1_1 - Dxn_1_1 - X_1_3 <= 0
 C_Pub_2_0: X_2_0 - 105 Y_2_0_0 - 45 Y_2_0_1 - 11 Y_2_0_2 - 7.4 Y_2_0_3
   <= 0
 C_Plb_2_0: X_2_0 + 105 Y_2_0_0 + 45 Y_2_0_1 + 11 Y_2_0_2 + 7.4 Y_2_0_3
   >= 0
 C_OOOMa_2_0: Y_2_0_2 = 1
 C_OOOMb_2_0: Y_2_0_0 + Y_2_0_1 + Y_2_0_3 = 0
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
 C_Pub_2_3: X_2_3 - 105 Y_2_3_0 - 45 Y_2_3_1 - 11 Y_2_3_2 - 7.4 Y_2_3_3
   <= 0
 C_Plb_2_3: X_2_3 + 105 Y_2_3_0 + 45 Y_2_3_1 + 11 Y_2_3_2 + 7.4 Y_2_3_3
   >= 0
 C_OOOMa_2_3: Y_2_3_2 = 1
 C_OOOMb_2_3: Y_2_3_0 + Y_2_3_1 + Y_2_3_3 = 0
 C_Enet_2: 6 X_2_0 + 6 X_2_1 + 6 X_2_2 + 6 X_2_3 >= 4.453125
 C_Elb_2_0: 6 X_2_0 >= -19
 C_Eub_2_0: 6 X_2_0 <= 19
 C_Elb_2_1: 6 X_2_0 + 6 X_2_1 >= -19
 C_Eub_2_1: 6 X_2_0 + 6 X_2_1 <= 19
 C_Elb_2_2: 6 X_2_0 + 6 X_2_1 + 6 X_2_2 >= -19
 C_Eub_2_2: 6 X_2_0 + 6 X_2_1 + 6 X_2_2 <= 19
 C_Dxp_2_1: - X_2_0 - Dxp_2_0 + X_2_2 <= 0
 C_Dxn_2_1: X_2_0 - Dxn_2_0 - X_2_2 <= 0
 C_Dxp_2_2: - X_2_1 - Dxp_2_1 + X_2_3 <= 0
 C_Dxn_2_2: X_2_1 - Dxn_2_1 - X_2_3 <= 0
 C_numCh_1_0: Y_1_1_0 + Y_2_1_0 <= 1
 C_numCh_1_1: Y_1_1_1 + Y_2_1_1 <= 1
 C_numCh_1_2: Y_1_1_2 + Y_2_1_2 <= 1
 C_numCh_1_3: Y_1_1_3 + Y_2_1_3 <= 1
 C_numCh_2_0: Y_0_2_0 <= 1
 C_numCh_2_1: Y_0_2_1 <= 1
 C_numCh_2_2: Y_0_2_2 <= 1
 C_numCh_2_3: Y_0_2_3 <= 1
 C_nodal_Ronne_0: - X_0_0 - Lp_0-Ronne-Nexo_0 + Ln_0-Ronne-Nexo_0
   - Lp_1-Ronne-Tejn_0 + Ln_1-Ronne-Tejn_0 + P_Biomass_0 + P_WindWest_0
   + P_SolarWest_0 + P_Cable_0 = 12864.40677966102
 C_nodal_Ronne_1: - X_0_1 - Lp_0-Ronne-Nexo_1 + Ln_0-Ronne-Nexo_1
   - Lp_1-Ronne-Tejn_1 + Ln_1-Ronne-Tejn_1 + P_Biomass_1 + P_WindWest_1
   + P_SolarWest_1 + P_Cable_1 = 19296.61016949153
 C_nodal_Ronne_2: - X_0_2 - Lp_0-Ronne-Nexo_2 + Ln_0-Ronne-Nexo_2
   - Lp_1-Ronne-Tejn_2 + Ln_1-Ronne-Tejn_2 + P_Biomass_2 + P_WindWest_2
   + P_SolarWest_2 + P_Cable_2 = 19296.61016949153
 C_nodal_Ronne_3: - X_0_3 - Lp_0-Ronne-Nexo_3 + Ln_0-Ronne-Nexo_3
   - Lp_1-Ronne-Tejn_3 + Ln_1-Ronne-Tejn_3 + P_Biomass_3 + P_WindWest_3
   + P_SolarWest_3 + P_Cable_3 = 17745.7627118644
 C_nodal_Nexo_0: - X_1_0 + Lp_0-Ronne-Nexo_0 - Ln_0-Ronne-Nexo_0
   - Lp_2-Nexo-Tejn_0 + Ln_2-Nexo-Tejn_0 + P_WindEast_0 + P_SolarEast_0
   = 4288.13559322034
 C_nodal_Nexo_1: - X_1_1 + Lp_0-Ronne-Nexo_1 - Ln_0-Ronne-Nexo_1
   - Lp_2-Nexo-Tejn_1 + Ln_2-Nexo-Tejn_1 + P_WindEast_1 + P_SolarEast_1
   = 6432.203389830509
 C_nodal_Nexo_2: - X_1_2 + Lp_0-Ronne-Nexo_2 - Ln_0-Ronne-Nexo_2
   - Lp_2-Nexo-Tejn_2 + Ln_2-Nexo-Tejn_2 + P_WindEast_2 + P_SolarEast_2
   = 6432.203389830509
 C_nodal_Nexo_3: - X_1_3 + Lp_0-Ronne-Nexo_3 - Ln_0-Ronne-Nexo_3
   - Lp_2-Nexo-Tejn_3 + Ln_2-Nexo-Tejn_3 + P_WindEast_3 + P_SolarEast_3
   = 5915.254237288136
 C_nodal_Tejn_0: - X_2_0 + Lp_1-Ronne-Tejn_0 - Ln_1-Ronne-Tejn_0
   + Lp_2-Nexo-Tejn_0 - Ln_2-Nexo-Tejn_0 + P_WindNorth_0 + P_SolarNorth_0
   = 4288.13559322034
 C_nodal_Tejn_1: - X_2_1 + Lp_1-Ronne-Tejn_1 - Ln_1-Ronne-Tejn_1
   + Lp_2-Nexo-Tejn_1 - Ln_2-Nexo-Tejn_1 + P_WindNorth_1 + P_SolarNorth_1
   = 6432.203389830509
 C_nodal_Tejn_2: - X_2_2 + Lp_1-Ronne-Tejn_2 - Ln_1-Ronne-Tejn_2
   + Lp_2-Nexo-Tejn_2 - Ln_2-Nexo-Tejn_2 + P_WindNorth_2 + P_SolarNorth_2
   = 6432.203389830509
 C_nodal_Tejn_3: - X_2_3 + Lp_1-Ronne-Tejn_3 - Ln_1-Ronne-Tejn_3
   + Lp_2-Nexo-Tejn_3 - Ln_2-Nexo-Tejn_3 + P_WindNorth_3 + P_SolarNorth_3
   = 5915.254237288136
Bounds
 X_0_0 free
 X_0_1 free
 X_0_2 free
 X_0_3 free
 X_1_0 free
 X_1_1 free
 X_1_2 free
 X_1_3 free
 X_2_0 free
 X_2_1 free
 X_2_2 free
 X_2_3 free
 Lp_0-Ronne-Nexo_0 <= 100000
 Ln_0-Ronne-Nexo_0 <= 100000
 Lp_0-Ronne-Nexo_1 <= 100000
 Ln_0-Ronne-Nexo_1 <= 100000
 Lp_0-Ronne-Nexo_2 <= 100000
 Ln_0-Ronne-Nexo_2 <= 100000
 Lp_0-Ronne-Nexo_3 <= 100000
 Ln_0-Ronne-Nexo_3 <= 100000
 Lp_1-Ronne-Tejn_0 <= 100000
 Ln_1-Ronne-Tejn_0 <= 100000
 Lp_1-Ronne-Tejn_1 <= 100000
 Ln_1-Ronne-Tejn_1 <= 100000
 Lp_1-Ronne-Tejn_2 <= 100000
 Ln_1-Ronne-Tejn_2 <= 100000
 Lp_1-Ronne-Tejn_3 <= 100000
 Ln_1-Ronne-Tejn_3 <= 100000
 Lp_2-Nexo-Tejn_0 <= 100000
 Ln_2-Nexo-Tejn_0 <= 100000
 Lp_2-Nexo-Tejn_1 <= 100000
 Ln_2-Nexo-Tejn_1 <= 100000
 Lp_2-Nexo-Tejn_2 <= 100000
 Ln_2-Nexo-Tejn_2 <= 100000
 Lp_2-Nexo-Tejn_3 <= 100000
 Ln_2-Nexo-Tejn_3 <= 100000
 P_Biomass_0 <= 15000
 P_Biomass_1 <= 15000
 P_Biomass_2 <= 15000
 P_Biomass_3 <= 15000
 P_WindWest_0 <= 6483.369856519296
 P_WindWest_1 <= 6247.136571921738
 P_WindWest_2 <= 6430.43338206911
 P_WindWest_3 <= 6666.666666666667
 P_WindNorth_0 <= 6483.369856519296
 P_WindNorth_1 <= 6247.136571921738
 P_WindNorth_2 <= 6430.43338206911
 P_WindNorth_3 <= 6666.666666666667
 P_WindEast_0 <= 6483.369856519296
 P_WindEast_1 <= 6247.136571921738
 P_WindEast_2 <= 6430.43338206911
 P_WindEast_3 <= 6666.666666666667
 P_SolarWest_0 = 0
 P_SolarWest_1 <= 1666.666666666667
 P_SolarWest_2 <= 1666.666666666667
 P_SolarWest_3 = 0
 P_SolarNorth_0 = 0
 P_SolarNorth_1 <= 1666.666666666667
 P_SolarNorth_2 <= 1666.666666666667
 P_SolarNorth_3 = 0
 P_SolarEast_0 = 0
 P_SolarEast_1 <= 1666.666666666667
 P_SolarEast_2 <= 1666.666666666667
 P_SolarEast_3 = 0
 -50000 <= P_Cable_0 <= 50000
 -50000 <= P_Cable_1 <= 50000
 -50000 <= P_Cable_2 <= 50000
 -50000 <= P_Cable_3 <= 50000
Binaries
 Y_0_0_0 Y_0_0_1 Y_0_0_2 Y_0_0_3 Y_0_1_0 Y_0_1_1 Y_0_1_2 Y_0_1_3 Y_0_2_0
 Y_0_2_1 Y_0_2_2 Y_0_2_3 Y_0_3_0 Y_0_3_1 Y_0_3_2 Y_0_3_3 Y_1_0_0 Y_1_0_1
 Y_1_0_2 Y_1_0_3 Y_1_1_0 Y_1_1_1 Y_1_1_2 Y_1_1_3 Y_1_2_0 Y_1_2_1 Y_1_2_2
 Y_1_2_3 Y_1_3_0 Y_1_3_1 Y_1_3_2 Y_1_3_3 Y_2_0_0 Y_2_0_1 Y_2_0_2 Y_2_0_3
 Y_2_1_0 Y_2_1_1 Y_2_1_2 Y_2_1_3 Y_2_2_0 Y_2_2_1 Y_2_2_2 Y_2_2_3 Y_2_3_0
 Y_2_3_1 Y_2_3_2 Y_2_3_3
End
