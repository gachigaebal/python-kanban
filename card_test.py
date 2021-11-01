from board import Board


def test_create_board():
    board = Board()

    assert board

class Card:
    def __init__(self, x):
        pass

def test_create_card():
    card = Card("description")

    assert card

def test_add_card():
    board = Board()
    card = Card("description")

    # board.cards.append(card)
    # board += card
    # card.add_to(board)
    board.add(card)
    add_card_to_board(card, board)
    # add(card(to(board)))

    # assert len(board.cards) == 1
    # assert board.card_count() == 1

