"""
Problem :- Write a program that takes a number N as the input, and prints it to the output.

Input Format :- The only line contains a single integer.

Output Format :- Output the answer in a single line.

Constraints :- 0≤N≤10^5
 
Sample 1:-

Input :- 123
Output :- 123

Sample 2:-

Input :- 15
Output :- 15

"""

#Solution

T = int(input())
for tc in range(T):
	# Read integers a and b.
	(a, b) = map(int, input().split(' '))
	
	ans = a + b
	print(ans)
