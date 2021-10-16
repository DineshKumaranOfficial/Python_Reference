while True:
    try:
        age = int(input('Type your age : '))
        100/age
    except ValueError:
        print("Kindly Enter a number")
    except ZeroDivisionError:
        print("Kindly enter a number greater than zero")
    else:
        print("Good the age is accepted")
        break
    finally:
        print("This is Finally block")
