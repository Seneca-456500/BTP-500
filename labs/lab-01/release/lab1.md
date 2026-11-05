Part A:

sum_to_goal function: 

Wrote the function.
I estimate that because there is a loop in a loop, that the complexity will be O(n^2)

Traded functions.

Discussed as a group.

Everyone had a different complexity. My teammates analysis did mactch what I thought the runtime was. However, depending on the outcome of the function, the complexity could be O(1), O(n) or O(n^2).
I think my version seems to run the fastest.

Rewriting the function:
def sum_to_goal(numbers_list, goal):
for i in range(len(numbers_list)):
for j in range(i + 1, len(numbers_list)):
if numbers_list[i] + numbers_list[j] == goal:
return (numbers_list[i] * numbers_list[j])
return None

My guess was correct and my teammates analysis was also correct but like I mentioned, it changes depending on the input.

How I would test the function: By running increasingly larger lists, I could compare the run times and the input increases. If the size is doubled, it should take roughly twice as long. I also need to test cases where no pair would reach the goal value and it would force every single outcome including the worst case.

I estimate that the complexity of this function is O(n).

Did your teammate's analysis match what you thought your function's runtime was? 
- No my teammates analysis did not match what I thought the runtime was.

Was there any version in the group that had a different complexity?
No, there was not.



Fibonacci Function:
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

To test this, I would test the complexity by running the Fibonacci function with larger and larger values for n and looking at the time it takes to execute. Since the time complexity is O(2ⁿ), the execution time should increase very quickly as n increases. I would compare the results to see if the growth is there. 



PART B:

def function1(n):         O(1)
	total = 0               O(1)

	for i in range(n):      O(n)}
		x = i + 1             O(2)} loop total = O(4n)
		total += x * x        O(2)}

	return total            O(1)

	O(1) + O(1) + O(4n) + O(1) = O(4n)
	
	Big O time complexity: O(n)


	def function2(n):
		return (n * (n + 1) * (2 * n + 1)) // 6

		There are 7 operations, therefore the time complexity is O(7).
		Big O time complexity: O(1)



def function3(list):            O(1)
	n = len(list)                 O(2) 
	for i in range(n - 1):        O(n-1)
		for j in range(n - 1 - i):    O((n^2-n)/n)
			if list[j] > list[j + 1]:   O(4)
				tmp = list[j]               O(2)
				list[j] = list[j + 1]       O(3)
				list[j + 1] = tmp           O(2)

Therefore, the time complexity of function3 is O(n^2) as biggest term is O(n^2).

	Big O time complexity: O(n^2)