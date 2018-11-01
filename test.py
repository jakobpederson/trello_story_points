from unittest import TestCase

from story_points import get_score, get_total, get_breakdown


class StoryPointTests(TestCase):

    def setUp(self):
        self.board = TrelloBoard('master')
        self.list_1 = self.board.add_list('backlog')
        self.list_2 = self.board.add_list('in progress')
        self.list_3 = self.board.add_list('done')
        self.list_4 = self.board.add_list('meta')
        self.card_1 = self.list_1.add_card('1: x')
        self.card_2 = self.list_1.add_card('2: x')
        self.card_3 = self.list_1.add_card('3: x')
        self.card_4 = self.list_2.add_card('4: x')
        self.card_5 = self.list_2.add_card('5: x')
        self.card_6 = self.list_2.add_card('6: x')
        self.card_7 = self.list_3.add_card('7: x')
        self.card_8 = self.list_3.add_card('8: x')
        self.card_9 = self.list_3.add_card('91: x')
        self.card_10 = self.list_4.add_card('x')

    def test_gets_correct_score_from_string(self):
        self.assertEqual(get_score('1: first string'), 1)
        self.assertEqual(get_score('11: second string'), 11)
        self.assertEqual(get_score('x: third string'), 0)
        self.assertEqual(get_score('fourth string'), 0)

    def test_get_total(self):
        cards = self.board.open_cards()
        result = get_total(cards)
        self.assertEqual(result, 127)

    def test_get_list_breakdown(self):
        result = get_breakdown(self.board)
        expected = {
            'backlog': {
                'points': 6,
                'cards': 3
            },
            'done': {
                'points': 106,
                'cards': 3
            },
            'meta': {
                'points': 0,
                'cards': 1
            },
            'in progress': {
                'points': 15,
                'cards': 3
            }
        }
        self.assertEqual(result, expected)


class TrelloBoard():

    def __init__(self, name):
        self.trello_lists = []
        self.name = name

    def add_list(self, name):
        trello_list = TrelloList(name, self)
        self.trello_lists.append(trello_list)
        return trello_list

    def open_cards(self):
        result = []
        for trello_list in self.trello_lists:
            result.extend(trello_list.list_cards())
        return result

    def open_lists(self):
        return self.trello_lists


class TrelloList():

    def __init__(self, name, board):
        self.cards = []
        self.board = board
        self.name = name

    def add_card(self, name):
        card = TrelloCard(name, self)
        self.cards.append(card)
        return card

    def list_cards(self):
        return self.cards


class TrelloCard():

    def __init__(self, name, trello_list):
        self.trello_list = trello_list
        self.name = name

    def get_list(self):
        return self.trello_list
