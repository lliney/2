import requests
with open('dataset_3378_2.txt') as file1:
    url1=file1.read()
file2=requests.get(url1.strip())
a=(file2.text)
i=0
for j in a.splitlines():
    i+=1
print(i)

