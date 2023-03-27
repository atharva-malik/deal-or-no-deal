import random

def deal_or_no_deal():
    briefcases= {}
    for i in range(1, 27):
        briefcases[str(i)] = random.randint(1, 1000000)
    print(briefcases)
    remaining_briefcases = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

deal_or_no_deal()
