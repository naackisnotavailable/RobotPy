import wpilib
import wpilib.drive
import ctre
import rev
from ntcore import _ntcore
import wpilib.interfaces


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        #time.sleep(5.0)
        #navx.AHRS.create_spi(wpilib._wpilib.SPI.Port.kMXP, 500000, 60)  # try .createspi if it doesnt work
        # https://robotpy.readthedocs.io/projects/navx/en/stable/api.html
        #self.Talon1.configMotionAcceleration(0.5, 0)

        self.neo1 = rev.CANSparkMax(14, rev.CANSparkMax.MotorType.kBrushless)
        self.leftTalon1 = ctre.TalonFX(5)
        self.leftTalon2 = ctre.TalonFX(6)
        self.rightTalon1 = ctre.TalonFX(7)
        self.rightTalon2 = ctre.TalonFX(8)
        self.leftTalon1.configFactoryDefault()
        self.leftTalon2.configFactoryDefault()
        self.rightTalon1.configFactoryDefault()
        self.rightTalon2.configFactoryDefault()
        #self.leftTalon2.setInverted(True)
        #self.l_stick = wpilib.Joystick(0)
        #self.r_stick = wpilib.Joystick(1)
        self.stick = wpilib.XboxController(0) # its something 0-5 lol

    def teleopPeriodic(self):
        sped = self.stick.getLeftY()
        if abs(sped) >= 0.05:
            self.leftTalon1.set(ctre.ControlMode.PercentOutput, sped)
            self.leftTalon2.set(ctre.ControlMode.PercentOutput, sped)
            self.rightTalon1.set(ctre.ControlMode.PercentOutput, sped)
            self.rightTalon2.set(ctre.ControlMode.PercentOutput, sped)
        elif abs(sped) <= 0.2:
            self.leftTalon1.set(ctre.ControlMode.PercentOutput, 0.0)
            self.leftTalon2.set(ctre.ControlMode.PercentOutput, 0.0)
            self.rightTalon1.set(ctre.ControlMode.PercentOutput, 0.0)
            self.rightTalon2.set(ctre.ControlMode.PercentOutput, 0.0)


if __name__ == "__main__":
    wpilib.run(Robot)
