import matplotlib.pyplot as plt

def calculate_triangle_area(p1, p2, p3):
    # Calculate the vectors between the points
    v1 = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
    v2 = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])

    print(v1,v2)
    # Calculate the cross product of the vectors
    cross_product = (
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    )

    # Calculate the magnitude of the cross product
    magnitude = (cross_product[0]**2 + cross_product[1]**2 + cross_product[2]**2) ** 0.5

    # Calculate the area of the triangle
    area = 0.5 * magnitude

    return area

# Define the points
p1 = (5, 17, 43)
p2 = (7, 2, 0)
p3 = (1, 0, 13)

# Calculate the area of the triangle
triangle_area = calculate_triangle_area(p1, p2, p3)
print("Area of the triangle:", triangle_area)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(*p1, color='r', label='Point 1')
ax.scatter(*p2, color='g', label='Point 2')
ax.scatter(*p3, color='b', label='Point 3')

# Plot the triangle
ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'r-')
ax.plot([p1[0], p3[0]], [p1[1], p3[1]], [p1[2], p3[2]], 'g-')
ax.plot([p2[0], p3[0]], [p2[1], p3[1]], [p2[2], p3[2]], 'b-')

# Create the triangular surface plot
ax.plot_trisurf([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], [p1[2], p2[2], p3[2]], triangles=[[0, 1, 2]], shade=True, color='grey')


# Set labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Set title and display the area
ax.set_title('Triangle Area: {:.2f}'.format(triangle_area))

# Show the plot
plt.show()

