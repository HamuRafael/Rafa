def remove_duplicatas(n):
    l=[]
    for i in n:
        if i not in l:
            l.append(i)
    return l
print(remove_duplicatas([1,2,2,3]))
            