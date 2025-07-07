# this is my comment
# this is palindrome
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Example usage
word = "Racecar"
print(is_palindrome(word))  # Output: True
