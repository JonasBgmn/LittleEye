import mss
import os

try:
    os.mkdir('outputs')
except:
    pass

with mss.mss() as sct:
    sct.shot(mon = 0, output='outputs/mon-{mon}_{date:%Z-%Y-%m-%d}_{date:%H-%M-%S}.png')