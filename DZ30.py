def is_even(number):
    a = str(list(range(0, 9, 2)))
    number = str(number)
    if number[-1] in a:
        return True
    else:
        return False
is_even(5)



