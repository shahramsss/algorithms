# [2,11,7,15] , 9 



def t_s(nrs , tr ):
    dic= {}

    for i , num in enumerate(nrs):
        if tr-num in dic:
            return [dic[tr- num] , i ]
        dic[num] = i 
    return None


print(t_s([2,11,7,15] , 9 ))