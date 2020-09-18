#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime complexity is O(n).  n is being performed at n^3 but a is being increased by n^2... So it should condense to O(n) runtime.  

b) Runtime complexity is O(nLogn).  The outer for loop runs at O(n) while the inner loop does not need to even run "n" times.  

c) Runtime complextity is O(n).  The algorithm recursively executes n times based on the amount of bunnies (counts down).  


## Exercise II 

ANSWER:

    1. We could initially drop an egg at the middle floor and the floor above the middle floor.

    2. If the egg doesnt break at the middle floor but does at middle + 1, f = 1 floor above the middle floor of the building.

    3. If it doesn't break at either, we can repeat the binary search with the upper half of the building (Where our starting point is middle + 1)

    3. If the egg breaks at the middle also, we can restart this process but towards the ground floor (Starting point is ground floor .. up to middle - 1).

    4. Keep repeating this binary search process until you find your answer or two floors remain .. where process of elimination of those two floors will give you the answer.  

    This method follows O(log n) runtime complexity.   

























Notes: 
-N Story building ... egg breaks if thrown off floor f or higher .. (so if floor > f .. egg = broken?)  Determine f so that eggs broken is small as possible.  Sorted array... floors 0 - n 

So basically no idea where f is ... So question is asking what is the best search method for finding f?   Binary search has low runtime complexity but might be a better option?  

Binary search is typically O(log n) vs linear which is O(n)

So basically we would check middle and middle + 1 ... if it doesn't break at middle but does at mid + 1 .. f = middle + 1?  if neither, we check next lowest midpoint .. 

So if we're at 1/4 ... and restart the process ... 