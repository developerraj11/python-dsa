"""
You are given a positive integer N. Your task is to find and return its square root. If N is not a perfect square, then return the floor value of sqrt(N).


Note:
In case, if you are facing the test case failure, take the variables inside the function in 'unsigned int' data type.
Example:
Input: N = 6

Output: 2

Explanation: The square root of the number 6 lies between 2 and 3, so the floor value is 2.


Constraints:
0 <= N <= 10 ^ 16

Time Limit: 1 sec.
Sample Input 1:
6
Sample Output 1:
2
Explanation of Sample Input 1:
The square root of the given number 6 lies between 2 and 3, so the floor value is 2.
Sample Input 2:
100
Sample Output 2:
10
Explanation of Sample Output 2:
The square root of the given number 100 is 10.
"""

def squareroot(n):
    # Write your code logic here !!
    left = 0
    right = n-1
    ans = 0
    while(left <= right):
        # mid = (left+right) // 2; 
        mid = left + (right - left) // 2
        square = mid * mid;
        if(square <= n):
            ans = mid
            left = mid +1
        else:
            right = mid -1
    return ans;
