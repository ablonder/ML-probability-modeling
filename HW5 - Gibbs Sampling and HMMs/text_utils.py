import string
import io

def dict_from_file(filename):
    d = {}
    with io.open(filename, encoding = "ISO-8859-1") as f:
        for line in f:
            line = line.split()
            if len(line) > 0:
                d[line[0]] = 1
    return d
        
def encode_string_to_int_list(s):
    ints = range(27)
    letters = list(string.ascii_lowercase)
    letters.append(' ')
    d = dict(zip(letters, ints))
    s_list = list(s)
    result = []
    for char in s_list:
        result.append(d[char])
    return result

def decode_int_list_to_string(i_list):
    ints = range(27)
    letters = list(string.ascii_lowercase)
    letters.append(' ')
    d = dict(zip(ints, letters))
    result = []
    for i in i_list:
        result.append(d[i])
    return ''.join(result)

def check_validity(l, d):
    tokens = str.split(l)
    for w in tokens:
        if w not in d:
            return False
    return True

# ##### Test cases    
# print encode_string_to_int_list('food')
# # Should return [5, 14, 14, 3]
# print decode_int_list_to_string([6, 14, 14, 3, 26, 5, 14, 14, 3])
# # Should return 'good food'
#  
# d = dict_from_file('brit-a-z.txt')
# l1 = 'the quick brown fox jumped over the lazy dog'
# l2 = 'the quick brown fox jumped over the lazy dob'
#  
# print check_validity(l1, d)
# # Should yield True
# print check_validity(l2, d)
# # Should yield False
