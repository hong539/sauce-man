# src: https://www.geeksforgeeks.org/python-os-environ-object/
# Python program to explain os.environ object 

# importing os module 
import os 

# Get the value of 
# 'HOME' environment variable 
home = os.environ['HOME'] 

# Print the value of 
# 'HOME' environment variable 
print("HOME:", home) 

# Get the value of 
# 'JAVA_HOME' environment variable 
# using get operation of dictionary 
java_home = os.environ.get('JAVA_HOME') 

# Print the value of 
# 'JAVA_HOME' environment variable 
print("JAVA_HOME:", java_home) 
