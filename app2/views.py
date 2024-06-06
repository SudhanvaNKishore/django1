from django.shortcuts import render
from app2.forms import inputforms

def home(request):
    result3=[]
    result4=""
    w3=""
    w4=""
    if request.method == "POST":
        form1= inputforms(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            w3=data.get("word3")
            print("....................................")
            
            result3=perm3(w3)
            # result4 = perm4(w4)
            return render(request , "myapp/permutations.html",{"param1":result3,"form":form1})
    else:
        form1=inputforms()
    return render(request , "myapp/permutations.html",{"param1":result3,"form":form1})
def perm3(s3):
    c1=s3[0:1]
    c2=s3[1:2]
    c3=s3[2:3]
    list3=[]    
    list3.append(c1+c2+c3)
    list3.append(c1+c3+c2)
    list3.append(c2+c1+c3)
    list3.append(c2+c3+c1)
    list3.append(c3+c1+c2)
    list3.append(c3+c2+c1)
    return list3
def perm4(s4):
    c1=s4[0:1]
    c2=s4[1:2]
    c3=s4[2:3]
    c4=s4[3:4]
    list4=[]
    part1=c1
    part2=c2+c3+c4
    temp=perm3(part2)
    for i in range(0,len(temp),1):
        list4.append(part1+temp[i])
    part1=c2
    part2=c1+c3+c4
    temp=perm3(part2)
    for i in range(0,len(temp),1):
        list4.append(part1+temp[i])
    part1=c3
    part2=c1+c2+c4
    temp=perm3(part2)
    for i in range(0,len(temp),1):
        list4.append(part1+temp[i])
    part1=c4
    part2=c1+c2+c3
    temp=perm3(part2)
    for i in range(0,len(temp),1):
        list4.append(part1+temp[i])
    return list4

