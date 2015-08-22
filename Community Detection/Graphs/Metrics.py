'''
Created on Apr 11, 2015

@author: jayakumara
'''
import time
import datetime
import csv
import json
import os
from itertools import chain

def get_metrics(object):
    """
        Fetch Communities
    """
    metricsList = list()
        
    tmpDict = {
        'name' : object.get('name')
    }
    
    metrics = object.get('metrics')
    
    for key in object.get('metrics').keys():
        tmpDict[key] = metrics[key]['aggregations']['Mean']
        tmpDict['noofcommunities'] = metrics[key]['aggregations']['Size']
        
    metricsList.append(tmpDict)
                    
    return metricsList

def dicts_to_csv(source, output_file):
    """
        Write dicts to csv
    """
    def build_row(dict_obj, keys):
        return [dict_obj.get(k) for k in keys]

    keys = sorted(set(chain.from_iterable([o.keys() for o in source])))
    rows = [build_row(d, keys) for d in source]

    cw = csv.writer(output_file)
    cw.writerow(keys)

    for row in rows:
        cw.writerow([c.encode('utf-8') if isinstance(c, str)
                     or isinstance(c, unicode) else c for c in row])


def get_std_time(ts):
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


############################################################
print "Start Time: " + get_std_time(time.time()) + "\n" 

inputDir = "F:\\Temp\\SG\\1"

metricsFile = "F:\\Temp\\SG\\1\\SG_1.csv"

dicts = list()

print "List of files in the dir\n"

for root, dirs, files in os.walk(inputDir):
        for f in files:
            if os.path.join(root, f).endswith((".json")):
                with open(os.path.join(root, f)) as input_file:
                    json_str = input_file.read()
                    print(os.path.join(root, f))
                    object = json.loads(json_str)
                    dicts.extend(get_metrics(object))

with open(metricsFile, "wb") as output_file:
    dicts_to_csv(dicts, output_file)
    
print "\nEnd Time: " + get_std_time(time.time()) + "\n"
############################################################