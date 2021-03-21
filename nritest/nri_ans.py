#!/usr/bin/env python3

# author         : Freeman
# date           : 2021.03.21
# desc           : Parsing number of questions
# version        : 0.0.1
################################################

import sys
import time
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 0 = ok
# 1 = not good

# my Goals:
# Case: 1 Q return strand section 1 Only
# Case: 2 Q return strand section 1 and 2
# Case: 3+ Q return strand section 1 and 2 and difficult level < .5
# Case: 3+ Q return strand section 1 and 2 and difficult level > .5

def retTable(num_questions):
    df = pd.read_csv('questions.csv')
    print(df)
    #df = df.groupby(['strand_id','standard_id','difficulty'])['difficulty'].count().reset_index(name='dist')
    #df['dist'] = df['dist'] / df['dist'].sum()
    #print(df)
    if num_questions == 1:
        a = df.groupby(['strand_id']) # ['difficulty'].lt(.5)
        pd.Index(list(range(5)), name='strand_id')
        pass
    elif num_questions == 2:
        pass
    elif num_questions >= 3:
        # Case 1 simple hard Difficult level
        pass
        # Case 2 harder hard based on Difficult level
    else:
        print("idk")




def main():

    if len(sys.argv) > 2:
        print("Too many parameters")
        print("python nri_ans NumQuestions")
        sys.exit(0)
    elif len(sys.argv) == 2:
        retTable(int(sys.argv[1]))
    elif len(sys.argv) < 2:
        print("not enough parameters")
        print("python nri_ans NumQuestions")
        sys.exit(0)
    else:
        print("idk")

if __name__ == "__main__":
    main()