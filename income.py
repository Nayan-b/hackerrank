'''
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.





X = int(input())
total_price = 0
size_array = list(map(int, input().split()))
N = int(input())
for i in range(N):
    shoe_size, price = map(int, input().split())
    if shoe_size in size_array:
        total_price += price
        size_array.remove(shoe_size)
        
       
print(total_price)