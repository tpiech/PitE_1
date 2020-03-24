#flight simulator

import random
import time

############################## class representing plane
class Plane:
    def __init__(self): 
        self.right_wing_angle = 0
        self.left_wing_angle = 180
        print("Welcome on board")
        print('')
    def turblations(self, tilt_angle):
        self.right_wing_angle = tilt_angle
        self.left_wing_angle =  180 - self.right_wing_angle
    def check_angles(self):
        if self.right_wing_angle > 20 or self.right_wing_angle < -20:
            print("WARINIG! Plane's roll is " + str(self.right_wing_angle) )
            print("Correcting")
            for i in range(1,4):
                print("." * i)
                time.sleep(1)
            self.right_wing_angle = 0
            self.left_wing_angle = 180
###################################


#################################### function simulating flight - turbulations are happening or not
def flight_time(My_Plane):
    rand_angle = random.gauss(0, 45)
    My_Plane.turblations(rand_angle)
    print("Right wing: " + str( My_Plane.right_wing_angle ) + " Left wing: "  + str(My_Plane.left_wing_angle) )
    My_Plane.check_angles()
    print("Current angles: Right: " + str(My_Plane.right_wing_angle) + " Left: " + str(My_Plane.left_wing_angle))   
#####################################



################################## function simulating plane flight

def start_of_flight():
    print('Starting of the plane')
    My_Plane = Plane()
    while True:
        flight_time(My_Plane)
        print('\n')
        time.sleep(1)
################################



#let's go!
start_of_flight() 