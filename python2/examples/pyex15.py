#!/usr/bin/env python

# Author  : freeman
# Date    : 2019.05.08
# Version : 0.0.1
# Desc    : Program 
#         : python grade Calculator
#         : python pyex15.py grades.txt 
###################################################################


import sys
from sys import argv


def processGrades(f):
    grade = open(f, 'r') 
    hw, quiz, test, lab = [], [], [], []
    stuff = grade.readlines()
    for i in stuff:
        items = i.split()
        #print items
        if items[0] == "hw":
            for a in items:
                hw.append(a.strip("\n"))
        elif items[0] == 'quiz':
            for b in items:
                quiz.append(b.strip("\n"))
        elif items[0] == 'lab':
            for c in items:
                lab.append(c.strip("\n"))
        elif items[0] == 'test':
            for d in items:
                test.append(d.strip("\n"))
        else:
            print "there are no other options"

    calculateGrades(hw, quiz, lab, test)

def calculateGrades(h, q, l, t):
    hw_sum, quiz_sum, test_sum, lab_sum = 0.0, 0.0, 0.0, 0.0
    hwG, quizG, testG, labG = 0.0, 0.0, 0.0, 0.0
    # 20% HW, 20% labs, 20% quiz, 40% test
    # 30 pts max for each lab assignment
    # 10 pts max for each quiz
    # 100 pts max for each lab
    # 100 pts max for each test
    if h[0].lower() == "hw":
        for i in h:
            if i.isdigit():
                hw_sum += float(i)
        hwG = float( ( hw_sum / ((len(h)-1)*30.00) ) * .20)
    if q[0].lower() == "quiz":
        for i in q:
            if i.isdigit():
                quiz_sum += float(i)
        quizG = float( ( quiz_sum / ((len(q)-1)*10.00) ) * .20)
    if l[0].lower() == "lab":
        for i in l:
            if i.isdigit():
                lab_sum += float(i)
        labG = float( ( lab_sum / ((len(l)-1)*100.00) ) * .20)
    if t[0].lower() == "test":
        for i in t:
            if i.isdigit():
                test_sum += float(i)
        testG = float( ( test_sum / ((len(t)-1)*100.00) ) * .40)

    print "Your Final Grade ist: " + str(float(hwG+quizG+labG+testG)*100)


def main():
    if len(sys.argv) == 2:
        data = sys.argv[1]
        processGrades(data)
    else:
        print "Student, you forgot the data file !"
        sys.exit(1)


if __name__ == "__main__":
    main()
