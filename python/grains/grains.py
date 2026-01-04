def square(number):
    if number > 1 and number < 65:
        count = 1
        for i in range(1, number):
            count += count
    elif number == 1:
        count = 1
    else:
        raise ValueError("square must be between 1 and 64")
    return count

def total():
    grans = [1]
    for i in range(63):
        grans.append(grans[-1] * 2)

    return sum(grans)
