# What is a Function?
#   A PROCEDURE is a piece of code that you can easily use over and over. 
#   We will refer to this as a FUNCTION in this class
#   A function is a piece of code that has a name and completes a specific task.
#
# Creating Functions
#   We declare a function using the keyword def at the start
#   A function is invoked using parens () 
#   A function can accept parameters
#   A function can have a return value
#
# built in functions (these are like tools available to you)
#   print()
#   type()
#   len()
#   input()
#   range()
#   int(), str(), float(), bool(), list()
#   many more
#
# you can create your own functions
# you can comment functions to help organize and document what they do
# 
# Parts of a Function
#   Declare - def - give it a name and add the code to execute when it is called
#   Parameter (param1, param2) - values passed into a function
#   Return - return "foo" - also known as Output 
#   Call - my_method() - when you want to use the function
#
#python 1-procedures.py
def checkout_books(has_account, number_of_books):
    if not has_account:
        print("You need an account to check out books")
    elif int(number_of_books) > 4:
        print("You can only have 5 books checked out at a time")
    else:
        print("You can check out more books")
def say_hi(name):
    greeting="What's up:"+name
    return greeting
def average_score(total_points, games_played):
    average_score=total_points / games_played
    return average_score
def main():
    pass 

    # print() 
    print("hello")
    name="Bob"
    print("hello", name)
    # type()
    Member_name= "John Smith"
    Total_points=123
    Games_played=5
    Is_playing_game=True
    
    print("Member_name type", type(Member_name))
    print("Total_points type", type(Total_points))
    print("Games_played type", type(Games_played))
    print("Is_playing_game type", type(Is_playing_game))

    # Custom function example
    average=average_score(Total_points, Games_played)
    print("average:", average)
    # Custom function task 1
    Name=input("what is your name?")
    print(say_hi(Name))
    # Custom function task 2
    has_account=input("Do you have an account yes or no?")
    number_of_books=input("How many books do you have checked out?(Use an integer)")
    checkout_books(has_account, number_of_books)
    # len()
    Store_name="Cane Pole"
    print(len(Store_name))
    if len(Store_name) < 10:
        print("hey, you need a longer name")
    else:
        print("Store name looks good")
    
    Favorite_players= ("Larry Bird", "Kobe Bryant", "Michael Jordan")
    print("Favorite_players:", len(Favorite_players))
    # input()
    age=input("How old are you?")
    if int(age) < 19 and int(age) > 13:
        print("you are a teenager")
    else:
        print("you are not a teenager")
    print("You entered", age)
     # range()

    # int() 

    # str()

    # float()

    # bool()

    # list() 


if __name__ == "__main__":
    main()
