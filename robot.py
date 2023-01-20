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

        #self.l_stick = wpilib.Joystick(0)
        #self.r_stick = wpilib.Joystick(1)
        self.stick = wpilib.XboxController(0) # its something 0-5 lol

    def teleopPeriodic(self):
        inst = _ntcore.NetworkTableInstance.getDefault()
        table = inst.getTable("limelight")

        table.putNumber('ledMode', 3)
        table.putNumber('camMode', 0)
        tv = table.getNumber('tv', None)
        tx = table.getNumber('tx', None)
        ty = table.getNumber('ty', None)
        ta = table.getNumber('ta', None)

        if tv == True:
            self.neo1.set(0.5)
        if tv == False:
            self.neo1.set(0.0)

if __name__ == "__main__":
    wpilib.run(Robot)

