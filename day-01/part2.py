#!/usr/bin/env python3


def main():
    observed = set()
    freq = 0
    done = False
    while not done:
        with open("input") as f:
            for line in f:
                freq += int(line)
                if freq in observed:
                    print(freq)
                    done = True
                    break
                else:
                    observed.add(freq)


if __name__ == "__main__":
    main()

