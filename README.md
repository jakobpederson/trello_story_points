# Story Point Counter
* goes over trello cards in a board and breaks down story point scores and card counts

# Card Format
Card names need to have this format for this script to work:
`[story point score number]: [description]`

example:
* 2: fix issue with some app

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
time run : 2018-11-02 09:33
---
total points: 59
total cards : 26
---
backlog
Points:         37 (62.71% total points)
Cards :         16 (61.54% total cards)
---
done did it ya'll hear now
Points:          8 (13.56% total points)
Cards :          4 (15.38% total cards)
---
gitting it done
Points:         14 (23.73% total points)
Cards :          6 (23.08% total cards)
---
