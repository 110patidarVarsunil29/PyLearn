from sys import argv
from os.path import exists

script, from_script, to_script=argv
print(f"Copying from {from_script} to {to_script}")

in_script=open(from_script)
in_data=in_script.read()

print(f"The input file is {len(in_data)} bytes long")
print(f"Does the output file exist? {exists(to_script)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")

input()

out_file = open(to_script, 'w')
out_file.write(in_data)

print("Alright, all done.")

in_script.close()
out_file.close()