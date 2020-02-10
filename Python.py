## Get Server Name and IP Address
import socket

host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name) 
print(host_name)
print(host_ip) 

## Substring
string = "freeCodeCamp"
print(string[0:5])
##freeC

## Get now
from datetime import datetime, timedelta
now = datetime.now() 
print(now)
cday = now.strftime('%Y-%m-%d %H:%M:%S')
print(cday)
new_time = now + timedelta(hours=10)
print(new_time)

## If
age = 3

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


## list
a = [1,2,5,7]
print (a[0])  # first element
print (a[len(a) - 1])   # last element or
print (a[-1])


## For loop
# example 1
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# example 2
for i in range (1,10):
    print ("Hello " + str(i))

# example 3
friends = ["Jim", "Karen", "Kevin"]
for index  in range(len(friends)):
    print (friends[index])


## While loop
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

## import password invisible (will keep ask you to imput if you just pree "enter")
import getpass

password = getpass.getpass('Password:')

while password != "invisible":
    password = getpass.getpass('Password:')


## Random number
import random

print(random.random())

print(random.randint(1,10))

items = [1, 2, 5, 8]
x = random.choice(items)
print(x)
y = random.choices(items,k=3)
print(y)

## Run external command
import os

os.system("notepad")


## Function
def collect(a,b=None):
    if b == None:
        return a
    else:
        return a+b

print( collect(2))
print( collect(2,3))


## command line arguments
import sys
print ('list ', str(sys,argv))

filename = sys.argv[1]
print (filename)


## list file
import glob
files = []
files = glob.glob("/home/linux/*")
print(files)


## read file
with open("filename.txt") as fobj:
    data = fobj.read()
    print(data)

## read file line by line
with open("filename.txt") as fobj:
    data = fobj.read()
    lines = data.split("\n")
    print(lines[0])


## read from csv file
import pandas as pd
df = pd.read_csv('example.csv')
print(df['salary'][0])


## write file (overwrite)
with open("newfile.txt",'w') as fobj:
    fobj.write("this is new file\n")
# append with open("newfile.txt",'a') as fobj:


## Send email
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'mysqladmin@ec2-dbaadmin-03'
receivers = ['yichenl@telenav.com']
message = MIMEText(content, 'plain', 'utf-8')
subject = 'Warning! Some MySQL RDS audit logs failed to sync to S3'
message['Subject'] = Header(subject, 'utf-8')
smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, message.as_string())

## MySQL Connect
# importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

# connecting to the database using 'connect()' method
# it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "10.189.101.160",
    user = "dbadmin",
    passwd = "agm43gadsg",
    database = "dba"
)

cursor = db.cursor()

# executing the statement using 'execute()' method
cursor.execute("SHOW TABLES")

# 'fetchall()' method fetches all the rows from the last executed statement
tables = cursor.fetchall() # it returns a list of all databases present

# printing the list of databases
print(tables)

cursor.close()


# Monitor system
import psutil
a = psutil.virtual_memory().percent  #内存占用率
b = psutil.cpu_percent(interval=1.0) #cpu占用率