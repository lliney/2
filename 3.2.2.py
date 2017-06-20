# put your python code here
st = input().lower().split()
d={i:st.count(i) for i in st }
for key,value in d.items():
    print(key,value)