def some_function(num1, num2):
    try:
        num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(f"Oh my god there is an error and it is this : {err}")


some_function(1, '2')
some_function(4, 0)
