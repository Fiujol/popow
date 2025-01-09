import pyautogui
import random
import time
import subprocess

# Step 1: Sleep for 3 seconds
time.sleep(3)

# Step 2: Click at location (553, 625)
pyautogui.click(553, 625)

# Step 3: Sleep for 2 seconds
time.sleep(2)

# Step 4: Click randomly on one of the updated first set of locations
locations1 = [
    (474, 172), (477, 183), (463, 182), (480, 180), 
    (461, 177), (480, 176), (472, 161), (473, 187), (482, 186)
]
random_location1 = random.choice(locations1)
pyautogui.click(random_location1)

# Step 5: Sleep for 3 seconds
time.sleep(3)

# Step 6: Click randomly on one of the updated second set of locations
locations2 = [
    (644, 477), (573, 418), (599, 418), (648, 421), (627, 395), 
    (569, 385), (658, 384), (625, 450), (578, 457), (669, 457), (706, 457)
]
random_location2 = random.choice(locations2)
pyautogui.click(random_location2)

# Step 7: Sleep for 3 seconds
time.sleep(3)

# Step 8: Run the delete.py script
subprocess.run(['python3', 'delete.py'])

# Sleep for 10 minutes (600 seconds) after running the script
time.sleep(600)
