from Car import *
from tools import *
import random
import matplotlib.pyplot as plt

delay = 0.4 # second
i = 0

car1 = Car(40,60,'car1')
car2 = Car(0,60,'car2')
car2.Hcar = car1

cars = [car1,car2]
# while(i<100):
#     if random.uniform(1,10) <= 2:
#         car1.change_speed(random.uniform(-1, 1))
#         cars_driving_forward(cars,delay)
#         reaction_of_change(car2)
#     else:
#         cars_driving_forward(cars,delay)
#     print_distance_result(cars)
#     i += 1
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()