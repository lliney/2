dic1={}
dic2={}
str1=input()
str2=input()
str3=input()
str4=input()
for i in range(len(str1)):
    dic1[str1[i]]=str2[i]
    dic2[str2[i]]=str1[i]
for i in str3:
    print(dic1.get(i),end='')
print()
for i in str4:
    print(dic2.get(i),end='')




