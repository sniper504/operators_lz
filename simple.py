input_data = open('input.txt','r') 
a = input_data.read()
a=int(a)
k=0
for i in range(2,a):
    if a%i==0:
        k+=1
if k==0:
    output_data = open('output.txt','w')
    output_data.write('Y')
else:
    output_data = open('output.txt','w')
    output_data.write('N')
input_data.close()
output_data.close()
