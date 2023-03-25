bids = {}
bids_are_open = True

def highest_bid(bids):
    highest_bid = 0
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
    print(f"The highest bid is {winner} with price ${highest_bid}")



while bids_are_open:
    name = input(f"Type name of person: ")
    amount_of_bid = int(input(f"How much money do they bid? $"))

    bids[name] = amount_of_bid

    another = input(f"Are there other persons? 'yes' to continue or 'no' to quit bidding ")
    if another == "no":
        bids_are_open = False
        # print(f"The winner is {max(bids)} with bid of ${max(bids.values())}.")
        # instead of using max() function use my defined function:
        highest_bid(bids)

    
