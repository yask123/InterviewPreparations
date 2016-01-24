'''
Q: Making a change
'''
def no_of_coins(coins,amount_left,n):
	if amount_left == 0:
		return 1

	elif n < 0 or amount_left <0:
		return 0

	return no_of_coins(coins,amount_left-coins[n],n) + no_of_coins(coins,amount_left,n-1)

print no_of_coins([20,10],20,1)	