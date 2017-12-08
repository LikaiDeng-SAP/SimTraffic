class Car(object):
    def __init__(self,initialDistance,initialSpeed,name):
        self.distance = initialDistance
        self.acc = 0
        self.speed = initialSpeed
        self.name = name
        self.self_distance_result = []
        self.self_speed_result = []

    def change_speed(self,acc):
        self.speed += acc
        self.self_speed_result.append(self.speed)

    def drive_forward(self,time,acc):
        if acc == 0 :
            self.distance += self.speed*time
            self.self_distance_result.append(int(self.distance))
        elif acc != 0 :
            self.distance += self.speed*time + acc*time*time/2
            self.self_distance_result.append(int(self.distance))
