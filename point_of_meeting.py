import math
class point:
   def __init__(self,x,y):
      self.x=x
      self.y=y
    

points=[]
num=int(raw_input());

for i in range(num):
   inp=raw_input().split();
   x=long(inp[0])
   y=long(inp[1])
   points.append(point(x,y))

ave_x=0.0
ave_y=0.0

for i in range(num):
   ave_x += points[i].x;
   ave_y += points[i].y;

ave_x /= num;
ave_y /= num;

print 'Average %s,%s' % (ave_x, ave_y)

diff_x = points[0].x - ave_x;
diff_y = points[0].y - ave_y;

best = 0;
best_dist = 10**30

for i in range(0,num):
   diff_x = points[i].x - ave_x;
   diff_y = points[i].y - ave_y;

   hold_dist = math.sqrt(abs(diff_x) ** 2 + abs(diff_y) ** 2)

   if hold_dist < best_dist:
      best_dist = hold_dist;
      best = i;
   
best_pt = points[best];
print best_pt.x, best_pt.y

total_dist = 0;

for i in range(0,num):
   diff_x = math.fabs(points[i].x-best_pt.x);
   diff_y = math.fabs(points[i].y-best_pt.y);
   total_dist += abs(diff_y - diff_x) + (diff_x % abs(diff_y - diff_x)) + (diff_y % abs(diff_y - diff_x))
   
print(int(total_dist));
