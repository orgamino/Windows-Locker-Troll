import os
from random import randint
import time

def locker(seconds):
	"""Locks computer for a certain amount of seconds between 1 second and 120 seconds."""
	time.sleep(seconds)
	os.system('rundll32.exe user32.dll,LockWorkStation')


while True:
    seconds = randint(1, 120)
    locker(seconds)