import numpy as np


sluttfart = [1.152,1.153,1.144,1.148,1.138,1.161,1.151,1.147,1.145,1.157]

average_velocity = sum(sluttfart)/len(sluttfart)
sum_deviation_squared = 0
for i in range(len(sluttfart)):
    sum_deviation_squared+= (sluttfart[i]-average_velocity)
standard_deviation = np.sqrt(sum_deviation_squared/(len(sluttfart)-1))
standard_error = standard_deviation/np.sqrt(len(sluttfart))


m = 0.031
r = 0.011
I = (2/5)*m*(r**2)
average_omega = average_velocity/r
average_omega_error = standard_error/r
average_kinetic_energy = 1/2*m*(average_velocity**2) + 1/2*I*(average_omega**2)
average_kinetic_energy_error = 1/2*m*(standard_error**2) + 1/2*I*(average_omega_error**2)

print(f"Gjennomsnittlig sluttfart på: {average_velocity} m/s ± {standard_error}")
print(f"Gjennomsnittlig kinetisk energi på: {average_kinetic_energy:.4f} J ± {average_kinetic_energy_error}")



