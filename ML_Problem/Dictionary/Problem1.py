data = {
    'apple' : 20,
    'banana' : 70,
    'orange' : 15,
    'cherry' : 50,
    'pineapple' : 30,
    'grapes' : 40,
}

asc_sort = dict(sorted(data.items() ,key = lambda item:item[1]))
print(asc_sort)
