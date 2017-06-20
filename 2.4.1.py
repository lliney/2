st = input()
st.upper()
i=0
for n  in st:
    if n=='C' or n=='G' or n=='c' or n=='g' :
        i += 1


print((i*100)/(len(st)))