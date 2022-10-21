import matplotlib.pyplot as plt
file = 'lab_data.txt'
f = open(file, 'r')
data_list = f.readlines()
time_data, x_data, y_data, v_data, ek_data = [],[],[],[],[]
m = 0.031
r = 0.011
I = (2/5)*m*(r**2)

for i in range(2,len(data_list)):
    data_list[i] = data_list[i].replace(',','.')
    data = data_list[i].strip('\n').split('\t')
    time_data.append(float(data[0]))
    x_data.append(float(data[1]))
    y_data.append(float(data[2]))
    v_data.append(float(data[3]))
    omega = float(data[3])/r
    e_kinetic = (1/2)*m*(float(data[3])**2)
    e_rotation = (1/2)*I*(omega**2)
    ek_data.append(e_kinetic+e_rotation)


#banens form
posisjon = plt.figure('y(x)', figsize=(12, 6))
plt.plot(x_data,y_data)
plt.title('Banens form')
plt.xlabel('$x$ (m)', fontsize=20)
plt.ylabel('$y$ (m)', fontsize=20)
plt.grid()
plt.show()

#farten som funskjon av tid
farttid = plt.figure('y(x)', figsize=(12, 6))
plt.plot(time_data, v_data)
plt.title('Farten')
plt.xlabel('$x$ (m)', fontsize=20)
plt.ylabel('$v$ (m/s)', fontsize=20)
plt.grid()
plt.show()


#farten
fart = plt.figure('y(x)', figsize=(12, 6))
plt.plot(x_data, v_data)
plt.title('Farten')
plt.xlabel('$x$ (m)', fontsize=20)
plt.ylabel('$v$ (m/s)', fontsize=20)
plt.grid()
plt.show()

#kinetisk energi
kinetiskenergi = plt.figure('y(x)', figsize=(12, 6))
plt.plot(x_data, ek_data)
plt.title('Kinetisk energi')
plt.xlabel('$x$ (m)', fontsize=20)
plt.ylabel('$EK$ (J)', fontsize=20)
plt.grid()
plt.show()






