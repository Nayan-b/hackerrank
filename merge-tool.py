'''
Consider the following:

A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  substrings where each
 subtring, , consists of a contiguous block
 of  characters in . Then, use each  to create 
string  such that:

The characters in  are a subsequence of the characters in
 .
Any repeat occurrence of a character is removed 
from the string such that each character in  
occurs exactly once. In other words, if the 
character at some index  in  occurs at a previous index
  in , then do not include the character in string .
Given  and , print  lines where each line  
denotes string .


'''
def merge_the_tools(string, k):
    # your code goes here
    distinct = []
    chunks = [string[i:i+k] for i in range(0, len(string), k)]  #hold the list of substring of length k from string
    
    new_chunks = []

    #store the substring with no duplicate character in it in new_chunks list

    for chunk in chunks:
        t = ""
        for char in chunk:
            
            if char in t:
                pass
            else:
                t += char
        new_chunks.append(t)
        

    for new_chunk in new_chunks:
        print(new_chunk)
    
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)