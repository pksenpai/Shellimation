"""
>>> Making Animation for Shell <<<
   >>>  JUST FOR FUN :3  <<<

"""
from time import sleep


ANIMATION = [
    "[ [       ] Loading   ] ", #0
    "[ [D      ] Loading.  ] ", #1
    "[ [:D     ] Loading.. ] ", #2
    "[ [+:D    ] Loading...] ", #3
    "[ [++:D   ] Loading   ] ", #4
    "[ [+++:D  ] Loading.  ] ", #5
    "[ [++++:D ] Loading.. ] ", #6
    "[ [+++++:D] Loading...] ", #7
    "[ [++++++:] Loading   ] ", #8
    "[ [+++++++] Loading.  ] ", #9
    "[ [3++++++] Loading.. ] ", #10
    "[ [:3+++++] Loading...] ", #11
    "[ [.:3++++] Loading   ] ", #12
    "[ [..:3+++] Loading.  ] ", #13
    "[ [...:3++] Loading.. ] ", #14
    "[ [....:3+] Loading...] ", #15
    "[ [.....:3] Loading   ] ", #16
    "[ [......:] Loading.  ] ", #17
    "[ [.......] Loading.. ] ", #18
    "[ [o......] Loading...] ", #19
    "[ [:o.....] Loading   ] ", #20
    "[ [ :o....] Loading.  ] ", #21
    "[ [  :o...] Loading.. ] ", #22
    "[ [   :o..] Loading...] ", #23
    "[ [    :o.] Loading   ] ", #24
    "[ [     :o] Loading.  ] ", #25
    "[ [      :] Loading.. ] ", #26
    "[ [       ] Loading...] ", #27
]

TOTAL_FRAME = len(ANIMATION)

time = [0, 'unlimited', 28] # [start time, unlimited time, >limited time<]
start_time = time[0]
fin_time = time[2] # [1]: unlimited time or [2]: limited time

if fin_time == time[1]:
    while True:
        print(ANIMATION[start_time % TOTAL_FRAME], end="\r")
        sleep(0.2)
        start_time += 1
else:
    while start_time <= fin_time:
        print(ANIMATION[start_time % TOTAL_FRAME], end="\r")
        sleep(0.2)
        start_time += 1
