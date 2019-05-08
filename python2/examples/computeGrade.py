#!/usr/bin/env python

# Author  : freeman
# Date    : 2019.05.08
# Version : 0.0.1
# Desc    : Program
#         : python grade Calculator
# run     : python computeGrade.py
#         : It needs a gData.txt file
###################################################################

"""
Grade Breakdown: 20% HW, 20% labs, 20% quiz, 40% test
30 pts max for each lab assignment
10 pts max for each quiz
100 pts max for each lab
100 pts max for each test
This is the verticle Approach, pyex15.py was my horizontal Approach
"""

def getGrade(): 
    quiz, lab, hw, test, stuff = [], [], [], [], []
    hw_sum, lab_sum, quiz_sum, test_sum = 0, 0, 0, 0
    with open("gData.txt", "r") as f:
        stuff = f.readlines()
    for i in stuff:
        data = i.split(' ')
        if data[0].lower() == "hw":
            hw.append(int(data[1].strip("\n")))
        if data[0].lower() == "quiz":
            quiz.append(int(data[1].strip("\n")))
        if data[0].lower() == "lab":
            lab.append(int(data[1].strip("\n")))
        if data[0].lower() == "test":
            test.append(int(data[1].strip("\n")))
    for i in hw:
        hw_sum += int(i)
    hw_g = float( ( hw_sum / (len(hw)*30.00) ) * .20) 
    print hw_g
    for i in lab:
        lab_sum += int(i)
    lab_g = float( ( lab_sum / (len(lab)*100.00) ) * .20) 
    print lab_g
    for i in quiz:
        quiz_sum += int(i)
    quiz_g = float( ( quiz_sum / (len(quiz)*10.00) ) * .20) 
    print quiz_g
    for i in test:
        test_sum += int(i)
    test_g = float( ( test_sum / (len(test)*100.00) ) * .40) 
    print test_g
    result = (hw_g + lab_g + quiz_g + test_g) * 100.00
    print "Your Current grade is: " + str(result)
	
def main():
    getGrade()
	
if __name__ == "__main__":
    main()
