'''
There is an array of  integers. There are also  disjoint sets,
  and , each containing  integers. You like all the integers in
 set  and dislike all the integers in set . Your initial happiness is .
 For each  integer in the array, if , you add  to your happiness. If ,
 you add  to your happiness. Otherwise, your happiness does not change.
 Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However,
 the array might contain duplicate elements.

'''

a=input().split(' ')
l=([int(i) for i in input().split(' ')])
firstset=set([int(i) for i in input().split(' ')])
secondset=set([int(i) for i in input().split(' ')])
p=0
for i in l:
    if i in firstset:
        p+=1
    if i in secondset:
        p-=1
print(p)