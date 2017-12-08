import random
def get_delta_distance(Hcar,Tcar):
    return Hcar.distance - Tcar.distance

# core of  this project
# to be improved
def reaction_of_change(car):
    Hacc = car.Hcar.acc
    delta_distance = get_delta_distance(car.Hcar,car)
    if Hacc >= 0:
        car.acc = Hacc * (delta_distance/50)*random.uniform(-0.01, 0.01)
    elif Hacc< 0:
        car.acc = Hacc * 1.5*random.uniform(-0.01, 0.01)


def print_distance_result(cars):
    distance_result = []
    for car in cars :
        distance_result.append(car.name + ': ' + str(int(car.distance)))
    print(distance_result[0] + '  ' + distance_result[1])

def cars_driving_forward(cars,time):
    for car in cars :
        if car.acc == 0 :
            car.distance += car.speed*time
            car.distance_result.append(car.distance)
        elif car.acc != 0 :
            car.distance += car.speed*time + car.acc*time*time/2
            #car.distance_result.append(car.distance)