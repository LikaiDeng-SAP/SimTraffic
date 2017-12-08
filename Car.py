class Car(object):

    def __init__(self,initialDistance,initialSpeed,name):
        self.distance = initialDistance
        self.acc = 0
        self.speed = initialSpeed
        self.name = name

    def change_speed(self,acc):
        self.speed += acc

    def drive_forward(self,time,acc):
        if acc == 0 :
            self.distance += self.speed*time
        elif acc != 0 :
            self.distance += self.speed*time + acc*time*time/2
        #print(self.name +': ' + str(self.distance))
