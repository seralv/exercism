def value_of_card(card):
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    if card_one == card_two:
        return (card_one, card_two)
    elif (card_one == '10' and card_two == 'J') or (card_one == 'Q' and card_two == '10'):
        return (card_one, card_two)
    elif value_of_card(card_one) > value_of_card(card_two):
        return card_one
    else:
        return card_two


def value_of_ace(card_one, card_two):
    if card_one == 'A' and card_two not in ['J', 'Q', 'K']:
        calculate_value = 11 + value_of_card(card_two)
        if calculate_value + 11 <= 21:
            return 11
        else:
            return 1
    elif card_two == 'A' and card_one not in ['J', 'Q', 'K']:
        calculate_value = value_of_card(card_one) + 11
        if calculate_value + 11 <= 21:
            return 11
        else:
            return 1
    else:
        calculate_value = value_of_card(card_one) + value_of_card(card_two)
        if calculate_value + 11 <= 21:
            return 11
        else:
            return 1


def is_blackjack(card_one, card_two):
    if (card_one == 'A' and card_two in ['10', 'J', 'Q', 'K']):
        return True
    elif (card_one in ['10', 'J', 'Q', 'K'] and card_two == 'A'):
        return True
    else:
        return False



def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    calculate_value = value_of_card(card_one) + value_of_card(card_two)
    if calculate_value == 9 or calculate_value == 10 or calculate_value == 11:
        return True
    else:
        return False
