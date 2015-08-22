'''
@author: jayakumara
'''
import string
import csv

def read_csv(csv_file):
    file_handler = open(csv_file, "rb")
    result = []
    for line in file_handler.xreadlines():
        temp_list = []
        line = line.replace('"', '').strip()
        temp_list.extend(string.split(line, ','))
        result.append(temp_list)
    
    return result
    
def merge_csv(first_list, second_list, write_file):
    write_handler = open(write_file, 'wb')    
    cw = csv.writer(write_handler)
    
    for i in range(len(first_list) - 1):
        first_list[i].extend(second_list[i+1])
#         print first_list[i]
        cw.writerow(first_list[i])
    

csv_file = "C:\\Users\\jayakumara\\Desktop\\Temp\\DS_Test\\output.csv"
csv_file = "F:\\Group\\SDMA\\US\\out1.csv"
write_file = "C:\\Users\\jayakumara\\Desktop\\Temp\\DS_Test\\result.csv"
write_file = "F:\\Group\\SDMA\\US\\graph.csv"
first_list = read_csv(csv_file)
second_list = first_list
merge_csv(first_list, second_list, write_file)