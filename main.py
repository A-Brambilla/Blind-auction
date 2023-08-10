from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

auction = {}
more_bidders = True
while more_bidders:
  name = input("What is your name?: ")
  bid = int(input("How much would you like to bid? $"))
  auction[name] = bid

  another_bidder = input("Any more bidders? yes or no: ")
  if another_bidder == "no":
    more_bidders = False
  else:
    clear()
    print(logo)
    
highest_bid = 0
highest_bidder = ""
for bidder in auction:
  if auction[bidder] > highest_bid:
    highest_bidder = bidder
    highest_bid = auction[bidder]
print(f"The highest bidder is {highest_bidder}")
print(f"They bid {highest_bid}")
