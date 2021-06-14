# press ctrl + f2 to stop rotation
# pressshift + f10 to rerun 

import rotatescreen
import time

screen = rotatescreen.get_primary_display()
# screen.rotate_to(0)

for i in range(120):
    time.sleep(1)
    screen.rotate_to(i*90 % 360)


