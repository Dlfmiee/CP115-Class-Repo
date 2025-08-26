import physics_constants
import math

# physics_constants.Standard_gravity , physics_constants.Ball_mass , physics_constants.Building_height , physics_constants.Initial_velocity
time = 2

Position = (physics_constants.Building_height + physics_constants.Initial_velocity )*time - (physics_constants.Ball_mass*physics_constants.Standard_gravity * (time*time))
Velocity = physics_constants.Initial_velocity - (physics_constants.Standard_gravity*time)
Kinetic = 0.5 * physics_constants.Ball_mass * (physics_constants.Initial_velocity*physics_constants.Initial_velocity)

print (f"Ball Position : {Position}")
print (f"Velocity : {Velocity}")
print (f"Kinetic Energy : {Kinetic}")
print (f"Motion Status : Moving Down")