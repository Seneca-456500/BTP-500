# Lab 2

## Part A: In-Class Discussion

### Group members

Group 2  
Eren Kilinc  
Aydin Arif  
The Duy Vu  
Rohith Haridas

---

## 1. What do the functions do?

### Function 1:

```python
def one(mylist, key):
	total = 0
	for i in range(len(mylist)):
		for j in range(i+1,len(mylist)):
			if i != j:
				if mylist[i] + mylist[j] == key:
					total += 1
	return total
```

This function is passed a list of numbers and a key value. It will count how many pairs of elements in the list add up to the key and return the number of matching pairs.

For example if mylist = [1, 2, 3, 4, 5] and the key = 6, then the matching pairs are (1, 5) and (2, 4), so the function returns 2. The main difference is that it checks by checking possible pairs.

### Function 2:

```python
def two(mylist, key):
	total = 0
	mylist.sort()
	i = 0
	j = len(mylist)-1
	while (i < j):
		if(mylist[i] + mylist[j] < key):
			i+=1
		elif(mylist[i] + mylist[j] > key):
			j-=1
		else:
			total += 1
			i+=1
			j-=1
	return total
```

This function is also passed a list of numbers and a key value. It sorts the list, then counts pairs of numbers that add up to the key and returns the number of matching pairs.

For example, if mylist = [1, 2, 3, 4, 5] and the key = 6, then the matching pairs are (1, 5) and (2, 4), so the function returns 2 but the main difference is that sorts and searches from both ends. 

### Function 3:

```python
def three(mylist, key):
	items={}
	total = 0
	for number in mylist:
		items[number]=1
	for number in mylist:
		other = key-number
		if(other in items):
			total+=1
	return total//2
```

This function is also passed a list of numbers and a key value. It will determine how many numbers have another number in the list that can be added to them to equal the key, and returns half that count to avoid counting each pair twice. For example, if mylist = [1, 2, 3, 4, 5] and the key = 6, then the matching pairs are (1, 5) and (2, 4), so the function returns 2 but the main difference is that it uses a dictionary to find matching values.

---

## 2. **WITHOUT DOING AN ANALYSIS** (so by gut feeling alone), rank your 3 functions individually... does your group's rankings match?

Ranking the 3 functions on gut feeling alone:

I'd say that the best function is the third function because it uses a dictionary to find matching values.

Next I'd say that the first function because it checks the possible pairs of numbers in the list to find matches.

Finally, I'd say the second function is the slowest because it uses the sort() function to sort the list before finding matches, resulting in O(n log n) time complexity.

---

## 3. Run `lab2_timing.py`. Does the timing validate your ranking? Any surprises?

The timing shows that the 3rd is the fastest, then the second and then the first is the slowest. I thought it would take longer for the second one to run than the first one, but the timing shows that it is the opposite.

---

## 4. Analyze at least one of the 3 functions (`one()`, `two()`, or `three()`). Each team member should analyse a different function.

```python
def one(mylist, key):
	total = 0                                 O(1)
	for i in range(len(mylist)):              O(n+2)
		for j in range(i+1,len(mylist)):        let X represent the
		                                        number of times the 
																						inner loop runs = 
																						((n-1)n)/2
																						Therefore the complexity of this
																						line is 0(3n + X).
																						
			if i != j:                            O(X)
				if mylist[i] + mylist[j] == key:    O(2X)
					total += 1                        O(2X) (worst case)
	return total                              O(1)
```

```text
T(n) = 1 + n+2 + 3n + X + X + 2x +2X + 1
     = 1 + 2 + 1 + n + 3n + X + X + 2X + 2X
     = 4 + 4n + 6X
     = 4 + 4n + 6( ((n-1)n) /2)
     = 4 + 4n + 3((n-1)n)
     = 4 + 4n + 3(n^2 - n)
     = 4 + 4n + 3n^2 - 3n
     = 3n^2 + n + 4
```

Therefore T(n) = 3n^2 + n + 4.  
In Big Notation, T(n) = O(n^2) as it is the dominant term.

---

## 5. Run `lab2_timing.py` with increasing values of the amount of data (increase by 1000 each time). Is there a pattern? (Note: ensure that you are using the same "machine" as you change the data size. Ideally a local computer to avoid inconsistencies). Does the timing reflect what you expect based on your analysis? Draw a plot in Excel that shows how the execution time increases with each input size for each function.

Yes, there is a  pattern. As the input size increases, the execution time for all three functions increases, but function one() increases much faster than the others. This matches my analysis of function one(), which has a time complexity of O(n²). The timing results support this, since increasing the data size causes the runtime of function one() to grow faster. The second and third functions increase much more slowly. From the timing results, function three() is the fastest, and then function two(), and finally function one() is the slowest. This is consistent with the timing results and shows that the data reflects what we would expect.

<img width="1204" height="714" alt="Screenshot 2026-10-04 183206" src="https://github.com/user-attachments/assets/ab3531ef-2cbc-4fe0-8423-592e3c8520fb" />
<img width="1200" height="706" alt="Screenshot 2026-10-04 183301" src="https://github.com/user-attachments/assets/5649aaaa-2a11-41fb-8951-82dfb95403e2" />
