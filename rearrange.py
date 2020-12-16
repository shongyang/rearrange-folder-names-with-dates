import os, sys

# stuffsortsort = input("key-in in this format (00-00-0000)  =   ")
# stuffsortsort = "01-01-2000"
# print("The dir is: %s" % os.listdir(os.getcwd()))

# https://stackoverflow.com/questions/502726/converting-date-between-dd-mm-yyyy-and-yyyy-mm-dd

# https://stackoverflow.com/questions/12595051/check-if-string-matches-pattern
import re
import datetime

masses = os.listdir(os.getcwd())

# https://www.w3schools.com/python/python_regex.asp
# https://stackoverflow.com/questions/14966647/check-python-string-format
# https://www.tutorialspoint.com/python/os_rename.htm

checkmethod123 = input("Are you converting dd-mm-yyyy to yyyymmdd [y/n] = ")

if checkmethod123 == "y":
    for mass in masses:
        if re.match(".{2}-.{2}-.{4}", mass):
            abc = datetime.datetime.strptime(mass, "%d-%m-%Y").strftime("%Y%m%d")
            os.rename(mass, abc)
            # print("Yes")
elif checkmethod123 == "n":
    for mass in masses:
        if re.match(".{4}.{2}.{2}", mass):
            abc = datetime.datetime.strptime(mass, "%Y%m%d").strftime("%d-%m-%Y")
            os.rename(mass, abc)
            # print("Yes")
else:
    print("blahblahblah")