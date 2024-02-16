#tasks.py
def calculate_square(x:int):
    #The way to use exponential it is clear I guess.
    return x**2

def report_success(job, connection, result,*args, **kwargs):
    print(f"SUCCESS JOB, The value is: {result}")
    
def report_failure(job, connection, type, value, traceback):
    print(f"Job Failed due to: {traceback}")