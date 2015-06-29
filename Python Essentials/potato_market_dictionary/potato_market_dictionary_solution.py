
# Buying and Selling Potatoes
# ===========================
# 
# Background
# ----------
# In this example, we're going to use a couple of dictionaries to  track the buy/sell orders in a (very) simple financial market -- well actually, a potato market.
# 
# In any kind of market, folks meet together to buy and sell "stuff." At a flea market that stuff is fossils, broken electronics, Aunt Nelly's coffee table, etc.  In the financial market the stuff is stocks (IBM, GOOG, ATT), commodities (oil, potatoes, pork bellies), currency (pounds, yen, euros), and many others.
# 
# 
# If you're familiar with how a market works, you can probably skip to the end of this section.  If not, then let's imagine you have a potato market that works in the following way. Every morning, potato farmers (the sellers) show up with a bag of  potatoes to sell, and chefs (the buyers) show up to buy potatoes for their restaurants.  After everyone has their coffee, discusses the weather and the new fashion in overalls, the farmers sit down together on a bench.  Each farmer holds up a price that they are willing to sell their bag of potatoes for. Now, one of them may have a fishing trip planned in the afternoon and he'll price his potatoes cheaply so they will sell fast. Another might have his eye on a new fishing pole he wants, and would like to sell his bag of potatoes for as much as possible. (Our farmers like to fish...) As you might guess, the farmer selling at a lower (minimum) price will sell his bag first.  
# 
# Meanwhile, the chefs will gather around the bench and hold up the price they are willing to pay for a bag of potatoes.  The ones who need to get back and prepare a big dinner might be willing to pay a high
# price for potatoes while the ones not sure they even want potatoes on the menu tonight might only be willing to buy if they get a good deal, so they hold up a low price.  For the buyers, the person willing to pay the highest (maximum) price will be the first to head back to their restaurant with a bag of potatoes.
# 
# At anytime while the market is open, a farmer or chef can change their price.  Also, new farmers/chefs may join the market, and others may leave the market.
# 
# As you can see, this really results in two different prices for potatoes. There is an "offer" or "ask" price which is what the farmers are willing to sell potatoes for, and there is a "bid" price which is what chefs are willing to pay.  Only when these two match do potatoes and cash change hands.  
# 
# So, during all of this commotion, there is a potato market manager in the corner. He has two jobs.  First, he watches both buyer and seller prices to see if any of them "match."  When that happens, he pairs the farmer and the chef together so they can exchange their potatoes and money.  His second job?
# Make sure the transistor radio crackling from the window sill stays tuned to the local AM radio station, KAND.
# 
# Our potato market is pretty similar to a financial market that uses a [limit order book](http://www.nasdaq.com/investing/glossary/l/limit-order-book): this is a collection of buy (chef) and sell (farmer) orders from various traders where the trader is willing to wait to get the price he wants rather than trading immediately.
# 
# To conclude, the offer price is the lowest of the sell orders in the limit order book, while the bid price is the highest of the buy orders in the limit book.
# 
# Buy/Sell Dictionaries
# ----------------------
# 
# Ok, so now that we have a problem defined, let's imagine that we use one dictionary to track the farmers' sell orders and one to watch the chefs' buy orders.  From here, we'll figure out the existing offer/ask prices, folks entering the market, leaving the market, an order match, and... dum-dum-dum--dum, a [black swan event](http://en.wikipedia.org/wiki/Black_swan_theory).
# 
# *Note: In a real financial market, each order will also have the number of shares to buy or sell associated with an order (I'll sell 1000 shares at a price of 20.50).  In our potato market, we'll ignore that detail.  Every order will be for a single bag of potatoes. Also, instead of using a person's name for an order, typically something like an (integer) order id would be used.  But, for our case, it is more fun to use names...*


# Farmers selling potatoes and the price they are willing to sell at.
sell_orders = {
    "Joe": 10.50,
    "Jane": 10.25,
    "Bob": 10.75,
    "Melvin": 11.00,
}

# Chefs ready to buy potatoes and the price they are willing to pay.
buy_orders = {
    "Pierre": 9.50,
    "Joel": 9.25,
    "Geno": 9.75,
    "Ellen": 9.50
}


# Question 1
# ----------
# 
# Compute the offer price and the bid price for potatoes.  

# Hint: There are a couple of functions, `min()` and `max()`, that are "built-in" to python.  They should be 
# useful on this one.  At the python command prompt, type `min?` and `max?` to see how they work.
# You'll probably want to grab the values from each of the dictionaries and then use the appropriate
# one of these functions on them.


# For the prices offered by the farmers, the lowest is considered the current
# offer price for potatoes
offer_price = min(sell_orders.values())
print "Offer price:", offer_price

# For the prices bid by the chefs, the highest is considered the current
# bid price for potatoes
bid_price = max(buy_orders.values())
print "Bid price:", bid_price


# Question 2
# ----------
# 
# A new farmer, Arnold, shows up ready to sell his bag of potatoes for $10.00. Update the
# sell orders to reflect this and print it out.


sell_orders['Arnold'] = 10.00
print sell_orders


# Question 3
# ----------
# 
# Geno's wife calls and says to come home quick, the dog got tangled in an extension cord.  Geno rolls his eyes and reluctantly heads home, rueing the day he got that stinking dog.  
# 
# Remove Geno from the market.  What is the new bid price?


del buy_orders["Geno"]
bid_price = max(buy_orders.values())
print "Bid price:", bid_price


# Question 4
# ----------
# 
# Chef Juan, comes running up after a bus bound for the Vegetarians Who Love Eggs Conference stopped at his taco stand and cleared him out of potato tacos.  He needs more potatoes for the late morning run that always happens.
# 
# Chef Juan bids 10.00 for a bag of potatoes.  Add him to the buy order.  Again, check the bid and offer prices.  Hmm. They should be the same now.


buy_orders['Juan'] = 10.00
print 'bid:', max(buy_orders.values())
print 'offer:', min(sell_orders.values())


# Question 5
# ==========
# At this point, the market manager notices that Juan is bidding the same price that Arnold is offering.  He teams these two up and they shake hands. Juan pays, gets his potatoes and dashes back to make more tacos.  Arnold, heads back to tune the carburetor on his tractor -- it konked out on the back 40 last week, and he had to walk all the way home.
# 
# Since they are now gone, remove both of these guys from the market.  As you do this, compare there bid and offer prices just to make sure they match.


# one approach is to use pop to remove the key/value pairs from the dictionary
# while also returning the values so you can compare them.
offer = sell_orders.pop('Arnold')
bid = buy_orders.pop('Juan')
print 'Bid matches offer:', bid == offer

# An alternative is to compare the values directly and remove them afterward.
# You could add an if statement if you wanted to only remove them if the
# bid/offer match, but we will save that for later when we have covered
# control flow.
#print 'Bid matches offer:', buy_orders['Jaun'] == sell_orders['Arnold']
#del buy_orders['Arnold']
#del sell_orders['Juan']


# Question 6
# ----------
# 
# And then it happens...  The devastating event that turns the potato market upside down.  From the window sill, crackling over the air waves comes the announcement.  Frank, owner of "Be the Fish: Lure Store" announces his  retirement sale.  All of his famous handmade Super-Z fishing jigs are half off while supplies last.  As soon as the farmers hear this, they eye each other suspiciously and simultaneously make a mad scramble for the door.  The potato seller bench clears in 3 seconds flat, leaving all the chefs in a panic.  Where will they get their potatoes?  
# 
# As they walk back to their restaurants, they notice that Juan, having already heard the news from the pack of farmers running by, potatoes in hand, was busy changing his sign from "potato tacos \$1.00" to "potato tacos \$1.50."
# 
# Clear out the `sell_orders` dictionary to show there are no longer any sellers.  Print out the names of the sad chefs who are left without any potatoes.


sell_orders.clear()
print 'sell orders:', sell_orders
print "Sad chef's with no potatoes:"
print buy_orders.keys()

