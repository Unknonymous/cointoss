import random
def cointoss(num):
    heads = 0
    tails = 0
    for y in range (1, num):
        x = random.random()
        #print x
        x = round(x)
        #print x
        if x == 1:
            heads += 1
            statement = "It's a head! "
        elif x == 0:
            tails += 1
            statement = "It's a tail! "
        print "Attempt #" ,y, "Throwing a coin... " + statement + "...Got", heads, "head(s) so far and", tails, "tail(s) so far."
        y += 1

cointoss(5000)

