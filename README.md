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
total points: 67
total cards : 30
---
percentage done points: 20.00%
percentage done cards : 19.35%
---
Backlog
Points 45
Cards  19
---
Meta
Points 0
Cards  2
---
In Progress
Points 21
Cards  8
---
Done
Points 1
Cards  1
---
