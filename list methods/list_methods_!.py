# append(): Used for appending and adding elements to List.It is used to add elements to the last position of List.
# Syntax: list.append (element)
# Adds List Element as value of List.
print("_______________append______________________")
List = ['Mathematics', 'chemistry', 1997, 2000]
List.append(20544)
print(List)
print("_________________insert________________________")
# insert(): Inserts an elements at specified position.
# Syntax:
#  list.insert(<position, element)
List = ['Mathematics', 'chemistry', 1997, 2000]
# Insert at index 2 value 10087
List.insert(2,10087)
print(List)
print("_________________extend________________________")
# extend(): Adds contents to List2 to the end of List1
# Syntax:
# List1.extend(List2)
List1 = [1, 2, 3]
List2 = [2, 3, 4, 5]

# Add List2 to List1
List1.extend(List2)
print(List1)
# Add List1 to List2 now
List2.extend(List1)
print(List2)
print("_________________sum________________________")
# sum() : Calculates sum of all the elements of List.
# Syntax: sum(List)
List = [1, 2, 3, 4, 5]
print(sum(List))
print("____________________count__________________")
# count():Calculates total occurrence of given element of List.
# Syntax:List.count(element)
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1))

print("_________________length________________________")
# length: Calculates total length of List.
# Syntax: len(list_name)
List = [1,2,3,4,5,'vamshi','dhar',2.56]
print(len(List))
print("_________________index________________________")
# index(): Returns the index of first occurrence. Start and End index are not necessary parameters.
# Syntax: List.index(element[,start[,end]])
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2))
print(List.index(2,2))
print("_________________min & max________________________")
# min() : Calculates minimum of all the elements of List.
# Syntax: min(List)
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print("min value",min(List))
print("max value",max(List))
print("_________________sort________________________")
# reverse(): Sort the given data structure (both tuple and list) in ascending order. Key and reverse_flag are not necessary parameter and reverse_flag is set to False, if nothing is passed through sorted().
# Syntax:
# sorted([list[,key[,Reverse_Flag]]])
#  list.sort([key,[Reverse_flag]])

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
#Reverse flag is set True
List.sort(reverse=True)
#List.sort().reverse(), reverses the sorted list
print(List)
sorted(List)
print(List)

print("__________________pop_____________________")
# pop(): Index is not a necessary parameter, if not mentioned takes the last index.
# Syntax: list.pop([index])
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop())
print(List.pop(0))
print(List)
print("_________________Delete________________________")
# del() : Element to be deleted is mentioned using list name and index.
# Syntax:
# del list.[index]
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
del List[0]
print(List)

print("_________________remove________________________")
# remove(): Element to be deleted is mentioned using list name and element.
# Syntax:
#  list.remove(element)
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
List.remove(3)
print(List)

print("_________________End________________________")
