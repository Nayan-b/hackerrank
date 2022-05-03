'''

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

'''

def minion_game(string):
    # your code goes here
    vowel_list = ['A','E','I','O','U']
    vowel_word = []
    const_word = []
    
    for i in range(len(string)):
        for j in range(i,len(string)):
            if string[i] in vowel_list:
                vowel_word.append(string[i:j])     #appending the word starting with vowel in list
            else:
                const_word.append(string[i:j])   #appending the word starting with consonant in list
    
    if len(const_word) > len(vowel_word):
        ans = f"Stuart {len(const_word)}"
    elif len(const_word) < len(vowel_word):
        ans = f"Kevin {len(vowel_word)}"
    else:
        ans = "Draw"
        
    print(ans)
        

if __name__ == '__main__':
    s = input()
    minion_game(s)


'''
Below code is simplified version of above 
There is no need of list for storing the words
we can directly increment count for each word found


def minion_game(string):
    # your code goes here
    vowel_list = ['A','E','I','O','U']
    count_vowel = 0
    count_const = 0
    
    for i in range(len(string)):
        for j in range(i,len(string)):
            if string[i] in vowel_list:
                count_vowel += 1     
            else:
                count_const += 1   
    
    if count_const > count_vowel:
        ans = f"Stuart {count_const}"
    elif count_const < count_vowel:
        ans = f"Kevin {count_vowel}"
    else:
        ans = "Draw"
        
    print(ans)
        

if __name__ == '__main__':
    s = input()
    minion_game(s)

'''

