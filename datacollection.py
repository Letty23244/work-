#lists
#sets
#dictionaries
#turples
#1 lists(crud)
#they store multiple items
#crud=(create, read, update, delete)
#syntax
#they are square brackets
#list:are mutable , it also works with index
# items stored shud be the same
studentNames = ['sandra', 'patricia','phionah','anitah']
studentMarks =[90,80,70,60]


# access the whole list
print(studentNames, type(studentNames))

#INDEX are used
# index positive indexing (starts from the left and the intial is the 0)
print(studentNames[0])
print(studentNames[1])
print(studentNames[2])
print(studentNames[3])

#index(negative indexing)
print(studentNames[-4])
print(studentNames[-3])
print(studentNames[-2])
print(studentNames[-1])

#Appending an item
#adding new item at  the  end of the list
#at the end
studentNames.append('michelle')
print(studentNames)

#Inserting an item
#at aparticular position
studentNames.insert(2, 'faith')
print(studentNames)