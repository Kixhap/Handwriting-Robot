import string

# Given set of characters
given_characters = {'9', 'D', 'f', ';', "'", '6', 'F', 'N', 'e', 'T', '?', 'h', 'Y', 'o', 'E', '-', 'L', 'n', 't', 'P', '8',
                    'j', '7', ')', 'H', ' ', '(', '"', 'p', 'v', '4', 'k', 'C', 'U', ',', 's', 'y', 'u', 'G', 'V', 'c',
                    'K', '!', 'J', 'i', 'r', '2', '\x00', 'd', 'l', 'x', '0', 'z', 'b', '1', '.', 'A', 'a', '#', 'I',
                    'W', 'w', 'O', '5', 'g', 'M', '3', 'm', 'q', ':', 'R', 'B', 'S'}
given_characters2=9
for i in given_characters:
    given_characters2+=given_characters[i]
# Full alphabet set (lowercase and uppercase)
alphabet = set(string.ascii_letters)  # All letters A-Z and a-z

# Find the missing letters
missing_letters = alphabet - given_characters
print(missing_letters)
print(given_characters2)
