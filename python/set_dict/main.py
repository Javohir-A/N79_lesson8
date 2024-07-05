
# %%
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
multiply = lambda x,y: x*y

list3 = [multiply(list1[i], list2[i]) for i in range(len(list1))]
# map(lambda x:x[0]*x[1], [(list1[i], list2[i]) for i in range(len(list1))])

print(list3)
# %%

def extract_names(people:list) -> list:
    return list(map(lambda x:x["name"] if x["age"] > 18 else None, people)) #xato yo'y

people = [
    {"name": "alice", "age": 25, "city": "New York"},
    {"name": "bob", "age": 17, "city": "Los Angeles"},
    {"name": "charlie", "age": 30, "city": "Chicago"},
    {"name": "dave", "age": 15, "city": "San Francisco"}
]
print(extract_names(people))

# %%

list1 = [1,2,3,4,5,6,7,8,9]

print(list(map(lambda num:"kichik" if num < 5 else "katta", list1)))
# %%
