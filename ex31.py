print "you enter a dark room with two doors, Do you go through door #1 or door #2?"

door = raw_input(">>")

if door == "1":
    print "There is a giant bear here eating a cheese cake. What do you do?" 
    print "1.Take the cake.\n2.Scream at the bear"
	
    bear = raw_input(">>")
	
    if bear == "1":
	    print "The bear is angry, bitting your leg ,game over"
    elif bear == "2":
        print "The bear is angry, bitting your leg ,game over"
    else:
        print "yeah, the %s is better, run away"% bear
		
elif door == "2":
    print "you stare into the endless abyss at Cthulhu's retina."
    print "1. blueberries.\n2. yellow jacket clothespins."
    print "3. understanding revolvers yelling melodies"

    insanity = raw_input(">>")
    if insanity == "1" or insanity == "2":
        print "your body survives powered by a mind of yello. Good job!"
    else:
        print "the insanity rots your eyes into a pool of muck. good job!"
		
else:
    print "you stumble around and fall on a knife and die. Good job!"