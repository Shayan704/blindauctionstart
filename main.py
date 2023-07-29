from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to garage sale.. Item on sale is a vintage gun.. Kindly start the bidding process")
condition="yes"
auction={}
while(condition=="yes"):
  name=input("What is your name?: ")
  bid=int(input("What's your bid?: $"))
  auction[name]=bid
  condition=input("Are there any other bidders? Type Yes or No\t").lower()
  clear()

high=0
highest_bidder=""
for person in auction:
  if(auction[person]>high):
    high= auction[person]
    highest_bidder=person

print(f"The winner is {highest_bidder} with a bid of ${high}.")