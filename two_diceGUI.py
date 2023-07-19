"""
Program: two_diceGUI.py
Author: Hamza 7/18/2023

GUI-based version of the two dice game which compares random number and provides the games outcome

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly
"""

from breezypythongui import EasyFrame
import random
from tkinter.font import Font
#Other imports go here

# Class header
class TwoDiceGUI(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):
		EasyFrame.__init__(self, title = "Two dice game", width = 340, height = 280, resizable = False, background = "seagreen")
		# add the various components tothe window
		self.addLabel(text = "Two dice game", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "seagreen", font = Font(family = "Impact", size = 30))
		self.addLabel(text ="Player's roll is:", row = 1, column = 0, sticky = "NE", background = "seagreen")
		self.playerRoll = self.addIntegerField(value = 0, row = 1, column = 1, width = 4, state = "readonly")
		self.addLabel(text = "Computer's roll is:", row = 1, column = 0, sticky = "NW", background = "seagreen")
		self.computerRoll = self.addIntegerField(value = 0, row = 1, column = 1, width = 4, state = "readonly", sticky = "NW")
		self.button = self.addButton(text = "Roll dice!", row = 3, column = 0, columnspan = 2, command = self.roll)
		self.resultArea = self.addLabel(text = "", row = 4, column = 0, columnspan = 2, background = "seagreen", foreground = "yellow", font = Font(family = "Georgia", size = 20), sticky = "NSEW")
	# defintition of the roll() function
	def roll(self):
		# variables for this function
		playerDie = random.randint(1, 6)
		compDie = random.randint(1, 6)

		# processing phase
		if playerDie > compDie:
			result = "congratulations, you win!"
			self.resultArea["foreground"] = "yellow"
		elif playerDie < compDie:
			result = "Sorry, you lost..."
			self.resultArea["foreground"] = "red"
		else:
			result = "we have a tie."
			self.resultArea["foreground"] = "white"

		# output phase
		self.playerRoll.setNumber(playerDie)
		self.computerRoll.setNumber(compDie)
		self.resultArea["text"] = result


# Global definition of the main() method
def main():
	TwoDiceGUI().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()