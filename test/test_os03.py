# Python program to explain os.getenv() method 
	
# importing os module 
import os 

# Get the value of 'home' 
# environment variable 
key = 'home'
value = os.getenv(key, "value does not exist") 

# Print the value of 'home' 
# environment variable 
print("Value of 'home' environment variable :", value) 