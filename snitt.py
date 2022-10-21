sluttfart = [1.152,1.153,1.144,1.148,1.138,1.161,1.151,1.147,1.145,1.157]

average_final_velocity = sum(sluttfart)/len(sluttfart)
error_up_value = max(sluttfart)-average_final_velocity
error_down_value = average_final_velocity-min(sluttfart)
max_error = max(error_up_value,error_down_value)
max_percentage_error = max_error/average_final_velocity

m = 0.031
average_kinetic_energy = 1/2*m*average_final_velocity**2
kinetic_energy_error_up = 1/2*m*(average_final_velocity+error_up_value)**2
kinetic_energy_error_down = 1/2*m*(average_final_velocity-error_down_value)**2
max_kinetic_energy_error = max(kinetic_energy_error_down,kinetic_energy_error_up)
max_kinetic_energy_error_percentage = max_kinetic_energy_error/average_kinetic_energy


print(f"Den gjennomsnittlige sluttfarten er: {average_final_velocity} m/s")
print(f"Det positive avviket har en verdi på: {error_up_value:.4f} m/s")
print(f"Det negative avviket har en verdi på: {error_down_value:.4f} m/s")
print(f"Det maksimale avviket har dermed en verdi på: {max_error:.4f} m/s")
print(f"Dette gir oss en gjennomsnittlig sluttfart på: {average_final_velocity} m/s ± {max_percentage_error:.2f}%")
print("\n"f"Den gjennomsnittlige kinetiske energien til kula er: {average_kinetic_energy:.4f} J")
print(f"Det positive avviket til den kinetiske energien har en verdi på: {kinetic_energy_error_up:.4f} J")
print(f"Det negative avviket til den kinetiske energien har en verdi på: {kinetic_energy_error_down:4f} J")
print(f"Det maksimale avviket til den kinetiske energien har dermed en verdi på: {max_kinetic_energy_error:.4f} J")
print(f"Dette gir oss en gjennomsnittlig kinetisk energi på: {average_kinetic_energy:.4f} J ± {max_kinetic_energy_error_percentage:.2f}%")
