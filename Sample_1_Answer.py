import math 

step = int(input("Enter the step travel by beatel"));
point = input("Enter the step travel by beatel");
points = point.split(',');
k = 0;

for i in range(step-1):
	if (points[(i*3)]==points[((i+1)*3)] == '0' or points[(i*3)+1]==points[((i+1)*3)+1] == '0' or points[(i*3)+2]==points[((i+1)*3)+2] == '0' or points[(i*3)]==points[((i+1)*3)] == '10' or points[(i*3)+1]==points[((i+1)*3)+1] == '10' or points[(i*3)+2]==points[((i+1)*3)+2] == '10' ) : 
		y = math.floor( (int(points[(i*3)]) - int(points[((i+1)*3)]))**2 + (int(points[(i*3)+1]) - int(points[((i+1)*3)+1]))**2 + (int(points[(i*3)+2]) - int(points[((i+1)*3)+2]))**2 ) ; 
		y = y**0.5;
		y = math.ceil(y);
		y = y*(math.pi/3);
		k = k + y;
	else :
		y = math.floor( (int(points[(i*3)]) - int(points[((i+1)*3)]))**2 + (int(points[(i*3)+1]) - int(points[((i+1)*3)+1]))**2 + (int(points[(i*3)+2]) - int(points[((i+1)*3+2)]))**2 );
		y = y**0.5;
		y = math.ceil(y);
		k = k + y;
		

print("%.2f"%k);
