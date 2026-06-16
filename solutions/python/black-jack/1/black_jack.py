"""Note : A means ace, J means jack, Q means queen, and K means king. Jokers are discarded.
* Face cards (J, Q, K) are scored at 10 points and any other card is worth its numerical value.
"""
A = "A"
face_cards = ("J", "Q", "K")

def value_of_card(card):
    """Determine the scoring value of a card and fix the value of an ace card at 1 for now.

    Parameters: card (str): The given card.
    Returns: int: The value of a given card.  See below for values.
    """
    if card == "A":
        return 1
    elif card in ('J', 'Q', 'K'):
        return 10
    else:
        return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.
    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.
    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """
    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)
    if val_one > val_two:
        return card_one
    elif val_one < val_two:
        return card_two
    else:
        return card_one, card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.
    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.
    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """
    def card_value(card):
        if card == 'A':
            return 11      # A should now be 11
        return value_of_card(card)
    
    total = card_value(card_one) + card_value(card_two)
    if total + 11 <= 21:
        return 11
    return 1

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.
    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.
    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """
    ten_cards = ("J", "K", "Q", "10")
    if card_one == "A" and card_two in ten_cards:
        return True
    elif card_two == "A" and card_one in ten_cards:
        return True
    else:
        return False

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.
    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.
   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.
    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.
    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    if total in (9, 10, 11):
        return True
    return False