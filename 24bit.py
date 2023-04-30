import sty    

print("24 bit color chart:-")
for i in range(0,256):
    for j in range(0,256):
        for h in range(0,256):
            print(sty.fg(i,j,h),i,j,h)

