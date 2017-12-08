from Car import *
from tools import *
import random
import matplotlib.pyplot as plt
import numpy as np

delay = 0.4 # second
i = 0

car1 = Car(40,60,'Hcar')
car2 = Car(0,60,'Tcar')
car2.Hcar = car1

cars = [car1,car2]
#ToDo
#change it into a dynamic way
#acc changes with distance every time point
while(i<1000):
    if random.uniform(1,10) <= 2:
        car1.change_speed(random.uniform(-1, 1))
        car1.drive_forward(delay,0)
        car2.drive_forward(delay, 0)
        reaction_of_change(car2)
    else:
        car1.drive_forward(0.01, 0)
        car2.drive_forward(0.01, 0)
    print_distance_result(cars)
    i += 1

print(len(car1.self_distance_result))
x = np.linspace(0,1000,1000)
y1 = car1.self_distance_result
y2 = car2.self_distance_result
y1_array = np.array(y1)
y2_array = np.array(y2)

delta_distance_array = y1_array - y2_array
plt.plot(x,delta_distance_array)
#plt.plot(x,y2,color='red')
plt.ylabel('Disntance')
plt.xlabel('Time')
plt.show()
