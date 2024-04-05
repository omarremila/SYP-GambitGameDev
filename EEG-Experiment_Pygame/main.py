            
'''

            # Store the x_pos value in the array
            x_target.append(x_pos)
            y_target.append(y_pos)
            
            # Calculate the time passed since the last position change
         
            countdown = current_time() - last_position_change_time
            # print(f"Countdown: {countdown}, Interval: {i}")  # Debugging line

            if countdown >= position_change_interval  :
                
                #black_target_index = random.randint(0, num_targets - 1)  # Choose a new target to be black.
                #print(f"New black target is {black_target_index}")  # Print the new target for demonstration purposes
                last_position_change_time = current_time()  # Reset the last position change time to now
                position_change_interval = 5  # Reset the interval
                target_disp(x_target, num_targets)
            else:
                pass
            # NOT USED because when colour change too much cant see; too fast. X is best
            if i == black_target_index : 
                print(f"New black target is {black_target_index}")  # Print the new target for demonstration purposes

                targets[i].flicker(random.randint(1, 8), x_target[i], y_target[i], "green")
            else :
                targets[i].flicker(random.randint(1, 8), x_target[i], y_target[i], "red")

        


            if i == black_target_index : 
                print("hit it")
                targets[i].flicker(random.randint(1, 8), x_target[i], y_target[i], "green")
            else:
                targets[i].flicker(random.randint(1, 8), x_target[i], y_target[i], "red")
            # Calculate the time passed since the last position change
            countdown = current_time() - last_position_change_time
            if countdown >= position_change_interval  :
                black_target_index = random.randint(0, num_targets - 1)  # Choose a new target to be black.
                last_position_change_time = current_time()  # Reset the last position change time to now
                position_change_interval = 5  # Reset the interval
'''
'''
            # Store the x_pos value in the array
            x_target.append(x_pos)
            y_target.append(y_pos)
            
            # Calculate the time passed since the last position change
         
            countdown = current_time() - last_position_change_time
            # print(f"Countdown: {countdown}, Interval: {i}")  # Debugging line

            if countdown >= position_change_interval  :
                
                #black_target_index = random.randint(0, num_targets - 1)  # Choose a new target to be black.
                #print(f"New black target is {black_target_index}")  # Print the new target for demonstration purposes
                last_position_change_time = current_time()  # Reset the last position change time to now
                position_change_interval = 5  # Reset the interval
                target_disp(x_target, num_targets)
            else:
                pass
            # NOT USED because when colour change too much cant see; too fast. X is best
            if i == black_target_index : 
                print(f"New black target is {black_target_index}")  # Print the new target for demonstration purposes

                targets[i].flicker(random.randint(1, 8), x_target[i], y_target[i], "green")
            else :
                targets[i].flicker(random.randint(1, 8), x_target[i], y_target[i], "red")


            ------------------------------------
            # Get the current screen resolution
            infoObject = pg.display.Info()
            WIDTH = infoObject.current_w
            HEIGHT = infoObject.current_h
            DISPLAY = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
'''
# GAMBIT Flicker Demo!
# Created by Connor McLeod for ECED 4502.

import sys
import pygame as pg
import random
import time 
import csv

from target import Target

pg.init()

new_state = False
previous_state = -1
focus_target_index = None  

logged_data = []

#  function returns the number of seconds passed since epoch, this is used to set an interval 
def current_time():
    return time.time()
last_position_change_time = current_time() 
position_change_interval = 0.1  # determines number of seconds to change the target selector 



def target_disp(x_target, y_target, num_targets):
    global last_position_change_time, position_change_interval, new_state, focus_target_index

    # Calculate the time passed since the last position change
    if new_state == True :
        focus_target_index = 0
    

    for i in range(num_targets):
        targets[i].flicker(random.randint(1, 8), x_target[i], y_target[i], "red")
        countdown = current_time() - last_position_change_time
        #If countdown reached draw X in new spot 
        
        if countdown >= position_change_interval  :
            focus_target_index = random.randint(0, num_targets - 1) 
            focus_target_index = random.randint(0, num_targets - 1) 
            last_position_change_time = current_time()  # Reset the last position change time to now
            targets[0].draw_x(x_target[focus_target_index], y_target[focus_target_index], "BLUE")  # Draw an 'X'
        #targets[i].flicker_x(random.randint(1, 8), x_target[focus_target_index], y_target[focus_target_index], "blue")
        log_data(state, focus_target_index, x_target[focus_target_index], y_target[focus_target_index], current_time()-test_start_time)
    

def target_arrange(num_targets):
    

    x_pos = 0
    y_pos = 0 
    # Initialize the array to store x_pos values
    x_target = []
    y_target =[]
    global last_position_change_time, position_change_interval
    black_target_index = -1

    if num_targets != 9 and num_targets != 4 :
        y_pos = (DISPLAY.get_height() / 2)
        for i in range(num_targets):
            x_pos = (DISPLAY.get_width() / (num_targets + 1)) + x_pos
            x_target.append(x_pos)  # Append x_pos instead of x_gap
            y_target.append(y_pos)  # Append y_pos instead of y_gap

        
    elif num_targets ==9 : 
        # Code for arranging targets in a 3x3 grid
        grid_size = 3  # Because it's a 3x3 grid
        x_gap = DISPLAY.get_width() / (grid_size + 1)
        y_gap = DISPLAY.get_height() / (grid_size + 1)
        positions = [(x_gap * (i % grid_size + 1), y_gap * (i // grid_size + 1)) for i in range(num_targets)]

        for i, (x_pos, y_pos) in enumerate(positions):
            x_target.append(x_pos)  # Append x_pos instead of x_gap
            y_target.append(y_pos)  # Append y_pos instead of y_gap
    else : 

        x_margin = 64  # You can adjust this value as needed
        y_margin = 50
        corner_positions = [
            (0, 0),  # Top-left corner
            (DISPLAY.get_width() - x_margin, 0),  # Top-right corner
            (0, DISPLAY.get_height() - x_margin),  # Bottom-left corner
            (DISPLAY.get_width() - x_margin, DISPLAY.get_height() - x_margin)  # Bottom-right corner
        ]

        for x_pos, y_pos in corner_positions:
            x_target.append(x_pos)
            y_target.append(y_pos)

    target_disp(x_target, y_target, num_targets)
    
# Define a function to save data to a CSV file
def save_data_to_csv():
    global logged_data
    with open('flicker_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["State", "Target Index", "X Position", "Y Position", "Time"])
        writer.writerows(logged_data)

def log_data(state, target_index, x_pos, y_pos, current_time):
    global logged_data
    logged_data.append([state, target_index, x_pos, y_pos, current_time])

# Initalizes the main display surface.
WIDTH = 1080
HEIGHT = 800
DISPLAY = pg.display.set_mode((WIDTH, HEIGHT))

# Set the framerate (can be set higher if you have a high-framerate display).
FPS = 70
framerate = pg.time.Clock()
test_start_time = current_time()
# Play music!
pg.mixer.music.load("music/menu.mp3")
pg.mixer.music.play(-1)

# Print the title
font = pg.font.Font(None, 32)
text = font.render("Welcome to the GAMBIT Flicker Demo! Please be aware there will be many flashing lights.", True, "black")
textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)

# Super basic way to draw a square (target) at a given location.
targets = []
for i in range(9):
    targets.append(Target(DISPLAY))

# Game state variable that tracks which portion of the game's execution we are in.
state = 0
trials_rem = 0 #Remaining trials
timer_event = pg.USEREVENT + 1
pg.time.set_timer(timer_event, 5000)

trial_num = ""
test_trials = 10

# Game loop begins!
while True:
    for event in pg.event.get():
        # User exits the program.
        if event.type == pg.QUIT:
            save_data_to_csv()  # Save the data before exiting
            pg.quit()
            sys.exit()

        # Timer event that triggers every 5000 frames.
        if event.type == timer_event:
            #if there are remaining trials in a test
            if trials_rem != 0:
                trials_rem -= 1
                DISPLAY.fill("white")
                pg.display.update()
                pg.time.set_timer(timer_event, 0) # Stop timer between trials
                pg.time.wait(1000) # Wait 1 sec
                pg.time.set_timer(timer_event, 5000) # Restart timer

            #No remainging trials
            if trials_rem == 0:
                if state >= 5:
                    state = 0
                else:
                    state += 1

            # Check if the state has changed
            if state != previous_state:
                new_state = True
                previous_state = state  # Update previous_state to the new state

    # Clear the display.
    DISPLAY.fill("white")
    if new_state:
        print(f"Entering new state: {state}")
        new_state = False  # Reset new_state after handling the new state


    if state == 0:
        print(f"State: {state}")
        focus_target_index = 0
        # Add code for title screen!
        text = font.render("Welcome to the GAMBIT Flicker Demo! Please be aware there will be many flashing lights.", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)
    
    # Begin Test 1.
    if state == 1:
        if trials_rem == 0:
            trials_rem = test_trials
        trial_num = "Trial " + str(test_trials - trials_rem + 1)
        print(f"State: {state}")
        # Add code for Test 1!
        text = font.render("Test 1, " + trial_num +". A single flickering target will be shown.", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)
        target_arrange(1)


    # Begin Test 2.
    if state == 2:
        if trials_rem == 0:
            trials_rem = test_trials
        trial_num = "Trial " + str(test_trials - trials_rem + 1)
        print(f"State: {state}")
        # Add code for Test 2!
        text = font.render("Test 2, " + trial_num +". Three targets will be shown flickering at differing frequencies.", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)
        target_arrange(3)


    # Begin Test 3.
    if state == 3:
        if trials_rem == 0:
            trials_rem = test_trials
        trial_num = "Trial " + str(test_trials - trials_rem + 1)
        print(f"State: {state}")
        # Add code for Test 3!
        text = font.render("Test 3, " + trial_num +". Four targets will be shown at each of the four corners of the display.", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)
        target_arrange(4)

    # Begin Test 4.         
    if state == 4:
        if trials_rem == 0:
            trials_rem = test_trials
        trial_num = "Trial " + str(test_trials - trials_rem + 1)
        print(f"State: {state}")
        # Add code for Test 4!
        text = font.render("Test 4, " + trial_num +". Nine targets will be shown in a 3x3 grid.", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)
        target_arrange(9)

    # Congratulate the user!
    if state == 5:
        print(f"State: {state}")
        # Add code!
        text = font.render("Thank you for taking part in our experiment!", True, "black")
        textpos = text.get_rect(centerx = DISPLAY.get_width() / 2, y=10)

    DISPLAY.blit(text, textpos)

    pg.display.update()


    # Limit the framerate to the integer specified
    framerate.tick(FPS)
