################                  CL Function to create the game base of a working piano game                   ########################
## comments are all CL
##image transformation to zoom the background image and the keyboard
transform zoom1:
    yalign 0.00000001
    xalign 0.05
    zoom 0.45

label ddrgamesetup:
    $ renpy.block_rollback()
    show qnc piano at zoom1
    show keyboard:
        zoom 2.8
        xalign 0.5
        yalign 0.8
    with Dissolve(3)
    $ cont = 0 #continue variable
    $ arr_keys = ["a", "s", "d", "f", "g", "h", "j", "k", "l"] #list of keyboard inputs to be selected from (https://www.pygame.org/docs/ref/key.html) keys
    $ noteremain = 50
    $ Livesleft1 = 3
    "Use the A-->L row of keys on your keyboard to Input"
    "Game Start"
    play music "<from 5.0>audio/HungarianDance.mp3" volume 1.5
    call piano_setup(0.5, 0.5, 0.007, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, 0.5) from _call_piano_setup
    # in the above, I randomly select a key from a previously defined set of keys (arr_keys), and randomize the location
    jump ddrgame

label ddrgame:
    $ renpy.block_rollback()
    while cont == 1:
        call piano_setup(0.5, 0.5, 0.007, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, 0.5) from _call_piano_setup_1
        # to repeat the qte events until it is missed
    jump pianoend

## The label that will call the screen that the game is held in
label piano_setup(time_start, time_max, interval, trigger_key, x_align, y_align):
    $ renpy.block_rollback()
    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen piano_game

    $ cont = _return
    # 1 if key was hit in time, 0 if key not

    return

transform pianokey:
    zoom 0.8

## The Screen that contains the visuals for the game itself
screen piano_game:
    text "Notes Remaining: [noteremain]":
            ypos 10
            xalign 0.95
            color "#fff"
            size 50
            outlines [ (6,"#000000",0,0) ]
    text "Lives: [Livesleft1]":
        ypos 10
        xalign 0.05
        color "#fff"
        size 50
        outlines [ (6,"#000000",0,0) ]

    ###disable the inputs:
    for i in arr_keys:
        python:
            if i == trigger_key:
                wrongtrigger = True
            else:
                wrongtrigger = False
        if wrongtrigger == True:
            key trigger_key action Jump('onkeypress')
        else:
            key i action Jump('missedkey')
    #key input qte

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_simple')])
    # timer, using variables from label qte_setup
    # false is the condition if the timer runs out - and this will be reached if the user doesn't get hit the key on time

    key trigger_key action Jump('onkeypress')
    # the "key detector" (ends qte_event by returning 1)

    vbox:
        xalign x_align
        yalign y_align
        spacing 25
        # vbox arrangement
        $ trigger_key_dis= str.capitalize(trigger_key)
        imagebutton auto "images/Keyback1_%s.png" ypos 140 at pianokey action NullAction()
        text trigger_key_dis:
            ypos -10
            xalign 0.5
            color "#fff"
            size 45
            outlines [ (6,"#000000",0,0) ]
            # text showing the key to press

        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 150
            if time_start < (time_max * 0.25):
                left_bar "#f00"
                # this is the part that changes the colour to red if the time reaches less than 25%

label missedkey:
    ##function that ticks down the lives if a note is missed and checks to see if there are lives left
    with vpunch
    if Livesleft1 >1:
        $ Livesleft1-=1
        $ cont = 1
    else:
        $ cont = 0
        jump pianoend

label onkeypress:
    ##function that will tick down the notes remaining if the key is pressed in time
    if noteremain>1:
        $ noteremain -=1
        $ cont = 1
    else:
        $ cont=2
    jump ddrgame

label pianoend:
    ##function that occurs once either the lives hits 0 or when the notes counter hits 0 or when a note time is missed
    play music qnc
    ## if statement that defines your reward based on song success
    if cont == 2:
        $ shipfavour+=20
        N "Wow you actually managed to complete the song..."
        N "Waterloon kids scare me"
        N "Anyway Jupyter seems to like you a bit more now at least"
    else:
        N "Imagine failing to play the piano..." with hpunch
        N "What? did your parents not force you into piano lessons as a child.."
        N "Are you sure you belong in Waterloon???"
        N "Oh well at least you tried"
        N "Have a cookie and enjoy your participation award (Derogatory)"
    jump returnfromddr