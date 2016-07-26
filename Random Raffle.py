# Random Raffle - by David Lee - 2016

import random

def winning(tickets):
    winning_ticket=random.randint(1,tickets)
    return winning_ticket

def main():
    tickets=input("How many people have entered the raffle? ")
    tickets=int(tickets)
    input("And the winning ticket is... Press Enter ")
    winning_ticket=winning(tickets)
    print("Number", winning_ticket, ", Congratulations!")
    input()
    main()

main()
