import wpilib
from wpilib.drive import DifferentialDrive
import wpilib.drive
import ctre
import rev
from ntcore import _ntcore
import wpilib.interfaces
import time

import functions


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.neo1 = rev.CANSparkMax(14, rev.CANSparkMax.MotorType.kBrushless)
        self.leftTalon1 = ctre.TalonFX(5)
        self.leftTalon2 = ctre.TalonFX(6)
        self.rightTalon1 = ctre.TalonFX(7)
        self.rightTalon2 = ctre.TalonFX(8)
        self.leftTalon1.configFactoryDefault()
        self.leftTalon2.configFactoryDefault()
        self.rightTalon1.configFactoryDefault()
        self.rightTalon2.configFactoryDefault()
        self.leftTalon1.configIntegratedSensorAbsoluteRange(360)

        self.leftMotors = (self.leftTalon1, self.leftTalon2)
        self.rightMotors = (self.rightTalon1, self.rightTalon2)

        self.stick = wpilib.XboxController(0) # its something 0-5 lol

    def teleopPeriodic(self):
        (leftMotorSpeed, rightMotorSpeed) = functions.tankDrive(self.stick.getLeftX(), self.stick.getLeftY())
        for x in self.leftMotors:
            x.set(ctre._ctre.TalonFXControlMode.PercentOutput, 0.25)
        for x in self.rightMotors:
            x.set(ctre._ctre.TalonFXControlMode.PercentOutput, 0.25)
    def autonomousPeriodic(self):
        deg = functions.moveDist(100)
        self.rightTalon2.set(ctre._ctre.TalonFXControlMode.Position, deg)




if __name__ == "__main__":
    wpilib.run(Robot)