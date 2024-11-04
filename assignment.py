#1 print Patricia Phiona and Anitah
#Add masha at the fourth position
#update the name phionah to Phionah Alidinnah
#display the length of the student list
#print all the students names having update the list using a for loop
# calculatethe total marks for the studentsmarks variables
studentNames = ['Sandra','Patricia','Phionah','Anitah'] 
studentMarks =[80,56,78,90]
data =['Sandra',90,'Kamokya']
print(studentNames[-3])
print(studentNames[-2])
print(studentNames[-1])

studentNames.insert(4,'masha')
print(studentNames)

studentNames[2] = 'phioah Alidinnah'
print(studentNames)

print(len(studentNames))
  
for name in studentNames:
    print(studentNames)
    
total_mark = sum(studentMarks)
print(total_mark)