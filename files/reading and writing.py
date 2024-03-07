# topic-2 reading and writing file in json format , CSV format csv stands for Comma Seperated Values and binary format

data={
    "name":"subramanya",
    "mail_id" : "asubramanya370@gmail.com",
    "phone":9019347642,
    "subject":["dsa","python","DBMS","computer networks"]    
}

import json
with open("data.json", "w") as f:
    json.dump(data,f)
# dump helps us to write json format file

# if we want to read the json file
 
with open("data.json", "r") as f:
    read_values=json.load(f)
print(read_values)
# here load is used for reading the values in the json file

# --------------------------------------------------------------------------------------------

import csv
data1=[["name","email","phone"],
      ["subramanya","asubramanya","9019347642"],
      ["darshan","ddshatgar@gmail.com","61626132"]]

with open("data1.csv", "w") as f:
    writer=csv.writer(f)
    
    for i in data1:
        writer.writerow(i)

# reading the csv file
with open("data1.csv", "r") as f:
    read_values=csv.reader(f)
    
    for i in read_values:
        print(i)
        
# ---------------------------------------------------------------------------------------------
# topic-binary data
with open("test10.bin", "wb") as f:
    f.write(b"\x01\x02\x03\x04\x05\x06\x07 42123213213123")

# reading 
with open("test10.bin", "r") as f:
    print(f.read())
     