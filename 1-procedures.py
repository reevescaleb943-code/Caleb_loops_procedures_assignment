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

    # range()

    # int() 

    # str()

    # float()

    # bool()

    # list() 


if __name__ == "__main__":
    main()
