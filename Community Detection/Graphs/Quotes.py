'''
Created on Apr 13, 2015

@author: jayakumara
'''
import csv
import time
import datetime

def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))

def get_std_time(ts):
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        

############################################################
print "Start Time: " + get_std_time(time.time()) + "\n" 

InputFile = "F:\\Temp\\"
    
print "\nEnd Time: " + get_std_time(time.time()) + "\n"
############################################################