# Story Point Counter
* goes over trello cards in a board and breaks down story point scores and card counts and points and cards per members or member combination.

# Card Format
Card names need to have this format for this script to work:
`[story point score number]: [description]`

example:
* 2: fix issue with some app

Cards that have names that are not in that format get a score of 0.

# Command line
`python story_points.py --board_id=(gotten from url) --api_key=API_KEY --api_token=API_TOKEN --skip=(comma separated list of lists to skip)`

url:
https://trello.com/b/[board_id]/board_name

API_KEY and TOKEN can be found here:
https://trello.com/app-key

# Example Output
```
\```
---
Board: (board name)
time run : 2018-11-27 14:53
---
total points: 48
total cards : 21
---
(list name)
Points:         48 (100.00% total points)
Cards :         21 (100.00% total cards)
---
Bill and Michael:                7 points - 2 cards
Tom and Mark and Bill:           2 points - 1 cards
Mark:                            2 points - 1 cards
Johnny:                          5 points - 2 cards
Mark and Michael:                3 points - 1 cards
Kyle:                            6 points - 2 cards
Bill:                            3 points - 1 cards
Michael:                         5 points - 1 cards
Jessica:                         5 points - 2 cards
Tom:                             10 points - 5 cards
---
\```
