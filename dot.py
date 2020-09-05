list_c= [] 
n = int(input()) 
for i in range(0, n): 
    lst= int(input()) 
    list_c.append(lst)

print(list_c)
def natural_b(list_c):
    return list_c[0], list_c[-1]