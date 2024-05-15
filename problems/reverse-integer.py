
def reverse(num,rev=0):

	isNegetive = False

	if num < 0:
		isNegetive = True
		num =  -num

	while num!=0:
		rev = rev*10 + (num%10)
		num //= 10

	return -rev if isNegetive else rev


print(reverse(-123))