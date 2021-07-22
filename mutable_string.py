'''
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.

'''


def mutate_string(string, position, character):
    my_list = list(string)
    my_list[position] = character
    return ''.join(my_list)		#converting list into string with no space and return it

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)