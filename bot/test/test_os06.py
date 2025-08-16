# src: https://www.geeksforgeeks.org/python-os-environ-object/
# Python program to explain os.environ object

# importing os module
import os


# Print the value of
# 'JAVA_HOME' environment variable
print("JAVA_HOME:", os.environ["JAVA_HOME"])

# Modify the value of
# 'JAVA_HOME' environment variable
os.environ["JAVA_HOME"] = "/home / ihritik / jdk-10.0.1"

# Print the modified value of
# 'JAVA_HOME' environment variable
print("Modified JAVA_HOME:", os.environ["JAVA_HOME"])
