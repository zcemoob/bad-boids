"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

# boids_x=[random.uniform(-450,50.0) for x in range(50)]
# boids_y=[random.uniform(300.0,600.0) for x in range(50)]
# boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
# boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
# tries
#[boids_x, boids_y]=[[random.uniform(-450,50.0), random.uniform(300.0,600.0)] for x in range(50)]
#[boids_x, boids_y]=[[random.uniform(-450,50.0), random.uniform(300.0,600.0)] for x, y in range(50)]
n = 50
[boids_x, boids_y] = [[random.uniform(-450,50.0) for x in range(n)], [random.uniform(300.0,600.0) for x in range(n)]]
[boid_x_velocities, boid_y_velocities] = [[random.uniform(0,10.0) for x in range(n)], [random.uniform(-20.0,20.0) for x in range(n)]]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
	xs,ys,xvs,yvs=boids
	a = 0.01
	b = 0.125

	# Fly towards the middle
	# for i in range(len(xs)):
	# 	for j in range(len(xs)):
	# 		xvs[i]=xvs[i]+(xs[j]-xs[i])*a/len(xs)
	# for i in range(len(xs)):
	# 	for j in range(len(xs)):
	# 		yvs[i]=yvs[i]+(ys[j]-ys[i])*a/len(xs)
	
	def set_range(val_s, val_vs):
		for i in range(len(xs)):
			for j in range(len(val_s)):
				val_vs[i] = val_vs[i] + (val_s[j] - val_s[i])*a/len(xs)
				    
	set_range(xs, xvs)
	set_range(xs, xvs)
	


	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])

	# Try to match speed with nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*b/len(xs)
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*b/len(xs)

	# Move according to velocities
	for i in range(len(xs)):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))  #replace -500(c), 1500(d) ?
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(list(zip(boids[0],boids[1])))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50) #replace 50(n or e?)..at all?

if __name__ == "__main__":
    plt.show()
