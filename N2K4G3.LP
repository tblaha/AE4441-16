\ Model Advanced Model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  1e-06 Y_0_0_0 + 1e-06 Y_0_0_1 + 1e-06 Y_0_0_2 + 1e-06 Y_0_0_3
   + 1e-06 Dxp_0_0 + 1e-06 Dxn_0_0 + 1e-06 Y_0_1_0 + 1e-06 Y_0_1_1
   + 1e-06 Y_0_1_2 + 1e-06 Y_0_1_3 + 1e-06 Dxp_0_1 + 1e-06 Dxn_0_1
   + 1e-06 Y_0_2_0 + 1e-06 Y_0_2_1 + 1e-06 Y_0_2_2 + 1e-06 Y_0_2_3
   + 1e-06 Y_work_0_0 + 1e-06 Y_work_0_1 + 1e-06 Y_work_0_2
   + 1e-06 Y_work_0_3 + 1e+09 S_0_Emin + 1e-06 Y_1_0_0 + 1e-06 Y_1_0_1
   + 1e-06 Y_1_0_2 + 1e-06 Y_1_0_3 + 1e-06 Dxp_1_0 + 1e-06 Dxn_1_0
   + 1e-06 Y_1_1_0 + 1e-06 Y_1_1_1 + 1e-06 Y_1_1_2 + 1e-06 Y_1_1_3
   + 1e-06 Dxp_1_1 + 1e-06 Dxn_1_1 + 1e-06 Y_1_2_0 + 1e-06 Y_1_2_1
   + 1e-06 Y_1_2_2 + 1e-06 Y_1_2_3 + 1e-06 Y_work_1_0 + 1e-06 Y_work_1_1
   + 1e-06 Y_work_1_2 + 1e-06 Y_work_1_3 + 1e+09 S_1_Emin
   + 1e-06 Lp_0_Ronne2Nexo_0 + 1e-06 Ln_0-Ronne2Nexo_0
   + 1e-06 Lp_0_Ronne2Nexo_1 + 1e-06 Ln_0-Ronne2Nexo_1
   + 1e-06 Lp_0_Ronne2Nexo_2 + 1e-06 Ln_0-Ronne2Nexo_2
   + 1e-06 Lp_1_Ronne2Tejn_0 + 1e-06 Ln_1-Ronne2Tejn_0
   + 1e-06 Lp_1_Ronne2Tejn_1 + 1e-06 Ln_1-Ronne2Tejn_1
   + 1e-06 Lp_1_Ronne2Tejn_2 + 1e-06 Ln_1-Ronne2Tejn_2
   + 1e-06 Lp_2_Nexo2Tejn_0 + 1e-06 Ln_2-Nexo2Tejn_0
   + 1e-06 Lp_2_Nexo2Tejn_1 + 1e-06 Ln_2-Nexo2Tejn_1
   + 1e-06 Lp_2_Nexo2Tejn_2 + 1e-06 Ln_2-Nexo2Tejn_2 + 8 P_Kraftvaerk_0
   + 8 P_Kraftvaerk_1 + 8 P_Kraftvaerk_2 + 8 P_WindWest_0 + 8 P_WindWest_1
   + 8 P_WindWest_2 + 8 P_WindNorth_0 + 8 P_WindNorth_1 + 8 P_WindNorth_2
   + 8 P_WindEast_0 + 8 P_WindEast_1 + 8 P_WindEast_2 + 8 P_SolarWest_0
   + 8 P_SolarWest_1 + 8 P_SolarWest_2 + 8 P_SolarNorth_0
   + 8 P_SolarNorth_1 + 8 P_SolarNorth_2 + 8 P_SolarEast_0
   + 8 P_SolarEast_1 + 8 P_SolarEast_2 + 16 P_SeaCable_0 + 16 P_SeaCable_1
   + 16 P_SeaCable_2
Subject To
 C_OOOMWork_0: Y_work_0_0 + Y_work_0_1 + Y_work_0_2 + Y_work_0_3 <= 1
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
 C_WorkAssign_0_1_0: Y_0_1_0 - Y_work_0_0 <= 0
 C_WorkAssign_0_1_1: Y_0_1_1 - Y_work_0_1 <= 0
 C_WorkAssign_0_1_2: Y_0_1_2 - Y_work_0_2 <= 0
 C_WorkAssign_0_1_3: Y_0_1_3 - Y_work_0_3 <= 0
 C_Pub_0_2: X_0_2 - 41 Y_0_2_0 - 41 Y_0_2_1 - 22 Y_0_2_2 - 7.4 Y_0_2_3
   <= 0
 C_Plb_0_2: X_0_2 + 41 Y_0_2_0 + 41 Y_0_2_1 + 22 Y_0_2_2 + 7.4 Y_0_2_3
   >= 0
 C_OOOMa_0_2: Y_0_2_3 = 1
 C_OOOMb_0_2: Y_0_2_0 + Y_0_2_1 + Y_0_2_2 = 0
 C_Enet_0: 8 X_0_0 + 8 X_0_1 + 8 X_0_2 >= 0
 C_Elb_0_0: 8 X_0_0 >= -20.8
 C_Eub_0_0: 8 X_0_0 <= 20.8
 C_Elb_0_1: 8 X_0_0 + 8 X_0_1 >= -20.8
 C_Eub_0_1: 8 X_0_0 + 8 X_0_1 <= 20.8
 C_Dxp_0_0: - X_0_0 - Dxp_0_0 + X_0_1 <= 0
 C_Dxn_0_0: X_0_0 - Dxn_0_0 - X_0_1 <= 0
 C_Dxp_0_1: - X_0_1 - Dxp_0_1 + X_0_2 <= 0
 C_Dxn_0_1: X_0_1 - Dxn_0_1 - X_0_2 <= 0
 C_OOOMWork_1: Y_work_1_0 + Y_work_1_1 + Y_work_1_2 + Y_work_1_3 <= 1
 C_Pub_1_0: X_1_0 - 105 Y_1_0_0 - 45 Y_1_0_1 - 11 Y_1_0_2 - 7.4 Y_1_0_3
   <= 0
 C_Plb_1_0: X_1_0 + 105 Y_1_0_0 + 45 Y_1_0_1 + 11 Y_1_0_2 + 7.4 Y_1_0_3
   >= 0
 C_OOOMa_1_0: Y_1_0_2 = 1
 C_OOOMb_1_0: Y_1_0_0 + Y_1_0_1 + Y_1_0_3 = 0
 C_Pub_1_1: X_1_1 - 105 Y_1_1_0 - 45 Y_1_1_1 - 11 Y_1_1_2 - 7.4 Y_1_1_3
   <= 0
 C_Plb_1_1: X_1_1 + 105 Y_1_1_0 + 45 Y_1_1_1 + 11 Y_1_1_2 + 7.4 Y_1_1_3
   >= 0
 C_WorkAssign_1_1_0: Y_1_1_0 - Y_work_1_0 <= 0
 C_WorkAssign_1_1_1: Y_1_1_1 - Y_work_1_1 <= 0
 C_WorkAssign_1_1_2: Y_1_1_2 - Y_work_1_2 <= 0
 C_WorkAssign_1_1_3: Y_1_1_3 - Y_work_1_3 <= 0
 C_Pub_1_2: X_1_2 - 105 Y_1_2_0 - 45 Y_1_2_1 - 11 Y_1_2_2 - 7.4 Y_1_2_3
   <= 0
 C_Plb_1_2: X_1_2 + 105 Y_1_2_0 + 45 Y_1_2_1 + 11 Y_1_2_2 + 7.4 Y_1_2_3
   >= 0
 C_OOOMa_1_2: Y_1_2_2 = 1
 C_OOOMb_1_2: Y_1_2_0 + Y_1_2_1 + Y_1_2_3 = 0
 C_Enet_1: 8 X_1_0 + 8 X_1_1 + 8 X_1_2 >= 0
 C_Elb_1_0: 8 X_1_0 >= -19
 C_Eub_1_0: 8 X_1_0 <= 19
 C_Elb_1_1: 8 X_1_0 + 8 X_1_1 >= -19
 C_Eub_1_1: 8 X_1_0 + 8 X_1_1 <= 19
 C_Dxp_1_0: - X_1_0 - Dxp_1_0 + X_1_1 <= 0
 C_Dxn_1_0: X_1_0 - Dxn_1_0 - X_1_1 <= 0
 C_Dxp_1_1: - X_1_1 - Dxp_1_1 + X_1_2 <= 0
 C_Dxn_1_1: X_1_1 - Dxn_1_1 - X_1_2 <= 0
 C_numCh_1_0: Y_0_1_0 + Y_1_1_0 <= 1
 C_numCh_1_1: Y_0_1_1 + Y_1_1_1 <= 1
 C_numCh_1_2: Y_0_1_2 + Y_1_1_2 <= 1
 C_numCh_1_3: Y_0_1_3 + Y_1_1_3 <= 1
 C_nodal_Ronne_0: - X_1_0 - Lp_0_Ronne2Nexo_0 + Ln_0-Ronne2Nexo_0
   - Lp_1_Ronne2Tejn_0 + Ln_1-Ronne2Tejn_0 + P_Kraftvaerk_0 + P_WindWest_0
   + P_SolarWest_0 + P_SeaCable_0 = 12711.86440677966
 C_nodal_Ronne_1: - X_1_1 - Lp_0_Ronne2Nexo_1 + Ln_0-Ronne2Nexo_1
   - Lp_1_Ronne2Tejn_1 + Ln_1-Ronne2Tejn_1 + P_Kraftvaerk_1 + P_WindWest_1
   + P_SolarWest_1 + P_SeaCable_1 = 19067.79661016949
 C_nodal_Ronne_2: - X_1_2 - Lp_0_Ronne2Nexo_2 + Ln_0-Ronne2Nexo_2
   - Lp_1_Ronne2Tejn_2 + Ln_1-Ronne2Tejn_2 + P_Kraftvaerk_2 + P_WindWest_2
   + P_SolarWest_2 + P_SeaCable_2 = 20782.37288135593
 C_nodal_Nexo_0: - X_0_0 + Lp_0_Ronne2Nexo_0 - Ln_0-Ronne2Nexo_0
   - Lp_2_Nexo2Tejn_0 + Ln_2-Nexo2Tejn_0 + P_WindEast_0 + P_SolarEast_0
   = 4237.28813559322
 C_nodal_Nexo_1: - X_0_1 + Lp_0_Ronne2Nexo_1 - Ln_0-Ronne2Nexo_1
   - Lp_2_Nexo2Tejn_1 + Ln_2-Nexo2Tejn_1 + P_WindEast_1 + P_SolarEast_1
   = 6355.932203389831
 C_nodal_Nexo_2: - X_0_2 + Lp_0_Ronne2Nexo_2 - Ln_0-Ronne2Nexo_2
   - Lp_2_Nexo2Tejn_2 + Ln_2-Nexo2Tejn_2 + P_WindEast_2 + P_SolarEast_2
   = 6927.457627118644
 C_nodal_Tejn_0: Lp_1_Ronne2Tejn_0 - Ln_1-Ronne2Tejn_0 + Lp_2_Nexo2Tejn_0
   - Ln_2-Nexo2Tejn_0 + P_WindNorth_0 + P_SolarNorth_0 = 4237.28813559322
 C_nodal_Tejn_1: Lp_1_Ronne2Tejn_1 - Ln_1-Ronne2Tejn_1 + Lp_2_Nexo2Tejn_1
   - Ln_2-Nexo2Tejn_1 + P_WindNorth_1 + P_SolarNorth_1 = 6355.932203389831
 C_nodal_Tejn_2: Lp_1_Ronne2Tejn_2 - Ln_1-Ronne2Tejn_2 + Lp_2_Nexo2Tejn_2
   - Ln_2-Nexo2Tejn_2 + P_WindNorth_2 + P_SolarNorth_2 = 6927.457627118644
Bounds
 X_0_0 free
 X_0_1 free
 X_0_2 free
 X_1_0 free
 X_1_1 free
 X_1_2 free
 Lp_0_Ronne2Nexo_0 <= 100000
 Ln_0-Ronne2Nexo_0 <= 100000
 Lp_0_Ronne2Nexo_1 <= 100000
 Ln_0-Ronne2Nexo_1 <= 100000
 Lp_0_Ronne2Nexo_2 <= 100000
 Ln_0-Ronne2Nexo_2 <= 100000
 Lp_1_Ronne2Tejn_0 <= 100000
 Ln_1-Ronne2Tejn_0 <= 100000
 Lp_1_Ronne2Tejn_1 <= 100000
 Ln_1-Ronne2Tejn_1 <= 100000
 Lp_1_Ronne2Tejn_2 <= 100000
 Ln_1-Ronne2Tejn_2 <= 100000
 Lp_2_Nexo2Tejn_0 <= 100000
 Ln_2-Nexo2Tejn_0 <= 100000
 Lp_2_Nexo2Tejn_1 <= 100000
 Ln_2-Nexo2Tejn_1 <= 100000
 Lp_2_Nexo2Tejn_2 <= 100000
 Ln_2-Nexo2Tejn_2 <= 100000
 P_Kraftvaerk_0 <= 15000
 P_Kraftvaerk_1 <= 15000
 P_Kraftvaerk_2 <= 15000
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
 -25000 <= P_SeaCable_0 <= 25000
 -25000 <= P_SeaCable_1 <= 25000
 -25000 <= P_SeaCable_2 <= 25000
Binaries
 Y_0_0_0 Y_0_0_1 Y_0_0_2 Y_0_0_3 Y_0_1_0 Y_0_1_1 Y_0_1_2 Y_0_1_3 Y_0_2_0
 Y_0_2_1 Y_0_2_2 Y_0_2_3 Y_work_0_0 Y_work_0_1 Y_work_0_2 Y_work_0_3
 S_0_Emin Y_1_0_0 Y_1_0_1 Y_1_0_2 Y_1_0_3 Y_1_1_0 Y_1_1_1 Y_1_1_2 Y_1_1_3
 Y_1_2_0 Y_1_2_1 Y_1_2_2 Y_1_2_3 Y_work_1_0 Y_work_1_1 Y_work_1_2
 Y_work_1_3 S_1_Emin
End
