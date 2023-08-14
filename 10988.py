#팰린드롬인지 확인하기

word = input()
palindrome = 0

if len(word) == 1:
    palindrome = 1

elif len(word)%2 == 0:
    for i in range(len(word)//2):
        if word[i] == word[-i-1]:
            palindrome = 1
            continue
        else:
            palindrome = 0
            break
else:
    for i in range((len(word)//2)+1):
        if word[i] == word[-i-1]:
            palindrome = 1
            continue
        else:
            palindrome = 0
            break
print(palindrome)

