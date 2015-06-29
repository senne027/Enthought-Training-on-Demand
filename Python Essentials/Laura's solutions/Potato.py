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

#1

offer = min(sell_orders.values())
print "Offer price:", offer

bid = max(buy_orders.values())
print "Bid price:", bid

#2

sell_orders["Arnold"] = 10.0
print sell_orders

#3
del buy_orders["Geno"]
bid = max(buy_orders.values())
print "Bid price:", bid

#4

buy_orders["Juan"] = 10.0
offer = min(sell_orders.values())
print offer
bid = max(buy_orders.values())
print bid


del buy_orders['Juan']
del sell_orders['Arnold']

print 'Bid matches offer:', bid == offer

'''
offer = sell_orders.pop('Arnold')
bid = buy_orders.pop('Juan')
'''

sell_orders.clear()
print 'sell orders:', sell_orders
print "Chefs that are sad and with no potatoes:"
print buy_orders.keys()