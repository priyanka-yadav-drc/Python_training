def buy_and_sell(stock_price):
	print(stock_price)
	max_profit_val=0
	max_s=max(stock_price)
	min_s=min(stock_price)
	max_profit_val=max_s-min_s
	return max_profit_val

print(buy_and_sell([8, 10, 7, 5, 7, 15]))
print(buy_and_sell([6, 2, 8, 11]))

