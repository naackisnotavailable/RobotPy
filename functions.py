import robot
import wpilib
from wpilib.drive import DifferentialDrive
import wpilib.drive
import ctre
import rev
from ntcore import _ntcore
import wpilib.interfaces
import time

def tankDrive(leftX, leftY):
        try:
                leftX = float(leftX)
                leftY = float(leftY)
                return (leftY-leftX, -1 * (leftY + leftX))
        except Exception as e:
                print(str(e))
def moveArm(toggleRT):
        return toggleRT

def balancePreset(wheelCir):
        return moveDist(100)

def moveDist(x):
            pi = 3.141592
            wheelDia = 20
            revDist = wheelDia * pi
            deg = x * 360 / revDist
            return deg
def tagDist(ta):
        59.6
        49.7