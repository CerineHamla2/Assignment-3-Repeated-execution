
stop="continue"
#######################final####################
while(stop!= "stop"):
    mode=0
    num1=0
    num2=0
    while(mode!=1 and mode!=2):
        mode=int(input("choose 1 for GCF mode or 2 for LCM: "))

    while(num1<=0 or num2<=0):
        num1=int(input("please enter the first number:"))
        num2=int(input("please enter the second number:"))
    diff1=num1
    diff2=num2
    if mode==1: ##GCF
    

        while(diff1!=diff2):   #ex diff1=72 and diff2=48 
            if diff1>diff2:     #72>48
                diff1=diff1-diff2      #diff1=72-48=24 ()
            else:                       #diff2>diff1 (48>24)
                diff2=diff2-diff1       #diff2=48-24= 24                        
        gcf=diff1                       #diff2==diff1 so 24 is the GCF 
        print("the gcf is:",gcf)
    
    else:  ### mode==2 so calculate LCM

        while(diff1!=diff2):
              # diff1=diff1-diff2
            if diff1>diff2:
                diff1=diff1-diff2
            else:
                diff2=diff2-diff1
            gcf=diff1 
        lcm=(num1*num2)//gcf       #use gcf to calculate lcm
        print("the LCM is:",lcm)
    stop=(input("enter stop if you want to stop here or continue: "))

#lcm
rows=0
print("\n ###Pascal pyramid###")
while(rows<=0):
    rows=int(input("enter a valid number of rows: "))
row=" "
num_spaces=rows     
for i in range(0,rows):
    row=" "*(num_spaces-1)      #to create space at the begining of each row (for the pyramid shape)
    coef=1                      # the start of the row
    for j in range(i+1):         # i+1 is the number of numbers in each row
        row=row+str(coef)+" "
        coef=coef * (i-j)//(j+1)
    num_spaces-=1               #After each row, we decrease the number of spaces because the next row is getting wider.
    print(row)