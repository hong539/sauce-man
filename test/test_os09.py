# src: https://www.geeksforgeeks.org/python-os-environ-object/
# Python program to explain os.environ object 


# importing os module 
import os 

# Method 1 
# Print the value of 
# 'MY_HOME' environment variable 
print("MY_HOME:", os.environ.get('MY_HOME', "Environment variable does not exist")) 


# Method 2 
try: 
	print("MY_HOME:", os.environ['MY_HOME']) 
except KeyError: 
	print("Environment variable does not exist") 