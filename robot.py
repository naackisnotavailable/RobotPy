import wpilib
import wpilib.drive
#from wpilib.drive import DifferentialDrive
import rev
import ctre
import time
import wpilib.interfaces

#from ctre import _ctre as ct
#from networktables import NetworkTable
#import cv2
#import networktables.networktable
#from networktables import NetworkTablesInstance as NetworkTables
#from networktables.networktable import NetworkTable as nt
#from networktables import NetworkTables
#from pynetworktables import NetworkTables
from ntcore import _ntcore
import navx


rightMotor11 = ctre.TalonFX(13)
rightMotor11.configAllSettings(ctre.TalonFXConfiguration, 0)
class Robot(wpilib.TimedRobot):
    def robotInit(self):
        #time.sleep(5.0)
        navx.AHRS.__init__(wpilib._wpilib.SPI.Port.kMXP, 500000, 60)  # try .createspi if it doesnt work
        # https://robotpy.readthedocs.io/projects/navx/en/stable/api.html
        self.rightMotor1 = ctre._ctre.TalonFX(5)
        self.rightMotor2 = ctre._ctre.TalonFX(6)
        self.leftMotor1 = ctre._ctre.TalonFX(7)
        self.leftMotor2 = ctre._ctre.TalonFX(8)
        #self.rightMotor.configAllSettings(ctre._ctre.TalonFXConfiguration, 50)
        #self.rightMotor.configAllSettings(ct.TalonFX, ct.TalonFXConfiguration, 50)
        #self.driveTrain = DifferentialDrive(self.leftMotor, self.rightMotor)
        self.leftMotor = rev.CANSparkMax(22, rev.CANSparkMax.MotorType.kBrushless)

        #self.rightMotor = ctre.TalonFX(5)

        #self.l_stick = wpilib.Joystick(0)
        #self.r_stick = wpilib.Joystick(1)

    def teleopPeriodic(self):
        #table = NetworkTables.getTable("limelight")
        #self.rightMotor.set(ctre._ctre.TalonFXControlMode.PercentOutput, float(0.5))
        self.rightMotor1.set(ctre._ctre.ControlMode.PercentOutput, 0.5, ctre._ctre.DemandType.AuxPID, 0.5)
        self.rightMotor2.set(ctre._ctre.ControlMode.PercentOutput, 0.5, ctre._ctre.DemandType.AuxPID, 0.5)
        self.leftMotor1.set(ctre._ctre.ControlMode.PercentOutput, 0.5, ctre._ctre.DemandType.AuxPID, 0.5)
        self.leftMotor2.set(ctre._ctre.ControlMode.PercentOutput, 0.5, ctre._ctre.DemandType.AuxPID, 0.5)


        #inst = _ntcore.NetworkTableInstance.getDefault()
        #table = inst.getTable("limelight")
        #table.putNumber('ledmode', 3)
        #table.putNumber('camMode', 0)
        #tv = table.getNumber('tv', None)
        #self.leftMotor.setVoltage(1.0)
        #table.putNumber('ledMode', 3)
        #table.putNumber('camMode', 0)
        #tv = table.getNumber('tv', None)

        # Create tank drive
        #self.driveTrain.tankDrive(self.l_stick.getY(), self.r_stick.getY())
        t = 0
        self.leftMotor.set(0.1)
        
        #while t<= 2:
        #    t+=0.1
        #    time.sleep(0.2)
        #self.leftMotor.setVoltage(0.0)
        #while True:
        #    if tv == 1:
        #        self.leftMotor.setVoltage(1.0)
        #    elif tv == 0:
        #        self.leftMotor.setVoltage(0.0)
        #    time.sleep(1)
    def autonomousPeriodic(self) -> None:

        return super().autonomousPeriodic()
        


if __name__ == "__main__":
    wpilib.run(Robot)