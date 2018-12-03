#!/usr/bin/env python3

from collections import Counter


def main():
    twos_counter = 0
    threes_counter = 0
    with open('input') as f:
        for line in f:
            line = line.strip()
            counter = Counter(line)
            twos_filtered = list(filter(lambda x : x[1]==2, counter.items()))
            threes_filtered = list(filter(lambda x : x[1]==3, counter.items()))
            if twos_filtered:
                twos_counter += 1
            if threes_filtered:
                threes_counter += 1
    print(twos_counter)
    print(threes_counter)
    print(twos_counter * threes_counter)


if __name__ == "__main__":
    main()

