from sys import argv
from os.path import exists

script, fromScript, toScript=argv
print(f"copying files from {fromScript} to {toScript} ")
# Exception Handling in Python
try:
    source=open(fromScript)  # Create a variable
    sourcedata=source.read()
    print(f"The input file is {len(sourcedata)} bytes long")
    print(f"Does the output file exist? {exists(toScript)}")

    desc=open(toScript,'w')
    descdata=desc.write(sourcedata)

    print("Data copied Successfully! You can check logs.")
#except FileNotFoundError as identifier:
#    identifier.filename.close()
#    identifier.filename2.close()

finally:
    source.close()
    desc.close()