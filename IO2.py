from sys import argv

script, filename = argv
txt=open(filename,'a')
txt.write("This is a test13 environment!!! ")
txt.close()

txt=open(filename)
print(txt.read())
txt.close()