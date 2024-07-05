#%%
def is_even(num):
    if num < 0:
        return "no dan kichik"
    return "0 dan katta"

nums = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda num: "3 dan katta" if num > 3 else "3 dan kichik", nums)))

print(list(filter(is_even, nums)))
# %%
def make_dictionary(lst: list) -> dict:
    new_dict = {}
    for el in lst:
        new_dict[el] = type(el) 
    return new_dict

list1 = ["map", "filter", 12, 212.3, True, None, False, False]

print(make_dictionary(list1))

def print_dict(elements):
    result = make_dictionary(elements)
    for key, value in result.items():
        print(f"Element: {key}, Tip: {value}")

list1 = ["map", "filter", 12, 212.3, True, None, False, False]

print_dict(elements)
# %%
tuples = [(1, 'bir'), (2, 'ikki'), (3, 'uch'), (4, 'to\'rt')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)

# %%
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)

# %%
multiply = lambda x, y: x * y
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
product_list = list(map(multiply, list1, list2))
print(product_list)

# %%
def calculate_average(students):
    return list(map(lambda student: {**student, 'average': sum(student['grades'].values()) / len(student['grades'])}, students))

def filter_passing_students(students, passing_grade):
    return list(filter(lambda student: student['average'] >= passing_grade, students))

def extract_student_names(students):
    return list(map(lambda student: student['name'], students))

# Funksiyalarni sinab ko'rish
students = [
    {"name": "Alice", "grades": {"math": 85, "science": 78, "english": 92}},
    {"name": "Bob", "grades": {"math": 56, "science": 65, "english": 58}},
    {"name": "Charlie", "grades": {"math": 95, "science": 88, "english": 93}},
    {"name": "Dave", "grades": {"math": 45, "science": 52, "english": 48}}
]

averages = calculate_average(students)
print("O'rtacha baholar:", averages)

passing_students = filter_passing_students(averages, 60)
print("O'tgan talabalar:", passing_students)

passing_student_names = extract_student_names(passing_students)
print("O'tgan talabalar ismlari:", passing_student_names)

# %%

def filter_by_category(products, category):
    return list(filter(lambda product: product['category'] == category, products))

def apply_discount(products, discount):
    return list(map(lambda product: {**product, 'price': product['price'] * (1 - discount)}, products))

def extract_product_info(products):
    return list(map(lambda product: (product['name'], product['price']), products))


products = [
    {"name": "Laptop", "price": 1000, "category": "Electronics"},
    {"name": "Shirt", "price": 50, "category": "Clothing"},
    {"name": "Phone", "price": 500, "category": "Electronics"},
    {"name": "Shoes", "price": 80, "category": "Clothing"}
]

electronics = filter_by_category(products, "Electronics")
print("Kategoriya bo'yicha filtrlangan:", electronics)

discounted_electronics = apply_discount(electronics, 0.10)
print("Chegirmadan keyingi elektronika:", discounted_electronics)

product_info = extract_product_info(discounted_electronics)
print("Mahsulot ma'lumotlari:", product_info)

# %%
def extract_names(people):
    return list(map(lambda person: person['name'], people))

def filter_by_age(people, min_age):
    return list(filter(lambda person: person['age'] >= min_age, people))

def capitalize_names(names):
    return list(map(lambda name: name.upper(), names))

# Funksiyalarni sinab ko'rish
people = [
    {"name": "alice", "age": 25, "city": "New York"},
    {"name": "bob", "age": 17, "city": "Los Angeles"},
    {"name": "charlie", "age": 30, "city": "Chicago"},
    {"name": "dave", "age": 15, "city": "San Francisco"}
]

names = extract_names(people)
print("Ismlar:", names)

adults = filter_by_age(people, 18)
adult_names = extract_names(adults)
print("Yosh bo'yicha filtrlangan:", adult_names)

capitalized_names = capitalize_names(adult_names)
print("Katta harflarda yozilgan ismlar:", capitalized_names)

# %%
