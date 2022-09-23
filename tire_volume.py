#import the math module so i can use math.pi ans math.pow
import math

#print a description of this program for the user to see

print("This program reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.")

#get the data from the user
width = float(input('Enter the width of the tire in mm (ex 205):'))
ratio = float(input('Enter the aspect ratio of the tire (ex 60):'))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15):'))

# compute the volume of the wheel
operation1 = math.pi * width**2 * ratio 
operation2 = width * ratio + 2540 * diameter
volume = (operation1 * operation2)/10000000000

#print the volume of the wheel for the user to see
print (f'The approximate volume is {volume:.2f} liters')

from datetime import datetime

current_date = datetime.now()

with open ('volumes.txt', 'a', encoding='utf-8') as volumes:
        volumes.write(f'{current_date.strftime("%x")}, {width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume:.2f} \n')
    
