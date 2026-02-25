def bounce_ball(num_of_bounces):
    for i in range(num_of_bounces):
        print("move up")
        print("fall down")
def main():
    """
    Loop Statements allow you to easily repeat a chunk of code many times.

    Example: in a game with a bouncing ball, it would be too much work to type
    out the code to make the ball bounce up and down a thousand times
    (move up, then fall down, move up then fall down, repeat 1000 times).
    Instead you can put the repeated code in a loop

    Loops not only save programmers time, they also make programs shorter.
    python 2-for-loops.py
    """

    # bounce a ball
    print("move up")
    print("fall down")

    # now repeat this 1000 times 

    # FOR LOOP (range)
    bounce_ball(1000)

    # FOR iterate
    # bounce_actions = []
    bucket = [
        "catfish",
        "trout",
        "bass",
        "carp",
        "mackerel",
        "shark",
        "swordfish",
    ]

    for fish in bucket:
        print("fish", fish)

    print("bucket[0]:", bucket[0])
    print("bucket[1]:", bucket[1])
    print("bucket[2]:", bucket[2])
    print("bucket[3]:", bucket[3])
    print("bucket[4]:", bucket[4])
    print("bucket[5]:", bucket[5])
    print("bucket[6]:", bucket[6])

    numbers=range(10)
    print("numbers[0]:", numbers[0])
    print("numbers[1]:", numbers[1])
    print("numbers[2]:", numbers[2])
    print("numbers[3]:", numbers[3])
    print("numbers[4]:", numbers[4])
    print("numbers[5]:", numbers[5])
    print("numbers[6]:", numbers[6])
    
if __name__ == "__main__":
    main()
