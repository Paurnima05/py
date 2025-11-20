myfile = open("/content/np.txt", "r")
print(myfile.read())

myfile = open("/content/np.txt", "w")
myfile.write("Data Science")
myfile.close()

myfile = open("np.txt", "r")
print(myfile.read())