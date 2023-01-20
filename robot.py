import wpilib
import wpilib.drive
import rev
import ctre
import time
import wpilib.interfaces
from ntcore import _ntcore
import navx


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        #time.sleep(5.0)
        #navx.AHRS.__init__(wpilib._wpilib.SPI.Port.kMXP, 500000, 60)  # try .createspi if it doesnt work
        # https://robotpy.readthedocs.io/projects/navx/en/stable/api.html

        #self.Talon1 = ctre._ctre.TalonFX(5)
        #self.Talon2 = ctre._ctre.TalonFX(6)
        #self.Talon3 = ctre._ctre.TalonFX(7)
        #self.Talon4 = ctre._ctre.TalonFX(8)

        #self.Talon1.configAllSettings(ctre._ctre.TalonFXConfiguration, 50)
        #self.Talon2.configAllSettings(ctre._ctre.TalonFXConfiguration, 50)
        #self.Talon3.configAllSettings(ctre._ctre.TalonFXConfiguration, 50)
        #self.Talon4.configAllSettings(ctre._ctre.TalonFXConfiguration, 50)

        self.leftMotor = rev.CANSparkMax(22, rev.CANSparkMax.MotorType.kBrushless)

        #self.l_stick = wpilib.Joystick(0)
        #self.r_stick = wpilib.Joystick(1)

    def teleopPeriodic(self):
        #table = NetworkTables.getTable("limelight")
        #self.rightMotor.set(ctre._ctre.TalonFXControlMode.PercentOutput, float(0.5))
        #self.Talon1.set(ctre._ctre.ControlMode.PercentOutput, 0.5, ctre._ctre.DemandType.AuxPID, 0.5) 
        #self.Talon2.set(ctre._ctre.ControlMode.PercentOutput, 0.5, ctre._ctre.DemandType.AuxPID, 0.5)
        #self.Talon3.set(ctre._ctre.ControlMode.PercentOutput, 0.5, ctre._ctre.DemandType.AuxPID, 0.5)
        #self.Talon4.set(ctre._ctre.ControlMode.PercentOutput, 0.5, ctre._ctre.DemandType.AuxPID, 0.5)

        inst = _ntcore.NetworkTableInstance.getDefault()
        table = inst.getTable("limelight")
        table.putNumber('ledmode', 3)
        table.putNumber('camMode', 0)
        tv = table.getNumber('tv', None)
        self.leftMotor.setVoltage(1.0)
        table.putNumber('ledMode', 3)
        table.putNumber('camMode', 0)
        tv = table.getNumber('tv', None)

        self.leftMotor.set(0.5) #Random NEO motor

        while t<= 2:
            t+=0.1
            time.sleep(0.2)
        self.leftMotor.setVoltage(0.0)
        while True:
            if tv == 1:
                self.leftMotor.setVoltage(1.0)
            elif tv == 0:
                self.leftMotor.setVoltage(0.0)
            time.sleep(1)
        


if __name__ == "__main__":
    wpilib.run(Robot)