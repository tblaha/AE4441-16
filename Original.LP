\ Model Advanced Model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  6 P_Biomass_0 + 6 P_Biomass_1 + 6 P_Biomass_2 + 6 P_Biomass_3
   + 6 P_WindWest_0 + 6 P_WindWest_1 + 6 P_WindWest_2 + 6 P_WindWest_3
   + 6 P_WindNorth_0 + 6 P_WindNorth_1 + 6 P_WindNorth_2 + 6 P_WindNorth_3
   + 6 P_WindEast_0 + 6 P_WindEast_1 + 6 P_WindEast_2 + 6 P_WindEast_3
   + 6 P_SolarWest_0 + 6 P_SolarWest_1 + 6 P_SolarWest_2 + 6 P_SolarWest_3
   + 6 P_SolarNorth_0 + 6 P_SolarNorth_1 + 6 P_SolarNorth_2
   + 6 P_SolarNorth_3 + 6 P_SolarEast_0 + 6 P_SolarEast_1 + 6 P_SolarEast_2
   + 6 P_SolarEast_3 + 12 P_Cable_0 + 12 P_Cable_1 + 12 P_Cable_2
   + 12 P_Cable_3
Subject To
 C_0_0_OOOM: Y_0_0_0 + Y_0_0_1 + Y_0_0_2 + Y_0_0_3 + Y_0_0_4 + Y_0_0_5
   + Y_0_0_6 = 1
 C_0_0_Pbat: X_0_0 + 11 Y_0_0_0 + 5 Y_0_0_1 + 2 Y_0_0_2 - 2 Y_0_0_4
   - 5 Y_0_0_5 - 11 Y_0_0_6 = 0
 C_0_1_OOOM: Y_0_1_0 + Y_0_1_1 + Y_0_1_2 + Y_0_1_3 + Y_0_1_4 + Y_0_1_5
   + Y_0_1_6 = 1
 C_0_1_Pbat: X_0_1 + 11 Y_0_1_0 + 5 Y_0_1_1 + 2 Y_0_1_2 - 2 Y_0_1_4
   - 5 Y_0_1_5 - 11 Y_0_1_6 = 0
 C_0_2_OOOM: Y_0_2_0 + Y_0_2_1 + Y_0_2_2 + Y_0_2_3 + Y_0_2_4 + Y_0_2_5
   + Y_0_2_6 = 1
 C_0_2_Pbat: X_0_2 + 11 Y_0_2_0 + 5 Y_0_2_1 + 2 Y_0_2_2 - 2 Y_0_2_4
   - 5 Y_0_2_5 - 11 Y_0_2_6 = 0
 C_0_3_OOOM: Y_0_3_0 + Y_0_3_1 + Y_0_3_2 + Y_0_3_3 + Y_0_3_4 + Y_0_3_5
   + Y_0_3_6 = 1
 C_0_3_Pbat: X_0_3 + 11 Y_0_3_0 + 5 Y_0_3_1 + 2 Y_0_3_2 - 2 Y_0_3_4
   - 5 Y_0_3_5 - 11 Y_0_3_6 = 0
 C_0_E_net: 6 X_0_0 + 6 X_0_1 + 6 X_0_2 + 6 X_0_3 >= 4.5
 C_0_0_E_lb: 6 X_0_0 >= -20
 C_0_0_E_ub: 6 X_0_0 <= 20
 C_0_1_E_lb: 6 X_0_0 + 6 X_0_1 >= -20
 C_0_1_E_ub: 6 X_0_0 + 6 X_0_1 <= 20
 C_0_2_E_lb: 6 X_0_0 + 6 X_0_1 + 6 X_0_2 >= -20
 C_0_2_E_ub: 6 X_0_0 + 6 X_0_1 + 6 X_0_2 <= 20
 C_1_0_OOOM: Y_1_0_0 + Y_1_0_1 + Y_1_0_2 + Y_1_0_3 + Y_1_0_4 + Y_1_0_5
   + Y_1_0_6 = 1
 C_1_0_Pbat: X_1_0 + 11 Y_1_0_0 + 5 Y_1_0_1 + 2 Y_1_0_2 - 2 Y_1_0_4
   - 5 Y_1_0_5 - 11 Y_1_0_6 = 0
 C_1_1_OOOM: Y_1_1_0 + Y_1_1_1 + Y_1_1_2 + Y_1_1_3 + Y_1_1_4 + Y_1_1_5
   + Y_1_1_6 = 1
 C_1_1_Pbat: X_1_1 + 11 Y_1_1_0 + 5 Y_1_1_1 + 2 Y_1_1_2 - 2 Y_1_1_4
   - 5 Y_1_1_5 - 11 Y_1_1_6 = 0
 C_1_2_OOOM: Y_1_2_0 + Y_1_2_1 + Y_1_2_2 + Y_1_2_3 + Y_1_2_4 + Y_1_2_5
   + Y_1_2_6 = 1
 C_1_2_Pbat: X_1_2 + 11 Y_1_2_0 + 5 Y_1_2_1 + 2 Y_1_2_2 - 2 Y_1_2_4
   - 5 Y_1_2_5 - 11 Y_1_2_6 = 0
 C_1_3_OOOM: Y_1_3_0 + Y_1_3_1 + Y_1_3_2 + Y_1_3_3 + Y_1_3_4 + Y_1_3_5
   + Y_1_3_6 = 1
 C_1_3_Pbat: X_1_3 + 11 Y_1_3_0 + 5 Y_1_3_1 + 2 Y_1_3_2 - 2 Y_1_3_4
   - 5 Y_1_3_5 - 11 Y_1_3_6 = 0
 C_1_E_net: 6 X_1_0 + 6 X_1_1 + 6 X_1_2 + 6 X_1_3 >= 16
 C_1_0_E_lb: 6 X_1_0 >= -16.88
 C_1_0_E_ub: 6 X_1_0 <= 16.88
 C_1_1_E_lb: 6 X_1_0 + 6 X_1_1 >= -16.88
 C_1_1_E_ub: 6 X_1_0 + 6 X_1_1 <= 16.88
 C_1_2_E_lb: 6 X_1_0 + 6 X_1_1 + 6 X_1_2 >= -16.88
 C_1_2_E_ub: 6 X_1_0 + 6 X_1_1 + 6 X_1_2 <= 16.88
 C_nodal_Ronne_0: - X_1_0 - L_0-Ronne-Nexo_0 - L_1-Ronne-Tejn_0
   + P_Biomass_0 + P_WindWest_0 + P_SolarWest_0 + P_Cable_0
   = 7146.892655367232
 C_nodal_Ronne_1: - X_1_1 - L_0-Ronne-Nexo_1 - L_1-Ronne-Tejn_1
   + P_Biomass_1 + P_WindWest_1 + P_SolarWest_1 + P_Cable_1
   = 10720.33898305085
 C_nodal_Ronne_2: - X_1_2 - L_0-Ronne-Nexo_2 - L_1-Ronne-Tejn_2
   + P_Biomass_2 + P_WindWest_2 + P_SolarWest_2 + P_Cable_2
   = 10720.33898305085
 C_nodal_Ronne_3: - X_1_3 - L_0-Ronne-Nexo_3 - L_1-Ronne-Tejn_3
   + P_Biomass_3 + P_WindWest_3 + P_SolarWest_3 + P_Cable_3
   = 9858.757062146891
 C_nodal_Nexo_0: - X_0_0 + L_0-Ronne-Nexo_0 - L_2-Nexo-Tejn_0
   + P_WindEast_0 + P_SolarEast_0 = 7146.892655367232
 C_nodal_Nexo_1: - X_0_1 + L_0-Ronne-Nexo_1 - L_2-Nexo-Tejn_1
   + P_WindEast_1 + P_SolarEast_1 = 10720.33898305085
 C_nodal_Nexo_2: - X_0_2 + L_0-Ronne-Nexo_2 - L_2-Nexo-Tejn_2
   + P_WindEast_2 + P_SolarEast_2 = 10720.33898305085
 C_nodal_Nexo_3: - X_0_3 + L_0-Ronne-Nexo_3 - L_2-Nexo-Tejn_3
   + P_WindEast_3 + P_SolarEast_3 = 9858.757062146891
 C_nodal_Tejn_0: L_1-Ronne-Tejn_0 + L_2-Nexo-Tejn_0 + P_WindNorth_0
   + P_SolarNorth_0 = 7146.892655367232
 C_nodal_Tejn_1: L_1-Ronne-Tejn_1 + L_2-Nexo-Tejn_1 + P_WindNorth_1
   + P_SolarNorth_1 = 10720.33898305085
 C_nodal_Tejn_2: L_1-Ronne-Tejn_2 + L_2-Nexo-Tejn_2 + P_WindNorth_2
   + P_SolarNorth_2 = 10720.33898305085
 C_nodal_Tejn_3: L_1-Ronne-Tejn_3 + L_2-Nexo-Tejn_3 + P_WindNorth_3
   + P_SolarNorth_3 = 9858.757062146891
Bounds
 -11 <= X_0_0 <= 11
 -11 <= X_0_1 <= 11
 -11 <= X_0_2 <= 11
 -11 <= X_0_3 <= 11
 -11 <= X_1_0 <= 11
 -11 <= X_1_1 <= 11
 -11 <= X_1_2 <= 11
 -11 <= X_1_3 <= 11
 -100000 <= L_0-Ronne-Nexo_0 <= 100000
 -100000 <= L_0-Ronne-Nexo_1 <= 100000
 -100000 <= L_0-Ronne-Nexo_2 <= 100000
 -100000 <= L_0-Ronne-Nexo_3 <= 100000
 -100000 <= L_1-Ronne-Tejn_0 <= 100000
 -100000 <= L_1-Ronne-Tejn_1 <= 100000
 -100000 <= L_1-Ronne-Tejn_2 <= 100000
 -100000 <= L_1-Ronne-Tejn_3 <= 100000
 -100000 <= L_2-Nexo-Tejn_0 <= 100000
 -100000 <= L_2-Nexo-Tejn_1 <= 100000
 -100000 <= L_2-Nexo-Tejn_2 <= 100000
 -100000 <= L_2-Nexo-Tejn_3 <= 100000
 P_Biomass_0 <= 15000
 P_Biomass_1 <= 15000
 P_Biomass_2 <= 15000
 P_Biomass_3 <= 15000
 P_WindWest_0 <= 8333.333333333334
 P_WindWest_1 <= 8333.333333333334
 P_WindWest_2 <= 5829.648252961087
 P_WindWest_3 <= 5829.648252961085
 P_WindNorth_0 <= 8333.333333333334
 P_WindNorth_1 <= 8333.333333333334
 P_WindNorth_2 <= 5829.648252961087
 P_WindNorth_3 <= 5829.648252961085
 P_WindEast_0 <= 8333.333333333334
 P_WindEast_1 <= 8333.333333333334
 P_WindEast_2 <= 5829.648252961087
 P_WindEast_3 <= 5829.648252961085
 P_SolarWest_0 = 0
 P_SolarWest_1 <= 3333.33333333333
 P_SolarWest_2 <= 3333.333333333333
 P_SolarWest_3 = 0
 P_SolarNorth_0 = 0
 P_SolarNorth_1 <= 3333.33333333333
 P_SolarNorth_2 <= 3333.333333333333
 P_SolarNorth_3 = 0
 P_SolarEast_0 = 0
 P_SolarEast_1 <= 3333.33333333333
 P_SolarEast_2 <= 3333.333333333333
 P_SolarEast_3 = 0
 -80000 <= P_Cable_0 <= 80000
 -80000 <= P_Cable_1 <= 80000
 -80000 <= P_Cable_2 <= 80000
 -80000 <= P_Cable_3 <= 80000
Binaries
 Y_0_0_0 Y_0_0_1 Y_0_0_2 Y_0_0_3 Y_0_0_4 Y_0_0_5 Y_0_0_6 Y_0_1_0 Y_0_1_1
 Y_0_1_2 Y_0_1_3 Y_0_1_4 Y_0_1_5 Y_0_1_6 Y_0_2_0 Y_0_2_1 Y_0_2_2 Y_0_2_3
 Y_0_2_4 Y_0_2_5 Y_0_2_6 Y_0_3_0 Y_0_3_1 Y_0_3_2 Y_0_3_3 Y_0_3_4 Y_0_3_5
 Y_0_3_6 Y_1_0_0 Y_1_0_1 Y_1_0_2 Y_1_0_3 Y_1_0_4 Y_1_0_5 Y_1_0_6 Y_1_1_0
 Y_1_1_1 Y_1_1_2 Y_1_1_3 Y_1_1_4 Y_1_1_5 Y_1_1_6 Y_1_2_0 Y_1_2_1 Y_1_2_2
 Y_1_2_3 Y_1_2_4 Y_1_2_5 Y_1_2_6 Y_1_3_0 Y_1_3_1 Y_1_3_2 Y_1_3_3 Y_1_3_4
 Y_1_3_5 Y_1_3_6
End
