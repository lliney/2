n=int(input())
#введення кількості матчів
d={}
#порожній словник
for i in range(0,n):
    s=(input().split(';'))
    #введення вхідних даних (стрічки)
    if (s[0] in d):
      d[s[0]][0]+=1
      if (int(s[1])>int(s[3])):
          d[s[0]][1]+=1
          d[s[0]][4]+=3
      elif (int(s[1])==int(s[3])):
          d[s[0]][2]+=1
          d[s[0]][4]+=1
      else: d[s[0]][3]+=1
    elif (s[0] not in d):
        if int(s[1])>int(s[3]):
            d[s[0]]=[1,1,0,0,3]
        elif int(s[1])==int(s[3]):
            d[s[0]]=[1,0,1,0,1]
        else: d[s[0]]=[1,0,0,1,0]
    if (s[2] in d):
      d[s[2]][0]+=1
      if (int(s[3])>int(s[1])):
          d[s[2]][1]+=1
          d[s[2]][4]+=3
      elif (int(s[1])==int(s[3])):
          d[s[2]][2]+=1
          d[s[2]][4]+=1
      else: d[s[2]][3]+=1
    elif (s[2] not in d):
        if int(s[3])>int(s[1]):
            d[s[2]]=[1,1,0,0,3]
        elif int(s[1])==int(s[3]):
            d[s[2]]=[1,0,1,0,1]
        else: d[s[2]]=[1,0,0,1,0]
for w in d:
    print(w+':',end='')
    print(str(d[w][0])+' ',end='')
    print(str(d[w][1])+' ',end='')
    print(str(d[w][2])+' ',end='')
    print(str(d[w][3])+' ',end='')
    print(d[w][4])