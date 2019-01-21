from unittest import TestCase

from story_points import get_score, get_total, get_breakdown, get_percentages, filter_skip_cards, get_counts


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

    def test_get_correct_score_handles_two_digit_integers(self):
        self.assertEqual(get_score('11: second string'), 11)

    def test_get_correct_score_returns_zero_if_score_is_not_int(self):
        self.assertEqual(get_score('x: third string'), 0)

    def test_get_correct_score_handes_no_score_at_all(self):
        self.assertEqual(get_score('fourth string'), 0)

    def test_get_correct_score_handes_multiple_colons(self):
        self.assertEqual(get_score('1: x: fourth string'), 1)

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

    def test_get_list_breakdown_with_skip(self):
        result = get_breakdown(self.board, skip='meta')
        expected = {
            'backlog': {
                'points': 6,
                'cards': 3
            },
            'done': {
                'points': 106,
                'cards': 3
            },
            'in progress': {
                'points': 15,
                'cards': 3
            }
        }
        self.assertEqual(result, expected)

    def test_filter_skip_cards(self):
        all_lists = [x.get_list().name for x in self.board.open_cards()]
        self.assertTrue('meta' in all_lists)
        result = [x.get_list().name for x in filter_skip_cards(self.board.open_cards(), skip='meta')]
        self.assertTrue('meta' not in result)

    def test_can_filter_multiple_skip_cards(self):
        later = self.board.add_list('later')
        later.add_card('y')
        all_lists = [x.get_list().name for x in self.board.open_cards()]
        self.assertTrue('meta' in all_lists)
        self.assertTrue('later' in all_lists)
        result = [x.get_list().name for x in filter_skip_cards(self.board.open_cards(), skip='meta,later')]
        self.assertTrue('meta' not in result)
        self.assertTrue('later' not in result)

    def test_get_percentage(self):
        points = 10
        total_points = 100
        cards = 5
        total_cards = 10
        percent_points, percent_cards = get_percentages(points, cards, total_points, total_cards)
        self.assertEqual(percent_points, 10)
        self.assertEqual(percent_cards, 50)

    def test_get_percentage_when_totals_are_zero(self):
        points = 1
        total_points = 0
        cards = 5
        total_cards = 0
        percent_points, percent_cards = get_percentages(points, cards, total_points, total_cards)
        self.assertEqual(percent_points, 0)
        self.assertEqual(percent_cards, 0)

    def test_percentages_add_up_to_100(self):
        list_breakdown = {
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
        total_points = 127
        total_cards = 10
        total_percent_points = 0
        total_percent_cards = 0
        for key, item in list_breakdown.items():
            points = list_breakdown[key]['points']
            cards = list_breakdown[key]['cards']
            percent_points, percent_cards = get_percentages(points, cards, total_points, total_cards)
            total_percent_points += percent_points
            total_percent_cards += percent_cards
        self.assertEqual(total_percent_points, 100)
        self.assertEqual(total_percent_cards, 100)

    def test_member_and_card_count(self):
        self.card_1.idMembers = [TrelloMember('member 1', self.card_1).id]
        self.card_2.idMembers = [TrelloMember('member 1', self.card_2).id, TrelloMember('member 2', self.card_2).id]
        self.card_3.idMembers = [TrelloMember('member 1', self.card_3).id]
        cards = [self.card_1, self.card_2, self.card_3]
        members_dict = {'member 1_id': 'member 1', 'member 2_id': 'member 2'}
        result, card_count, _ = get_counts(cards, members_dict)
        expected = {'member 1 and member 2': 2, 'member 1': 4}
        expected_card_count = {'member 1': 2, 'member 1 and member 2': 1}
        self.assertEqual(result, expected)
        self.assertEqual(card_count, expected_card_count)

    def test_total_points_count(self):
        self.card_1.idMembers = [TrelloMember('member 1', self.card_1).id]
        self.card_2.idMembers = [TrelloMember('member 1', self.card_2).id, TrelloMember('member 2', self.card_2).id]
        self.card_3.idMembers = [TrelloMember('member 1', self.card_3).id]
        cards = [self.card_1, self.card_2, self.card_3]
        members_dict = {'member 1_id': 'member 1', 'member 2_id': 'member 2'}
        _, _, totals = get_counts(cards, members_dict)
        expected = {'member 1': 6, 'member 2': 2}
        self.assertEqual(totals, expected)

    def test_member_and_card_count_accounts_for_different_order_of_member_ids(self):
        self.card_1.idMembers = [TrelloMember('member 1', self.card_1).id]
        self.card_2.idMembers = [TrelloMember('member 2', self.card_2).id, TrelloMember('member 1', self.card_2).id]
        self.card_3.idMembers = [TrelloMember('member 1', self.card_3).id]
        cards = [self.card_1, self.card_2, self.card_3]
        members_dict = {'member 1_id': 'member 1', 'member 2_id': 'member 2'}
        result, card_count, _ = get_counts(cards, members_dict)
        expected = {'member 1 and member 2': 2, 'member 1': 4}
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
        self.idMembers = []
        self.id = 'this_is_{}_id'.format(name)

    def get_list(self):
        return self.trello_list

    @property
    def member_id(self):
        return self.idMembers


class TrelloMember():

    def __init__(self, name, card):
        self.card = card
        self.name = name
        self.id = '{}_id'.format(name)
