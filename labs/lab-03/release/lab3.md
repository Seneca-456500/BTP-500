## Part A: Analysis

### Function 1

```python
def function1(value, n):
	if (n == 0):
		return 1
	elif (n == 1):
		return value
	else:
		return value * function1(value, n - 1)
```



### Function 2

```python
def recursive_function2(mystring, a, b):
	if(a >= b ):
		return True
	else:
		if(mystring[a] != mystring[b]):
			return False
		else:
			return recursive_function2(mystring, a + 1, b - 1)

def function2(mystring):
	return recursive_function2(mystring, 0, len(mystring) - 1)
```



### Function 3

```python
def function3(value, n):
	if (n == 0):
		return 1
	elif (n == 1):
		return value
	else:
		half = n // 2
		result = function3(value, half)
		if (n % 2 == 0):
			return result * result
		else:
			return value * result * result
```



## Part C: Reflection

Answer the following questions:
1. Describe how to approach writing recursive functions, what steps do you take?
2. Describe the process of analyzing recursive functions.  How does it differ from analyzing non-recursive functions?  How is it the same? 
3. Described what you learned in the implementation for the linked lists.  What approach did you take?  What bugs did you find most difficult to fix.
