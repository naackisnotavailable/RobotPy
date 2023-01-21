import wpilib
from wpilib.drive import DifferentialDrive
import wpilib.drive
import ctre
import rev
from ntcore import _ntcore
import wpilib.interfaces

import tank


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

        self.leftMotors = (self.leftTalon1, self.leftTalon2)
        self.rightMotors = (self.rightTalon1, self.rightTalon2)

        self.stick = wpilib.XboxController(0) # its something 0-5 lol


    def teleopPeriodic(self):
        Ysped = 0.25 * self.stick.getLeftY()
        Xsped = 0.25 * self.stick.getLeftX()
        #lefty = 0.5 * self.stick.getLeftY()
        #righty = 0.5 * self.stick.getRightY()

        #self.leftTalon1.set(ctre.ControlMode.PercentOutput, lefty)
        #self.leftTalon2.set(ctre.ControlMode.PercentOutput, lefty)
        #self.rightTalon1.set(ctre.ControlMode.PercentOutput, righty)
        #self.rightTalon2.set(ctre.ControlMode.PercentOutput, righty)
#
        self.leftTalon1.set(ctre.ControlMode.PercentOutput, Ysped - Xsped)
        self.leftTalon2.set(ctre.ControlMode.PercentOutput, Ysped - Xsped)
        self.rightTalon1.set(ctre.ControlMode.PercentOutput, -1 * (Ysped + Xsped))
        self.rightTalon2.set(ctre.ControlMode.PercentOutput, -1 * (Ysped + Xsped))
        #if abs(sped) >= 0.05:
        #    self.leftTalon1.set(ctre.ControlMode.PercentOutput, sped)
        #    self.leftTalon2.set(ctre.ControlMode.PercentOutput, sped)
        #    self.rightTalon1.set(ctre.ControlMode.PercentOutput, sped)
        #    self.rightTalon2.set(ctre.ControlMode.PercentOutput, sped)
        #elif abs(sped) <= 0.2:
        #    self.leftTalon1.set(ctre.ControlMode.PercentOutput, 0.0)
        #    self.leftTalon2.set(ctre.ControlMode.PercentOutput, 0.0)
        #    self.rightTalon1.set(ctre.ControlMode.PercentOutput, 0.0)
        #    self.rightTalon2.set(ctre.ControlMode.PercentOutput, 0.0)

if __name__ == "__main__":
    wpilib.run(Robot)