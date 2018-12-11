#!/usr/bin/env python3

import re
from collections import defaultdict, Counter


def main():
    lines = sorted([ line.strip() for line in open('input')])
    guards = defaultdict(list)
    guards_minutes = defaultdict(int)
    start, end = 0, 0
    for line in lines:
        time, action = line.split('] ')
        minutes = int(time[-1 : -3 : -1][::-1])

        gid = re.findall(r'#(\d+)', action)
        if gid:
            guard = gid[0]
        elif 'asleep' in action:
            start = minutes
        elif 'wakes' in action:
            end = minutes
            m = [ i for i in range(start, end)]
            guards[guard].extend(m)
            guards_minutes[guard] += (end-start)

    top_sleeper = max(guards_minutes.items(), key=lambda x : x[1])[0]
    counter = Counter(guards[top_sleeper])
    m = counter.most_common(1)[0][0]
    print("Guard number {} slept for higesht time with top minutes as :: {}".format(top_sleeper, m))
    print( int(top_sleeper) * m)

if __name__ == "__main__":
    main()

