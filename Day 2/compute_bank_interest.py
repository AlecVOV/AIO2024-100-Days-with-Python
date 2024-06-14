def compute_interest(money, period):
    result = money  
    n = period   
    for _ in range(period):
        result = (1 + (1/n))**n
    return print(result)  

compute_interest(1, 12)
compute_interest(1, 365)
compute_interest(1, 730)
