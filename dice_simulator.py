# Listing_23-2.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------
# Changes by Brian Skinner - Sept, 2013
# Modified by Steve Tangsombatvisit - March 2017

# Rolling two six-sided dice 1000 times.

import random

#track how many times value comes up
rolled_2 = 0
rolled_3 = 0
rolled_4 = 0
rolled_5 = 0
rolled_6 = 0
rolled_7 = 0
rolled_8 = 0
rolled_9 = 0
rolled_10 = 0
rolled_11 = 0
rolled_12 = 0

for i in range(1000):
    #### INSERT YOUR CODE HERE ####
    ## 1. Create two dice variables
    
    ## 2. Roll each dice
    
    ## 3. Sum up the dice rolls
    
    ## 4. Update the variable to track how many times that number has been rolled
    ## IE if 4 was rolled, update rolled_4

#why did we skip spots 0 and 1?
print ("2 was rolled", rolled_2, "times")
print ("3 was rolled", rolled_3, "times")
print ("4 was rolled", rolled_4, "times")
print ("5 was rolled", rolled_5, "times")
print ("6 was rolled", rolled_6, "times")
print ("7 was rolled", rolled_7, "times")
print ("8 was rolled", rolled_8, "times")
print ("9 was rolled", rolled_9, "times")
print ("10 was rolled", rolled_10, "times")
print ("11 was rolled", rolled_11, "times")
print ("12 was rolled", rolled_12, "times")

# BONUS
# 1. Print out the number that was rolled the most and the least
# 2. How would you do three dices?
# 3. Allow user to enter in the number of dices and number of rolls

