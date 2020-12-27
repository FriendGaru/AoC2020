def build_decks(filename):
    p1 = []
    p2 = []
    current_p2 = False
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line == "Player 1:":
                continue
            elif line == "Player 2:":
                current_p2 = True
                continue
            elif line == "":
                continue
            elif current_p2:
                p2.append(int(line))
            else:
                p1.append(int(line))
    return p1, p2

def combat_round(p1, p2):
    p1_card = p1.pop(0)
    p2_card = p2.pop(0)
    if p1_card > p2_card:
        p1.append(max(p1_card, p2_card))
        p1.append(min(p1_card, p2_card))
    elif p2_card > p1_card:
        p2.append(max(p1_card, p2_card))
        p2.append(min(p1_card, p2_card))
    else:
        raise ValueError

def score_deck(deck):
    mult = 1
    score = 0
    for card in reversed(deck):
        score += mult * card
        mult += 1
    return score


def combat(p1_deck, p2_deck):
    rounds = 0
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        combat_round(p1_deck, p2_deck)
        rounds += 1

    print("Rounds: {}".format(str(rounds)))
    print("P1 Score: " + str(score_deck(p1_deck)))
    print(p1_deck)
    print("P2 Score: " + str(score_deck(p2_deck)))
    print(p2_deck)


p1, p2 = build_decks("input.txt")
combat(p1, p2)

