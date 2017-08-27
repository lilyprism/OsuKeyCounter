import keyboard
import os

op = 0
pp = 0
die = False
def callback(keys):
    if str(keys).find("up") != -1:
        if keys.name == ".":
            global die
            die = True

        if keys.name == "o":
            global op
            op += 1
        elif keys.name == "p":
            global pp
            pp += 1
        elif keys.name == "r":
            pp = 0
            op = 0
    print("O: %s | P: %s" % (op, pp), end="\r")

os.system("mode con:cols=18 lines=1")
keyboard.hook(callback)

while die == False:
    a = "a"