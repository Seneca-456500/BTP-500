#
#   Author: Catherine Leung
#   This file is for the inclass discussion (Part A)
#

import time
import random



def one(mylist, key):
	total = 0
	for i in range(len(mylist)):
		for j in range(i+1,len(mylist)):
			if i != j:
				if mylist[i] + mylist[j] == key:
					total += 1
	return total



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



AMOUNT_OF_DATA = 5000



# generate a list of unique random numbers (AMOUNT_OF_DATA unique values)
my_list = random.sample(range(1, AMOUNT_OF_DATA*10), AMOUNT_OF_DATA)
my_list2 = my_list.copy()
my_list3 = my_list.copy()

total_time = 0

# generate an odd number as the target
target = random.randint(1,AMOUNT_OF_DATA*10-1)
if target % 2 == 0:
    target += 1  


start_time = time.perf_counter()
result = one(my_list, target)
end_time = time.perf_counter()
total_time = (end_time-start_time)
print(f"time for one()= {total_time}")


start_time = time.perf_counter()
result = two(my_list, target)
end_time = time.perf_counter()
total_time = (end_time-start_time)
print(f"time for two()= {total_time}")

start_time = time.perf_counter()
result = three(my_list, target)
end_time = time.perf_counter()
total_time = (end_time-start_time)
print(f"time for three()= {total_time}")
