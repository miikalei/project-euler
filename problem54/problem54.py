from hand import PokerHand

def compute():
    with open('problem54.txt') as file:
        player1_wins = 0
        for line in file:
            line = line.rstrip()
            cards = line.split(' ')
            player1_cards = cards[0:5]
            player2_cards = cards[5:10]
            player1_hand = PokerHand(player1_cards)
            player2_hand = PokerHand(player2_cards)
            if player1_hand.wins(player2_hand):
                player1_wins += 1
            # print(player1_cards)
            # print(player2_cards)
        print(f"Player 1 win count: {player1_wins}")

compute()