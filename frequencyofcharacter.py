def count(string):
    dict = {}
    for s in string:
        if s in dict.keys():
            dict[s] += 1
        else:
            dict[s] = 1
    print("total count is ", dict)
    
count('Hello world')