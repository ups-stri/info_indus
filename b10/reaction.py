# IMPORT the required libraries (sense_hat, time, random) 
from sense_hat import SenseHat
from time import sleep
from random import choice

# CREATE a sense object
sense = SenseHat()

# Set up the colours (white, green, red, empty)

w = (150, 150, 150)
g = (0, 255, 0)
r = (255, 0, 0)
e = (0, 0, 0)

# Create images for three different coloured arrows

arrow = [
w,w,w,e,e,w,w,w,
w,w,e,e,e,e,w,w,
w,e,w,e,e,w,e,w,
e,w,w,e,e,w,w,e,
w,w,w,e,e,w,w,w,
w,w,w,e,e,w,w,w,
w,w,w,e,e,w,w,w,
w,w,w,e,e,w,w,w
]

arrow_red = [
w,w,w,r,r,w,w,w,
w,w,r,r,r,r,w,w,
w,r,w,r,r,w,r,w,
r,w,w,r,r,w,w,r,
w,w,w,r,r,w,w,w,
w,w,w,r,r,w,w,w,
w,w,w,r,r,w,w,w,
w,w,w,r,r,w,w,w
]

arrow_green = [
w,w,w,g,g,w,w,w,
w,w,g,g,g,g,w,w,
w,g,w,g,g,w,g,w,
g,w,w,g,g,w,w,g,
w,w,w,g,g,w,w,w,
w,w,w,g,g,w,w,w,
w,w,w,g,g,w,w,w,
w,w,w,g,g,w,w,w
]

# Set a variable pause to 3 (the initial time between turns)  
# Set variables score and angle to 0  
# Create a variable called play set to True (this will be used to stop the game later)  
pause = 3
score = 0
angle = 0
play = True

sense.show_message("Trouvez comment jouer.", scroll_speed=0.05, text_colour=[0, 255, 0])

# WHILE play == True 
while play:
  
    # CHOOSE a new random angle 
    last_angle = angle
    while angle == last_angle:
        angle = choice([0, 90, 180, 270])
        
    sense.set_rotation(angle)
    
    # DISPLAY the white arrow
    sense.set_pixels(arrow)
    
    # SLEEP for current pause length  
    sleep(pause)
    
    
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x, 0)
    y = round(y, 0)

    print(angle)
    print(x)
    print(y)

    # IF orientation matches the arrow...
    if x == -1 and angle == 180:
        # ADD a point and turn the arrow green  
        sense.set_pixels(arrow_green)
        score += 1
    elif x == 1 and angle == 0:
      sense.set_pixels(arrow_green)
      score += 1
    elif y == -1 and angle == 90:
      sense.set_pixels(arrow_green)
      score += 1
    elif y == 1 and angle == 270:
      sense.set_pixels(arrow_green)
      score += 1
    else:
      # SET play to `False` and DISPLAY the red arrow
      sense.set_pixels(arrow_red)
      play = False

    # Shorten the pause duration slightly  
    pause = pause * 0.95
    
    # Pause before the next arrow 
    sleep(0.7)

# When loop is exited, display a message with the score  
msg = "Ton score est : %s" % score
sense.show_message(msg, scroll_speed=0.05, text_colour=[100, 100, 100])
