# Lab 3

This assessment contains materials that may be subject to copyright and other intellectual property rights. 

Modification, distribution, or reposting of this document is strictly prohibited. Learners found reposting this document or its solution anywhere will be subject to the college’s Academic Integrity policy.



## Due:
This lab is due at the end of the day that is before your next lab:
- section `NAA`: Monday, Oct 19 2026, @ 23:59
- section `NBB`: Thursday, Oct 22 2026, @ 23:59


## Objectives:

- Practice analysis of recursive functions
- Practice programming linked lists



## Setup

Set up your repository as instructed in [lab 0](lab-00.md).  In your repository, create a folder named `lab-03` and put there the content of the folder `release` and update those files as instructed below.

Unless otherwise stated, all writing goes into the file `lab3.md`.



## Resources

You may find the following parts of the notes useful:
* [how to do an analysis in 5 steps](https://seneca-ictoer.github.io/data-structures-and-algorithms/B-Algorithms-Analysis/how-to-do-an-analysis)
* [how to do a recursive analysis](https://seneca-ictoer.github.io/data-structures-and-algorithms/C-Recursion/analysis-of-recursive-functions)


## Part A: Analysis

Students who are more than 15 minutes late at the lab, cannot get credit for this part (this part will be considered incomplete for them).

This part of the lab must be done in class.  Get together into a small group of 3 to 4 students.  Write your complete answers in the `lab3.md` in your repository.

Perform a full analysis of the following recursive functions. The analysis must be complete:
  - identify the base case and the recursive case(s); analyze them separately.
  - for the base case(s):
    - on each line of the code, identify how many operations are performed, and what those operations are.
    - write your $T(base_case)$ by copying the number of operations from each line of code (identified above).
    - simplify your $T(base_case)$
  - for the recursive case(s):
    - on each line of the code, identify how many operations are performed, and what those operations are.
    - write your $T(n)$ by copying the number of operations from each line of code (identified above).
    - simplify your $T(n)$; you should get a recursive formula. Solve the recursion (to remove the $T(...)$ from the right side of the formula) and show/explain how you do it.
  - identify the dominant factor in the $T(n)$ formula.
  - state the complexity using *Big-O* notation.



### Function 1:

Analyze the following function with respect to `n`.

```python
def function1(value, n):
	if (n == 0):
		return 1
	elif (n == 1):
		return value
	else:
		return value * function1(value, n - 1)
```



### function 2:

Analyze the following function with respect to the length of the `mystring`.

**Hint:** you will need to set up two mathematical functions for operator counting:  one for `function2` and the other for `recursive_function2`.

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

Analyze the following function with respect to `n`.

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



## Part B: Programming

In this section of the lab, you will implement some functions for a *doubly linked list*, for both the *sentinel* and *non-sentinel* version of the list.  In your lab template you will find some drawing templates.  Use these to help you with your programming of these lists.

This part is considered complete if it passes testing with the provided unit tester.



### `Node` class

The `Node` class is declared within both the `DoublyLinked` and `Sentinel` class.  It stores:
- a piece of data
- a reference to the next node in the list
- a reference to the previous node in the list

When a `Node` is initialized, it is passed a data value.  Optionally it is also passed a reference to the next node and a reference to the previous node (in that order).  If the data values are not passed in, they are defaulted to `None`.

The `Node` class has the following member functions:

```python
def get_data(self):
    # returns data stored in node
```

```python
def get_next(self):
    # returns reference to next node in the list
```

```python
def get_previous(self)
    # returns reference to previous node in the list
```



### `DoublyLinked` and `Sentinel` Classes

```python
def get_front(self):
    # returns a reference to the first data node in the list.
    #   If the list is empty, returns `None`.


def get_back(self):
    # returns a reference to the last data node in the list.
    #   If the list is empty, returns `None`.


def push_front(self, data):
    # adds `data` to the front of the list (before the first data node).


def push_back(self,data):
    # adds data to the back of the list (after the last data node).


def pop_front(self):
    # removes the first data node from the list and
    #   returns the value stored in that node.
    # If the function is called on an empty list,
    #   raise the `IndexError` with this statement
    #   `raise IndexError('pop_front() used on empty list')`.


def pop_back(self):
    # removes the last data node from the list and
    #   returns the value stored in that node.
    # If the function is called on an empty list,
    #   raise the `IndexError` with this statement
    #   `raise IndexError('pop_front() used on empty list')`.
```



## Part C Reflection

1. Describe how to approach writing recursive functions, what steps do you take?

2. Describe the process of analyzing recursive functions.  How does it differ from analyzing non-recursive functions?  How is it the same? 

3. Described what you learned in the implementation for the linked lists.  What approach did you take?  What bugs did you find most difficult to fix.


## Submitting your lab

Push an updated version of the files found in the `release` and any other relevant files into the `lab-03` folder of your lab repository. Submit in BlackBoard the link to your repository.



## Lab Rubric:

| Criteria       | Poor - 0%                        | Fair - 50%                                           | Good - 100%         |
| -------------- | -------------------------------- | ---------------------------------------------------- | ------------------- |
| Lab Completion | Parts A and C not completed      | (part B) completed; (part A) or (part C) poorly done | All parts completed |
