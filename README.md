# Story Point Counter
* goes over trello cards in a board and breaks down story point scores and card counts

# Card Format
Card names need to have this format for this script to work:
`[story point score number]: [description]`

Cards that have names that are not in that format get a score of 0.

# Command line
`python story_points.py --board_id=(gotten from url) --api_key=API_KEY --api_token=API_TOKEN`

url:
https://trello.com/b/[board_id]/board_name

API_KEY and TOKEN can be found here:
https://trello.com/app-key

# Example Output
```
---
total points: 65
total cards : 31
---
backlog
Points          29 (29.00% total points)
Cards           14 (14.00% total cards)
---
done
Points          19 (19.00% total points)
Cards            8 (8.00% total cards)
---
in progress
Points          17 (17.00% total points)
Cards            7 (7.00% total cards)
---
meta
Points           0 (0.00% total points)
Cards            2 (2.00% total cards)
---
