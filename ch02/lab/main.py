import random
#Part A
classes_per_week = 3
print("Classes per week:", classes_per_week)
weeks = 16
print("Number of weeks:", weeks)
classes = 5
print("Number of classes:", classes)
tuition = 6000
print("Cost of tuition:", tuition)
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class)
#Part B
numbers = [1, 2, 3, 4, 5]
print(random.choice(numbers))