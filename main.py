print()
print("Project One: Identity Jam")
print()
print()

first_name = "Mitchell"
last_name = "Marczak"
age = 13
print(first_name, last_name, age)
print()
age = 13 + 1
print(age, last_name)
print()
age = 13
school_grade = age - 5
print(school_grade,"th grade")
print()
x = 8 - school_grade
print("I will enter highschool in", x, "years!")

print()
print()
print("Project Two: Identity Jam")
print()
print()

favorite_things = ["family", "pets", "tacos", "hockey", "blue"]
print(favorite_things [1])
print()

print(favorite_things [-4])
print()

favorite_things1 = ["family", "pets"]
favorite_things2 = ["tacos", "hockey", "blue"]
print(favorite_things1)
print()

print(favorite_things2)
print()
favorite_things1 = ["family", "friends"]
favorite_things2 = ["hockey", "blue", "tacos"]
print(favorite_things1 + favorite_things2)

print()
print()
print("Project Three: Class Rosters")
print()
print()

class_a = ["Harris", "Ashton", "Leah", "Patricia"]
class_b = ["Jaden", "Gus", "Lilly", "Clara"]
class_a.append(class_b)
class_roster = class_a
print(class_roster)
print()

class_a = ["Harris", "Ashton", "Leah", "Patricia"]
class_roster = class_a + class_b
print(class_roster)
print()

class_roster.insert(5, "Mitchell")
print(class_roster)
print()

class_roster.remove("Ashton")
print(class_roster)
print()

class_project_group_1 = class_roster [0:4]
class_project_group_2 = class_roster [4:8]
print("Project Group 1: Bird Migration")
print("Students in group:", class_project_group_1)
print()

print("Project Group 2: Volcanoes")
print("Students in group:", class_project_group_2)
print()

student_trade_1 = class_project_group_1.pop(1)
student_trade_2 = class_project_group_2.pop(2)
class_project_group_1.insert(1, student_trade_2)
class_project_group_2.insert(2, student_trade_1)
print("Project Group 1: Bird Migration")
print("Students in group:", class_project_group_1)
print()

print("Project Group 2: Volcanoes")
print("Students in group:", class_project_group_2)

class_roster.clear()