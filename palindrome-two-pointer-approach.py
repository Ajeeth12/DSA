def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            print(False)
        left += 1
        right -= 1

    print(True)



Input = "A man, a plan, a canal: Panama"
is_palindrome(Input)