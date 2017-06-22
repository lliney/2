sum={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0}
num={}
with open('dataset_3380_5.txt') as r:
    for c in r:
        s=c.strip().split('\t')
        sum[int(s[0])]=sum.get(int(s[0]))+(int(s[2]))
        if num.get(int(s[0]))!=None:
            num[int(s[0])]=num.get(int(s[0]))+1
        else: num[int(s[0])]=1
for i in num:
    sum[i]=sum.get(i)/(num.get(i))
for s in sum:
    print(s,sum[s] if sum[s]!=0 else '-') 