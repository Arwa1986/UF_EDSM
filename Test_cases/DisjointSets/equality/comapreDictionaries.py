# dict1 = {'Name': 'asif', 'Age': 5}
# dict2 = {'Name': 'lalita', 'Age': 78}
# if dict1 == dict2:
#     print("dict1 is equal to dict2")
# else:
#     print("dict1 is not equal to dict2")
# #  Answer: NOt equal
#
# dict1 = {'Name': 'asif', 'Age': 5}
# dict2 = {'Name': 'asif', 'Age': 5}
# if dict1 == dict2:
#     print("dict1 is equal to dict2")
# else:
#     print("dict1 is not equal to dict2")
# #  Answer: equal
#
# dict1 = {'Name': ['asif'], 'Age': [5]}
# dict2 = {'Name': ['asif'], 'Age': [5]}
# if dict1 == dict2:
#     print("dict1 is equal to dict2")
# else:
#     print("dict1 is not equal to dict2")
# #  Answer: equal
#
# dict1 = {'Name': ['asif', 'Arwa'], 'Age': [5, 20]}
# dict2 = {'Name': ['asif', 'Arwa'], 'Age': [5, 20]}
# if dict1 == dict2:
#     print("dict1 is equal to dict2")
# else:
#     print("dict1 is not equal to dict2")
# #  Answer: equal
#
# dict1 = {'Name': ['asif', 'Arwa'], 'Age': [5, 20]}
# dict2 = {'Name': ['Arwa', 'asif'], 'Age': [5, 20]}
# if dict1 == dict2:
#     print("dict1 is equal to dict2")
# else:
#     print("dict1 is not equal to dict2")
# #  Answer: NOt equal
#
# dict1 = {'Name': ['asif', 'Arwa'], 'Age': [5, 20]}
# dict2 = {'Name': ['asif','Arwa'], 'Age': [20, 5]}
# if dict1 == dict2:
#     print("dict1 is equal to dict2")
# else:
#     print("dict1 is not equal to dict2")
# #  Answer: NOt equal
#
# d = {"a": 3, "b": 2}
# d1 = {"a": 2, "b": 3}
# res = all((d1.get(k) == v for k, v in d.items()))
# print(res)
#
# d = {"a": 3, "b": 2}
# d1 = {"b": 2, "a": 3}
# res = all((d1.get(k) == v for k, v in d.items()))
# print(res)
#
# d = {'Name': ['asif', 'Arwa'], 'Age': [5, 20]}
# d1 = {'Name': ['asif','Arwa'], 'Age': [20, 5]}
# res = all((d1.get(k) == v for k, v in d.items()))
# print(res)
#
# # d = {'Name': ['asif', 'Arwa'], 'Age': [5, 20]}
# # d1 = {'Name': ['asif','Arwa'], 'Age': [20, 5]}
# # res =  set(d.values()) == set(d1.values())
# # print(res)
#
# set1 = ['Arwa', 'Alfini']
# set2 = ['Arwa']
# res = set1 == set2
# print(res)
#
# set1 = ['Arwa', 'Alfitni']
# set2 = ['Arwa', 'Alfitni']
# res = set1 == set2
# print(res)
#
# set1 = ['Arwa', 'Alfitni']
# set2 = ['Alfitni', 'Arwa']
# res = set1 == set2
# print(res)

self_set = ['a', 'b']
other_set = ['a', 'c', 'b']
result = all(item in other_set for item in self_set)
print(result)