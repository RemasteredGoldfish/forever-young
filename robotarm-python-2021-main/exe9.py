from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

robotArm.speed = 3
robotArm.grab()

for i in range(5):
    for i in range(5):    
        robotArm.moveRight()
    for i in range(5):
        robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()
robotArm.wait()