# day1_sample_code

a_string = "like this" # snake case (cf.camelCase, superLongVariable)
a_number = 3
a_float = 3.14
a_boolean = False
a_none = None     # != flase

# print(type(a_string))
# print(type(a_number))
# print(type(a_float))
# print(type(a_boolean))
# print(type(a_none))

# sequence type : list, tuple
days = ["Mon", "Tue", "Wed", "Thur", "Fri"] #list
print(days)
print(type(days))

print("Mon" in days)
print(len(days))

# mutable operations : 값 변경 가능 (cf. Immutable)
print(days)
days.append("Sat")
print(days)
days.reverse()
print(days)

# immutable list
# 1. tuple
days = ("Mon", "Tue", "Wed", "Thur", "Fri")
print(days)
print(type(days))

# 2. dictionary
nico = {
  "name" :"Nico",
  "age" : 29,
  "korean" : "Favortie",
  "fav_food" : ["Kimch", "Sashmi"]  # list, tuple도 저장가능
}

print(nico["fav_food"])
nico["handsome"] = True   # new data
print(nico)

# built-in function
age = "18"
n_age = int(age)
print(type(age))
print(type(n_age))
