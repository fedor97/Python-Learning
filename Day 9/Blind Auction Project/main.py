import art

print(art.logo)

all_data = {}

# TODO-1: Ask the user for input
def bidder():

    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bidders = input("Are there any other bidders? yes or no. ")

    return name, bid, bidders

while True:
    name, bid, answer = bidder()
    all_data[name] = bid
    if answer == "no":
        break




# TODO-2: Save data into dictionary {name: price}




winner = max(all_data, key=all_data.get)
print(winner)
print(name, all_data[name])



# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


