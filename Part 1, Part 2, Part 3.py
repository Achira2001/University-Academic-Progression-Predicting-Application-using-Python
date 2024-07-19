Progress=0
Trailer=0
Retriever=0
Excluded=0
total=0

Progressm=[]
Trailerm=[]
Excludedm=[]
Retrieverm=[]

f=open("file.txt","a")
f.truncate(0)
f.write("Part 3:\n")
f.close()
    
choice="y"
while True and choice=="y":

    try:
        Pass = int(input("Please enter your credit at pass:"))
        if Pass not in range(0,140,20):
            print("Out of range\n")
            continue
    except ValueError:
        print("Integer required\n")
        continue

    try:
        Defer = int(input("Please enter your credit at defer:"))
        if Defer not in range(0,140,20):
            print("Out of range\n")
            continue
    except ValueError:
        print("Integer required\n")
        continue
        
    try:
        Fail = int(input("Please enter your credit at fail:"))
        if Fail not in range(0,140,20):
            print("Out of range\n")
            continue
    except ValueError:
        print("Integer required\n")
        continue
    
    def calculatecredits (num1=0,num2=0,num3=0):                
        return num1+num2+num3
    total=calculatecredits(Pass,Defer,Fail)

    Progress1=[]
    Trailerl=[]
    Excludedl=[]
    Retrieverl=[]
    
    if total==120:
        if  Pass == 120:
            print("Progress")
            Progress = Progress+1
            Progress1.extend([Pass,Defer,Fail])
            Progressm.append (Progress1)
            
        elif  Pass==100 and (Defer or Fail)==20:
            print("Progress(module trailer)")
            Trailer = Trailer+1
            Trailerl.extend([Pass,Defer,Fail])
            Trailerm.append(Trailerl)
            
        elif  Fail>=80 and total==120:
            print("Exclude")
            Excluded = Excluded+1
            Excludedl.extend([Pass,Defer,Fail])
            Excludedm.append(Excludedl)
            
        else:
            print("Do not Progress - module retriever")
            Retriever = Retriever+1
            Retrieverl.extend([Pass,Defer,Fail])
            Retrieverm.append(Retrieverl)
            
    else:
        print("Total incorrect\n")
        continue
    print()

    while True:
        choice = input("Would you like to enter another set of data?  \n Enter 'y' for yes or 'q' to quit : ")
        if choice=='y' or choice=='q':
             print()
             break
        else:
            print('Invalid Option')
            print()
            continue
            

if choice=='q':
    print("--------------------------------------------------------------- ")
    print("Histogram")
    print("Progress",(Progress)  ,"\t"":",((Progress)*"*" ))
    print("Trailer",(Trailer) ,"\t""\t"":", ((Trailer)*"*"))
    print("Retriever",(Retriever) ,"\t"":", ((Retriever)*"*"))
    print("Excluded",(Excluded)  ,"\t"":", ((Excluded)*"*"))
    print()
    print((Progress+Trailer+Retriever+Excluded), "outcomes in total ")
    print("---------------------------------------------------------------- ")
else:
    print()
    
print("Part 2:")       
for x in Progressm :
    string= str(x)
    string=string[1:-1]
    print("Progress - "+string)
    f=open("file.txt","a")
    f.write("Progress - "+string+'\n')
    f.close()
    
        
for x in Trailerm:
    string= str(x)
    string=string[1:-1]
    print("Progress (module trailer) - "+string)
    f=open("file.txt","a")
    f.write("Progress (module trailer) - "+string+'\n')
    f.close()
    
    
for x in Excludedm:
    string= str(x)
    string=string[1:-1]
    print("Exclude - "+string)
    f=open("file.txt","a")
    f.write("Exclude - "+string+'\n')
    f.close()
    
for x in Retrieverm:
    string= str(x)
    string=string[1:-1]
    print("Module retriever - "+string)
    f=open("file.txt","a")
    f.write("Module retriever - "+string+'\n')
    f.close()

