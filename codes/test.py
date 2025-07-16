def rot_s(s, k):
    print(k // len(s))
    long_s = s * (k // len(s) + 2)

    if k <= len(s):
        return long_s[k: k+len(s)]
    else:
        return long_s[k- len(s):k]
    

print(rot_s("hello" ,22))

# hellohellohellohellohellohello