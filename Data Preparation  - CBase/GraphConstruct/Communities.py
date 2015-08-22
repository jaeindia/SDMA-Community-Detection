'''
Created on Apr 11, 2015

@author: jayakumara
'''
import time
import datetime
import csv
import json
from itertools import chain

def get_communities(inputJSON):
    """
        Fetch Communities
    """
    communityList = list()
    
    with open(inputJSON) as input_file:
        json_str = input_file.read()
        object = json.loads(json_str)
        
        for index, community in enumerate(object.get('membership')):
            tmpDict = {
                'company' : index+1,
                'community' : community[0]
            }
            
            communityList.append(tmpDict)
                    
    return communityList

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

# inputJSON = "F:\\Temp\\SG\\2\\linkedin--clauset_newman_moore--0.json"
inputJSON = "F:\\Temp\\SG\\1\\linkedin--fastgreedy--0.json"
communitiesFile = "F:\\Temp\\1\\linkedin--clauset_newman_moore--0.csv"
communitiesFile = "F:\\Temp\\SG\\1\\linkedin--clauset_newman_moore--0.csv"

communityList = get_communities(inputJSON)
with open(communitiesFile, "wb") as output_file:
    dicts_to_csv(communityList, output_file)
    
print "\nEnd Time: " + get_std_time(time.time()) + "\n"
############################################################