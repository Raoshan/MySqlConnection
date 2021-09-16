import mysql.connector
import csv
import glob
import os
import shutil
source = os.path.join('C:/Users/RDATS/Desktop/Projects/Data')
conn = mysql.connector.connect(host="localhost", user = "root", port=3306, password="rdats4321", database="raoshanks")
cur = conn.cursor()
for fcnt,csvfile in enumerate(glob.iglob(source + '*.csv')):  # iterate through all csv files in this directory
    with open(csvfile,  encoding="utf8") as f:  # open spreadsheet file, fcnt is a count of files
        csvreader = csv.DictReader(f)
        next(csvreader)
        for row in  csvreader:
            # print(row['companyName'], row['Position'], row['Location'], row['companiesDescription'], row['NumberOfEmployees'], row['States'])
            query = 'insert into linkedin(companyName, jobPosition, Location, Description, NumberOfEmployees, States) VALUES (%s, %s, %s, %s, %s, %s)'
            cur.executemany(query,[(row['companyName'], row['Position'], row['Location'], row['companiesDescription'], row['NumberOfEmployees'], row['States'])])
            conn.commit()
            print("inserted")
  


