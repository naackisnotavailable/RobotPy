import wpilib
import wpilib.drive
from wpilib.drive import DifferentialDrive
import rev
import ctre
from networktables import NetworkTables
import cv2
import ovl

table = NetworkTables.getTable("limelight")
tx = table.getNumber('tx',None)
ty = table.getNumber('ty',None)
ta = table.getNumber('ta',None)
ts = table.getNumber('ts',None)

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.leftMotor = rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushless)
        ctre.TalonFXControlMode.PercentOutput
        ovl.Camera.get
        #self.driveTrain = DifferentialDrive(self.leftMotor, self.rightMotor)

        #self.l_stick = wpilib.Joystick(0)
        #self.r_stick = wpilib.Joystick(1)

    def teleopPeriodic(self):
        # Create tank drive
        #self.driveTrain.tankDrive(self.l_stick.getY(), self.r_stick.getY())
        self.leftMotor.setVoltage(1.20)
        


if __name__ == "__main__":
    wpilib.run(Robot)
