name="Batta Chetna Chowdary"
print(name[6:12]) # last letter not included
print(name[:5]) # start->index
print(name[6:]) # index->end

#negative indexing

print(name[-2:])
print(name[-4:])
print(name[-4:-2])

#inbult functions 

print(name.lower())
print(name.find('C'))
print(name.capitalize())
print(name.swapcase())
print(name.title())
print(len(name))

#string formating

txt1="My name is {fname}.I am {age}".format(fname="Chetna",age="19")
print(txt1) 
txt2="My name is {0}.I am {1}".format("hello","20")
print(txt2)

