from trello import TrelloClient
from argparse import ArgumentParser
from collections import defaultdict


def get_score(string):
    try:
        return int(string.split(':')[0])
    except ValueError:
        return 0


def get_total(cards):
    result = 0
    for card in cards:
        result += get_score(card.name)
    return result


def get_breakdown(board):
    result = defaultdict(dict)
    for trello_list in board.open_lists():
        result[trello_list.name.lower()] = {
            'points': get_total(trello_list.list_cards()),
            'cards': len(trello_list.list_cards())
        }
    return dict(result)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--api-key', required=True)
    parser.add_argument('--token', required=True)
    parser.add_argument('--board_id', required=False)
    args = parser.parse_args()

    client = TrelloClient(api_key=args.api_key, token=args.token)
    board = client.get_board(args.board_id)
    cards = board.open_cards()
    total_cards = len(cards)
    total_points = get_total(cards)

    print('-' * 3)
    print('total points: {}'.format(total_points))
    print('total cards : {}'.format(total_cards))
    print('-' * 3)

    list_breakdown = get_breakdown(board)

    for key, item in list_breakdown.items():
        print(key)
        print('Points         {}'.format(item['points']))
        print('Cards          {}'.format(item['cards']))
        print('% total points {0:.2f}%'.format(list_breakdown[key]['points']/total_points * 100))
        print('% total cards  {0:.2f}%'.format(list_breakdown[key]['cards']/total_cards * 100))
        print('-' * 3)
