# src: https://www.geeksforgeeks.org/python-os-environ-object/
# Python program to explain os.environ object 

# importing os module 
import os 

# Add a new environment variable 
os.environ['GeeksForGeeks'] = 'www.geeksforgeeks.org'

# Get the value of 
# Added environment variable 
print("GeeksForGeeks:", os.environ['GeeksForGeeks'])