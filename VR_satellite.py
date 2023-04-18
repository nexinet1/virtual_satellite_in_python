import math

# define the initial conditions of the satellite
x = 0.0   # initial position (m)
y = 0.0   # initial position (m)
vx = 100.0  # initial velocity (m/s)
vy = 0.0   # initial velocity (m/s)
dt = 0.1  # time step (s)

# simulate the motion of the satellite for 100 seconds
for t in range(0, 1000):
    # calculate the new position of the satellite using kinematics equations
    x = x + vx * dt
    y = y + vy * dt
    
    # calculate the new velocity of the satellite using the acceleration due to gravity
    g = 9.81  # acceleration due to gravity (m/s^2)
    ax = 0.0  # no acceleration in x direction
    ay = -g   # acceleration in y direction due to gravity
    vx = vx + ax * dt
    vy = vy + ay * dt
    
    # print the current position and velocity of the satellite
    print("t = %.1f s, x = %.2f m, y = %.2f m, vx = %.2f m/s, vy = %.2f m/s" % (t*dt, x, y, vx, vy))
