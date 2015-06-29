warehouse_log = """ frombicator      10
                    whitzlegidget    5
                    splatzleblock    12
                    frombicator      -3
                    frombicator      20
                    foozalator       40
                    whitzlegidget    -4
                    splatzleblock    -8
                """             
                
warehouse_log = warehouse_log.strip()

transactions = []
for line in warehouse_log.split("\n"):
    part, count = line.split()
    transaction = (part, int(count))
    transactions.append(transaction)
    
inventory = {} #initializing from zero

for part, count in transactions:
    inventory[part] = 0
    
for part, count in transactions:
    inventory[part] += count

for part in inventory:
    print "%-20s %d" % (part, inventory[part])
            