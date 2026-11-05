## Part A: Analysis

### Function 1

```python
def function1(value, n):
	if (n == 0):                              #O(1) - == 1 operation
		return 1                                #O(1) - return value 1 operation
	elif (n == 1):                            #O(1) - == 1 operation
		return value                            #O(1) - return value 1 operation
	else:                                     # no operations
		return value * function1(value, n - 1)  #O(3 + T(n-1))
```
Base case 1: n = 0
In this case, the function checks if the value is equal to 0, enters the if statement and then returns the value.
T(0) = 1 + 1
T(0) = 2

Base case 2: n = 1
In this case, the function checks if the value is equal to 0, does not enter the if statement, checks the elif statement, enters the elif statement and then returns the value.
T(1) = 1 + 1 + 1
T(1) = 3

Recursive case: n > 1
In this case, the function checks if the value is equal to 0, does not enter the if statement, checks the elif statement if it is equal to 1, does not enter, enters the else statement, performs the operations and returns a value.
T(n) = 1 + 1 + 3 + T(n-1)
T(n) = 5 + T(n-1)

Now to solve the recurrence:
T(n) = 5 + T(n-1)
(substitute T(n-1))
T(n) = 5 + 5 T(n-2)
T(n) = 10 + T(n-2)
(substitute T(n-2))
T(n) = 10 + 5 T(n-3)
T(n) = 15 + T(n-3)
(substitute T(n-3))
T(n) = 15 + 5 T(n-4)
T(n) = 20 + T(n-4)
(there is a pattern)
T(n) = 5k + T(n-k)
(since the recursion stops when n=1)
n-k=1
k=n-1
(substitute k=n-1)
T(n) = 5(n-1) + T(1)
(since T(1) = 3
T(n) = 5(n-1) + 3
T(n) = 5n - 5 + 3
T(n) = 5n - 2
Therefore, T(n) = 5n - 2 and the big 0 complexity is O(n).

### Function 2

```python
def recursive_function2(mystring, a, b):
	if(a >= b ):                                                #O(1) - >= 1 operation
		return True                                               #O(1) - return value 1 operatiom
	else:
		if(mystring[a] != mystring[b]):                           #O(3) - 2 indexing and 1 != operation
			return False                                            #O(1) - return value
		else:   
			return recursive_function2(mystring, a + 1, b - 1)      #O(4+T(n-2)) - return, mystring, +, -, and n-2 because its checking 2 less characters

def function2(mystring):
	return recursive_function2(mystring, 0, len(mystring) - 1)  #O(4) - function call, -, len(), return
```

Base case 1: a>= b
In this case, the function checks if the a is greater than or equal to b. If true, it enters the if statement and returns True.
T(O) = 1 + 1
T(O) = 2

Base case 2: mystring[a] != mystring[b]
In this case, the function checks if a is >= to b, does not enter the first if statement, enters the else statement, checks if the characters at positions a and b are different and returns false if they're different.
T(n) = 1 + 3 + 1
T(n) = 5

Recursive case: a < b and mystring[a] == mystring[b]
In this case, the function check if a is greater than or equal to b, does not enter the first if statement, enters the else statement, checks if the characters at positions a and b are different, does not enter the second if statement and enters the else statement. Then, it adds 1 to a and substracts 1 from b, and recursively calls the function with the updated values and returns the result.
T(n) = 8 + T(n-2)
(substitute T(n-2))
T(n) = 8 + 8 + T(n-4)
T(n) = 16 + T(n-4)
(substitute T(n-4)
T(n) = 16 + 8 + T(n-6)
T(n) = 24 + T(n-6)
(after k amount of recursive calls)
T(n) = 8k + T(n-2k)
(the recursion stops when n-2k = 0 for a string of even length)
n - 2k = 0
2k = n
k = n/2
(substitute k = n/2)
T(n) = 8(n/2) + T(O)
(since T(0) = 2)
Therefore, T(n) = 4n + 2 and the big O comeplxity is O(n).


### Function 3

```python
def function3(value, n):
    if (n == 0):                            # O(1) - == 1 operation
        return 1                            # O(1) - return value 1 operation
    elif (n == 1):                          # O(1) - == 1 operation
        return value                        # O(1) - return value 1 operation
    else:                                   # no operations
        half = n // 2                       # O(2) - integer division and assignment
        result = function3(value, half)     # O(2 + T(n//2)) - function call and assignment
        if (n % 2 == 0):                    # O(2) - modulo and comparison
            return result * result          # O(2) - multiplication and return
        else:                               # no operations
            return value * result * result  # O(3) - 2 multiplications and return
```
Base Case 1: n = 0
In this case, the function checks if n is equal to 0, enters the if statement, and returns 1.
T(O) = 1 + 1
T(O) = 2

Base Case 2: n = 1
In this case, the function checks if n is equal to 0, does not enter the if statement, checks the elif statement, enters it because n equals 1, and returns value.
T(1) = 1 + 1 + 1
T(1) = 3

Recursive Case 1: n > 1 and n is even
In this case, the function checks if n is equal to 0, does not enter the if statement, checks if n equals 1, does not enter the elif statement, and enters the else statement.
It divides n by 2 using integer division and assigns the result to half. It then recursively calls function3 using half and assigns the returned value to result.
Next, it checks whether n is even using modulo (n % 2 == 0). Since it is even, the function multiplies result by itself and returns the value.

T(n) = 1 + 1 + 2 + 2 + T(n/2) + 2 + 3
T(n) = 10 + T(n/2)

Recursive Case 2: n > 1 and n is odd
In this case, the function checks if n is equal to 0, does not enter the if statement, checks if n equals 1, does not enter the elif statement, and enters the else statement.
It divides n by 2 using integer division and assigns the result to half. It then recursively calls function3 using half and assigns the returned value to result.
Next, it checks whether n is even using modulo. Since n is odd, the function enters the else statement, multiplies value by result and then by result again, and returns the value.
T(n) <= 11 + T(n/2)
(substitute T(n/2))
T(n) <= 11 + 11 + T(n/4)
T(n) <= 22 + T(n/4)
(substitute T(n/4))
T(n) <= 22 + 11 + T(n/8)
T(n) <= 33 + T(n/8)
(substitute T(n/8))
T(n) <= 33 + 11 + T(n/16)
T(n) <= 22 + T(n/16
(there is a patttern of T(n) <=11k + T(n/2^k))
(the recursion stops when n reaches 1)
n/2^k = 1
(multiplying both sides by 2
n = 2^k
(log of both sides)
log2n = k
k = log2n
(sub k = log2n into recurrence)
T(n) <= 11 log2n + T(1)
(from base case 2 T(1) = 3)
Therefore: T(n) <= 11 log2n + 3 and the time complexity in big o notation is O(log n)





## Part C: Reflection

Answer the following questions:
1. Describe how to approach writing recursive functions, what steps do you take?
When writing a recursive function, I first try to understand what the function needs to do. Then, I identify the base case, which is when the function should stop calling itself. After that, I work on the recursive case, where the function calls itself with a smaller problem. I also make sure that each recursive call gets closer to the base case to avoid infinite recursion. Finally, I test the function with different inputs to make sure it works correctly.

2. Describe the process of analyzing recursive functions.  How does it differ from analyzing non-recursive functions?  How is it the same? 
When analyzing recursive functions, I start by identifying the base case and recursive case. I count the operations performed in each case and use them to create a recurrence formula, such as T(n) = T(n-1) + 5. I then solve the recurrence to find the time complexity using Big-O notation. The difference is that recursive functions require us to consider how many times the function calls itself, while non-recursive functions usually involve analyzing loops and other operations directly. They are similar because both involve counting operations, finding the dominant factor, and determining the overall time complexity.

3. Described what you learned in the implementation for the linked lists.  What approach did you take?  What bugs did you find most difficult to fix.
While implementing linked lists, I learned how nodes are connected using pointers or references and how to insert, delete, and traverse nodes. My approach was to work on one function at a time and test it before moving to the next one. I also tried to understand how changing one node's reference could affect the rest of the list. The most difficult bugs were related to updating the links between nodes, especially when inserting or deleting nodes at the beginning or end of the list. I also found it challenging to handle empty lists and avoid accessing nodes that didn't exist. Testing different cases helped me understand where the problems were and how to fix them.