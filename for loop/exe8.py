from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

robotArm.speed = 3
robotArm.moveRight()

for i in range(8):
    for i in range(8):
        robotArm.grab()
        robotArm.moveRight()
    for i in range(8):
        robotArm.drop()
        robotArm.moveLeft()

robotArm.wait()