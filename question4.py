
def stairs(steps):
    """
    steps is the number of steps that we want the child to stop at
    """
    # clarify for the if possible to overshoot the number of steps 
    # for example is steps = 3 and pattern is [1,3]
    # use recursion 
    if steps <= 1:
        return steps
    counter = 0
    counter2 = 1
    while counter2<=3 and counter2<=steps:
        counter+=stairs(steps-counter2)
        counter2+=1
    return counter

def main(steps):
    return stairs(steps+1)


if __name__ == "__main__":
    print(main(3))