def palindrome_inefficient(s):
    i = 1
    is_palindrome = True
    for _ in s:
        a = s[i-1]
        b = s[len(s)-i]
        i += 1
        if a != b:
            is_palindrome = False
    return is_palindrome


print(palindrome_inefficient('racecar'))


def palindrome_efficient(s):
    return s == s[::-1]


print(palindrome_efficient('racecar'))


