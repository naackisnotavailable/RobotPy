import wpilib
import wpilib.drive
import ctre
import rev
#from ntcore import _ntcore
#import navx
import wpilib.interfaces
#print(str(Ttest.TalonFXConfiguration.motionCruiseVelocity.getter))
#ctre._ctre.TalonFX.configAllSettings(ctre._ctre.TalonFXConfiguration)
class Robot(wpilib.TimedRobot):
    def robotInit(self):
        #time.sleep(5.0)
        #navx.AHRS.create_spi(wpilib._wpilib.SPI.Port.kMXP, 500000, 60)  # try .createspi if it doesnt work
        # https://robotpy.readthedocs.io/projects/navx/en/stable/api.html

        self.Talon1 = ctre._ctre.TalonFX(5)
        self.Talon2 = ctre._ctre.TalonFX(6)
        self.Talon3 = ctre._ctre.TalonFX(7)
        self.Talon4 = ctre._ctre.TalonFX(8)

        self.Talon1.configFactoryDefault()
        self.Talon2.configFactoryDefault()
        self.Talon3.configFactoryDefault()
        self.Talon4.configFactoryDefault()
        #self.Talon1.configMotionAcceleration(0.5, 0)
        self.leftMotor = rev.CANSparkMax(22, rev.CANSparkMax.MotorType.kBrushless)

        #self.l_stick = wpilib.Joystick(0)
        #self.r_stick = wpilib.Joystick(1)
        self.stick = wpilib.PS4Controller(int) # its something 0-5 lol

    def teleopPeriodic(self):
        #table = NetworkTables.getTable("limelight")
        #self.rightMotor.set(ctre._ctre.TalonFXControlMode.PercentOutput, float(0.5))

        connectStick = self.stick.isConnected
        if connectStick == True:
            self.leftMotor.set(0.5)
        sped = self.stick.getLeftY

        self.Talon1.set(ctre._ctre.ControlMode.PercentOutput, sped, ctre._ctre.DemandType.AuxPID, 0.5) 
        self.Talon2.set(ctre._ctre.ControlMode.PercentOutput, sped, ctre._ctre.DemandType.AuxPID, 0.5)
        self.Talon3.set(ctre._ctre.ControlMode.PercentOutput, sped, ctre._ctre.DemandType.AuxPID, 0.5)
        self.Talon4.set(ctre._ctre.ControlMode.PercentOutput, sped, ctre._ctre.DemandType.AuxPID, 0.5)


if __name__ == "__main__":
    wpilib.run(Robot)