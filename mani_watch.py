def calcAngle(h,m): 
		if (h < 0 or m < 0 or h > 12 or m > 60): return -1
		if (h == 12): 
			h = 0
		if (m == 60): 
			m = 0
			h += 1; 
			if(h>12): 
				h = h-12; 
		hour_angle = 0.5 * (h * 60 + m) 
		minute_angle = 6 * m 
		angle = abs(hour_angle - minute_angle) 
		angle = min(360 - angle, angle) 
		return angle 
h,m = map(int,input().split())
if(int(calcAngle(h,m))==-1):
  print(-1)
else:
  print(int(calcAngle(h,m)))
