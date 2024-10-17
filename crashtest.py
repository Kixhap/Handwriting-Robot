import string
import re

# Given set of characters
#given_characters = {'9', 'D', 'f', ';', "'", '6', 'F', 'N', 'e', 'T', '?', 'h', 'Y', 'o', 'E', '-', 'L', 'n', 't', 'P', '8',
#                    'j', '7', ')', 'H', ' ', '(', '"', 'p', 'v', '4', 'k', 'C', 'U', ',', 's', 'y', 'u', 'G', 'V', 'c',
#                    'K', '!', 'J', 'i', 'r', '2', '\x00', 'd', 'l', 'x', '0', 'z', 'b', '1', '.', 'A', 'a', '#', 'I',
#                    'W', 'w', 'O', '5', 'g', 'M', '3', 'm', 'q', ':', 'R', 'B', 'S'}
regex = r"9Gn()T'p,ymRB0MLY#18si?-Du:b2AqeJ5g9!PatHoFcO.h6NIkd3 V 74rjlKWzESCU;xwvf"
# Initialize given_characters2 with a number, but it should likely be a string to concatenate with other characters
#given_characters2 = "9"
test = "żźćńłąęóŻŹĆŃŁĄĘÓ"
replacement_map = {
    "Z": "z", "Ż": "z", "Ź": "z", "ź": "z", "ż": "z",
    "Ś": "s", "ś": "s",
    "ł": "l", "Ł": "l",
    "ć": "c", "Ć": "c",
    "ą": "a", "Ą": "a",
    "ę": "e", "Ę": "e",
    "ń": "n", "Ń": "n",
    "ó": "o", "Ó": "o"
}
result = "".join(replacement_map.get(char, char) for char in test)
response = "".join(char for char in result if char in regex)

print(response)