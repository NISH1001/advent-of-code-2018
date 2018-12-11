#!/usr/bin/env python3


def main():
    with open('input') as f:
        res = sum([ int(line) for line in f])
        print(res)

if __name__ == "__main__":
    main()

