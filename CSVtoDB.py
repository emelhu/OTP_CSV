# import CSV files to database #

import sys
import os
import csv




def CSVtoDB(command):

    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        rows = list(spamreader)

    for row in rows:
        print(row)

    print("\nA 3. sor 2. oszlopa: ", rows[2][1])