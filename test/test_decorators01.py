# src:https://www.geeksforgeeks.org/decorators-in-python/
# 請問Python Decorators與C function pointer 比較有哪些相同或差異?
# Python Decorators和C function pointer都是用於函數的擴展。Python Decorators是一種函數，它可以接受另一個函數作為參數，並在不修改該函數源代碼的情況下擴展該函數的功能。C function pointer是一種指向函數的指針，它可以將函數作為參數傳遞給其他函數，並在運行時動態決定要調用哪個函數。
# 因此，Python Decorators和C function pointer都是用於在不修改源代碼的情況下擴展函數的功能，但它們的實現方式不同。
# src: https://stackoverflow.com/questions/7370801/how-do-i-measure-elapsed-time-in-python

from time import time

def measure_execution_time(func):
    t1 = time()
    func
    t2 = time()
    elapsed = t2 - t1
    
    return print('Elapsed time is %f seconds.' % elapsed)

def main():
    return print("I am the main func for testing and execution")

if __name__ == "__main__":
    measure_execution_time(main)