class A:
    try:
        for i in range(1, 5):
            print(5 / i)
    # A Generic except After All Excepts.
    except:
        print("You can't divide number by Zero")

    finally:
        print("Doesn't matter what will happen, whether exception occured or not, finally block will always executed.")

    # Python Multiple Exception in one Except
    try:
        a, b = 1, 0
        print(a / b)
    except(ZeroDivisionError, TypeError, Exception):
        print("Numbers can't divided by zero.")

    # Generic exception vs Specific exception

try:
    c, d = 1, 0
    print(c / d)
except Exception:
    print("Handled by Exception")
except ZeroDivisionError:
    print("ZeroDivisionError ")
except:
    print("Handled by Generic exception")

class B:
    x, y = int(input("X ")), int(input("Y "))
    try:
        print(x / y)
        if x == 0 and y == 0:
            raise ZeroDivisionError
    except:
        print("Divide by zero")
    finally:
        print("Finally block")

    # Raise Without a Specified Exception

    try:
        a='10'
        b=10
        print(a+b)
        if type(a)==str:
            raise Exception
    except:
        print("jjhhh")