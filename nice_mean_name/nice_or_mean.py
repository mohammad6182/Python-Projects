

def start(nice=0, mean=0, name=""):
    #get users name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)



def describe_game(name):
    """
        check if this is new game or not.
        if it is new, get the users name.
        if it is not a new game , thank the player
        for playing again and countinue with the game
    """
    #meaning, if we do not already have this users name,
    #then they are a new player and we need to get their name

    if name != "":
        print("\n thank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\n what is your name? \n>>>  ").capitalize()
                if name != "":
                    print("\n Welcome,  {}!".format(name))
                    print("\n In this game, you will be greated \nby several different people. \nYou can choose to be nice or mean")
                    print("\but at the end of the game you fate \nWill be sealed by your actions.")
                    stop= False

    return name


def nice_mean(nice,mean,name):
    stop= True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approches you for a \nconversation. will you be nice \nor mean? (N/M)  \n>>>: ").lower()
        if pick == "n":
            print("\n the stranger walks away smilling....")
            nice=(nice+1)
            stop=False
        if pick == "m":
            print("\nthe stranger glares at you \nmenacingly and storms off....")
            mean=(mean + 1)
            stop = False
    score(nice, mean, name) # pass the 3 variables to the score()




def show_score(nice,mean,name):
    print("\n{}, your current total: \n({},Nice) and ({}, Mean) ".format(name,nice,mean))



def score(nice, mean, name):
    #score_function is being passed the value stored within the 3 variables
    if nice >2: #if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:               #else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)



def win(nice,mean,name):
    #substitute the {} wildcards with our variable values
    print("\nNice jon {}, You Win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)



def lose(nice,mean,name):
     #substitute the {} wildcards with our variable values
    print("\nAhhh too bad, game ove! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)
    



def again(nice,mean,name):
    stop= True
    while stop:
        choice = input("\nDo you want to play again? (Y/N):\n>>> ").lower()
        if choice == "y":
            stop=False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop=False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Notice , i do not reset the name variable as that same user has electes to play again
    start(nice,mean,name)













if __name__ == "__main__":
    start()


















