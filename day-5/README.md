## Link
https://adventofcode.com/2018/day/5

## Approach

### Bruteforce
Initially, I tried bruteforce approach - reducing the string at a time per iteration until there's no further change in the length of 
the string. However (:/) it didn't go well because the amount of time it took to run the whole solution is out of this world :D. 

The `react` function does the job. 
```python
# the brute force approach
def react(polymer):
    units = list(polymer)
    n = len(units)
    loc = 0
    for i in range(0, n-1):
        current = polymer[i]
        nextc = polymer[i+1]
        if abs(ord(current) - ord(nextc)) == 32:
            loc = i
            break
    del units[loc]
    del units[loc+1]
    return ''.join(units)
```
I just had to loop through this function until no change is seen.

To know if two letters are polar opposite, I just have to find the ascii difference between them. If it was 32, they 
were same letter but with opposite **CASE**.

The time complexity for this is **O(n^2)**, since the reduction is done at a time per iteration and there's another main loop that 
keeps on feeding the *reduced* string to this function.


### Optimized
Here, I tried optmizing the shit by making use of stack. The `react` function had become as:
```python
def react(polymer):
    stack = []
    for c in polymer:
        if stack and are_opposite(c, stack[-1]):
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)
```

#### Breakdown
There's a stack named (well, you guess it right!) `stack` that keeps track of the character that didn't get destroyed.  
Everytime a new character **c** from the polymer is seen (as per forward iteration), it compares that charater with the character 
sitting at the end of the stack (referenced as `stack[-1]`. If, they aren't of opposite nature, we just add the current character **c** 
to the stack. Else, we pop the character (the one at the end of the stack) off from the stack.

The time complexity for this approach is **O(n)** since we are just going from left to right once (a character per iteration).


#### Part 2
For part 2. It was easy: 
```python
    - loop each character from the list of lowercases `abcdefghijklmnopqrstuvwxyz`.
    - replace the occurence of that character along with its uppercase couterpart by an empty character (done using regex)
    - reduce the resulting string using `react` function
    - keep track of length of the reduced string
    - finally, find minimum length which is the answer
```
