# PillowWriter se GIF format me save karein
f = r"gradient_descent_cost.gif"
writergif = animation.PillowWriter(fps=2)

print("GIF saving in progress...")
anim.save(f, writer=writergif)
print(f"Animation successfully saved as '{f}'!")