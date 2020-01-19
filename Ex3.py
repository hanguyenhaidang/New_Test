with open('Ex3_input.txt','r') as f:
	fn=f.readlines();
	print(fn);
f.close();
def FileAnalyzer(n):
	lines = len(n);
	words=0;
	characters=0;
	print('Lines:',lines);
	for i in range(len(n)):
		for k in range(0,len(n[i])):
			t=n[i][k];
			if(t==' '): words+=1;
			if(t!='\n'): characters+=1;
	print('words:',words+1);
	print('characters:',characters);
FileAnalyzer(fn);