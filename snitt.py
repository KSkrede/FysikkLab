import numpy as np
from scipy.stats import sem

sluttfart = [1.152,1.153,1.144,1.148,1.138,1.161,1.151,1.147,1.145,1.157]

average_velocity = np.mean(sluttfart)
standard_deviation = np.std(sluttfart)
standard_error = sem(sluttfart)
relative_error = standard_error/average_velocity

m = 0.031
r = 0.011
I = (2/5)*m*(r**2)
average_omega = average_velocity/r
standard_omega_error = standard_error/r
relative_omega_error = relative_error/r
average_kinetic_energy = 1/2*m*(average_velocity**2) + 1/2*I*(average_omega**2)
standard_kinetic_energy_error = 1/2*m*(standard_error**2) + 1/2*I*(standard_omega_error**2)
relative_kinetic_energy_error = 1/2*m*(relative_error**2) + 1/2*I*(relative_omega_error**2)

print(f"Gjennomsnittlig sluttfart på: {average_velocity:.2f} m/s ± {standard_error:.5f}")
print(f"Gjennomsnittlig sluttfart på: {average_velocity:.2f} m/s ± {relative_error:.5f}%")
print(f"Gjennomsnittlig kinetisk energi på: {average_kinetic_energy:.4f} J ± {standard_kinetic_energy_error:.10f}")
print(f"Gjennomsnittlig kinetisk energi på: {average_kinetic_energy:.4f} J ± {relative_kinetic_energy_error:.10f}%")



