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
        result[trello_list.name] = {
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

    print('=' * 50)
    print('total points: {}'.format(get_total(cards)))
    print('total cards : {}'.format(len(cards)))
    print('=' * 50)

    for key, item in get_breakdown(board).items():
        print(key)
        print('Points {}'.format(item['points']))
        print('Cards  {}'.format(item['cards']))
        print('=' * 50)
