def safe_print_division(a, b):
    try:
        result=a/b
    except TypeError:
        result="None"
    except ZeroDivisionError:
        result="None"
    finally:
        print("Inside result: {}".format(result))
    return(result)