def read():
  f = open("input",'r') 

  # read a  
  line = f.readline()
  split = line.split()
  a = split[2]
print(a)

#clean up
f.close()
