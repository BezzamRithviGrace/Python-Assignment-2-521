PROGRAM1
import math 
def getdividsors(num):
 n=math.ceil(math.sqrt(num))
 total=1
 divisor=2
 while(divisor<n):
  if (num%divisor==0):
    total+=divisor
    total+=num//divisor
  divisor+=1
 return total
n=int(input("enter the number:"))
print("1 is deficient number and sum is 0")
for i in range (2,n+1):
 t=getdividsors (i)
 if(t==i):
   print (i,"is perfect number and sum is",t)
 elif(t<i):
   print (i,"is deficient number and sum is",t)
 else:
  print(i,"is abundant number and sum is",t)
PROGRAM8
lst=[[1,2,6],[1,3,4,5,7,8],[1,3,5,6,8,9],[1,5,7,11],[1,4,7,5,8,12]]
nw_lst=[]
q=[]
nk=[]
nr=[]
dic={}
for i in lst:
  for j in i:
    nw_lst.append(j)
nw_lst.sort()   
for i in nw_lst :
 x=nw_lst.count(i)
 dic.update({i:x})
q=list(dic.values())
q.sort()
for i in range(8,11):
 for k in dic.keys():
  if (dic[k]==q[i]):
   nk.append(k)
   nr.append(q[i])
   break
print(nk[::-1])
print(nr[::-1])
PROGRAM7
import  string
import random
def getRandomLowerCaseLetter():
	var1=string.ascii_letters.lower()
	chars=[]
	for i  in range(0,100):
		chars.append(random.choice(var1))
	return (chars)
import RandomCharacterModule
chars=RandomCharacterModule.getRandomLowerCaseLetter()
print('list chars with random characters')
print(chars)
counts=[]
def countX(chars,x):
	count=0
	for ele in chars:
		if(ele==x):
	   	 count=count+1
	return count
	
	
for i in range(97,123):
	counts.append(countX(chars,chr(i)))
print('counts for each character in list chars is:\n',counts)
