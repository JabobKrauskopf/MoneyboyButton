from playsound import playsound
from os import listdir
from os.path import isfile, join
import keyboard
import random
soundfiles = [join('sounds', f) for f in listdir('sounds') if isfile(join('sounds', f))]

while(True):
    keyboard.wait('enter')
    playsound(random.choice(soundfiles))