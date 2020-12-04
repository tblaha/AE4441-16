\ Model Advanced Model
\ LP format - for model browsing.
Minimize
  1e-06 Y_0_0_0 + 1e-06 Y_0_0_1 + 1e-06 Y_0_0_2 + 1e-06 Y_0_0_3
   + 1e-06 Dxp_0_0 + 1e-06 Dxn_0_0 + 1e-06 Y_0_1_0 + 1e-06 Y_0_1_1
   + 1e-06 Y_0_1_2 + 1e-06 Y_0_1_3 + 1e-06 Dxp_0_1 + 1e-06 Dxn_0_1
   + 1e-06 Y_0_2_0 + 1e-06 Y_0_2_1 + 1e-06 Y_0_2_2 + 1e-06 Y_0_2_3
   + 1e-06 Dxp_0_2 + 1e-06 Dxn_0_2 + 1e-06 Y_0_3_0 + 1e-06 Y_0_3_1
   + 1e-06 Y_0_3_2 + 1e-06 Y_0_3_3 + 1e-06 Y_work_0_0 + 1e-06 Y_work_0_1
   + 1e-06 Y_work_0_2 + 1e-06 Y_work_0_3 + 1e+09 S_0_Emin + 1e-06 Y_1_0_0
   + 1e-06 Y_1_0_1 + 1e-06 Y_1_0_2 + 1e-06 Y_1_0_3 + 1e-06 Dxp_1_0
   + 1e-06 Dxn_1_0 + 1e-06 Y_1_1_0 + 1e-06 Y_1_1_1 + 1e-06 Y_1_1_2
   + 1e-06 Y_1_1_3 + 1e-06 Dxp_1_1 + 1e-06 Dxn_1_1 + 1e-06 Y_1_2_0
   + 1e-06 Y_1_2_1 + 1e-06 Y_1_2_2 + 1e-06 Y_1_2_3 + 1e-06 Dxp_1_2
   + 1e-06 Dxn_1_2 + 1e-06 Y_1_3_0 + 1e-06 Y_1_3_1 + 1e-06 Y_1_3_2
   + 1e-06 Y_1_3_3 + 1e-06 Y_work_1_0 + 1e-06 Y_work_1_1 + 1e-06 Y_work_1_2
   + 1e-06 Y_work_1_3 + 1e+09 S_1_Emin + 1e-06 Fp_0_Ronne2Nexo_0
   + 1e-06 Fn_0-Ronne2Nexo_0 + 1e-06 Fp_0_Ronne2Nexo_1
   + 1e-06 Fn_0-Ronne2Nexo_1 + 1e-06 Fp_0_Ronne2Nexo_2
   + 1e-06 Fn_0-Ronne2Nexo_2 + 1e-06 Fp_0_Ronne2Nexo_3
   + 1e-06 Fn_0-Ronne2Nexo_3 + 1e-06 Fp_1_Ronne2Tejn_0
   + 1e-06 Fn_1-Ronne2Tejn_0 + 1e-06 Fp_1_Ronne2Tejn_1
   + 1e-06 Fn_1-Ronne2Tejn_1 + 1e-06 Fp_1_Ronne2Tejn_2
   + 1e-06 Fn_1-Ronne2Tejn_2 + 1e-06 Fp_1_Ronne2Tejn_3
   + 1e-06 Fn_1-Ronne2Tejn_3 + 1e-06 Fp_2_Nexo2Tejn_0
   + 1e-06 Fn_2-Nexo2Tejn_0 + 1e-06 Fp_2_Nexo2Tejn_1
   + 1e-06 Fn_2-Nexo2Tejn_1 + 1e-06 Fp_2_Nexo2Tejn_2
   + 1e-06 Fn_2-Nexo2Tejn_2 + 1e-06 Fp_2_Nexo2Tejn_3
   + 1e-06 Fn_2-Nexo2Tejn_3 + 6 P_Kraftvaerk_0 + 6 P_Kraftvaerk_1
   + 6 P_Kraftvaerk_2 + 6 P_Kraftvaerk_3 + 6 P_WindWest_0 + 6 P_WindWest_1
   + 6 P_WindWest_2 + 6 P_WindWest_3 + 6 P_WindNorth_0 + 6 P_WindNorth_1
   + 6 P_WindNorth_2 + 6 P_WindNorth_3 + 6 P_WindEast_0 + 6 P_WindEast_1
   + 6 P_WindEast_2 + 6 P_WindEast_3 + 6 P_SolarWest_0 + 6 P_SolarWest_1
   + 6 P_SolarWest_2 + 6 P_SolarWest_3 + 6 P_SolarNorth_0
   + 6 P_SolarNorth_1 + 6 P_SolarNorth_2 + 6 P_SolarNorth_3
   + 6 P_SolarEast_0 + 6 P_SolarEast_1 + 6 P_SolarEast_2 + 6 P_SolarEast_3
   + 12 P_SeaCable_0 + 12 P_SeaCable_1 + 12 P_SeaCable_2 + 12 P_SeaCable_3
Subject To
 C_numCh_1_0: Y_0_1_0 + Y_1_1_0 <= 1
 C_numCh_1_1: Y_0_1_1 + Y_1_1_1 <= 1
 C_numCh_1_2: Y_0_1_2 + Y_1_1_2 <= 1
 C_numCh_1_3: Y_0_1_3 + Y_1_1_3 <= 1
 C_numCh_2_0: Y_0_2_0 + Y_1_2_0 <= 1
 C_numCh_2_1: Y_0_2_1 + Y_1_2_1 <= 1
 C_numCh_2_2: Y_0_2_2 + Y_1_2_2 <= 1
 C_numCh_2_3: Y_0_2_3 + Y_1_2_3 <= 1
 C_OOOMWork_0: Y_work_0_0 + Y_work_0_1 + Y_work_0_2 + Y_work_0_3 <= 1
 C_WorkAssign_0_1_0: Y_0_1_0 - Y_work_0_0 <= 0
 C_WorkAssign_0_1_1: Y_0_1_1 - Y_work_0_1 <= 0
 C_WorkAssign_0_1_2: Y_0_1_2 - Y_work_0_2 <= 0
 C_WorkAssign_0_1_3: Y_0_1_3 - Y_work_0_3 <= 0
 C_WorkAssign_0_2_0: Y_0_2_0 - Y_work_0_0 <= 0
 C_WorkAssign_0_2_1: Y_0_2_1 - Y_work_0_1 <= 0
 C_WorkAssign_0_2_2: Y_0_2_2 - Y_work_0_2 <= 0
 C_WorkAssign_0_2_3: Y_0_2_3 - Y_work_0_3 <= 0
 C_OOOMa_0_0: Y_0_0_3 = 1
 C_OOOMb_0_0: Y_0_0_0 + Y_0_0_1 + Y_0_0_2 = 0
 C_OOOMa_0_3: Y_0_3_3 = 1
 C_OOOMb_0_3: Y_0_3_0 + Y_0_3_1 + Y_0_3_2 = 0
 C_Pub_0_0: X_0_0 - 41 Y_0_0_0 - 41 Y_0_0_1 - 22 Y_0_0_2 - 7.4 Y_0_0_3 <= 0
 C_Pub_0_1: X_0_1 - 41 Y_0_1_0 - 41 Y_0_1_1 - 22 Y_0_1_2 - 7.4 Y_0_1_3 <= 0
 C_Pub_0_2: X_0_2 - 41 Y_0_2_0 - 41 Y_0_2_1 - 22 Y_0_2_2 - 7.4 Y_0_2_3 <= 0
 C_Pub_0_3: X_0_3 - 41 Y_0_3_0 - 41 Y_0_3_1 - 22 Y_0_3_2 - 7.4 Y_0_3_3 <= 0
 C_Plb_0_0: X_0_0 + 41 Y_0_0_0 + 41 Y_0_0_1 + 22 Y_0_0_2 + 7.4 Y_0_0_3 >= 0
 C_Plb_0_1: X_0_1 + 41 Y_0_1_0 + 41 Y_0_1_1 + 22 Y_0_1_2 + 7.4 Y_0_1_3 >= 0
 C_Plb_0_2: X_0_2 + 41 Y_0_2_0 + 41 Y_0_2_1 + 22 Y_0_2_2 + 7.4 Y_0_2_3 >= 0
 C_Plb_0_3: X_0_3 + 41 Y_0_3_0 + 41 Y_0_3_1 + 22 Y_0_3_2 + 7.4 Y_0_3_3 >= 0
 C_Enet_0: 6 X_0_0 + 6 X_0_1 + 6 X_0_2 + 6 X_0_3 >= 0
 C_Eub_0_0: 6 X_0_0 <= 20.8
 C_Eub_0_1: 6 X_0_0 + 6 X_0_1 <= 20.8
 C_Eub_0_2: 6 X_0_0 + 6 X_0_1 + 6 X_0_2 <= 20.8
 C_Elb_0_0: 6 X_0_0 >= -20.8
 C_Elb_0_1: 6 X_0_0 + 6 X_0_1 >= -20.8
 C_Elb_0_2: 6 X_0_0 + 6 X_0_1 + 6 X_0_2 >= -20.8
 C_Dxp_0_0: - X_0_0 - Dxp_0_0 + X_0_1 <= 0
 C_Dxp_0_1: - X_0_1 - Dxp_0_1 + X_0_2 <= 0
 C_Dxp_0_2: - X_0_2 - Dxp_0_2 + X_0_3 <= 0
 C_Dxn_0_0: X_0_0 - Dxn_0_0 - X_0_1 <= 0
 C_Dxn_0_1: X_0_1 - Dxn_0_1 - X_0_2 <= 0
 C_Dxn_0_2: X_0_2 - Dxn_0_2 - X_0_3 <= 0
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
 C_WorkAssign_1_2_0: Y_1_2_0 - Y_work_1_0 <= 0
 C_WorkAssign_1_2_1: Y_1_2_1 - Y_work_1_1 <= 0
 C_WorkAssign_1_2_2: Y_1_2_2 - Y_work_1_2 <= 0
 C_WorkAssign_1_2_3: Y_1_2_3 - Y_work_1_3 <= 0
 C_Pub_1_3: X_1_3 - 105 Y_1_3_0 - 45 Y_1_3_1 - 11 Y_1_3_2 - 7.4 Y_1_3_3
   <= 0
 C_Plb_1_3: X_1_3 + 105 Y_1_3_0 + 45 Y_1_3_1 + 11 Y_1_3_2 + 7.4 Y_1_3_3
   >= 0
 C_OOOMa_1_3: Y_1_3_2 = 1
 C_OOOMb_1_3: Y_1_3_0 + Y_1_3_1 + Y_1_3_3 = 0
 C_Enet_1: 6 X_1_0 + 6 X_1_1 + 6 X_1_2 + 6 X_1_3 >= 0
 C_Elb_1_0: 6 X_1_0 >= -19
 C_Eub_1_0: 6 X_1_0 <= 19
 C_Elb_1_1: 6 X_1_0 + 6 X_1_1 >= -19
 C_Eub_1_1: 6 X_1_0 + 6 X_1_1 <= 19
 C_Elb_1_2: 6 X_1_0 + 6 X_1_1 + 6 X_1_2 >= -19
 C_Eub_1_2: 6 X_1_0 + 6 X_1_1 + 6 X_1_2 <= 19
 C_Dxp_1_0: - X_1_0 - Dxp_1_0 + X_1_1 <= 0
 C_Dxn_1_0: X_1_0 - Dxn_1_0 - X_1_1 <= 0
 C_Dxp_1_1: - X_1_1 - Dxp_1_1 + X_1_2 <= 0
 C_Dxn_1_1: X_1_1 - Dxn_1_1 - X_1_2 <= 0
 C_Dxp_1_2: - X_1_2 - Dxp_1_2 + X_1_3 <= 0
 C_Dxn_1_2: X_1_2 - Dxn_1_2 - X_1_3 <= 0
 C_nodal_Ronne_0: - X_1_0 - Fp_0_Ronne2Nexo_0 + Fn_0-Ronne2Nexo_0
   - Fp_1_Ronne2Tejn_0 + Fn_1-Ronne2Tejn_0 + P_Kraftvaerk_0 + P_WindWest_0
   + P_SolarWest_0 + P_SeaCable_0 = 12711.86440677966
 C_nodal_Ronne_1: - X_1_1 - Fp_0_Ronne2Nexo_1 + Fn_0-Ronne2Nexo_1
   - Fp_1_Ronne2Tejn_1 + Fn_1-Ronne2Tejn_1 + P_Kraftvaerk_1 + P_WindWest_1
   + P_SolarWest_1 + P_SeaCable_1 = 19067.79661016949
 C_nodal_Ronne_2: - X_1_2 - Fp_0_Ronne2Nexo_2 + Fn_0-Ronne2Nexo_2
   - Fp_1_Ronne2Tejn_2 + Fn_1-Ronne2Tejn_2 + P_Kraftvaerk_2 + P_WindWest_2
   + P_SolarWest_2 + P_SeaCable_2 = 19067.79661016949
 C_nodal_Ronne_3: - X_1_3 - Fp_0_Ronne2Nexo_3 + Fn_0-Ronne2Nexo_3
   - Fp_1_Ronne2Tejn_3 + Fn_1-Ronne2Tejn_3 + P_Kraftvaerk_3 + P_WindWest_3
   + P_SolarWest_3 + P_SeaCable_3 = 18764.74576271186
 C_nodal_Nexo_0: - X_0_0 + Fp_0_Ronne2Nexo_0 - Fn_0-Ronne2Nexo_0
   - Fp_2_Nexo2Tejn_0 + Fn_2-Nexo2Tejn_0 + P_WindEast_0 + P_SolarEast_0
   = 4237.28813559322
 C_nodal_Nexo_1: - X_0_1 + Fp_0_Ronne2Nexo_1 - Fn_0-Ronne2Nexo_1
   - Fp_2_Nexo2Tejn_1 + Fn_2-Nexo2Tejn_1 + P_WindEast_1 + P_SolarEast_1
   = 6355.932203389831
 C_nodal_Nexo_2: - X_0_2 + Fp_0_Ronne2Nexo_2 - Fn_0-Ronne2Nexo_2
   - Fp_2_Nexo2Tejn_2 + Fn_2-Nexo2Tejn_2 + P_WindEast_2 + P_SolarEast_2
   = 6355.932203389831
 C_nodal_Nexo_3: - X_0_3 + Fp_0_Ronne2Nexo_3 - Fn_0-Ronne2Nexo_3
   - Fp_2_Nexo2Tejn_3 + Fn_2-Nexo2Tejn_3 + P_WindEast_3 + P_SolarEast_3
   = 6254.915254237289
 C_nodal_Tejn_0: Fp_1_Ronne2Tejn_0 - Fn_1-Ronne2Tejn_0 + Fp_2_Nexo2Tejn_0
   - Fn_2-Nexo2Tejn_0 + P_WindNorth_0 + P_SolarNorth_0 = 4237.28813559322
 C_nodal_Tejn_1: Fp_1_Ronne2Tejn_1 - Fn_1-Ronne2Tejn_1 + Fp_2_Nexo2Tejn_1
   - Fn_2-Nexo2Tejn_1 + P_WindNorth_1 + P_SolarNorth_1 = 6355.932203389831
 C_nodal_Tejn_2: Fp_1_Ronne2Tejn_2 - Fn_1-Ronne2Tejn_2 + Fp_2_Nexo2Tejn_2
   - Fn_2-Nexo2Tejn_2 + P_WindNorth_2 + P_SolarNorth_2 = 6355.932203389831
 C_nodal_Tejn_3: Fp_1_Ronne2Tejn_3 - Fn_1-Ronne2Tejn_3 + Fp_2_Nexo2Tejn_3
   - Fn_2-Nexo2Tejn_3 + P_WindNorth_3 + P_SolarNorth_3 = 6254.915254237289
Bounds
 X_0_0 free
 X_0_1 free
 X_0_2 free
 X_0_3 free
 X_1_0 free
 X_1_1 free
 X_1_2 free
 X_1_3 free
 Fp_0_Ronne2Nexo_0 <= 100000
 Fn_0-Ronne2Nexo_0 <= 100000
 Fp_0_Ronne2Nexo_1 <= 100000
 Fn_0-Ronne2Nexo_1 <= 100000
 Fp_0_Ronne2Nexo_2 <= 100000
 Fn_0-Ronne2Nexo_2 <= 100000
 Fp_0_Ronne2Nexo_3 <= 100000
 Fn_0-Ronne2Nexo_3 <= 100000
 Fp_1_Ronne2Tejn_0 <= 100000
 Fn_1-Ronne2Tejn_0 <= 100000
 Fp_1_Ronne2Tejn_1 <= 100000
 Fn_1-Ronne2Tejn_1 <= 100000
 Fp_1_Ronne2Tejn_2 <= 100000
 Fn_1-Ronne2Tejn_2 <= 100000
 Fp_1_Ronne2Tejn_3 <= 100000
 Fn_1-Ronne2Tejn_3 <= 100000
 Fp_2_Nexo2Tejn_0 <= 100000
 Fn_2-Nexo2Tejn_0 <= 100000
 Fp_2_Nexo2Tejn_1 <= 100000
 Fn_2-Nexo2Tejn_1 <= 100000
 Fp_2_Nexo2Tejn_2 <= 100000
 Fn_2-Nexo2Tejn_2 <= 100000
 Fp_2_Nexo2Tejn_3 <= 100000
 Fn_2-Nexo2Tejn_3 <= 100000
 P_Kraftvaerk_0 <= 15000
 P_Kraftvaerk_1 <= 15000
 P_Kraftvaerk_2 <= 15000
 P_Kraftvaerk_3 <= 15000
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
 -25000 <= P_SeaCable_0 <= 25000
 -25000 <= P_SeaCable_1 <= 25000
 -25000 <= P_SeaCable_2 <= 25000
 -25000 <= P_SeaCable_3 <= 25000
Binaries
 Y_0_0_0 Y_0_0_1 Y_0_0_2 Y_0_0_3 Y_0_1_0 Y_0_1_1 Y_0_1_2 Y_0_1_3 Y_0_2_0
 Y_0_2_1 Y_0_2_2 Y_0_2_3 Y_0_3_0 Y_0_3_1 Y_0_3_2 Y_0_3_3 Y_work_0_0
 Y_work_0_1 Y_work_0_2 Y_work_0_3 S_0_Emin Y_1_0_0 Y_1_0_1 Y_1_0_2 Y_1_0_3
 Y_1_1_0 Y_1_1_1 Y_1_1_2 Y_1_1_3 Y_1_2_0 Y_1_2_1 Y_1_2_2 Y_1_2_3 Y_1_3_0
 Y_1_3_1 Y_1_3_2 Y_1_3_3 Y_work_1_0 Y_work_1_1 Y_work_1_2 Y_work_1_3
 S_1_Emin
End
