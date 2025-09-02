import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# X values manually
x = [i * 0.05 for i in range(200)]

# Create figure and axis
fig, ax = plt.subplots()
line, = ax.plot(x, [math.sin(i) for i in x])
ax.set_xlim(0, max(x))
ax.set_ylim(-1.1, 1.1)
ax.set_title("Saya pun taktau")

# Update function for animation
def update(frame):
    y = [math.sin(i + frame * 0.1) for i in x]
    line.set_ydata(y)
    return (line,)

# Animate
anim = FuncAnimation(fig, update, frames=120, interval=50, blit=True)

# Save as GIF
anim.save("animated_sine_wave.gif", writer=PillowWriter(fps=60))

plt.show()
