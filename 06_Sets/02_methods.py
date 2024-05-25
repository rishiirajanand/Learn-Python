# Set Methods

# 1. add(ele) ==> add the element

set1 = set()
set1.add(10)
print(set1)

# 2. remove(ele) ==> remove the element based on argument if present in set else give KeyError

set2 = {2,'rishi', False, 10.2, False} 
set2.remove(2)
print(set2)

# 3. clear() ==> clear the all element from set

set3 = {4,6,2}
set3.clear()
print(set3)

# 4. pop()  ==> remove random element from sets

set4 = {4,6, 'Rishi' , 21.2}
set4.pop()
print(set4)

# 5. union(set) ==> conbines both value and return new set

set5 = {1,2,3}
set6 = {2,3,4,5}
newSet = set5.union(set6)
print(newSet)

# 6. intersection ==> combines common value and return new sets

set7 = {1,2,4}
set8 = {1,2,6,7}
newSet2 = set7.intersection(set8)
print(newSet2)