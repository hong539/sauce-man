# src: https://www.geeksforgeeks.org/python-os-environ-object/
# Python program to explain os.environ object 

# importing os module 
import os 

# Print the value of 
# 'MY_HOME' environment variable 
print("MY_HOME:", os.environ['MY_HOME'])


# If the key does not exists 
# it will produce an error 