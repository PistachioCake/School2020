# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  02b Program 1
# Date:        09 03 2020

from math import tan

print('Rushil Udani, UIN: 730003662')
print('My favorite ice cream is dark chocolate sea salt caramel. Yum!')

# Ohm's Law: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
voltage = 20
resistance = 5
current = voltage * resistance
print(current)

# Kinetic Energy: https://www.britannica.com/science/kinetic-energy
mass = 100
velocity = 21
energy = 1/2 * mass * velocity**2
print(energy)

# Reynold's Number: https://byjus.com/reynolds-number-formul
velocity = 100
viscosity = 1.2
lin_dim = 2.5
reynolds_number = velocity * lin_dim / viscosity
print(reynolds_number)

# Stefan-Boltzmann Law: https://www.sciencedirect.com/topics/earth-and-planetary-sciences/stefan-boltzmann-law
temperature = 2200
SB_constant = 5.67e-8
flux_density = SB_constant * temperature ** 4
print(flux_density)

# Mohr Coulomb Failure Criterion: https://abaqus-docs.mit.edu/2017/English/SIMACAETHERefMap/simathe-c-mohrcoulomb.htm
cohesion = 2
normal_stress = 20
angle_internal_friction = 35
shear_stress = cohesion - normal_stress * tan(angle_internal_friction)
print(shear_stress)
