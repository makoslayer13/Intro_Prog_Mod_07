# ------------------------------------------------- #
# Title: Assignment_07
# Description: Assignment 07, Pickling and Error Handling
# ChangeLog: (Who, When, What)
# <Tim Quintana>,<12.1.2020>, Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!


#Pickling#

cust_id = int(input("Enter the ID:"))
cust_id = str(input("Enter a Name:"))
cust_list = [cust_id, cust_id]
print(cust_list)


#Storing Data with .dump

local_file = open("AppData.dat", "ab")
pickle.dump(cust_list, local_file)
local_file.close()


#Read the data with the pickleload
local_file = open("AppData.dat", "rb")
local_file_data = pickle.load(local_file) #Loads the single row of data
local_file.close()
print(local_file_data)


#Error Handling

try:
    quotient = 100 / 0
    print(quotient)
except:
    print("There was an error, please try differnt numbers")

#Original To Show the Error Handling Above and Below
try:
    quotient = 100 / 1
    print(quotient)
except:
    print("There was an error")