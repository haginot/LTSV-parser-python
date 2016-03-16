in_file_path = raw_input("Which LTSV file use as input?: ")
out_file_path = raw_input("Enter output file name: ")

in_file = open(in_file_path, 'r')
out_file = open(out_file_path, 'w')

for line in in_file:
  stack = []
  for elm in line.split('\t'):
    stack.append(''.join(elm.split(':')[1:]))
  out_file.write(', '.join(stack))

in_file.close()
out_file.close()
