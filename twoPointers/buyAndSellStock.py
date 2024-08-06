# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Best Time to Buy and Sell Stock

def maxProfit(stock_prices: list[int | float]) -> int | float :
    l,r = 0,1
    MaxP = 0
    while(r<len(stock_prices)):
        if(stock_prices[l] < stock_prices[r]):
            MaxP = max(MaxP, stock_prices[r] - stock_prices[l])
        else:
            l = r
        r += 1
    return MaxP
