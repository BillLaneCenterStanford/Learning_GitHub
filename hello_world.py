print "hello, world." #automatically prints endline


#the range function -- it's like a for loop. It can take three arguments
#(maybe more, but I never use more than three)

for i in range(10): #will print 0-9
    print i #note that the print fuction automatically adds a return
    #also note that the indentation is four spaces, and you need
    #a colon for indentation

print "\n" #will actually print two endlines

for i in range (2,10):#now i starts at 2, goes to 10
    print i

print "\n"

for i in range (0,10,2):#now starts at zero, but 
    print i

print "\n"

for i in range (10,0,-1):#woah! check this out! going backwards! 
    print i

print "\n"

list1 = [1,2,3,4]
list2 = ["one","two",3,4]

for item in list2: #I use this syntax all the time -- it iterates thorugh
    print item #a 'list,' -- note that this isn't an "array"

for item1, item2 in zip(list1, list2): #this is just a funky way of iterating
    #through two lists that have the same length
    print list1, list2 #note that you can print multiple things with coma seperating them
