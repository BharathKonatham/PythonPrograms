
palin = "ada"
length = len(palin)
isPalin = True
for i in range(0,int(length/2)+1,1):
    if(palin[i]!=palin[length -1-i]):
        isPalin = False
print(isPalin)