def is_palindrome(word):
    for i in range(0, len(word)):
        if word[i] == word[len(word)-1-i]:
            continue
        else:
            print('No')
            return
    print('Yes')

is_palindrome(input('Enter the word: '))