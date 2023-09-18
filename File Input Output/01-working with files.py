myfile = open('test.txt')
# print(myfile)
# print(myfile.read())
# so let's read again the file 
# print(myfile.read())
# print(myfile.read())
# I'm able to read the first time around, but these two times I'm not reading anything why is that ? 

# Well, this open function has this idea of a cursor. That is, you can only read the file once.
# so when you open the file and then read is going to read using cursor so at the time by the end of this first reading, the cursor is going to be at the end of the file.

# So now when it tries to read, it's going to be end of the file and nothing will be left there
# so to prevent this you can get the cursor back to the beggining by saying 

# myfile.seek(0)  # the zero is the index you want the cursor to go
# print(myfile.read())


#  another unique thing that you can do is to do read line
# print(myfile.readline()) 
# run the first and then add new lines to the file 
# print(myfile.readline()) 

# as you can see we only getting the first line of the file.    why is that ? 
# cause this idea is the readline method just reads one line at the time so anytime you run the file it just reads only the first line so to solve this run multiple readline method at one time  you will get each line
# print(myfile.readline()) 
# print(myfile.readline()) 
# print(myfile.readline()) 


# Another thing that I can do is to just say readlines if I run this. I get a list that contains the entire file, reads all the lines
print(myfile.readlines())


# So now we have to do this is a little annoying things and  you actually have to manually close the file after you've opened it with open. So you can use it somewhere else in the program.

myfile.close()

# but  I'll show you how we don't need not to this anymore in the future (upcoming lessons)
