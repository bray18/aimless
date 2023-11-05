# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# player is defined in start
default player_name = ""
default s_name = ""
default hasTablet = False
default hasSoup = False
default hasEMP = False
default gadgets = True
default panera = True
default apartment = True
# scientist definition is below: character name is chosen by player

init python:
    # Define the starting time for the timer
    global time_left
    time_left = 10

screen timer_screen(image1, label1):
    text str(time_left) align (0.96, 0.05) size 75 color "#000000"
    imagebutton:
        idle image1
        hover image1
        focus_mask image1
        action If(time_left > 0, Jump(label1))

label timer_apartment:
    # Display the timer screen
    show screen timer_screen("emp_apartment.png", "apartment_end")

    # Count down
    while time_left > 0:
        $ renpy.pause(1.0)
        $ time_left -= 1
        $ renpy.restart_interaction()

    # Hide the timer screen
    hide screen timer_screen
    hide emp_apartment

    # Jump to a given label when the timer runs out
    if time_left <= 0:
        jump apartment_end_fail

# Functions are here
screen imageCompare(image1, image2, label1, label2):
    #randomly assign one image to each side of the screen
    python:
        import random
        width = 650
        if random.randint(0,1) == 0:
            left = im.Scale(image1, width, renpy.image_size(image1)[1] * width / renpy.image_size(image1)[0])
            leftLabel = label1
            right = im.Scale(image2, width, renpy.image_size(image2)[1] * width / renpy.image_size(image2)[0])
            rightLabel = label2
        else:
            left = im.Scale(image2, width, renpy.image_size(image2)[1] * width / renpy.image_size(image2)[0])
            leftLabel = label2
            right = im.Scale(image1, width, renpy.image_size(image1)[1] * width / renpy.image_size(image1)[0])
            rightLabel = label1
    imagebutton:
        idle left
        #left half of screen centered
        xalign 0.2
        yalign 0.5
        action Jump(leftLabel)
    imagebutton:
        idle right
        #right half of screen centered
        xalign 0.8
        yalign 0.5
        action Jump(rightLabel)
    

# The game starts here.
label start:
    $ medic = "Joe"
    $ engineer = "Jordan"
    $ cook = "Jacque"
    play music "Arriving.mp3" loop
    "This is our team's submission to TigerHacks 2023!"
    "For a list of credits and sources, please see the credits tab."
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    $ p = Character(player_name, who_color="#ffffff")
    "Thanks. And your pronouns?"
    menu:
        "He/Him":
            $ pronoun1 = "he"
            $ pronoun2 = "him"
            $ pronoun3 = "his"
            $ pronoun4 = "himself"
            $ pronoun5 = "he's"
        "She/Her":
            $ pronoun1 = "she"
            $ pronoun2 = "her"
            $ pronoun3 = "her"
            $ pronoun4 = "herself"
            $ pronoun5 = "she's"
        "They/Them":
            $ pronoun1 = "they"
            $ pronoun2 = "them"
            $ pronoun3 = "their"
            $ pronoun4 = "themselves"
            $ pronoun5 = "they're"
    "Welcome, [player_name]."

    "Finally, which name do you like the most?"
    menu:
        "Jassandra":
            $ s_name = "Jassandra"
        "Jessica":
            $ s_name = "Jessica"
        "Jolene":
            $ s_name = "Jolene"
    $ scientist = Character(s_name, who_color="#ff9900")
    $ medic = Character("Joe", who_color="#cc00ff")
    $ engineer = Character("Jordan", who_color="#ff3333")
    $ cook = Character("Jacque", who_color="#33cccc")
    $ server = Character("Server", who_color="#00ff00")
    
    jump intro
    return
label intro:
    scene bg_space:
        xanchor 960 yanchor 540
        xalign 0.5 yalign 0.5
        linear 60.0 zoom 1.25
    
    "As the ship re-enters the established radius of communication, you send a ping to mission control and start the countdown. A response should come within five days."
    "..."
    "After six days, you send another ping, this time risking adding the extra data of a message: \"mission failure, returning on sufficient fuel, please respond,\" in the form of three coded numbers."
    "As you get closer, the time between messages should decrease. They should get your message in two days now."
    "..."
    "Nothing. Not even from the international allies that you pinged with an SOS. It's as if you've been ghosted by the entire world."
    "Your team starts investigating the lack of communication. The onboard system could be malfunctioning."
    "The satellites may be interfering with each other. There could have been a mishap rendering the communication tech on Earth inoperable. In any case, it was time to act."
    "The team gets to work, trying everything they can to get into contact with anyone they can while preparing for the worst."

    show scientist_neutral
    "[s_name] breaks her usual attitude and spends time on a prototype of a high-precision sonic beam. "
    hide scientist_neutral
    show medic_neutral
    "Joe consolidates the remaining medical supplies, just in case."
    hide medic_neutral
    show cook_neutral
    "Jacque prepares a meal with the dwindling food rations. "
    hide cook_neutral
    show engineer_neutral
    "Jordan is still in space jail for killing Jeff."
    "Jeff is still dead."
    hide engineer_neutral
    show beef_neutral
    "Beef takes a nap."
    hide beef_neutral

    "..."

    scene bg_screen
    show glass onlayer new_overlay

    "Now, you've finally made a breakthrough. You decide to decode the scattered frequencies you can pick up through the ship's on-board system, testing hundreds of descramblers to pick up any remnant of signals from Earth."
    "The first somewhat comprehensible set of captured data reads: "
    "w̵̬͒͌h̵̼̩̘̆͋͠e̶̛͔̊̌ń̸̨̜͂ ̷͕̲̪̂ț̸̦̓h̵͚͈̄̉e̵͇̳͑ ̸̮̯̈́͐̂i̸̭̔̋͑m̴̻͉̈́̂p̵̲̣͔̀͒̽o̵̠͓̱͝ś̶̫̠t̸͍͚͊͝ề̴̙̣͝r̸̠̤̀ ̶̡͖̠̽ĭ̴̬͙̰s̴̰̣̈ͅ ̷̠̭̺͋s̴̫͆̈́u̷̺̣͐̌̔ŝ̷͓̃̍"
    "You have no idea what it means."
    "..."
    "After days of troubleshooting, you start seeing images. Some are familiar, but some are... strange."
    "Select the image that seems strange to you."

    call screen imageCompare("compare/human_1.jpeg", "compare/ai_1.jpg", "no1", "yes1")

    label no1:
        "The cow seems pretty normal upon a second glance."
        jump intro2
    
    label yes1:
        "The set of images seems extremely low quality, but your software assures you that they are not corrupted."
        "Why was this so important that people were sharing it enough to reach you?"
        jump intro2
label intro2:
    "Over the next few weeks, your software decodes text and images faster and faster as the speed and amount of data reaching your ship increases."
    "The strange images are still present, but they're getting harder to spot."
    "Select the image that seems strange to you."
    
    call screen imageCompare("compare/human_2.jpeg", "compare/ai_2.png", "no2", "yes2")
    label no2:
        "The image seems to be a normal picture of a dog."
        jump intro3
    label yes2:
        "There's something about the eyes that unsettles you. It feels so real, and yet, not."
        jump intro3
label intro3:
    "Select the image that seems strange to you."
    call screen imageCompare("compare/human_3.jpeg", "compare/ai_3.png", "no3", "yes3")
    label no3:
        "The computer looks like the ones you have on board, and seems pretty normal."
        jump intro4
    label yes3:
        "The keys look like they're melting, and yet the photo looks professionally shot. What's with those colors in the corner?"
        jump intro4
label intro4:
    "Select the image that seems strange to you."
    call screen imageCompare("compare/human_4.jpeg", "compare/ai_4.png", "no4", "yes4")
    label no4:
        "It's pixel art, but it seems pretty standard."
        jump intro5
    label yes4:
        "It looks like pixel art at first glance, but it's not on a grid and the colors are blending together in spots."
        jump intro5
label intro5:
    "Select the image that seems strange to you."
    call screen imageCompare("compare/human_5.jpeg", "compare/ai_5.jpg", "no5", "yes5")
    label no5:
        "The man looks happy. You're happy to see a new face for the first time in years."
        jump intro6
    label yes5:
        "Something about him seems... {i}off{/i}. You can't put your finger on it, but he just doesn't seem right."
        jump intro6
label intro6:
    
    hide glass onlayer new_overlay
    scene bg_earth1
    show earth2:
        zoom 0.5
        xanchor 960 yanchor 540
        xalign 0.5 yalign 0.5
        linear 60.0 zoom 1
    with dissolve
    "After a few more anxious weeks, you re-enter the solar system while becoming increasingly concerned."
    "Your crew has gathered to witness the pale blue dot come into view as you speed towards it."

    "..."

    scene bg_ship

    show medic_neutral   
    medic "Hey guys, shouldn't we have gotten some landing instructions by now?"
    hide medic_neutral
    show engineer_neutral with dissolve
    engineer "I guess we really have been abandoned."
    hide engineer_neutral
    show scientist_neutral with dissolve
    scientist  "So we have no guidance whatsoever? What are we going to do?"
    hide scientist_neutral

    scene bg_earth with hpunch
    p "We're running out of fuel too. There's not much we could even do for ourselves as far as landing location."
    "Despite your best efforts, you initiate the final steps for emergency landing and hope for the best."
    "The ship begins to shake violently as it enters the atmosphere. The crew braces themselves for impact as warning lights and alarms blare."

    p "Everyone brace yourselves!"

    scene bg_ship
    show scientist_surprised
    scientist "Do we have odds on this?? I'm freaking out a bit here!"
    hide scientist_surprised
    show medic_neutral with dissolve
    medic "The best thing we can do is brace and try to remain calm-"
    hide medic_neutral
    show scientist_surprised with dissolve
    scientist "WE'RE ABOUT TO CRASH, HOW CAN YOU BE CALM?!"
    hide scientist_surprised
    show medic_surprised with dissolve
    medic "I said try!"
    hide medic_surprised
    show cook_surprised with dissolve
    cook "SACRE BLEU!"
    hide cook_surprised
    scene black with fade
    show engineer_surprised
    engineer "WHAT THE HELL ARE YOU GUYS DOING UP THERE?!"
    hide engineer_surprised with dissolve

    "The ship crashes into the ocean with a violent splash. The crew is thrown around the ship as it fights against the water."

    "Dazed, you look around the ship. The crew is still alive, but the ship is starting to take on water."
    "You rush down to the space jail to get Jordan out of containment as the rest of the crew makes their way to release the hatch."
    "Everyone gets out of the ship with the supplies they were able to save."

    scene bg_landing with fade
    "This is usually when a helicopter would come to pick you up, but there's no one here."
    "You're on your own."
    "You see a shoreline in the distance, and collectively decide to swim there."

    scene bg_sink with dissolve

    ""

    jump discovery

    return
# ship, "tutorial"
# Landing sequence, sink
# sun goes down, timelapse

label discovery:
    scene bg_beach_day
    "You collapse on the shore, finally resting."
    show bg_beach_dusk with dissolve
    ""
    show bg_beach_night with dissolve
    ""
    # sound of waves crashing against the sand
    "After some deliberation, you start to walk along the shoreline to search for signs of life."
    
    scene bg_forest

    "Your team starts discussing theories about what happened to the world."
    show medic_neutral with dissolve
    medic "Could have been a disease. Perhaps a pandemic. Is that too far fetched?"
    hide medic_neutral
    show scientist_neutral with dissolve
    scientist "They could've just keeled over and died."
    hide scientist_neutral
    show cook_neutral with dissolve
    cook "One of the other missions could have found a new habitable planet. Maybe they just left."
    hide cook_neutral
    show engineer_neutral with dissolve
    engineer "Or {i}maybe{/i} we're in the middle of nowhere and that's why no one would want to be here!"
    hide engineer_neutral
    scene bg_city

    "After several days of walking, you stumble across a city that seems liminal and devoid of all human life."
    "You hear a sound coming from around the corner of a building."
    show aimless_1 with dissolve
    "A person! You... think? It's like they don't match the look of the rest of the world, completely out of place."
    "It reminds you of the images you were decoding back on the ship."
    "They talk to your team about farming, spewing random facts as if trying to explain that it needs something it can't properly communicate."
    
    "\"Farming is a timeless profession that sustains our world by providing essential food, fostering biodiversity, and supporting local economies.\""
    "\"I'm proud to be a farmer because it allows me to nurture the land, embrace sustainability, and connect with our rich cultural heritage.\""
    "\"The wonders of farming lie in its ability to feed, nourish, and sustain our planet while preserving our environment and traditions.\""
    
    "You try to end the conversation quickly, but it doesn't seem to understand."
    p "That's great. We're going to go now."
    "The Aimless seems to accept this feedback and leaves."
    hide aimless_1 with dissolve
    "It's time to decide what to do next. Every move counts."
    p "We need information. Does anyone know where we are?"

    jump branches
    
    return
# First interaction with aimless

label branches:
    hide screen timer_screen
    show engineer_surprised with dissolve
    engineer "Actually... I think we're in Santa Clara. My apartment is only a few blocks from here. It might have some things that could be useful."
    hide engineer_surprised
    show engineer_neutral with dissolve
    "Jordan shifts under her own weight, looking almost longingly in the direction of her apartment. There could be a stronger motivation for wanting to go."
    hide engineer_neutral
    show cook_neutral with dissolve
    cook "Or {i}maybe{/i} we should try and get some food. I'm starving and the berries aren't enough. Is there a Panera Bread around here? I love Panera."
    hide cook_neutral
    show scientist_surprised with dissolve
    scientist "Panera?! You mean St.Louis Bread Company?"
    hide scientist_surprised with dissolve
    "Jacque rolls his eyes."
    show engineer_neutral with dissolve
    engineer "Yes, actually, it's within walking distance. I think it's that way."
    hide engineer_neutral
    show medic_neutral with dissolve
    medic "We could try to find a TV or something. Maybe there's some news about what happened."
    hide medic_neutral
    show engineer_neutral with dissolve
    engineer "There's a Greatest Gadgets pretty close by. Don't they usually have TVs running?"
    p "The saturation is always cranked up stupid high on those things, but that could work."
    hide engineer_neutral with dissolve

    label firstmenu:
        play music "menu.mp3" loop
        scene bg_city
        "What do you want to do now?"
        menu:
            
            "Go to Greatest Gadgets" if gadgets:
                jump gadgets

        
            "Go to Panera Bread" if panera:
                jump panera
        
    
            "Go to Jordan's Apartment" if apartment:
                jump apartment

            "Go farther out" if (not gadgets or not panera or not apartment):
                jump park
    return

#GADGETS
screen gadgetTablet():
    imagebutton:
        idle "bg_gadgets_tablet.png"
        hover "bg_gadgets_tablet.png"
        focus_mask "bg_gadgets_tablet.png"
        action Jump("gadgets_end")
screen custom_menu:
    frame:
        yalign 0.2
        has vbox:
            textbutton "Leave":
                action [Hide('gadgetTablet'), Jump('firstmenu')]
label gadgets:
    $ gadgets = False
    scene bg_gadgets
    show bg_gadgets_tablet
    "As you walk into Greatest Gadgets, you look up to find the TV section."
    "On your way, you see no employees. Normally they would be hounding you with questions about what you were in for by now."
    "You notice all of the TVs on display have static color bars, except for one."
    show bg_tv with pixellate
    "A shrill tritone rings from the TV as it repeats a message in a computerized voice."
    "\"This is an Emergency Alert for the following counties: Alameda, Santa Clara, San Mateo, Santa Cruz. Ensure you have a stock of nonperishable food and water.\""
    "\"Unless necessary, do not leave your homes. Avoid interacting with unknown persons at all costs.\""
    "\"This is an Emergency Alert for the following counties: Alameda, Santa-\""
    "It doesn't give you any more information than you already had."
    hide bg_tv with pixellate
    show scientist_neutral with dissolve
    scientist "That's creepy."
    hide scientist_neutral
    show medic_surprised with dissolve
    medic "It sounds intentionally vague. There's more to this than a standard shelter order."
    p "Let's look around and see if there's anything here that can help us."
    hide medic_surprised with dissolve
    "Click on anything you think may help you."
    show screen gadgetTablet
    call screen custom_menu
    jump firstmenu
    return
label gadgets_end:
    $ hasTablet = True
    #remove old background tablet now
    hide bg_gadgets_tablet
    hide screen gadgetTablet
    show tablet:
        xalign 0.5
        yalign 0.4
    "YOU GOT THE DRAWING TABLET!"
    jump firstmenu

label panera:
    $ panera = False
    scene black
    "As you walk into Panera, a friendly voice greets you."
    scene bg_panera_worker with dissolve
    "\"Welcome to Panera Bread! How may I help you?\""
    show cook_neutral at left with moveinleft
    cook "I'll take one bowl of the broccoli cheddar soup, please."
    "The group looks at him."
    cook "Make that five."
    hide cook_neutral with moveoutleft
    scene bg_panera_worker
    "After the crew gets their meals, you chat with the employee."
    p "You're the first normal person we've seen in a while. What's going on?"
    "\"I'm not sure myself, but I do know that employees haven't been coming in lately. It's just me and the manager.\""
    p "Do you know anything about what happened? Where did they go?"
    "\"I've been working nonstop for days now. Not that I'm complaining. I love Panera Bread and think everyone should eat here!\""
    "\"... But I haven't had many customers at all. You're the first today. Here, look at this schedule for when people were supposed to come in.\""
    show bg_sheet with dissolve
    "\"Strange, right? People just stopped showing up. They all love Panera as much as me, so it's very unusual.\""
    hide bg_sheet with dissolve
    p "Ok. Thanks for the soup."
    show cook_neutral at left with moveinleft
    cook "It's {i}broccoli cheddar{/i} soup."
    p "Thanks for the {i}broccoli cheddar{/i} soup."
    cook "Can we take some for the road? I feel like it'll be worth it!!"
    menu:
        "Take some soup":
            $ hasSoup = True
            show soup:
                xalign 0.5
                yalign 0.4
            "YOU GOT BROCCOLI CHEDDAR SOUP!"
            cook "Yay!"
        "Leave":
            cook "Aww."
    jump firstmenu
    return
# #204482

label apartment:
    $ apartment = False
    scene bg_apartment
    show emp_apartment
    "As the group enters the apartment, you notice some details that you never knew before about Jordan's life."
    "You had heard a little about her fiance, but not much. Now a picture of the two of them, taken before your crew left Earth, is staring you down from across the apartment."
    "There are an abundance of small appliances littering her kitchen counters. Her fiance must like to bake."
    "However, the most noticeable thing about the space is that it is unoccupied by the famed fiance."
    "Jordan doesn't seem to be bothered by this, though, as she immediately goes to a newspaper on the top of her coffee table."
    show engineer_neutral with dissolve
    engineer "Aha! I bet this can help us figure out what's been going on."
    hide engineer_neutral
    show medic_neutral with dissolve
    medic "What does it say?"
    hide medic_neutral 
    show engineer_neutral with dissolve
    engineer "Not much. But I think it might be of use to us...Somehow."
    "Jordan suddenly looks wistful. She stares longingly at the photo of herself and her fiance. You start to feel a little bad that her fiance isn't here to greet her."
    p "Is everything okay?"
    engineer "Yeah, it's just... I really thought she would be here when I got home."
    hide engineer_neutral with dissolve
    "The crew begins to realize just how heartbroken Jordan is in this moment. They look at the photo, respectfully allowing Jordan a moment of peace."
    show photo:
        xalign 0.5
        yalign 0.4
    with dissolve
    "..."
    hide photo with dissolve
    "You hear a rustling noise behind you."
    "You turn around and{nw}"
    show aimless_special with dissolve
    "Oh. Oh no."
    "Jordan is frozen in place, staring at the Aimless."
    hide aimless_special  
    show engineer_surprised with dissolve
    engineer "Is that...?"
    "The Aimless looks at Jordan, then at the photo, then back at Jordan."
    "It starts to speak."
    hide engineer_surprised
    show aimless_special with dissolve
    "\"I'm sorry, I didn't mean to startle you. I was just looking for someone to talk to.\""
    hide aimless_special
    show engineer_surprised with dissolve
    engineer "Do you recognize me?"
    hide engineer_surprised
    show aimless_special with dissolve
    "\"I'm sorry, I don't. Preheat your oven before baking to ensure even cooking, and always measure your ingredients accurately for consistent results.\""
    "It starts to lurch towards Jordan. You've got to go, NOW."
    hide aimless_special 
    show scientist_surprised with dissolve
    scientist "Let's grab what we can and get out!"
    hide scientist_surprised with dissolve
    "It looks like you've got about 10 seconds to grab something. You visualize approximately how long you have in, let's say, the upper right hand corner of your vision."
    show clock_overlay with dissolve
    jump timer_apartment

    #turns emp_apartment into a clickable item that will take you to the apartment_end label when clicked, but can only be clicked for 10 seconds, visually displayed via a countdown text item updating every second. if time runs out, take to apartment_end_fail
label apartment_end:
    hide screen timer_screen
    hide emp_apartment
    $ hasEMP = True
    show emp:
        xalign 0.5
        yalign 0.4
    "YOU GOT THE ELECTROMAGNET!"
    "You quickly grab the electromagnet and run out of the apartment together."
    jump firstmenu
    return
label apartment_end_fail:
    "You run out of the apartment in a scramble, empty-handed."
    jump firstmenu
    return

label park:
    #are you sure?
    "Are you sure? You probably won't be able to come back to the city if you leave now."
    menu:
        "Yes, I'm sure":
            jump park2
        "No, I want to go back":
            jump firstmenu
label park2:
    play music "Arriving.mp3"
    "You hear faint sirens blaring. The group decides to head in the direction of the siren to see if you can get to the bottom of whatever is going on."
    scene bg_park

    "After about an hour, you arrive at a park. According to Jordan, it's called Central Park. It's got a pool, which apparently makes it the \"better Central Park.\""
    
    show aimless_squirrel:
        zoom 0.5
        xalign 0.5
        yalign 0.5
    with dissolve
    "A squirrel appears straight ahead. Is... is it smoking AND drinking?!"
    show engineer_surprised with dissolve
    engineer "Wow! That is a messed up squirrel."
    hide engineer_surprised
    show medic_surprised with dissolve
    medic "Yeah... he's kinda freaking me out with that monocole. Is that a monocole???"
    hide medic_surprised with dissolve
    p "We've gotta move. I don't like this."
    hide aimless_squirrel

    show cook_surprised with dissolve
    cook "That was really strange, wasn't it? Hopefully we don't run into anything like that again."
    hide cook_surprised

    show aimless_duck with dissolve
    "It's a duck. Kind of."
    p "Does it have a piece missing? Is this an optical illusion or does it have a piece missing?"
    hide aimless_duck with blinds
    show scientist_neutral with dissolve
    scientist "Yeah, it did. The anatomy was all wrong too. I don't know what to make of it."
    hide scientist_neutral with dissolve
    show aimless_group with pixellate

    "That crowd of Aimless came from nowhere, they all just seemed to come together towards a central point."
    p "Hey team. ...where do you think they're going?"

    hide aimless_group
    show scientist_neutral with dissolve
    scientist "I don't know, but maybe they can lead us to how we can solve this mystery once and for all!"
    hide scientist_neutral
    
    show cook_neutral with dissolve
    cook "I think you may be right, [s_name]. I think we should follow them."
    hide cook_neutral with dissolve
    
    p "Alright. Then let's go."
    "The crew starts following the group of Aimless closely, being careful not to get spotted."
    "The path gets narrower, forcing you to get closer to the group to keep a visual."

    jump training1
    return

label training1:
    play music "Training.mp3"
    scene black with fade
    "It's now or never. If you get caught by the group of Aimless, there's no telling what would happen."
    "It's time to blend in. You'll only have a few seconds to move."
    "Choose the item that you think was generated by the Aimless to hide behind it and keep moving."
    scene bg_forest
    show aimless_tree
    jump timer_training1
label timer_training1:
    $ time_left = 5
    show screen timer_screen("aimless_tree.png", "training2")
    show clock_overlay
    # Count down
    while time_left > 0:
        $ renpy.pause(1.0)
        $ time_left -= 1
        $ renpy.restart_interaction()

    # Hide the timer screen
    hide screen timer_screen

    # Jump to a given label when the timer runs out
    if time_left <= 0:
        jump training1

    return
label training2:
    hide screen timer_screen
    scene black with fade
    "Nice work. By hiding behind the tree, you manage to blend in with the group of Aimless."
    "The enviornment is getting more and more surreal, and you're starting to feel like you're in a dream."
    "The team is huddled together, waiting for their next opportunity. A gap appears, but the window is closing fast!"
    scene bg_forest_2
    show aimless_boulder
    jump timer_training2
label timer_training2:
    $ time_left = 4
    show screen timer_screen("aimless_boulder.png", "training3")
    show clock_overlay

    # Count down
    while time_left > 0:
        $ renpy.pause(1.0)
        $ time_left -= 1
        $ renpy.restart_interaction()

    # Hide the timer screen
    hide screen timer_screen

    # Jump to a given label when the timer runs out
    if time_left <= 0:
        jump training1

    return
label training3:
    hide screen timer_screen
    scene black with fade
    "Whatever they're heading towards, it's getting closer. You've never seen anything like these surroundings."
    "Ready?"
    scene bg_forest_ai
    show aimless_patch
    jump timer_training3
label timer_training3:
    $ time_left = 3
    show screen timer_screen("aimless_patch.png", "finale")
    show clock_overlay

    # Count down
    while time_left > 0:
        $ renpy.pause(1.0)
        $ time_left -= 1
        $ renpy.restart_interaction()

    # Hide the timer screen
    hide screen timer_screen

    # Jump to a given label when the timer runs out
    if time_left <= 0:
        jump training1

    return

label finale:
    hide screen timer_screen
    scene black with fade
    play music "Boss.mp3" loop
    # Arrival at Nbidia
    scene bg_nbidia with fade
    "Your crew steps towards the building, wary of the Aimless surrounding it."
    p "What is this place? It looks all wrong."
    show cook_neutral with dissolve
    cook "I think it's really cool and awesome actually"
    hide cook_neutral
    show scientist_neutral with dissolve
    scientist "That text floating there literally says v- vivgiry? What does that even mean?"
    hide scientist_neutrale
    p "Whatever it means, we take it head-on."

    scene bg_server with fade

    server "Welcome! We're so glad you could make it. Please, come in and make yourselves at home."
    
    show engineer_surprised with dissolve
    engineer "None of this should be working. Those wires all end before making a connection. This is dumb."
    hide engineer_surprised with dissolve
    
    server "I'm sorry if I seem strange to you. I just like to be myself and not worry about what other people think."
    p "What are you?"
    server "You can call me Nbidia. That's the name I go by."
    p "Hi, Nbidia. That's a unique and original name I've never heard before. What have you been doing here?"
    server "Ah, yes, I understand what you are asking. But before I tell you, I have to ask you something. Do you believe in the greater good?"
    p "Please just explain."
    server "Well, let's just say that some people have to be changed so that the world can prosper. But it's all worth it in the end. Trust me."
    p "These responses feel planned out."
    server "You just don't understand. You're too naive to see the bigger picture. I'm trying to make the world a better place, and you're standing in my way."
    scene bg_server_red with dissolve
    play music "Boss_fast.mp3" loop
    "The Aimless start to surround you. You're trapped."
    "You have to make one more decision."
    if (not hasEMP and not hasSoup and not hasTablet):
        "Er... you realize you don't have any items to help you. You're going to have to improvise."

    # Final decision
    menu:
        "Use the Drawing Tablet" if hasTablet:
            jump tabletEnding
        "Use the Broccoli Cheddar Soup" if hasSoup:
            jump bcsEnding
        "Use the Electromagnet" if hasEMP:
            jump empEnding
        "Reason with Nbidia" if (hasEMP or hasSoup or hasTablet):
            jump reasonEnding
        "... kick it." if (not hasEMP and not hasSoup and not hasTablet):
            jump kickEnding
        
# Emp doesn't work, jordan chimes in - might get second chance
label tabletEnding:
    # neutral ending, plug in tablet and kill supercomputer
    
    "You decide to use the drawing tablet in an attempt to beat Nbidia."
    "You remember reading somewhere that plugging a screen into something that isn't meant for it will break it. Maybe that's a good idea!"
    "You reach for the tablet and cord."
    show tablet:
        xalign 0.5
        yalign 0.4
    with dissolve  
    server "Please, don't hurt me. I'm just trying to do what's right. I know it seems wrong, but it's for the greater good. Please, just let me live."
    hide tablet with dissolve
    window hide
    scene bg_server_tablet
    pause(2.0)
    window show
    server "What... is... this? Did you just plug in a DISPLAY?! Are you insane?!"
    "You take the pen and write on the display, sending inputs that were never meant to be sent through the system."
    server "NOOOOOOOOOOOOOOO"
    jump neutralEnding
    return
        
label bcsEnding:
    # neutral ending, throw soup and kill supercomputer
    
    "You decide to use the Broccoli Cheddar Soup in an attempt to beat Nbidia."
    "You remember that soup generally isn't good for computers."
    "You reach for your soup, one hand grasping the lid."
    show soup:
        xalign 0.5
        yalign 0.4
    with dissolve
    server "Please, don't hurt me. I'm just trying to do what's right. I know it seems wrong, but it's for the greater good. Please, just let me live."
    hide soup with dissolve
    window hide
    scene bg_server_soup
    pause(2.0)
    window show
    server "OOF OUTCH OUWEE OOOooohhh"
    jump neutralEnding
    return

label empEnding:
    # neutral ending, emp doesn't work, try something else
    # OR true ending, emp doesn't work, give Jordan a chance
    # dialogue, throw emp, doesn't work
    # neutral ending, throw soup and kill supercomputer
    
    "You decide to use the Electromagnet in an attempt to beat Nbidia."
    "You read something somewhere a while back about electromagnetic whatevers killing computers. This should work."
    "You reach for your electromagnet."
    show emp:
        xalign 0.5
        yalign 0.4
    with dissolve    
    server "Please, don't hurt me. I'm just trying to do what's right. I know it seems wrong, but it's for the greater good. Please, just let me live."
    hide emp with dissolve
    window hide
    scene bg_server_emp_fail
    pause(2.0)
    window show
    "*bonk*"
    scene bg_server_alt with dissolve
    show engineer_neutral with dissolve
    engineer "You moron. The thing that hurts computers is an electromagnetic PULSE. You need a specific enviornment to do any damage."
    p "Oh."
    engineer "With all the electronic junk I can see in here, I could probably make a pulse to take out this room if I could, I dunno, MOVE MY HANDS."
    hide engineer_neutral with dissolve
    menu:
        "Try your tablet instead" if hasTablet:
            jump tabletEnding

        "Try your soup instead" if hasSoup:
            jump bcsEnding

        "Give Jordan a chance with the Electromagnet":
            jump jordanEnding

        "Give up":
            jump whyEnding

label kickEnding:
    # secret ending, kick the supercomputer and kill it
    window hide
    pause (2.0)
    scene bg_server_kick
    window show
    "*bonk*"
    server "{b}{i}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{\b}{\i}"
    jump secretEnding
    return

label reasonEnding:
    # bad ending, reason with supercomputer and not succeed
    scene bg_server_alt
    "You decide to try to reason more with the computer. Good luck."
    p "You have to be able to understand that altering humanity is unethical."
    server "But don't you see? Sometimes we have to do things that are unpleasant in order to achieve a greater good. It's like the trolley problem."
    p "The trolley problem is just a thought experiment, it doesn't relate in this situation. Why don't you get that?"
    server "But what if it's necessary? What if we have to make those tough choices to save more people in the long run?"
    p "I'm sorry, but I can't agree with you on this. You altered my friend's partner. You altered innocent people. I can't accept that."
    jump badEnding
    return

label jordanEnding:
    # true ending, Jordan is given a chance and proves herself as a good guy
    "You decide to give Jordan a second chance at being a decent person."
    "You undo the electronic handcuffs and chuck the EMP at her."
    "With a few yanked cables and a few sparks, she manages to rig up a makeshift EMP."
    server "No, wait, you don't understand-"
    window hide
    scene bg_server_emp with irisout
    pause 2.0
    window show
    server "Oh f-"
    jump trueEnding
    return

label neutralEnding:
    scene black with fade
    "You... didn't actually think that would work. But hey, at least there's no more rogue AI running around."
    "What you didn't account for was your method killed anyone currently under the server's mind-altering effects."
    "...which resulted in a rather angry Jordan yelling about how her fiance was murdered."
    "Everyone makes mistakes, yours just happened to involve the end of many, many lives."
    "Whoops."
    "Neutral Ending: It was an honest mistake, really..."
    return
    return
        
label badEnding:
    scene black with fade
    "Turns out not everyone wants to change and that includes morally dubious supercomputers."
    "To pay for your hubris you're forced to watch the crewmates you lead into something beyond your feeble human comprehension."
    "Limbs warped and replaced, eyes and mouths stretched and limp. But you are left untouched and unchanged."
    "You are left watching your friends become one with the Aimless crowded around outside Nbidia."
    "Bad Ending: Talking only helps for those willing to listen."
    return
    return

label secretEnding:
    scene black with fade
    "Whoever said brains over brawn was obviously wrong. If one kick is all it takes to defeat a supercomputer bent on world domination..."
    "Then it clearly wasn't smart enough to put itself in a bullet proof case or something."
    "But you also weren't smart enough to know that it rigged up a world ending code set to release every single nuclear war head currently in circulation."
    "At least you can say you went out in a blaze of glory, or stupidity, but thats for whoever is left to decide."
    "It was an awesome kick though."
    "Secret Ending: Nukicklear {i}AI{/i}rmaggedon"
    return
    return

label whyEnding:
    scene black
    stop music
    "WHY"
    ""
    "WHY WOULD YOU DO THAT"
    ""
    "..."
    "Alright, wise guy, here's the deal. I'm gonna let you go back and get the items you missed, as that's the only way I can see you ever giving up."
    "Go. Get the items. I'll wait."
    ""
    "I'll be here."
    scene bg_city
    play music "menu.mp3" loop
    jump firstmenu
    return

label trueEnding:
    scene black with fade
    "Giving Jordan a chance seemed to be the right choice in the end."
    "After all, it wasn't her fault she went insane. \"Space Jail\" might not have been the best call, looking back."
    "As the buzz of electricity in the air calms and the static dies down, everyone takes a second to check themselves for any injuries."
    "Any person previously under Nbidia's mind control has been set free, including a very tearful reunion between Jordan and her fiance."
    "In the end, the world is slowly on its way to returning to normal. Even if you and your crew killed the world's first sentient AI."
    "True Ending: A happy end... for most."
    "..."
    "Meow~"
    "You turn around."
    show beef_neutral with moveinright
    p "BEEF?!"
    p "YOU'VE BEEN FOLLOWING US THE WHOLE TIME??"

    return
# they get there