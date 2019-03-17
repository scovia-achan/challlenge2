
def fizzbuzz(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return "Invalid input"

    elif isinstance(a, list) and isinstance(b, int):
        return "Invalid input"

    elif isinstance(a, list) and isinstance(b, list):
        
        y = len(a) + len(b)

        if y%3 == 0:
            if y%5 == 0:
                return "fizzbuzz"
            return "fizz"
        elif y%5 == 0:
            return "buzz"

        elif y%3 != 0: 
            return y
fizzbuzz([1,2,3], [1,6,'a',12])

