#20,37,45,87,99,10

scores = []
scores.insert(0,20)
print(scores)
scores.extend([37,45,87,99,10])
print(scores)
highest_score = 0
for score in scores:
    if score > highest_score:
        highest_score = score
print(f"the highest score in the class is {highest_score}")


