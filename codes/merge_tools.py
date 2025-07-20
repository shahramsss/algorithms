"""
AAABCADDE

AAA BCA DDE

A BCA DE
"""


def merge_tools(string, k):
    unique = []

    for i in range(0, len(string), k):
        u = ""
        for ch in string[i : i + k]:
            if ch not in u:
                u = u + ch
        unique.append(u)

    print("\n".join(unique))

merge_tools('AAABCADDE' , 3)
