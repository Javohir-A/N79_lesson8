#%%
def type_elem(lst):
    dict={}
    for i in lst:
        dict[i]=type(i).__name__
     
    return dict




lst=["map", "filter", 12, 212.3, True, None, False, False]

dct=type_elem(lst)
print(dct)

# %%
def make_dict(lst):
    return {element: type(element).__name__ for element in lst}

list1 = ["map", "filter", 12, 212.3, True, None, False, False]

result = make_dict(list1)
print(result)

# %%

list1 = ["map", "filter", 12, 212.3, True, None, False, False]


