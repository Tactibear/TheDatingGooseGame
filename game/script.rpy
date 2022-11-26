﻿# Camilo - CL
# Charles - CL2
# Emily - EM
# Stephanie - SL
# SHIFT+I TO INSPECT IN GAME, over whatever the mouse is hovering over
init python:
    import pygame
    import random
    shipfavour=25
    if shipfavour<0:
        shipfavour==0
    if shipfavour>120:
        shipfavour==120
    
# main game script

###############              CL2               ################ 
## start python script to be recognized
init python:
    ## define a function, callback, and allow for the acceptance of any number of inputs into the function
    def callback(scrollingtextevent, **kwargs):
        ## if a defined event is occuring, in this case, the text is scrolling past the user,
        ## play the sound file that plays with scrolling text, a text "blip" sound
        if scrollingtextevent == "show":
            renpy.music.play("audio/textblipsoundeffect.mp3", channel="sound", loop=True, relative_volume=0.8)
        ## the other two possible states of the dialogue content is when is done scrolling,
        ## and sitting idle, where the sound stops playing
        elif scrollingtextevent == "slow_done" or scrollingtextevent == "end":
            renpy.music.stop(channel="sound")

###############             CL2                ################
## give character a name to be displayed and define to a variable, then assign them a colour, 
## and, when they are speaking dialogue, activate the text blip sound function
define N = Character("Goose God", color="#000000", callback=callback)
define mG = Character("Jupyter Journal", color="#ad2a28",callback=callback)
define MsG = Character("[MsGName]", color="#f542cb", callback=callback)
define MsGthinking = Character("[MsGName], Thinking", color="#a80883", callback=callback)
define T = Character("Timmy Tam", color= "#35ad28", callback=callback)
define A = Character("Ana Conda", color = "#2f1fc2", callback=callback)

## define and set a default value for the relationship score the player starts with
default shipfavour=25

###############              CL2               ################
## dialogue content starts here
label start:
    
    scene e6 window 2 goose god
    show e6 window 2 goose god with dissolve
    
    N "Welcome to the University of Waterloon!"
    scene e6 window 2 goose god
    show e6 window 2 goose god with dissolve
    N 'I go by Gregory but you can call me God.'
    N 'However you got here, be it by plane, car, train, wings, or admissions committee luck,'
    N 'You are in fact here.'
    N 'So what now.'
    N '...'
    N '.............'
    N 'How about we play a game? The bus wont come for another 35 minutes anyways.'
    N 'My all time favourite....'
    N 'ROCK PAPER SCISSORS!!!' with vpunch ##CL cool effect i found online
    stop music
    jump rpsagainstgod

###############            CL2                 ################
label afterrpsgod:
    play music titlescreenmusicac
    scene e6 window 2 goose god
    show e6 window 2 goose god with dissolve
    N "This is your first of many mistakes you'll make here, but it's ok."
    N "Mistakes are what makes us geese."
    N "Sorry what's your name again? I didn't quite catch it the first time."
    ## initiate python once again
    python:
        ##as for an input, and limit the input to 25 characters
        ## set that name to the users name for the rest of the game
        MsGName=renpy.input("Help me out here, bud:", length=25)
        ##if there are any spaces in front or behind the given name, take those away
        ##this saves on dialogue box space if someone decides to troll 
        MsGName=MsGName.strip()
        #capitalize first word of the string, can also str.title
        MsGName=str.capitalize(MsGName)
        ##if no name is inputted at all, set default to "CHE120"
        if not MsGName:
            MsGName="CHE120"
###############             EM, CL2                ################
    N "'[MsGName]'....."
    N "I see.............."
    N "What a funny name for a goose, does your mom also call you that?"
    N "Alright, so your job here now is to ignore me and indulge in university life."
    N "You may have noticed that about $16,000 has disappeared from your bank account, but such is life when you're at uwaterloon :)."
    N "Wait before you go....."
    N "Let's put you through a test."
    N "You're gonna be doing a lot of clicking today.... I think we need to make sure you are fit for the game ahead."
    N "So how about it?"

###############             CL2, CL                ################
label clickergameprompt:
    menu:
        "Oh yeah I trained my entire life for this.":
            jump yesclicker
        "Hmmmm may I at least put my bags down?":
            jump noclicker
label noclicker:
    N "Yeah no, you may not."
    N "So you playing or what?"
    menu:
        "Okok, I will, please don't smite me with that mighty beak.":
            N "Good, that's what I like to hear."
            jump clickergameprompt
        "I just want to play Riot Games hit arcade game League of Egg though.":
            N "Wow dude."
            N "You didn't have to hurt my feelings like that."
            N "Fine, just go play league then."
            N "It's whatever, not like you just opened my game."
            ##ehehehehehehehhe
            N "Goodbye."
            $ renpy.run(OpenURL('https://gamequitters.com/how-to-quit-playing-league-of-legends/'))
            $ renpy.quit()
label yesclicker:
    $ quick_menu=False
    $ renpy.block_rollback()
    stop music 
    #play music ""
    jump clickergamelabel
label returnfromclicker:
    $ renpy.block_rollback()
    $ renpy.checkpoint()
    $ quick_menu=True
    play music titlescreenmusicac
    menu:
        "Whew!":
            N "Pretty cool eh?"
            jump continuefromclicker
###############             CL2                ################
label continuefromclicker:
    if clicks>1:
        N "[clicks]..... I see..... Better than the average Laurier student."
        N "At the very least you knew to click the button."
    else: 
        N 'Did you not click the button at all??'
        N 'Please do consider glasses.'
    N "Welcome to campus little goosling, enjoy your stay. (Don't enjoy it too much though)"
###############            CL                 ################
    ##transition insertion before beginning the dialogue
    show screen Opening1() with dissolve
    hide e6 window 2 good god
    with dissolve
    

###############              CL2               ################
    # background here, just add file name, no file format at end
    play music "audio/rockgardenmusic-animalcrossing.mp3" volume 1.8

    show screen bars
    N "I should probably mention something before I let you go."
    N "See that little cool thing in the top left?"
    N "That's your relationship bar."
    N "It tracks how others view you, in favourability."
    N "It changes based on your words and actions around other geese."
    N "Please don't be like every other goose and try to get it as low as possible by pooping on things, honking aggressively, and generally being menaces on campus."
    N "Anyways, onto the campus, fly, little one!"
###############             EM,SL,CL2,CL                ################
    scene Opening1
    show screen day1 with dissolve
    pause 1
    hide screen day1 with dissolve
    scene rock garden 3
    hide screen Opening1 with dissolve
    show rock garden 3 with dissolve
    pause 2
    N "It's a beautiful Sunday afternoon. You and your friend, Ana Conda, are at the University of Waterloon's Rock Garden."
    N "It is currently 3pm, and you just got a text from your childhood friend, Timmy Tam, asking if you wanted to hang out with him and his friend, Jupyter Journal in MC."
    MsGthinking "I can't wait to see Timmy again! It's been so long since I last saw him."
    
    show mc trelfords office 2 with Dissolve(2)
    hide rock garden 3 with dissolve
    N "You and Ana walk into MC and take the elevator to the 6th floor, where Timmy and his friend are studying."
    MsG "I hope you don't mind that I brought my friend Ana!"
    show timmy wave with dissolve
    T "Oh my gosh, [MsGName]! I haven't seen you in so long! How have you been?"
    MsG "I've been doing great! I missed you so much Timmy!"
    T "Me too! This is my friend Jupyter by the way, he's in CS BBA, what a silly CS boy."
    hide timmy wave with dissolve
    show standard mr goose with dissolve
    MsGthinking "Omg Omg Jupyter is such a dapper goose!!! He is soooo cute"
    MsG "Hi Jupyter! I'm [MsGName] nice to meet you! I'm in Chem Eng :)"
    mG "Nice to meet you! How were your first week of classes?"
    MsG "It has been going well :). My favorite class so far has been Computer Literacy and Programming! I love coding and I am so amped to be learning Python"
    mG "That's great to hear! I code in G++, but I love Python way more!"
    hide standard mr goose with dissolve
    N "You and Jupyter talk more about your hobbies. You discover that you both enjoy swimming, playing GO FISH with your fellow goose comrades, and finding new plant-based recipes"
    N "The group continues to study and get to know each other. After a few hours of hard work on that Waterloon grind set, you all exchange information and plan to meet up the next day for more studying (and possibly more)."
    MsGthinking "Omg, should I check Wingstagram to see if Jupyter has a girlfriend?"
###############             CL2,EM,SL                ################
    ## menu defines a set of clickable choices for the user
    ## under each "if" circumstance, is a set of actions that happens upon selecting that option
    ## afterwards, the if statement breaks, continuing on with the next code
    menu:
        "Yes, stalk Jupyter's Wingstagram and see if he has a girlfriend":
            N "You open Wingstagram"
            MsGthinking "He has no tagged posts of him with any girls, or any photos with any girls... I think he's single!"
            N "You have learned that Jupyter is single, even though stalking his Wingstagram might be a little creepy... But is it really that creepy?"
            $ shipfavour+=5
            play sound highblingbuttonclickeffect
            pause 1
            play music "audio/rockgardenmusic-animalcrossing.mp3" volume 1.8
        "No, just suffer in ambiguity about Jupyter's relationship status":
            MsGthinking "Damn, I don't really know if I should look at Jupyter's Wingstagram, is that a little creepy?"
            N "You decided not to check Jupyter's Wingstagram to see his relationship status."
            N "Dude, why??"
            N "You know, you could save so much trouble right about now."
            N "Pick your battles then I guess."
            N "Battles that may or may not exist."
    show black with Dissolve(2)

########################################################################################################################################################################
########################################################################################################################################################################

###############            SL,CL2               ################
label day2start:
    show screen Opening1() with dissolve
    show screen day2() with dissolve
    hide mc trelfords office 2 
    hide screen day2 with Dissolve(2)
    ## wait before continuing with code (seconds) 
    pause 3 
    play music rch301musicpolybridge

    scene rch 301 
    show rch 301 with dissolve 
    hide screen Opening1
    show screen bars 
    N "You just finished your MATH 115 tutorial, when you receive a text from Ana. Ana made a group chat with herself, Timmy, Jupyter, and you, on Wingstagram."

    show daytwotextone with dissolve
    hide rch 301 with dissolve 

    menu: 
        "Sorry guys I’m gonna go home and play League of Egg, a new champion called Eggbert came out 3 hours ago!": 
            N "Really?" 
            N "Welp."
            jump day3start

        "Gee wilkers, I sure will join y'all.": 
            T "Yeah I’m down!"
            mG "Sounds good." 

    show dp library with dissolve 
    hide Day2Text1 with dissolve 

    MsGthinking "Omg omg, I’m so excited to see Jupyter again! I hope he can help me study these matrix applications though, I’m so bad at MATH 115."

    show standard mr goose with dissolve 
    mG "Hey [MsGName], nice to see you again!" 
    MsG "Blushing: H-hey Jupyter! How are you?"
    mG "Good good, I’m excited to study together today!"
    MsGthinking "Omg!!! He said he’s excited to study with me today."

    #play music PHONE NOTIFICATION SOUND 

    ## transitions into a text from ana conda 

    hide standard mr goose with dissolve 
    hide dp library with dissolve 

    #show WHAETEVR THE FILE NAME IS FOR THE CHAT with dissolve 
    ## ana says she cannot attend the study session on text message. 
    #hide WHATEVER THE FILE NAME IS FOR THE CHAT with dissolve 

    show dp library with dissolve 
    show standard mr goose with dissolve 

    mG "Damn, I guess it’s just us two. Should we go find a table to sit at to study together?"
    MsG "Yeah sure, let’s go!"
    N "The two of you sit down at a table."
    mG "Studying sucks, let’s play something instead!" 

    hide standard mr goose with dissolve 
    ## give option to play a game with Jupyter or to focus on studying instead 

###############            SL,CL2               ################
    menu: 
        "Choose to follow the original plan to study because you haven’t learned C’s get degrees" :
            MsG "Maybe we should study a bit before gaming it’s better to be prepared for the next tutorial right" 
            mG "Huh? What do you mean? I never study for my tutorials cause it’s such an easy course there’s no way anyone could struggle with it haha."
            MsG "......" 
            mG "Oh, you probably aren’t a very good student. I kind of don’t want to do any studying for now and since the others aren’t coming I think I’m just going to go… I’ll cya around though." 
            N "Somehow despite being given the best opportunity you still managed to mess things up… Your day ends in failure." 
            $shipfavour-=10 
            play sound loserelationshippoints
            pause 2
            jump day3start 

        "Choose to be a gamer goose with Jupyter.":
            N "Now would be a good time to earn some brownie relationship points…" 
            ## transition to game !!!! 

            hide dp library with dissolve 
            jump firstcoinmovingspritegame

###############          CL2                 ################
label returnlostlives:
    N "You failed your mission."
    $ shipfavour-=15
label day2continue: 
    show black    
    $timediff=ogtime-recordedtime+0.1
    if timediff>60:
        $timediffmin=timediff/60
        N "You took [timediffmin] minutes."
        N "Really took your time with that one eh?"
    else:
        N "[recordedtime] seconds, very well done."
    show dp library with dissolve 
    hide GAME SCREEN with dissolve 
    show standard mr goose with dissolve 
    menu:
        "DONE!":
            show dp library with dissolve
            show standard mr goose right facing
            MsG "Bye Jupyter! This was super fun!! We should do this again this week!!" 
            mG "See ya later [MsGName]!!" 
            MsGthinking "He’s so cute!!" 
            N "You walk back to your dorm room, thinking about your study session with Jupyter. It seems like you’ve developed a crush on our homie Jupyter." 

########################################################################################################################################################################
########################################################################################################################################################################

###############             EM              ################
label day3start:
    hide daytwotextone with dissolve
    scene e6 hallway
    show e6 hallway with dissolve
    N "Two weeks later..."
    N "You just finished a Chem Egg Student Society (CESS) meeting when you receive a text from Jupyter asking to hang out in the QNC basement."
    menu:
        "Say no and go to the WEEF office to ask questions about the CHE 100 assignment":
            N "You leave Jupyter on read and decide to head to WEEF to ask the WEEF TAs about your CHE 100 assignment. Boohoo, nerd."
            $shipfavour-=20
            jump day4start
        "Go to QNC and meet Jupyter for some fun times (+10 relationship points)":
            N "You decide to go to the QNC basement to hang out with Jupyter and hopefully get some 'studying' done while you're there."
            scene qnc basement
            show qnc basement with dissolve
            show standard mr goose with dissolve
            mG "Hey [MsG]!! What's up!"
            MsG "Hiiiiiii, I just finished a CESS meeting but I wanted to see you :))"
            hide standard mr goose with dissolve
            show blushing mr goose with dissolve
            mG "Ayo okay bro chill chill, I just wanted to show you my awesome piano skills on this piano."
            MsG "You play piano?! That's so slay, so do I! When did you start playing?"
            hide blushing mr goose with dissolve
            show standard mr goose with dissolve
            mG "Ever since I was a wee little gosling, I played piano in the Ryan Piano School for Goslings"
            MsG "Yoooo that's so cool! Let's play something together :))))"
            hide standard mr goose with dissolve
            N "Pick a song to play!"
            menu:
                "Hungarian Dance No 2. by Franz Liszt":
                    N "Spicy.. try not to mess it up"
                    $ shipfavour+=10
                    jump ddrgamesetup
                "Mary Had a Little Lamb ":
                    N "Seriously?"
                    N "You know what sure if thats what you want to play to impress the drippiest goose on all of campus"
                    N "Better hope Jupyter gets over the fact that you have the skill rating of a toddler..."
                    $ shipfavour-=10
                    jump ddrgamesetup2
                ####
                #transition to ddr minigame
                ###
                ## if game is won grant an additional 15 relationship points
                ## if game is lost no change is relationship points
            #regardless of win/loss/choice in song

###############            EM, CL2, CL              ################
label returnfromddr:
    scene qnc basement with dissolve
    show qnc basement
    N "You and Jupyter jam along happily on the QNC piano, possibly disturbing every other goose in the vicinity."
    show standard mr goose
    MsG "I think we make a pretty good duet! You play super well by the way"
    hide standard mr goosewith dissolve
    show blushing mr goose with dissolve
    mG "Aw thanks [MsGName], you're not so bad yourself!"
    MsG "Thanks Jupyter!! Let's continue to jam on the piano"
    hide blushing mr goose with dissolve
    N "You and Jupyter continue to jam out on the QNC piano, possibly sending every other goose in the room into the 4th dimension with how “beautiful” your playing was. An hour or two passes by, and before you both knew it, it was time for Jupyter to leave to his ECON 120 lecture."
    hide blushing mr goose with dissolve
    show standard mr goose with dissolve
    mG "Bye [MsGName]!! I had fun today!!"
    MsG "Bye Jupyter!! I did too, have fun in econ!"
    mG "Thanks! Have a great day too!!"
    menu:
        "Lean in for a hug":
            $shipfavour+=15
            hide standard mr goose 
            show blushing mr goose 
            N "You lean in for a hug. You can feel Jupyter stiffen and offer you an awkward hug back."
            hide blushing mr goose
            jump day4start
        "Wave goodbye":
            $shipfavour+=5
            hide standard mr goose 
            show standard mr goose right facing
            N "You wave goodbye at Jupyter and he waves back and smiles"
            N "You feel your heart beat a little faster than before. Maybe someone is beginning to feel like they're in love?"
            hide standard mr goose right facing
            jump day4start
                
#end of day 3

########################################################################################################################################################################
########################################################################################################################################################################

###############            SL, CL2               ################
label day4start: 

    show screen Opening1() with dissolve
    show screen day4() with dissolve 
    pause 3 
    hide screen day4 with dissolve

    #play music what audio? 

    scene Chatime
    show Chatime with dissolve
    hide screen Opening1

    show screen bars 
    N "A few weeks have gone by, and you’re getting Chatime in DC with Ana after finishing your CHE 102 Midterm." 
    show ana with dissolve 
    A "How was the midterm? I thought it was pretty easy, but then again, I’m kinda dumb." 
    MsG "I thought it was okay, I’m really glad Professor Tam taught us manometer pressure in CHE 100 because it showed up on our CHE 102 midterm somehow!" 
    A "Lucky duck, I haven’t learned that in any of my Tron courses!" 
    MsG "Sounds like a you problem, what a skill issue." 
    A "Screw you. Oh hey, they’re calling our Chatime orders. I’ll go grab our orders for us." 

    hide ana with dissolve 
    show standard mr goose with dissolve 

    mG "Oh hey [MsG], what are you doing here?" 
    MsG "Jupyter! Ana and I were grabbing Chatime after our CHE 102 midterm, what about you? Oh hey Timmy!" 

    hide standard mr goose with dissolve 
    show timmy with dissolve 

    T "Hey [MsG]! I just finished CHE 102 too! Man, that was so difficult for me. You and Ana got Chatime right? What did you get?" 
    MsG "Oh, I got a grass jelly roasted milk tea with 30 percent sugar and no ice. Are you guys getting Chatime too?" 
    T "Yeah, just give us a moment to order and get our bubble tea. Do you want to hangout together? We can go to E6 and fool around. Jupyter has another midterm next week, so he can study while we’re there." 

###############          SL                 ################
    menu: 
        "Go to E6 with Ana, Timmy, and Jupyter and spend some quality time with the homies": 
            N "You decide to go to E6 with Ana, Timmy, and Jupyter." 
            $shipfavour+=20
            play sound highblingbuttonclickeffect
            #hide CHATIME DC PHOTO with dissolve 
            show e6studyspace2 with dissolve 
            N "Jupyter pulls out his computer and starts doing some LEETCODE LIKE A NERDY CS BOY (which is exactly what he is). You decide to watch and admire Jupyter as he codes. Maybe you should complement him as he codes…"
            MsGthinking "Oh no what should I do???????"
            MsGthinking "Ahhhhhh think think think fast."
            MsGthinking "HhhhHHHHhh uhhhhhh let me weigh the options."
            jump tugofwar
        "Decline the offer and go back to your residence to die on the inside." :
            MsG "Sorry guys, I gotta go back to my res. My regularly scheduled mental breakdown is in 10 mins, and I need to cry my eyes out to the ending scene to the k-drama Snowdrop in order to feel something. Bye guys!" 
            show sad mr goose with dissolve 
            mG "Aw man, I really wanted to hang out with [MsG]. Who knew she was so weird?!"
            hide sad mr goose with dissolve 
            N "Safe to say, you had an amazing time bawling your eyes out to a TV show, while Ana, Jupyter, and Timmy hung out together in E6. If I were you, I’d watch out if you wanted to date Jupyter." 
            $shipfavour-=40 
            play sound loserelationshippoints
            pause 3
            jump day5  

###############            CL2               ################
label returnfromtog:
    menu:
        "By the way, I think you look so cool when you flap those wings, Jupyter.":
            scene e6studyspace2
            show e6studyspace2 with dissolve
            N "I should not have trusted you."
            $shipfavour+=20
            mG "Heh, thanks."
            N "He what????"
            jump day4end
        "....":
            scene e6studyspace2
            show e6studyspace2 with dissolve
            N "......"
            mG "....."
            MsG "....."
            mG "Uhhhh anyways, let's play a number guessing game...?"
            jump numberguessinggame

label returnfromnumberguessing:
    jump day4end

###############           SL                ################
label day4end:
    scene e6studyspace2
    show e6studyspace2 with dissolve

    N "You attempt to flirt with Jupyter as he codes." 
    show standard mr goose right facing with dissolve 

    MsG "Jupyter, are you a duck? Because you make my heart waddle." 

    hide standard mr goose right facing with dissolve 
    show blushing mr goose right facing with dissolve 

    mG "Haha good one! Are you made of fluorine, iodine, and neon? Because damn girl you’re fine." 
    MsG "Sheesh Jupyter that was pretty smooth!" 

    hide blushing mr goose right facing with dissolve 
    show timmy mouth at left with moveinleft 

    T "Hey Ana, are you getting some vibes from these two?" 

    show ana mouth at right with moveinright

    A "Yeah Timmy, the vibes are very very interesting…" 

    hide timmy mouth with dissolve 
    hide ana mouth with dissolve 

    N "You and Jupyter keep firing pickup lines at each other, making Ana and Timmy third wheel awkwardly on the side." 
    N "Needless to say, little leetcoding was done by Jupyter, and no studying was done by the rest of you. Before you knew it, it was already dinnertime. Ana had a club meeting after dinner, and Timmy had to go rescue his roommate from the depths of diarrhea in the V1 washroom."

    show standard mr goose with dissolve 

    mG "Hey [MsGName], do you wanna go get dinner together? Just the two of us?" 

    menu: 
        "Go get dinner with Jupyter – this might be a good chance to make a move":
            MsG "Of course!!" 
            $shipfavour+=20
            play sound highblingbuttonclickeffect
            pause 1
            jump campuspizzaline
        "Say no and go get crappy food from your residence’s dining hall":
            N "You decline the dinner invitation from Jupyter." 
            MsG "Sorry Jupyter, the residence chicken fingers kinda got a grip on my stomach, they’re just so memorable that I just have to have more." 

            hide standard mr goose with dissolve 
            show sad mr goose right facing with dissolve 

            mG "Bro you are so weird. I guess enjoy your Stockholm syndrome chicken fingers… Goodnight." 

            hide sad mr goose right facing with dissolve 

            N "You feel remorse as you see Jupyter’s back turn away from you and walk away. Maybe you should’ve eaten chicken fingers with him…" 
            N "-10 relationship points." 
            N "Why would you want to eat a bowl of chicken fingers for the 5th day in a row? Weirdo." 
            jump day5
        

###############           CL2                ################
label campuspizzaline:
    scene CampusPizza
    #show campus pizza background????
    hide e6studyspace2 with dissolve 
    mG "Man this line is taking so long."
    mG "Let's burn some time the old fashioned way?"
    menu:
        "Yeah, let's do it!":
            jump rpstest11
        "No, I just want to look at the cool neon signs":
            mG "Aw don't be a party pooper."
            mG "C'mon!"
            jump rpstest11
label returnfromrps:
    N "You and Jupyter later enjoy a very nice large pizza with grass instead of pepperoni (I mean, you both are geese…). The two of you are having a very nice conversation. Suddenly, Jupyter asks you an unexpected question." 
    mG "Hey [MsGName], do you have a crush on anyone?"
###############          SL                 ################
    menu: 
        "Say no, crushes are for lame geese, and you’re not lame!":
            show angry ms goose with dissolve 
            MsG "Nah, crushes are for weirdos. I’m a girlboss with attachment issues ya know? Why would I like anyone?!"
            hide angry ms goose with dissolve 
            pause 2
            show sad mr goose right facing with dissolve 
            mG "Ah, that’s fair!" 
            hide sad mr goose right facing with dissolve 
            $shipfavour-=50
            play sound loserelationshippoints
            pause 3
        "Say yes and refuse to elaborate.":
            show blushing ms goose right facing with dissolve 
            MsG "Yeah I kinda like this one guy goose, he’s a real charmer, y’know." 
            hide blushing ms goose right facing with dissolve 
            pause 2
            show blushing mr goose right facing with dissolve 
            mG "Oooh he must be one lucky goose then!" 
            $shipfavour+=40
            play sound highblingbuttonclickeffect
            pause 1
    mG "I didn’t know time could fly by so quickly! Should I walk you home?" 
    MsG "That would be great, thanks!!" 
    N "Jupyter walks you back to your residence. He gives you a goodbye hug and waits for you to enter your residence building before leaving. What a… romantic evening…?" 


########################################################################################################################################################################
########################################################################################################################################################################

###############            CL               ################
transform endingtrans:
    zoom 0.7
    xalign 0.5
    yalign 0.5
label day5:
    ##CL insert text here that leads to the endings
#    show screen wheretheconfessionhappens ###change these when a screen is decided
#   hide screen screenbeforetoday
    scene ago
    show ago with dissolve
    
    N "It’s been a crazy first term at the University of Waterloon and you can’t believe that it’s only been that long since you’ve met Jupyter! After a long day of classes, you get a text from him asking if you want to explore downtown Toronto with the group. Of course, you accept and you all explore the downtown area." 

    N "After a long ride on the GO Train, you go into the ago to see all the wonderful art it has to offer. Then, you waddle around the sketchy streets of Toronto before ending up in the Christmas Market."

    show christmas market 2 with dissolve
    hide ago

    show standard mr goose right facing:
        yalign 0.95
        xalign 0.05
        zoom 0.8
    with dissolve
    mG "Hey [MsG]! How were your final exams?"

    MsG "Jupyter!!!! I think they went well! All of our studying really paid off and I am confident I passed them all. Is everyone excited to be in the Christmas Market? Although I don’t love the cold, Christmas is my favourite holiday!"
    show ana:
        yalign 0.95
        xalign 0.95
        zoom 0.8
    with dissolve
    A "Frankly, I am super happy to be done exams! Chem was really hard!"
    show timmy:
        yalign 0.45
        xalign 0.5
        zoom 0.65
    with dissolve
    T "I personally wish I was down in Florida right now! This cold weather really sucks!"

    hide standard mr goose right facing
    hide ana
    hide timmy
    with dissolve

    show blushing ms goose with dissolve

    mG "I love Christmas too! It’s the best season to show the people you care about what they mean to you. I know there is someone whom I want to give extra thanks to."
    
    show standard ms goose:
        zoom 0.43
        xalign 0.5
        yalign 0.99
    hide blushing ms goose
    with dissolve

    MsG "Lets go explore the Market!!!!"
    
    hide standard ms goose
    
    show christmas market with dissolve

    N "You, Ana, Timmy and Jupyter waddle around the Christmas Market and explore all the beauty it has in store for you. The Christmas lights shine bright in the night sky and you all approach the gorgeous massive Christmas tree in the middle of the square."

    MsG "This has got to be the BIGGEST Christmas tree I’ve ever seen! Like how do they even get this thing in here?"
    show timmy:
        yalign 0.45
        xalign 0.5
        zoom 0.65
    show ana:
        yalign 0.95
        xalign 0.95
        zoom 0.8
    with dissolve
    T "I don’t know but it's pretty epic!"

    A "Hey Tim-Tim, do you want to come get some Hot Cocoa with me? I think there Is a booth down this way"

    T "For sure! I am so cold I feel like I will turn into a Goose-sicle"
    hide ana
    hide timmy
    with easeoutleft
    show standard mr goose right facing:
        yalign 0.95
        xalign 0.1
        zoom 0.8
    with dissolve
    N "Ana and Timmy go off and somehow you and and Jupyter have ended up alone. The mood in the square has given you a warm feeling of happiness and romance. Jupyter gets a little closer and seems to have an anxious look about him"

    MsG "Jupyter is everything ok? You look like you’re gonna throw up haha"

    hide standard mr goose right facing
    show blushing mr goose right facing:
        yalign 0.7
        xalign 0.1
        zoom 1.1
    with dissolve

    mG "Huh? Oh yea. Sorry I was just thinking about something. [MsG] there has been something I’ve been wanting to tell you for the longest time."

    MsG "What’s up? You can tell me anything"

    mG "I have had so much fun getting to know you over this past term. You have helped me with so many things and made me the goose I am today. This first term has been so stressful and hectic and I don’t think I would have survived it without you by my side. I guess what I am trying to say is…"
    
    mG "..."

    mG "I like you [MsG]... " ###Have fun rewriting this charles :D
    #CL create 2 endings that  have the conditional statements of having a certain likeability
    #need ending screens unless they continue from before

###############            CL               ################
    if shipfavour>=115:
        show blushing ms goose:
            yalign 0.7
            xalign 0.8
            zoom 0.9
        with dissolve 

        MsG "Oh Jupyter, I like you too! I’ve been meaning to tell you, but school just kept us so busy, and I never got the right opportunity to…" 

        show blushing mr goose right facing:
            yalign 0.7
            xalign 0.1
            zoom 1
        with dissolve 

        mG "Oh my goose-ness, really? I’m so happy you feel the same way, [MsG]. Would you like to be my girlfriend then?"
        MsG "I would love to! This is the best day in my entire life. Thank you, Jupyter!" 

        hide blushing mr goose with dissolve 

        ###please insert something into here i was hit by a frieght train of plot development way too quickly

        N "You and Jupyter end up dating! What a beautiful and romantic ending to this story. Makes me want to tear up as well."
        hide screen bars
        play music 'audio/Glimpseofus.mp3'
        scene EndCreditsBG
        show screen EndCreditsBG
        show screen EndCredits1 with Dissolve(2)
        pause 3
        hide screen EndCredits1 with dissolve
        hide screen EndCreditsBG
        jump endcredits2

        return
    else:
    ##CL  maybe add in a ms goose with an offset so that theyre facing each other?
        N "You tense up at Jupyter’s confession. You look like you’ve just seen a ghost and a half. The poor man Jupyter looks like he’s about to cry a river and not build a bridge to get over it."
        MsG "Oh okay.. Um… Thanks for telling me Jupyter."
        
        hide blushing mr goose right facing
        show sad mr goose right facing:
            yalign 0.9
            xalign 0.15
            zoom 0.9
        with dissolve
        
        mG "Oh yeah um… no rush to respond with your feelings… I just wanted to let you know." with hpunch
        MsG "Yeah um.. no worries!"
        MsGthinking "Aw honks, [MsG], you are such a mother fluffer! Now things between us will be awkward!! Why do I keep messing up these things"
        
        hide sad mr goose right facing

        show screen Timeskip with dissolve
        
        show screen TimeSkipText1 with Dissolve(5)
        
        hide screen TimeSkipText1 with dissolve
        
        show screen TimeSkipText2 with Dissolve(5)
        
        hide screen TimeSkipText2 with dissolve
        
        hide screen Timeskip with dissolve

        scene badending at endingtrans
        
        N "After your little screw up, Jupyter built a bridge and got over his feelings for you, and ends up dating your best friend, Ana Conda. Oops."
        mG "Hi [MsG]! Did I ever tell you that Ana and I are dating now?"
        MsG "That’s great news Jupyter! You deserve someone as great as Ana..."

        MsG "I-I’m so happy for the two of you....."

        hide screen bars
        play music 'audio/Glimpseofus.mp3'
        show screen EndCredits1 with Dissolve(2)
        pause 3
        hide screen EndCredits1 with dissolve
        jump endcredits2

        return

        ##play audio by Joji as an endtune and transition to an end screen
        #play music (filename)
        show screen EndCredits1() with dissolve ##change back to day1 after testing
    ## wait before continuing with code (seconds)
    pause 3
    hide screen EndCredits1 with Dissolve(3)##change back to day1 after testing
    ## add in the the end, and thank you screens --> for camilo to finish
    "placeholder"
    return