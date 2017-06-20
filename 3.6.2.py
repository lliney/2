import requests
with open('dataset_3378_3.txt') as file1:
    txt=file1.read()
url1='https://stepic.org/media/attachments/course67/3.6.3/'
file2=requests.get((txt).strip())
#print(txt)
#print(file2.text)
#i=0
while True:
    #i+=1
    file2=requests.get((url1+file2.text).strip())
    #print(file2.text)
    j = [str(i) for i in file2.text.split()]
    #for k in j:
     #   print(k)
    if j[0] == 'We':
        print(file2.text)
        #print(i)
        break



