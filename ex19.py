def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "you have %d cheeses! "% cheese_count
    print "you have %d boxes_of_crackers" % boxes_of_crackers
    print "man that's enough for a party!"
    print "get a blanket.\n"
	

print "we can just give the function numbers directly:"
cheese_and_crackers(20,30)


print "or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "do math inside"
cheese_and_crackers(10+1,10+35)

print "combine variables and numbers:"
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

print "numbers:"
cheese_count=input('>')
boxes_of_crackers=input('>')
cheese_and_crackers(cheese_count,boxes_of_crackers)