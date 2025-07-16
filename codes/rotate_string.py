"""
("hello" , 2) => "llohe"
("hello" , 3) => "lolhe"
("hello" , 6) => "elloh"
"""


def rotate_string(s, k):
    long_string = s * (k // len(s) + 2)
    if k <= len(s):
        return long_string[k : k + len(s)]
    else:
        return long_string[k - len(s) : k]


print(rotate_string("hello", 201))
