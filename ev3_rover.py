#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1
from time import sleep

# Initialize motors
tank = MoveTank(OUTPUT_B, OUTPUT_C)

# Initialize ultrasonic sensor
ultrasonic = UltrasonicSensor(INPUT_1)

print("Trash Distribution Rover Started")

SAFE_DISTANCE = 25

def move_forward():
    tank.on(40, 40)

def stop():
    tank.off()

def turn_left():
    tank.on_for_seconds(-30, 30, 1.2)

def turn_right():
    tank.on_for_seconds(30, -30, 1.2)

while True:

    distance = ultrasonic.distance_centimeters

    print("Distance:", distance)

    if distance < SAFE_DISTANCE:

        stop()
        print("Obstacle detected")

        sleep(1)

        # Random turn decision
        turn_left()

    else:

        move_forward()

    sleep(0.2)
