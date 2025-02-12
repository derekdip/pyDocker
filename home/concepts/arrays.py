values = ["apple", None,3, 2,"table"]
#arrays don't care about type of values inside
#its up to the developer to make sure values are what you want them to be

print(values)
print(values[0])

values[0]="banana"
print(values)

values.append("something")
print(values)

values.remove(2) #removes the value 2 not the index
print(values)