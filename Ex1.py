def SquareBroard(n):
	result = '';
	for i in range(n):
		for j in range(n):
			result += '#';
		result += '\n';
	return result;
n=int(input('Nhap N: '));
with open('Ex1.txt', 'w') as f:
	f.write(str(SquareBroard(n)));
f.close();
print("Result in file.txt")
SquareBroard(n);
