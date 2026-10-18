s = "radar"
is_palindrome = True
left, right = 0, len(s) - 1

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome) 
