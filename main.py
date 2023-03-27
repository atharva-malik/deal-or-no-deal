import random


def get_offer(briefcases):
    offer = sum(briefcases.values()) / len(briefcases) #TODO: Try to make this more exciting
    return offer


def init_briefcases():
    briefcases = {}
    amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000,
              750000, 1000000]
    for i in range(1, 27):
        briefcases[str(i)] = amount.pop(amount.index(random.choice(amount)))

def deal_or_no_deal():
    briefcases = init_briefcases()
    offer = 0
    briefcases_to_eliminate = 6
    print("You need to eliminate", briefcases_to_eliminate, "briefcases. What briefcases would you like to eliminate?")
    for i in range(0, briefcases_to_eliminate):
        number_to_eliminate = int(input("Briefcase to eliminate: "))
        print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
        remaining_briefcases.remove(number_to_eliminate)
    briefcases_to_eliminate -= 1
    offer = get_offer(briefcases)
    print("Remaining briefcases:", briefcases, "List", remaining_briefcases, "\nOffer: $", offer)
    while briefcases_to_eliminate >= 1:
        offer = get_offer(briefcases)
        print("Remaining briefcases:", len(remaining_briefcases), remaining_briefcases, "Offer: $", offer, "Deal or no deal?")
        choice = input("[D]eal or [n]o deal? ")
        if choice.lower() == "d":
            print("Good game! You got an offer of $", offer, "and you took it! You won $", offer, "! See you next time!")
            break
        elif choice.lower() == "n":
            if briefcases_to_eliminate == 1 and len(remaining_briefcases) == 1:
                print("You have one briefcase left. You must take it.")
                print("You won $", briefcases.pop(str(remaining_briefcases[0])), "!")
                break
            elif briefcases_to_eliminate == 1:
                print("There are", len(remaining_briefcases), "briefcases left. Pick which one you will discard.")
                number_to_eliminate = int(input("Briefcase to eliminate: "))
                print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
                remaining_briefcases.remove(number_to_eliminate)
            else:
                print("There are", len(remaining_briefcases), "briefcases left. Pick", briefcases_to_eliminate, "that you will discard.")
                for i in range(0, briefcases_to_eliminate):
                    number_to_eliminate = int(input("Briefcase to eliminate: "))
                    print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
                    remaining_briefcases.remove(number_to_eliminate)
                briefcases_to_eliminate -= 1
        else:
            continue

print("You know how to play this. Please add instructions later")
deal_or_no_deal()
