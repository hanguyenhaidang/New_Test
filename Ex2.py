def CozaLozaWoza(n):
	for i in range(1,n+1):
		if(i%3==0 and i%5==0 and i%7==0): print('CozaLozaWoza ',end='');
		elif(i%3==0 and i%5==0): print('CozaLoza ',end='');
		elif(i%3==0 and i%7==0): print('CozaWoza ',end='');
		elif(i%3==0): print('Coza ',end='');
		elif(i%5==0): print('Loza ',end='');
		elif(i%7==0): print('Woza ',end='');
		elif(i%11==0): print(i);
		else: print(i,'',end='');
n=int(input("Nhap n: "));
CozaLozaWoza(n)
		