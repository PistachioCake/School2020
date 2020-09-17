# By submitting this assignment, I agree to the following:
#  'Aggies do not lie, cheat, or steal, or tolerate those who do'
#  'I have not given or received any unauthorized aid on this assignment'
#
# Name:        Rushil Udani
# Section:     219
# Assignment:  02b Program 1
# Date:        09 03 2020

def color(s):
	return f'\u001b[38;5;165m{s}\u001b[0m'

print('Rushil Udani, UIN: 730003662')

# Kinetic Energy: https://www.britannica.com/science/kinetic-energy
print()
print(color('Calculating kinetic energy'))
mass = float(input('Mass: '))
velocity = float(input('Velocity: '))
energy = 1/2 * mass * velocity ** 2
print(energy)

# Reynold's Number: https://byjus.com/reynolds-number-formul
print()
print(color('Reynold\'s Number for a given fluid'))
velocity = float(input('Velocity: '))
viscosity = float(input('Viscosity: '))
lin_dim = float(input('Linear Dimension: '))
reynolds_number = velocity * lin_dim / viscosity
print(reynolds_number)

# Stefan-Boltzmann Law: https://www.sciencedirect.com/topics/earth-and-planetary-sciences/stefan-boltzmann-law
print()
print(color('Calculating the flux density of a given black body'))
temperature = float(input('Temperature: '))
SB_constant = float(input('Stefan-Boltzmann constant: '))
flux_density = SB_constant * temperature ** 4
print(flux_density)

