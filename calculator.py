def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1*num2

def divide(num1, num2):
	return num1/num2

def modulo(num1, num2):
	return num1%num2

def power(base, exponent):
	return base**exponent

def square(num):
	return num**2

print add(4,5)
print subtract(4,5)
print multiply(4,5)
print divide(30,6)
print modulo(42,8)
print power(2,3)
print square(3)

#a. (4+5) + (9-6)
print add(add(4,5),subtract(9,6))

#b. (12/2) - 60
print subtract(divide(12,2),60)

#c 1 + 2 + 3
print add(add(1,2),3)

#d. (1 + 2)2
print square(add(1,2))

#e (3%4) / 9*9 
print divide(modulo(3,4),multiply(9,9))

#f. 7 * (3+8)
print multiply(7,add(3,8))

#g (1+2) - 3 * (4+5)
print  subtract(add(1,2), multiply(3,add(4,5)))

#h. 3(2+3)
print power(3,add(2,3))

