han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    #print("Line:",line)
    if line == "" :
        #print("Skip Blnk")
        continue

    wrds = line.split()
    #print("Words:",wrds)
    if wrds[0] != "From" :
     #   print("Ignore")
        continue
    print(wrds[1])