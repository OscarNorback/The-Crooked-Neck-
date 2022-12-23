print("""Your name is Peyton Farquhar, you are standing upon a bridge with your hands and feet tied together. The material around your hands seems flimsy but sturdy enough to not let your hands escape, the same goes for your feet. However, what makes you nervous is the thing around your neck, a noose to be exact. It sits tightly around your neck and its coarse texture creates uncomfortable scratches and you wish you could itch it. With the soldiers shuffling and moving behind you, you know your time is limited. The flimsy plank you are standing on is shaking, which is only being held upright by the soldier standing on it behind you, a deadly game of see-saw. 

In the blink of an eye the plank below you drops and a searing pain shoots out through your body. If only you could move your hands or get that noose of your neck. What do you do now? 

Press 1 to try and jerks your head out of the noose
Press 2 to try and twist your hands out of their constraints.\n""")
print("Your name is Peyton Farquhar, you are standing upon a bridge with your hands and feet tied together. The material around your hands seems flimsy but sturdy enough to not let your hands escape, the same goes for your feet. However, what makes you nervous is the thing around your neck, a noose to be exact. It sits tightly around your neck and its coarse texture creates uncomfortable scratches and you wish you could itch it. With the soldiers shuffling and moving behind you, you know your time is limited. The flimsy plank you are standing on is shaking, which is only being held upright by the soldier standing on it behind you, a deadly game of see-saw.\n")

choice_1 = input("""In the blink of an eye the plank below you drops and a searing pain shoots out through your body. If only you could move your hands or get that noose of your neck. What do you do now?
     Press 1 to try and jerk your head out of the noose
     Press 2 to try and untie your hands\n""")

if choice_1 == ("1"):
    print("You decide that you have to get this noose off your neck, and in an instant you start moving your head around and trying to find any opening in which your head and fit however, as the noose seems to sink even lower into your neck you swear you can see black dots dancing in front of your eyes which are growing even bigger. You feel like your tongue doesn’t fit in your mouth anymore and as you perform your last struggle you close your eyes and for a moment see a familiar face of a woman\n")
    print("""You decide that you have to get this noose off your neck, and in an instant you start moving your head around and trying to find any opening in which your head and fit however, as the noose seems to sink even lower into your neck you swear you can see black dots dancing in front of your eyes which are growing even bigger. 
          You feel like your tongue doesn’t fit in your mouth anymore and as you perform your last struggle you close your eyes and for a moment see a familiar face of a woman.""")
    print("GAME OVER")
    exit
elif choice_1 == ("2"):
    print("You decide that in order to free yourself you must first free your hands. With all of your might you start twisting and turning your hands against the coarse rope, so much that your wrists start to bleed, but that doesn’t matter. After vigorous twisting and turning the rope gives out and your hands are now free!\n")
    print("!Your Hands are now loose!")
    choice_2 = input("""With your hands free you are now one step closer to escape however, your neck is still hurting and the blood flow to your brain is currently being cut off. It feels like your head will explode at any moment. Beneath you the river roars but your feet are still tied. You are left with the choice to free your feet or try and tear off the noose with your now released hands and land in the river with bound feet.\n
    Press 1 to attempt to untie your feet
    Press 2 to attempt to free yourself from the noose\n""")
    print("""You decide that in order to free yourself you must first free your hands. With all of your might you start twisting and turning your hands against the coarse rope, so much that your wrists start to bleed, 
          but that doesn’t matter. After vigorous twisting and turning the rope gives out and your hands are now free!""")
    print("! Your hands are now loose !\n")
    choice_2 = input("""With your hands free you are now one step closer to escape however, your neck is still hurting and the blood flow to your brain is currently being cut off. It feels like your head will explode at any moment. Beneath you the river roars but your feet are still tied. You are left with the choice to free your feet or try and tear off the noose with your now released hands and land in the river with bound feet.
    Press 1 to attempt to free yourself from the noose
    Press 2 to attempt to release your feet\n""")
    if choice_2 == ("1"):
        print("After contemplating you choose that falling into the river with bound feet maybe isn’t a good idea you start to reach down towards your feet. You try to bend your knees to bring your feet up and at the same time reach down with your hands. However, this proves a very difficult feat as your strength isn’t what it was 2 minutes ago when you were still standing on the bridge. With your last failed attempts to try and grab the feat around you feel like falling asleep, the rope around your neck feels like it’s joined with your neck and you eventually give up. The suffocation catches up to you and everything goes black.\n")
        print("GAME OVER")
        exit
    elif choice_2 == ("2"):
        print("Tear off noose")
        print("You are free")
        choice_3 = input("""You fall into the river and after splashing into the water you quickly dispose of the constraints binding your feet.You now have two choices. \n
        Press 1 to swim towards the forest against the current.
        Press 2 to swim with the current towards the waterfall later down the river.""")
        choice_3 = input("val3")
        if choice_3 == ("1"):
            print("You try to swim towards the forest against the current but you are getting tired and start to slow down and now the guards see you and have a clear shot at you. guards shoot. You die.")
            print("GAME OVER")
            exit
        elif choice_3 == ("2"):
            print("You try to swim with the current towards the waterfall later down the river. The guards can't see you because you are under the water and the stream is taking you away from the bridge.   ")
            print("You are now gonging to the water fall.")
            choice_4 = input("""""")
            if choice_4 == ("1"):
                print("You Continue swimming towards the forest despite your exhaustion. That was a bad idea. You can feel your body slowly sink down in the water and you are too exhausted to get yourself back up. You drown and died.")
                print("GAME OVER")
                exit
            elif choice_4 == ("2"):
                print("You try to swim with the current towards the waterfall later down the river. The guards can't see you because you are under the water and the stream is taking you away from the bridge.")
                print("You are now gonging to the water fall.")
                choice_5 = input("""You are now very exhausted and you are starting coming closer to the waterfall and you see land near bay and no guards perfect place for you  need to do a choice are you \n
                Press 1: Swim to the waterfall and trust that you suave the fall
                Press 2: Swim to the land but you are very tired. It's a 50/50 chance that you make it to the land.:""")
                if choice_5 == ("1"):
                    print("The waterfall was a bad idea, you can't trust it but now it's too late. You fall down the waterfall and break your neck when you hit the ground. You die")
                    print("GAME OVER")
                    exit
                elif choice_5 == ("2"):
                    print("You are trying to swim towards the land but you are getting more and more tired. you grab a big rock and drag your body to land. Congratulations, you made it to land.")
                    print("You are so tired but you need to continue into the forest so the guards do not find you.")
                    choice_6 = input("""You are a bit into the forest now and you are too tired so you have trouble standing up and seeing. You see a good place to relax and get your energy back up.\n
                     Press 1: You relax and go into hiding and get your energy back. 
                     Press 2: Try to find civilization or someone that can help you. Still you can't see and you are very tired.:""")
                    if choice_6 == ("1"):
                        print("You are trying to stand up and you have a hard time seeing you fall and scratch your arm but it is no big problem.")
                        print("Now you find a good place to rest again but you hear sounds but you do not know what they are.")
                    elif choice_6 == ("2"):
                        print("You are going to sleep and sleep for many hours but you wake up quickly and hear a man screaming. I see him get him. Pannnggg You die.")
                        print("GAME OVER")
                        exit
                        choice_7 = input("""You start to feel a pain in your neck and at the same time the sounds get louder but the sounds are still far away. You nearly can't see any more and you do not feel your legs \n
                        Press 1: Rest and find your strength agen so you can keep going.
                        Press 2: You try to see what the noises are and where they come from.
                        Press 3: You do not what to know what the noises are and don't care about sleep reel sigma. :""")
                        if choice_7 == ("1"):
                            print("You choice to rest. You lay down on moss and start sleeping but when you wake up you see your family and your house. You start to run to your family but when you come ner dome you can feel the pain in your neck getting more and more painful. When you about to hug you family you neck get broken hand you hang from the  bridge")
                            exit
                        elif choice_7 == ("2"):
                            print("you want to know what the noises are so you start to wake towards the noises. After some time you start to hear what the noise is. There's a guard yelling for you. You start running in the other direction to get away from the guard but it doesn't help he has seen you and now everyone knows you are there. the guards surround you and now it's over you think.")
                            exit
                        elif choice_7 == ("3"):
                            print("You don't want to sleep and you don't want to know what the sound is. So you choose to keep walking and try to find home. You are still tired and your vision is blurry, you have difficulty standing up straight. After a few hours you will start to see smoke rising from a scotch. You start walking towards the house where smoke is coming from. After another hour of going to the house, you're done. It turned out to be your house and you are overjoyed to see your house. You can't wait until you can see your family again. You enter through the door...")
                            exit
