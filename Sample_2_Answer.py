x = input("enter the number of boxes and position of haviest box");
x = x.split(" ");
nb = int(x[0]);
bp = int(x[1]);
y = input("enter weigths");
y = y.split(" ");
for i in range(len(y)):
	y[i] = int(y[i]);
t = y[:];
t.sort();
for i in range(bp,nb+1):
	z = t[i-1];
	t[i-1] = t[nb-1];
	t[nb-1] = z;
k = 0;
for i in range(nb-1):
	if(y[i] == t[i]):
		continue;
	
	else : 
		check1 = y[i]*t[i];
		if(y[i]>t[i]):
			check2 = t[i]*t[0] + t[0]*y[i] + t[0]*t[i];
		else:
			check2 = y[i]*t[0] + t[0]*t[i] + t[0]*y[i];
		if (check1 > check2):
			k = k + check2;
		else:
			k = k + check1;
		z = y[i];
		y[i] = t[i];
		y[t.index(z)] = z;
print(k);