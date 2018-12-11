## Link
https://adventofcode.com/2018/day/4


## Approach


### Setup
Initially, it seems the date time parsing has to be done  and then input is sorted according to the datetime. 
But, no hard work is to be done for sorting the input. We can directly sort the input as a problem of:  
*sorting list of strings* since the input is formatted in a very specific way that sorting as string works inherently for sorting based on  datetime.  


Also, we only have to consider the **minutes** part of the time. Rest can be ignored and doesn't contribute anything to the problem.

### Minute Tracking
I assume that parsing for falling asleep and waking up is self-implied in the code. So, here I tracked the list of minutes per every guard. 

First this is done  is done by getting the **waking up minute** and **sleeping minute** and getting all the numbers betwen them.
In the code, they are tracked 
using `end` and `start` variables respectively. We get the list using `range(start, end)` that captures all the minutes that the 
guard was falling asleep.

And `end-start` tracks the total time the guard fell asleep.

There are two dictionaries (hashmap, associative array, and other shit you can call...), namely:  
```python
guards = defaultdict(list)
guards_minutes = defaultdict(int)
```

The `guards` dict tracks all the minutes that the guard fell asleep in.  
The `guards_minutes` tracks the total time the guard fell asleep in.

### Part 1
For this, I found the top sleeping guard by finding the guard id who slept for maximum time by utilizing the ditionary `guards_minutes`. 
Once I found the guard id, I calculated using the `guards` dictionary the higest frequency minutes the guard fell asleep. This is 
done by making use of `Counter` from `collections` module.

And bingo, the result is obtained by multiplying the two shit.

### Part 2
This is quite simmilart to part 1.
All I did was to compute the highest minutes frequency for each guard, using the `guards` dict. This gives us the result in the format 
```python
# a list
[
    guard_id_1 => (minutes_x, frequency_a)
    ...
    ...
]
```

After that, I found the guard who had the highest sleeping frequency based on *frequency* part of the tuple.  
Finally, I get the minutes along with guard id and get the multiplication.
