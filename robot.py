#!/usr/bin/env python3

import magicbot
import wpilib
import ctre

from components.intake import Intake

class Robot(magicbot.MagicRobot):
  intake: Intake

  def createObjects(self):
    """Create motors and stuff here."""
    self.intake_motor = ctre.TalonSRX(0)
    self.game_pad = wpilib.XboxController(1)

  def teleopInit(self):
    """Initialise driver control."""
    pass

  def teleopPeriodic(self):
    """Allow the drivers to control the robot (20 times a sec)"""
    if self.game_pad.getAButtonPressed():
      self.intake.toggle()
    if self.game_pad.getBButtonPressed():
      self.intake.stop()
    if self.game_pad.getXButtonPressed():
      self.intake.emergency_stop()

if __name__ == "__main__":
  wpilib.run(Robot)