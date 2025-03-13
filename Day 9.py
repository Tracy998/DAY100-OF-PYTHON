# import art
# print (art.logo)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of Ksh {highest_bid}")

bids={}
continue_bidding = True
while continue_bidding:
        name = input("What is your name?\n").lower()
        price = int(input("what is your bid price?Ksh: "))
        bids [name]=price
        Should_continue = input("Do other users want to bid? Type 'yes' or 'no': ").lower()
        if Should_continue == "no":
            continue_bidding = False
            find_highest_bidder(bids)
        elif Should_continue == "yes":
            print("\n" * 20)





