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

        self.leftTalon1 = ctre._ctre.TalonFX(5)
        self.leftTalon2 = ctre._ctre.TalonFX(6)
        self.rightTalon1 = ctre._ctre.TalonFX(7)
        self.rightTalon2 = ctre._ctre.TalonFX(8)

        self.leftTalon1.configFactoryDefault()
        self.leftTalon2.configFactoryDefault()
        self.rightTalon1.configFactoryDefault()
        self.rightTalon2.configFactoryDefault()

        self.leftTalon1.setInverted(True)
        self.rightTalon1.setInverted(True)
        #self.Talon1.configMotionAcceleration(0.5, 0)
        self.neo1 = rev.CANSparkMax(14, rev.CANSparkMax.MotorType.kBrushless)

        #self.l_stick = wpilib.Joystick(0)
        #self.r_stick = wpilib.Joystick(1)
        self.stick = wpilib.XboxController(0) # its something 0-5 lol

    def teleopPeriodic(self):
        #table = NetworkTables.getTable("limelight")
        #self.rightMotor.set(ctre._ctre.TalonFXControlMode.PercentOutput, float(0.5))
        sped = self.stick.getLeftY()
        if abs(sped) >= 0.05:
            self.neo1.set(float(sped))
        #sped = bool(self.stick.getAButtonPressed)
        #while True:
        #    if sped == True:
#
        #        self.Talon1.set(ctre.ControlMode.PercentOutput, 0.25) 
        #        self.Talon2.set(ctre.ControlMode.PercentOutput, 0.25)
        #        self.Talon3.set(ctre.ControlMode.PercentOutput, 0.25)
        #        self.Talon4.set(ctre.ControlMode.PercentOutput, 0.25)
        #    elif sped == False:
        #        self.Talon1.set(ctre.ControlMode.PercentOutput, 0.0) 
        #        self.Talon2.set(ctre.ControlMode.PercentOutput, 0.0)
        #        self.Talon3.set(ctre.ControlMode.PercentOutput, 0.0)
        #        self.Talon4.set(ctre.ControlMode.PercentOutput, 0.0)

if __name__ == "__main__":
    wpilib.run(Robot)