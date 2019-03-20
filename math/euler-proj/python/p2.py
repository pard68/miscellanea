# Even Fibonacci Numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.
# Answer: 4613732

def fib(max):
	sequence = [1,2]
	prev = 1
	cur  = 2
	nex = 0

	while cur < max:
		nex  = cur + prev
		prev = cur
		cur  = nex
		sequence.append(nex)

	return sequence

def get_evens(numbers):
	return [x for x in numbers if is_even(x)] 

def is_even(num):
	if num % 2 == 0:
		return True
	else:
		return False

sequence = fib(4000000)
evens = get_evens(sequence)
print(sum(evens))
