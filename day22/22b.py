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

def score_deck(deck):
    mult = 1
    score = 0
    for card in reversed(deck):
        score += mult * card
        mult += 1
    return score

# Returns winner, p1deck, p2deck
def recursive_combat(p1_deck, p2_deck):

    p1_deck = p1_deck[:]
    p2_deck = p2_deck[:]

    round_count = 0

    played_rounds = set()

    while len(p1_deck) > 0 and len(p2_deck) > 0:

        current_round_str = "|".join((",".join([str(x) for x in p1_deck]), ",".join([str(x) for x in p2_deck])))
        if current_round_str in played_rounds:
            return "p1", p1_deck, p2_deck
        else:
            played_rounds.add(current_round_str)

        round_count += 1
        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)

        if len(p1_deck) >= p1_card and len(p2_deck) >= p2_card:
            winner, _, _ = recursive_combat(p1_deck[:p1_card], p2_deck[:p2_card])
        elif p1_card > p2_card:
            winner = "p1"
        elif p2_card > p1_card:
            winner = "p2"
        else:
            raise ValueError

        if winner == "p1":
            p1_deck.append(p1_card)
            p1_deck.append(p2_card)
        elif winner == "p2":
            p2_deck.append(p2_card)
            p2_deck.append(p1_card)
        else:
            raise ValueError

    if len(p1_deck) > 0 and len(p2_deck) == 0:
        return "p1", p1_deck, p2_deck
    elif len(p2_deck) > 0 and len(p1_deck) == 0:
        return "p2", p1_deck, p2_deck
    else:
        raise ValueError


p1_start, p2_start = build_decks("input.txt")
final_winner, p1_end_deck, p2_end_deck = recursive_combat(p1_start, p2_start)
print("Winner: {}".format(final_winner))
print("P1 Score: {}".format(str(score_deck(p1_end_deck))))
print("P2 Score: {}".format(str(score_deck(p2_end_deck))))

