Progress=0
Trailer=0
Retriever=0
Excluded=0
total=0

studentid={}    

choice='y' 
while True and choice=='y':                     
    while True:
        st_id=input('Enter your  ID :')
        if st_id in studentid:
            print('alredy given\n')
            continue
        else:
            break

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


    if total==120:
        if Pass==120:
            print("Progress")
            Progress = Progress+1
            studentid[st_id]='Progress - ',Pass,Defer,Fail 
        
        elif Pass==100 and (Defer or Fail)==20:
            print("Progress (module trailer)")
            Trailer = Trailer+1
            studentid[st_id]="Progress (module trailer) - ",Pass,Defer,Fail   
                                               
        elif Fail>=80 and total==120:
            print("Exclude")
            Excluded = Excluded+1
            studentid[st_id]= "Exclude - ",Pass,Defer,Fail 
                 
        else:
            print("Do not progress – module retriever")
            Retriever = Retriever+1
            studentid[st_id]= "Do not progress – module retriever - ",Pass,Defer,Fail   
                            
    else:
        print("Total incorrect\n")
        continue
    print()
    
    while True:
        choice= input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit : ")
        if choice== "y" or choice=="q" :
            print()
            break
            
        else:
            print('Invalid Option')
            print()
            continue
        
if choice=="q" :
    print("--------------------------------------------------------------- ")
    print("Histogram")
    print("Progress",(Progress)  ,"\t"":",Progress*"*" )
    print("Trailer",(Trailer) ,"\t""\t"":", ((Trailer)*"*"))
    print("Retriever",(Retriever) ,"\t"":", ((Retriever)*"*"))
    print("Excluded",(Excluded)  ,"\t"":", ((Excluded)*"*"))
    print()
    print((Progress+Trailer+Retriever+Excluded), "outcomes in total ")
    print("---------------------------------------------------------------- ")
    print("Part 4:")     
    print(studentid)    
