# import pandas as pd
# import numpy as np
# from scipy import stats
# pd.read_csv()
# np.mean()
# from module1 import *

import module1

import random

from matplotlib import pyplot as plt



dcc = []
dff = []
for i in range(5):
	dc = random.choice(range(-10,44))
	dcc.append(dc)
	df = module1.Celsius_F(dc)
	dff.append(dff)


plt.plot(dcc,dff)
plt.show()



















# < 30: E, 30-40: D, 41-60: C, 60 - 75: B, >75: A


# def GradingSystem(mark):
# 	if 0 < mark < 30:
# 		return "E"
# 	elif 30 <= mark <= 40:
# 		return "D"
# 	elif 40 < mark <= 60:
# 		return "C"
# 	elif 60 < mark <= 75:
# 		return "B"
# 	elif 75 < mark <=100:
# 		return "A"
# 	else:
# 		return "Invalid"


# marks = random.sample(range(-20,120),35)
# print(marks)

# for i in range(10): #range(0,10)
# 	a = random.choice(range(-20,120))
# 	grade = GradingSystem(mark=a)
# 	print(a, grade)



#Commision problem
# >10000R: "Excellent"
# between 2000R and 10000R: "Good"
# between 300R and 2000R: "Fair"
# any value less than 300R: "Poor"


# def CommisionProblem(amount):
# 	if amount>=10000:
# 		return "Excellent"
# 	elif amount>=2000 and amount<=10000:
# 		return "Good"
# 	elif amount>=300 and amount<2000:
# 		return "Fair"
# 	else:
# 		return "No commission"

# for i in range(40): #range(0,10)
# 	a = random.choice(range(-200,20000))
# 	comm = CommisionProblem(amount=a)
# 	print(a, comm)




# if condition and condition: # true true
# 	return something




# def Remuneration(rewards):
# 	if 2000 >= rewards and rewards <10000: # 2000 >= 775: true, 775 < 10000: true
# 		return "Good"

	# if rewards >= 2000 and rewards <10000:
	# 	return "Good"


# print(Remuneration(775))


# Discounts

# Define a function call DiscountsCalculator taking 
# an argument called amount

# > 4500R given 9% discount of amount
# 2000 and 4500 given discount of 5%
# 1000 and 2000 given discount 3%
# <1000 No discount

# The function should return discount amount


# Bonus: Modify the same function to return amount paid
# amount paid = amount - dicount


# def Discount(amount_spent):
# 	if amount_spent > 4500:
# 		discount = (9/100)*amount_spent
# 		return discount

# print(Discount(7800))










