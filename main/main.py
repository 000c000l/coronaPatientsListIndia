"""
    Github-Id:000c000l
    Name:Manish Kumar Srivastava
    Institute:IIT Tirupati
"""


import sys
import os
from src.update import csv_update
from src.upload import mysql_load
from src.query import mysql_query
from src.getLocation import location
if len(sys.argv)<2:
    print("Insufficient number of parameters")
    exit()
arg=sys.argv[1:]
# 
"""
    for updating csv file
"""
# 
pattern_string="--update"
for i in arg:
    if i.startswith(pattern_string):
        path=os.getcwd()
        os.system("wget https://raw.githubusercontent.com/covid19india/api/gh-pages/csv/latest/raw_data.csv")
        path=os.path.join(path,"raw_data.csv")
        if not os.path.exists(path):
            print(path)
            print("File does not exist")
        else:
            csv_update(path)
            # 
            """
                for uploading the newData.csv to mysql
            """
            # 
            path=os.path.join(os.path.dirname(path),"newData.csv")
            mysql_load(path)
            input()
        break
# 
"""
    querying the command 
"""
# 
pattern_string="--query="
for i in arg:
    if i.startswith(pattern_string):
        query=i[len(pattern_string):]
        list_of_locations=mysql_query(query)
        new_pattern_string="--get_location"
        for j in arg:
            if j.startswith(new_pattern_string):
                location(list_of_locations)
                break
        break



        
