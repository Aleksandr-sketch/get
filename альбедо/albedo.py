import lightFunctions as j
import matplotlib.pyplot as plt
import numpy as np

white = j.white_lamp
red = j.red
blue = j.blue
yellow = j.yellow
green = j.green

x1 = np.array(np.arange(0, 200, 1))
x2 = 1.64*x1 + 378.72
n1 = 0
n2 = 200
x2 = x2[n1:n2]
albedo_white = white[n1:n2]/white[n1:n2]
albedo_yellow= yellow[n1:n2]/white[n1:n2]
albedo_red = red[n1:n2]/white[n1:n2]
albedo_green = green[n1:n2]/white[n1:n2]
albedo_blue = blue[n1:n2]/white[n1:n2]

plt.plot(x2, white, 'black', label='белый')
plt.plot(x2, red, 'red', label='красный')
plt.plot(x2, blue, 'blue', label='синий')
plt.plot(x2, yellow, 'yellow', label='желтый')
plt.plot(x2, green, 'green', label='зеленый')
'''
plt.plot(x2, albedo_white, 'black', label='белый')
plt.plot(x2, albedo_red, 'red', label='красный')
plt.plot(x2, albedo_yellow, 'yellow', label='желтый')
plt.plot(x2, albedo_green, 'green', label='зеленый')
plt.plot(x2, albedo_blue, 'blue', label='синий')
'''
plt.ylabel('Альбедо, о.е.')
plt.xlabel('Длина волны, нм')
plt.legend()
plt.minorticks_on()
plt.grid(which='minor', alpha=0.2)
plt.grid(which='major', alpha=0.5)
plt.show()
