##############            SL, CL2            ##############
label numberguessinggame:
    mG "Hey [MsGName]! I'm thinking of an integer from 1 to 100. Guess the number I'm thinking of!"

label randomnumber:
    $answer = renpy.random.randint(1, 100)

label guessinggamestart:
    $number_guess = renpy.input("Go ahead, guess Jupyter's number: ", length = 3)
    if number_guess.isdigit() == False:
        mG "Come on [MsGName], enter a NUMBER BETWEEN 1 AND 100 !!!"
        jump guessinggamestart
    $number_guess = int(number_guess)
    if number_guess < 1 or number_guess > 100:
        mG "I SAID ENTER A NUMBER BETWEEN 1 AND 100 !!!"
        jump guessinggamestart
    if number_guess != answer:
        mG "Get good [MsGName]"
        if number_guess > answer:
            mG "The number I'm thinking of is smaller than your guess! Try again!"
        else:
            mG "The number I'm thinking of is greater than your guess! Try again!"
    if number_guess == answer:
        mG "You got my number!"
        jump correctanswer
    jump guessinggamestart

label correctanswer:
    mG "Wanna play another round? This time, I'm sure you won't guess my number!"
    menu:
        "Challenge Jupyter again":
            jump randomnumber
        "Don't play again, playing once was difficult enough!":
            jump returnfromnumberguessing

