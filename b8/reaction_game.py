from​ sense_hat ​ import​ SenseHat
from time import sleep
from random import choice
sense = SenseHat()
#set up the colours (white, green, red, empty)
w= (150, 150​, ​150​)
g= (0, 255​, 0​)
r= (255​, 0​, ​0​)
e= (0, ​0​, ​0​)

# create three differently coloured arrows
arrow = [
e,e,e,w,w,e,e,e,
w,w,e,e,e,e,w,w,
e,w,e,w,w,e,w,e,
e,w,w,e,e,w,w,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
w,w,w,e,e,w,w,w,
w,w,w,e,e,w,w,w]
arrow_red = [
w,w,w,r,r,w,w,w,
w,w,r,r,r,r,w,w,
w,r,w,r,r,w,r,w,
r,w,w,r,r,w,w,r,
w,w,w,r,r,w,w,w,
w,w,w,r,r,w,w,w,
w,w,w,r,r,w,w,w,
w,w,w,r,r,w,w,w]
arrow_green = [
e,e,e,g,g,e,e,e,
e,e,g,g,g,g,e,e,
e,g,e,g,g,e,g,e,
g,e,e,g,g,e,e,g,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e]
pause = 3
score = 0
angle = 0
play = True
sense.​ show_message​ ("Keep the arrow pointing up", text_colour​ = ​ [255​,0,0])
while​ play == True:
last_angle = angle
while angle == last_angle:
angle = random.​ choice​ ([0, 90, 180, 270])
sense.​ set_rotation​ (angle)
sense.​ set_pixels​ (arrow)
time.​ sleep​ (pause)
accelerometer_data = sense.get_accelerometer_raw()
x = ​ round​ (accelerometer_data[​ ' ​ x '], 0)
y = ​ round​ (accelerometer_data[​ ' ​ y ' ], 0)
print(x)
print(y)
if​ y == -1 and angle == 180:
sense.​ set_pixels​ (arrow_green)
score = score + 1
elif​ y == 1 and angle == 0:
sense.​ set_pixels​ (arrow_green)
score = score + 1
elif​ x == -1 and angle == 90:
sense.​ set_pixels​ (arrow_green)
score = score + 1
elif​ x == 1 and angle == 270:
sense.​ set_pixels​ (arrow_green)
score = score + 1
else​ :
sense.​ set_pixels​ (arrow_red)
play = False
pause = pause * 0.95
sleep​ (0.5)
msg = "Your score was %s" % (score)
sense.​ show_message​ (msg, scroll_speed​ = ​ 0.05, text_colour​ = ​ [ ​ 100​ , ​ 100​ , ​ 100​ ])
