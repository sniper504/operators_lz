input_data = open('input.txt','r') 
n = input_data.read()
n=int(n)
k=0
while n > 0:
    if n%3==0:
        n-=3
        k+=1
    if n%3==1:
        n-=1
        k+=1
    if n%3==2:
        n-=2
        k+=1
output_data = open('output.txt','w')
output_data.write(str(k))
input_data.close()
output_data.close()
