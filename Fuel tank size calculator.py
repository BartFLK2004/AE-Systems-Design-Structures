# Fuel tank size calculator
import math

#Fuel data
Mass_MMH = 504.58           #[kg]
rho_MMH = 0.88              #[kg m^-3]
Molarmass_MMH = 46.07       #[g mol^-1]
mol_MMH = (Mass_MMH * 10 **3) / Molarmass_MMH

Mass_NO = 825.68
rho_NO = 1.44
Molarmass_NO = 92.011
mol_NO =  (Mass_NO * 10 **3) / Molarmass_NO

Mass_He = 0
rho_He = 0.000166
Molarmass_He = 4.003
mol_He =  (Mass_He * 10 **3) / Molarmass_He

#tank geometry data
radius_out = 0.001          #[m]
thickness = 0.0001          #[m]
pressure = 27500000           #[Pa]
Volume_tank = 0             #[m^3]
Safety_factor = 2
h_cylinder = 0              #[m]

#tank material data
#Using Ti-6Al-6V-SN:
rho_tank = 4.54 * 1000      #[kg m^-3]
Yield_stress = 1210 * 10 ** 6    #[Pa]

def hoop_stress (pressure, thickness, radius):
    return (pressure * radius) / thickness

def tank_mass (radius_out, thickness, h_cylinder, rho_tank):
    radius_in = radius_out - thickness
    Volume_tank = h_cylinder * math.pi * (radius_out ** 2 - radius_in ** 2) + 4/3 * math.pi * (radius_out ** 3 - radius_in ** 3)
    mass_tank = rho_tank * Volume_tank
    return mass_tank

def tank_volume (radius_in, h_cylinder):
    return math.pi * h_cylinder * radius_in ** 2 + (4/3) * math.pi * radius_in ** 3
    


optimal_mass = float('inf')
optimal_dimensions = None

thickness = 0.0001
while thickness <0.05:
    radius_out = 0.001
    h_cylinder = 0
    while radius_out <0.36:    
        stress = 0.5 * hoop_stress(pressure, thickness, radius_out - 0.5 * thickness)
        if stress <= Yield_stress / Safety_factor and tank_volume(radius_out - thickness, h_cylinder) >= 0.0964:
            mass = tank_mass (radius_out, thickness, h_cylinder, rho_tank)
            if mass < optimal_mass:
                optimal_mass = mass
                optimal_dimensions = thickness, radius_out
        radius_out += 0.001
    while h_cylinder < 1:
        stress = hoop_stress(pressure, thickness, radius_out - 0.5 * thickness)
        if stress <= Yield_stress / Safety_factor and tank_volume(radius_out - thickness, h_cylinder) >= 0.0964:
            mass = tank_mass (radius_out, thickness, h_cylinder, rho_tank)
            if mass < optimal_mass:
                optimal_mass = mass
                optimal_dimensions = thickness, radius_out, h_cylinder
        h_cylinder += 0.001
    thickness += 0.0001

print(f'Optimal mass is: {optimal_mass} kg')
print(f'optimal dimensions are (thickness, radius): {optimal_dimensions}')







    