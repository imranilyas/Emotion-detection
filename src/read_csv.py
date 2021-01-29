import numpy as np
import time 

# CSV Imports
import os
import csv

# Feed urls into string array
def read_urls():
    pathtoURL = os.getcwd() + "\\links.csv"
    with open(pathtoURL, "r") as csv_url:
        csv_reader = csv.reader(csv_url)
        #next(csv_reader)
        urls = [line for line in csv_reader]
    return urls

# Load urls 
urls = read_urls()
name = urls

for i in name:
    print(i)