import wpilib
import wpilib.drive
#from wpilib.drive import DifferentialDrive
import rev
import ctre
import time
#from networktables import NetworkTable
#import cv2
#import networktables.networktable
#from networktables import NetworkTablesInstance as NetworkTables
#from networktables.networktable import NetworkTable as nt
#from networktables import NetworkTables
#from pynetworktables import NetworkTables
from ntcore import _ntcore

 #init networktabless

#tx = table.getNumber('tx',None)
#ty = table.getNumber('ty',None)
#ta = table.getNumber('ta',None)
#ts = table.getNumber('ts',None)

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        time.sleep(5.0)
        #NetworkTables.initialize(server='10.55.30.2')
        self.leftMotor = rev.CANSparkMax(22, rev.CANSparkMax.MotorType.kBrushless)
        #ctre.TalonFXControlMode.PercentOutput
        self.rightMotor = ctre.TalonFX(5, None)
        self.rightMotor.configAllSettings(ctre._ctre.TalonFXConfiguration, 0)
        #self.driveTrain = DifferentialDrive(self.leftMotor, self.rightMotor)

        #wpilib.CameraServer.launch()

        #self.l_stick = wpilib.Joystick(0)
        #self.r_stick = wpilib.Joystick(1)

    def teleopPeriodic(self):
        #table = NetworkTables.getTable("limelight")
        self.rightMotor.set(ctre._ctre.TalonFX, ctre._ctre.TalonFXControlMode.PercentOutput, float(0.5))
        inst = _ntcore.NetworkTableInstance.getDefault()
        table = inst.getTable("limelight")
        table.putNumber('ledmode', 3)
        table.putNumber('camMode', 0)
        tv = table.getNumber('tv', None)
        
        #table.putNumber('ledMode', 3)
        #table.putNumber('camMode', 0)
        #tv = table.getNumber('tv', None)

        # Create tank drive
        #self.driveTrain.tankDrive(self.l_stick.getY(), self.r_stick.getY())
        t = 0
        self.leftMotor.setVoltage(1.0)
        while t<= 2:
            t+=0.1
            time.sleep(0.2)
        self.leftMotor.setVoltage(0.0)

        if tv == 1:
            self.leftMotor.setVoltage(1.0)
        elif tv == 0:
            self.leftMotor.setVoltage(0.0)
        


if __name__ == "__main__":
    wpilib.run(Robot)
