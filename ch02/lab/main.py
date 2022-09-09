import random
#Part A
classes_per_week = 3
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class)
#Part B
mylist = [1, 2, 3, 4, 5]
print(random.choice(mylist))
