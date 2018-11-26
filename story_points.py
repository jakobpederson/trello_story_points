from trello import TrelloClient
import datetime
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


def get_breakdown(board, skip=None):
    result = defaultdict(dict)
    all_lists = board.open_lists()
    valid_lists = [x for x in all_lists if x.name.lower() not in skip] if skip else all_lists
    for trello_list in valid_lists:
        result[trello_list.name.lower()] = {
            'points': get_total(trello_list.list_cards()),
            'cards': len(trello_list.list_cards())
        }
    return dict(result)


def get_percentages(points, cards, total_points, total_cards):
    percent_points = points/total_points * 100 if total_points else 0
    percent_cards = cards/total_cards * 100 if total_cards else 0
    return percent_points, percent_cards


def filter_skip_cards(cards, skip=None):
    return [x for x in cards if x.get_list().name.lower() not in skip.lower()] if skip else cards


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--api-key', required=True)
    parser.add_argument('--token', required=True)
    parser.add_argument('--board_id', required=True)
    parser.add_argument('--skip', required=False)
    args = parser.parse_args()

    client = TrelloClient(api_key=args.api_key, token=args.token)
    board = client.get_board(args.board_id)
    all_cards = board.open_cards()
    skip = args.skip.lower() if args.skip else None
    cards = filter_skip_cards(all_cards, skip)
    total_cards = len(cards)
    total_points = get_total(cards)

    print('`' * 3)
    print('Board: {}'.format(board.name))
    print('time run : {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M')))
    print('-' * 3)
    print('total points: {}'.format(total_points))
    print('total cards : {}'.format(total_cards))
    print('-' * 3)

    list_breakdown = get_breakdown(board, skip=skip)

    for key, item in list_breakdown.items():
        points = list_breakdown[key]['points']
        cards = list_breakdown[key]['cards']
        percent_points, percent_cards = get_percentages(points, cards, total_points, total_cards)
        print(key)
        print('Points:        {0:3d}'.format(points) + ' ({:.2f}% total points)'.format(percent_points))
        print('Cards :        {0:3d}'.format(cards) + ' ({:.2f}% total cards)'.format(percent_cards))
        print('-' * 3)
    print('`' * 3)
