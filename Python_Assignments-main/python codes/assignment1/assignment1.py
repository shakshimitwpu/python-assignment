students_list = ["Atharv", "Soham", "Rishi", "Vignesh", "Om"]
print("students list: ", students_list)

students_list.append("Rohan")
print(students_list)

students_list.remove("Atharv")
print(students_list)

students_list = ["Atharv", "Soham", "Rishi", "Vignesh", "Om"]
students_list.pop(1)
print(students_list)

del students_list[3]
print(students_list)

students_list[2] = "Shreya"
print(students_list)

students_tuple = ("Atharv", "Soham", "Rishi", "Vignesh", "Om")
print("students tuple: ", students_tuple)

y = list(students_tuple)
y.append("Rohan")
y.append("Himesh")
y.append("Karan")
students_tuple = tuple(y)
print(students_tuple)

y = ("Riley",)
students_tuple += y
print(students_tuple)

y = list(students_tuple)
y.remove("Atharv")
y.remove("Om")
students_tuple = tuple(y)
print(students_tuple)

students_dict = {1: "Atharv", 2: "Soham", 3: "Rishi", 4: "Vignesh", 5: "Om"}
print("students dictionary: ", students_dict)

students_dict[6] = "Rohan"
print("After adding Rohan: ", students_dict)

del students_dict[3]
print("After deleting Rishi: ", students_dict)

students_dict[2] = "Shreya"
print("After updating Shreya: ", students_dict)
