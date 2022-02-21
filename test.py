

# define a function to divide two numbers
def division(a, b):
# use the try statement where error may occur
    try:
        return a/b
# if the error occurs, handle it !!
    except ZeroDivisionError:
        print("Cannot divide by Zero!!")
division(10,5)
## >> 2
division(10,0)
## >> Cannot divide by Zero!!
