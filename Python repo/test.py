# info = {
#     "name" : "ZAIN",
#     "Class" : 17
# }
# print(info)
# info["name"] = "Zain"
# print(info)
# student = {
#     "name" : "Zain",
#     "Class" : 17,
#     "subjects_marks" : {
#         "phy" : 87,
#         "math" : 94
#     }
# }
# student.update({"city" : "Sialkot"})
# print(student)
# set = {1, 2, 3, 4, 5}
# print(set)
# print(type(set))
# ad = set()
# ad.add(1)
# print(ad)
# ad.clear()
# print(ad)
# num = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(num.pop())
# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 3, 5}
# set = set1.intersection(set2)
# print(set)
# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 3, 5}
# set = set1.union(set2)
# print(set)
# dict = {
#     "cat" : "a small animal",
#     "table" : ["zain", "ZAIN"]
# }
# print(dict)
# marks = {}
# a = int(input("Enter marks of phy: "))
# marks.update({"phy" : a})
# b = int(input("Enter marks of chem: "))
# marks.update({"chem" : b})
# c = int(input("Enter marks of math: "))
# marks.update({"math" : c})
#
# print(marks)
# set = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(set)
obtained_marks = float(input("Enter the obtained marks: "))
total_marks = float(input("Enter the total marks: "))
percentage = (obtained_marks / total_marks) * 100
print(percentage)