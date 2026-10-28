#Rabbits and Recurrence Relations
#Given Positive integars n <= 40 and k <= 5
#Return: The total number of rabbit pairs present after n months
#This is if we begin with one pair and in each generation,
#every pair of repoduction-age rabbits produces a litter of k rabbits,
#instead of only one pair

def calculate(n,k):
    pairs_over_1_month = 0
    total = 1 #pairs of rabbits
    for i in range(n-1):
        pairs_over_1_month, total = total, total + (pairs_over_1_month*k)
    return total

n = 32
k = 2

print(calculate(n,k))