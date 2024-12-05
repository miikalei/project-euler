from typing import Self

card_values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suits = ['H','S','D','C']

def split_card(card: str):
    return {'value': card[0], 'suit': card[1]}

def card_to_value(card: str) -> str:
    return split_card(card)['value']

def value_wins(value: str, other: str):
    value_index = card_values.index(value)
    other_index = card_values.index(other)
    return value_index - other_index > 0

def card_wins(card: str, other: str):
    return value_wins(card_to_value(card), card_to_value(other))

class PokerHand:
    def __init__(self, cards: list[str]):
        self.cards: list[str] = cards

    def contains_value(self, value: str) -> bool:
        return any(value in card for card in self.cards)
    
    def count_value(self, value: str):
        return sum(1 for card in self.cards if value in card)

    def is_straight_from(self, high_card: str):
        value_index = card_values.index(high_card)
        return all(self.contains_value(card_values[m]) for m in range(value_index - 4, value_index+1))

    def is_straight(self):
        return next((card_values[n] for n in range(4,len(card_values)) if self.is_straight_from(card_values[n])),None)

    def is_flush_of(self, suit: str):
        return all(suit in card for card in self.cards)
    
    def is_flush(self):
        return any(self.is_flush_of(suit) for suit in suits)
    
    def high_card(self):
        max_card = max(self.cards, key=lambda x: card_values.index(card_to_value(x)))
        return max_card

    def is_straight_flush(self):
        return self.is_flush() and self.is_straight()
    
    def is_four_of_kind(self) -> str | None:
        return next((value for value in card_values if self.count_value(value) == 4), None)
    
    def is_three_of_kind(self) -> str | None:
        return next((value for value in card_values if self.count_value(value) == 3), None)
    
    def is_two_of_kind(self) -> str | None:
        return next((value for value in card_values if self.count_value(value) == 2), None)
    
    def is_two_pairs(self):
        pair_values = [value for value in card_values if self.count_value(value) == 2]
        if len(pair_values) == 2:
            return True
        return False
    
    def is_full_house(self):
        return self.is_three_of_kind() and self.is_two_of_kind()
    
    def wins(self, other: Self):
        ## Straight flush
        if (self.is_straight_flush() and not other.is_straight_flush()):
            return True
        if (not self.is_straight_flush() and other.is_straight_flush()):
            return False
        if (self.is_straight_flush() and other.is_straight_flush()):
            return card_wins(self.high_card(), other.high_card())
        ## Four of a kind
        if (self.is_four_of_kind() and not other.is_four_of_kind()):
            return True
        if (not self.is_four_of_kind() and other.is_four_of_kind()):
            return False
        if (self.is_four_of_kind() and other.is_four_of_kind()):
            self_high = self.is_four_of_kind()
            other_high = other.is_four_of_kind()
            return value_wins(self_high, other_high)
        ## Full house
        if (self.is_full_house() and not other.is_full_house()):
            return True
        if (not self.is_full_house() and other.is_full_house()):
            return False
        if (self.is_full_house() and other.is_full_house()):
            self3 = self.is_three_of_kind()
            other3 = other.is_three_of_kind()
            if (self3 != other3):
                return value_wins(self3,other3)
            self2 = self.is_two_of_kind()
            other2 = other.is_two_of_kind()
            return value_wins(self2,other2)
        ## Flush
        if (self.is_flush() and not other.is_flush()):
            return True
        if (not self.is_flush() and other.is_flush()):
            return False
        if (self.is_flush() and other.is_flush()):
            return card_wins(self.high_card(), other.high_card())
            
        ## Straight
        if (self.is_straight() and not other.is_straight()):
            return True
        if (not self.is_straight() and other.is_straight()):
            return False
        if (self.is_straight() and other.is_straight()):
            return card_wins(self.high_card(), other.high_card())

        ## Three of a kind
        if (self.is_three_of_kind() and not other.is_three_of_kind()):
            return True
        if (not self.is_three_of_kind() and other.is_three_of_kind()):
            return False
        if (self.is_three_of_kind() and other.is_three_of_kind()):
            self_high = self.is_three_of_kind()
            other_high = other.is_three_of_kind()
            return value_wins(self_high, other_high)

        ## Two pairs
        if (self.is_two_pairs() and not other.is_two_pairs()):
            return True
        if (not self.is_two_pairs() and other.is_two_pairs()):
            return False
        if (self.is_two_pairs() and other.is_two_pairs()):
            print("I have a problem!")
            return False

        ## One pair
        if (self.is_two_of_kind() and not other.is_two_of_kind()):
            return True
        if (not self.is_two_of_kind() and other.is_two_of_kind()):
            return False
        if (self.is_two_of_kind() and other.is_two_of_kind()):
            self_high = self.is_two_of_kind()
            other_high = other.is_two_of_kind()
            return value_wins(self_high, other_high)

        ## High card
        return card_wins(self.high_card(), other.high_card())
    
