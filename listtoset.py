'''
The first line contains an integer ,
 the total number of country stamps.
The next  lines contains the name of 
the country where the stamp is from.

Output the total number of distinct 
country stamps on a single line.

'''

N = int(input())
stamp_list = []
for _ in range(N):
    stamp_list.append(input())
stamp_set = set(stamp_list)
print(len(stamp_set))