def fib(number_for_fibonacci):
	# By Sarthak Rout:
	if number_for_fibonacci<=1 :
		return 0
	else :
		return fib(number_for_fibonacci-1)+fib(number_for_fibonacci-2)


def is_prime(number_to_check):
    # By Sarthak Rout:
	if number_to_check==2 or number_to_check==3 :
		return True
	else :
		k = int(sqrt(number_to_check)/6) ;
		for i in range(1, k):
			if number_to_check%(6*k-1)==0 or number_to_check%(6*k+1)==0:
				return False

		return True


def reverse_string(string_to_be_reversed):
	# Add code here
    return string_to_be_reversed[::-1]
	# return reversed_string

#Take input for fib in variable a

print(fib(a))


#Take input for is_prime in variable b
#By Sarthak Rout:
b=int(input())
print(is_prime(b))


#Take input for reverse in variable c

print(reversed_string(c))
