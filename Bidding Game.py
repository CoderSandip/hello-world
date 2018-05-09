import random
print ("Welcome to the Auction bro!!")
randomvalue = random.randint(1,1000)
print ("We start bidding!")
print ("Choose a bid between 1 and 1000. please enter your bid")
i = int(input())
if i >= randomvalue:
    print ("The value was", randomvalue)
    print ("You bid", i)
    print ("You won!")
else:
    print ("The value was", randomvalue)
    print ("You bid", i)
    print ("You lost!")
