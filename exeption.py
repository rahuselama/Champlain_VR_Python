x = input ("Enter a number   :")
y = input ("Enter a number   :")
try:
   result = print(int(x)/int(y))
except ZeroDivisionError:
    print("Sorry you cannot divide by zero")
except ValueError:
    print("Please enter only number")
except Exception:
    print("An unknown error has occurred")
else:
    print(result)
