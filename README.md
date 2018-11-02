# Story Point Counter
* goes over trello cards in a board and breaks down story point scores and card counts

# Card Format
Card names need to have this format for this script to work:
`[story point score number]: [description]`

Cards that have names that are not in that format get a score of 0.

# Command line
`python story_points.py --board_id=(gotten from url) --api_key=API_KEY --api_token=API_TOKEN --skip=(name of list to skip)`

url:
https://trello.com/b/[board_id]/board_name

API_KEY and TOKEN can be found here:
https://trello.com/app-key

# Example Output
```
---
Board: (board name)
---
total points: 65
total cards : 30
---
done
Points:         37 (56.92% total points)
Cards :         14 (46.67% total cards)
---
backlog
Points:         18 (27.69% total points)
Cards :          8 (26.67% total cards)
---
meta
Points:          0 (0.00% total points)
Cards :          2 (6.67% total cards)
---
in progress
Points:         10 (15.38% total points)
Cards :          6 (20.00% total cards)
---
