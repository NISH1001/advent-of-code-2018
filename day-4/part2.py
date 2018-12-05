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

    # compute the frequency for each guard and get hist most frequent minutes
    # in the format guard_id => (minutes, frequency)
    guards_frequency = { guard :Counter(minutes).most_common(1)[0] for guard, minutes in guards.items() }
    # find max based on frequency (not minutes)
    frequent_sleeper = max(guards_frequency.items(), key=lambda x : x[1][1])
    print(int(frequent_sleeper[0]) * frequent_sleeper[1][0])



if __name__ == "__main__":
    main()

