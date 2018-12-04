## Link
https://adventofcode.com/2018/day/3

## Approach
**Setup**  

Here, I have made use of `numpy` library and its vectorization shit.  

Here, I allocate **1000x1000** fabric matrix which is a zero matrix.  
After that, for each **claim** I keep on using sub-matrices of that fabric matrix and increase the value by 1 successively. 

**Part 1**  
When each claim has been seen, I simply find the locations in the **1000x1000** fabric matrix where value is greater than 1. 
This is done by using `np.where` function which returns the boolean values for every location fo the mentioned condition.  
And finally, I take the sum of that which gives total number of overlapping regions.  
This makes "sense" since any increment that exceeds `1` is telling us that the region is being incremented by another claim (sub matrix).  


**Part 2**
Like part 1, I loop through each claim one more time - each time extracting the sub-matrix (claim matrix) and finding the max max value 
within the sub matrix. If the max value is exactly equal to 1 I simply know that the region is not being overlapped with any other claims.


