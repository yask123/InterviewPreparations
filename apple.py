stock_prices_yesterday = [10, 9, 8, 7, 6, 5]


min_price = stock_prices_yesterday[0]
max_profit = stock_prices_yesterday[1]-stock_prices_yesterday[0]

for i in range(1,len(stock_prices_yesterday)):

	current_price = stock_prices_yesterday[i]

	potential_profit = current_price - min_price

	min_price = min(min_price,current_price)


	if max_profit <  potential_profit:
		max_profit = potential_profit

print max_profit	
