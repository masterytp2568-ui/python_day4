# 04_finally_cleanup_demo.py 

try:
    print("Start program")
    print("=============")
    number = int(input("number: "))
    print("Result: ", 100/number)

except ValueError:
    print("\nError: Please enter number only")

except ZeroDivisionError:
    print("\nError: Cannot divided by zero")

finally:
    print("===========")
    print("End program")