import random

GLOBAL_LIST = [[]]
X_GLOBAL_MIN = 0
X_GLOBAL_MAX = 0

def clip():
    global X_GLOBAL_MAX
    global X_GLOBAL_MIN

    X_GLOBAL_MAX = 0
    X_GLOBAL_MIN = range

    numbers = list(range(1000))
    random.shuffle(numbers)

    for number in numbers:
        if number > X_GLOBAL_MAX:
            X_GLOBAL_MAX = number

        if number < X_GLOBAL_MIN:
            X_GLOBAL_MIN = number

if __name__== "__main__":
    clip()

    print "Max: " + str(X_GLOBAL_MAX)
    print "Min: " + str(X_GLOBAL_MIN)
