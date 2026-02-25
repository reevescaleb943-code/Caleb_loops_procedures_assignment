def main():
    """ 
    A WHILE LOOP will run a chunk of code until a condition is met.

    This is used when you don’t know the exact number of times you want 
    the loop to repeat and it depends on another factor.
    """
    answer= 7
    is_correct_answer=False


    while not is_correct_answer:
        guess=input("how many continents are there? ")
        if int(guess) == answer:
            print("yay,you got it correct:")
            is_correct_answer = True
        else:
            print("nope, that's not right try again")

    # guess the correct answer
    # WHILE answer is not correct loop
    # conditional inside while to check the answer

    pass


if __name__ == "__main__":
    main()
