import matplotlib.pyplot as plt
file = 'lab_data.txt'
f = open(file, 'r')
data_list = f.readlines()
time_data, x_data, y_data, v_data = [],[],[],[]
for i in range(2,len(data_list)):
    data_list[i] = data_list[i].replace(',','.')
    data = data_list[i].strip('\n').split('\t')
    time_data.append(float(data[0]))
    x_data.append(float(data[1]))
    y_data.append(float(data[2]))
    v_data.append(float(data[3]))

#banens form
posisjon = plt.figure('y(x)', figsize=(12, 6))
plt.plot(x_data,y_data)
plt.title('Banens form')
plt.xlabel('$x$ (m)', fontsize=20)
plt.ylabel('$y$ (m)', fontsize=20)
plt.grid()
plt.show()

#farten
fart = plt.figure('y(x)', figsize=(12, 6))
plt.plot(x_data, v_data)
plt.title('Farten')
plt.xlabel('$x$ (m)', fontsize=20)
plt.ylabel('$v()$ (m/s)', fontsize=20)
plt.grid()
plt.show()


#farten som funskjon av tid
farttid = plt.figure('y(x)', figsize=(12, 6))
plt.plot(time_data, v_data)
plt.title('Farten')
plt.xlabel('$x$ (m)', fontsize=20)
plt.ylabel('$v()$ (m/s)', fontsize=20)
plt.grid()
plt.show()



