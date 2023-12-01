from calculate_ray_direction import calculate_ray_direction
from hex_to_rgb import hex_to_rgb
from is_shadowed import is_shadowed
from point import Point
from sphere import Sphere
from ray import Ray
# from color import color
from material import Material
from light import Light
from rgb_float import RGBFloat
from sphere import Sphere
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import Scale,colorchooser, Checkbutton, IntVar
from plane import Plane


# Define the image size
image_width = 800
image_height = 600

# Create an empty image with a white background
image = Image.new("RGB", (image_width, image_height), "white")


# Define eye, light, and sphere properties
eye = Point(0, 0, 0)



# Create light, sphere, and a ray from the eye to a point in the view plane
# light_position = Point(10, 10, 10)
# light_color = np.array([1, 1, 1])
# light_intensity = (1.8, 1.8, 1.8)  # White light with full intensity
# light = Light(light_position, light_color)




# Define a large sphere that will be the furthest away and act as the background object
large_sphere = Sphere(Point(0, 0, 20), 10, RGBFloat(0, 0, 1))

# Define a few smaller spheres in front of the large one
small_spheres = [
    Sphere(Point(1, 1, 10), 1, RGBFloat(1, 0, 0)),  # Red sphere
    Sphere(Point(-1, -1, 10), 1, RGBFloat(0, 1, 0)),  # Green sphere
    Sphere(Point(0, 0, 5), 1, RGBFloat(1, 1, 0)),  # Yellow sphere
    # Add more small spheres if needed
]

# objects = [
#     Sphere(Point(0, 0, 10), 1, RGBFloat(1, 0, 0)),
#     Sphere(Point(2, 0, 8), 1, RGBFloat(0, 1, 0)),
#     Sphere(Point(-2, 0, 12), 5, RGBFloat(0, 0, 1)),
#     # Add more objects if needed
# ]
# Combine all objects into one list, with the large sphere at the end
# The rendering loop will check objects in the order they appear in the list,
# so you want to check for intersections with the smaller spheres first.
objects = small_spheres + [large_sphere]



ray_direction = Point(0, 0, 1) - eye
ray = Ray(eye, ray_direction)

# # Scene setup
# ground_plane = Plane(Point(0, -1, 0), Point(0, 1, 0), RGBFloat(0.5, 0.5, 0.5))  # Example ground plane

# # Add the ground plane to the list of objects
# objects.append(ground_plane)






def shadow_color(intersection_point, obj, light, darkening_factor=0.5):
    """
    Calculate the shadow color for an object at the given intersection point.
    
    :param intersection_point: The point at which the object is intersected by a ray.
    :param obj: The object that is intersected by the ray.
    :param light: The light source object.
    :param darkening_factor: The factor by which the color is darkened (0-1 range).
    :return: A tuple representing the RGB color of the object in shadow.
    """
    # Get the color from the object's shading method
    original_color = obj.shade(intersection_point, light)
    
    # Convert the original color to a NumPy array if it's not already
    if isinstance(original_color, tuple):
        original_color = np.array(original_color)

    # Ensure darkening_factor is within the correct range
    darkening_factor = np.clip(darkening_factor, 0, 1)
    
    # Darken the color by the darkening factor
    shadowed_color = original_color * darkening_factor
    
    # Ensure the resulting color is in the valid range [0, 255]
    shadowed_color = np.clip(shadowed_color, 0, 255).astype(int)
    
    # Return the color as a tuple
    return tuple(shadowed_color)



# def reflect(ray_direction, normal):
#     return ray_direction - normal * 2 * ray_direction.dot(normal)

# def refract(ray_direction, normal, eta):
#     d_n = ray_direction.dot(normal)
#     k = 1 - eta**2 * (1 - d_n**2)
#     if k < 0:
#         return None  # Total internal reflection
#     return ray_direction * eta - normal * (eta * d_n + math.sqrt(k))

# # Check intersection
# hit, dist = sphere.intersect(ray)
# if hit:
#     intersection_point = ray.origin + ray.direction * dist
#     color = sphere.shade(intersection_point, light)
#     # Convert color to a format suitable for Pillow (0-255 range)
#     pil_color = tuple((np.clip(color, 0, 1) * 255).astype(int))
#     print(f"Intersection color: {pil_color}")

#     # Draw the color at a specific pixel (example: center of the image)
#     image.putpixel((image_width // 2, image_height // 2), pil_color)
# else:
#     print("No intersection detected.")

# # Save or show the image
# image.save("output.png")
# image.show()
# Loop through each pixel

def render_scene(hex_background_color, light_intensity,light_position, include_ground):
    light = Light(light_position, light_intensity)

    # Convert the hex background color to an RGB tuple
    background_color = hex_to_rgb(hex_background_color)
    print(f"Rendering scene with background color: {background_color}")
    # Assuming a supersample level of 2 for 4 samples per pixel
    supersample_level = 2
    # Create an empty image with the selected background color
    image = Image.new("RGB", (image_width, image_height), background_color)
    # print(f"Rendering scene with background color: {background_color}")
    # Scene setup
    if include_ground:
        ground_plane = Plane(Point(0, -1, 0), Point(0, 1, 0), RGBFloat(0.5, 0.5, 0.5))  # Example ground plane
        objects.append(ground_plane)

# Define the number of samples for supersampling (e.g., 2x2 grid)
    for x in range(image_width):
        for y in range(image_height):
            # Calculate ray direction for the current pixel
            ray_direction = calculate_ray_direction(eye, x, y, image_width, image_height)
            ray = Ray(eye, ray_direction)

            print(f"Ray direction: {ray_direction}")

            # Initialize the closest intersection distance and color
            closest_intersection = float('inf')
            # Background color
            # pixel_color = (255, 255, 255)
            pixel_color = background_color
            # Default background color
            # Check for intersections with all objects
            for obj in objects:
                
                hit, distance = obj.intersect(ray)
                if hit and distance < closest_intersection:
                    closest_intersection = distance
                    intersection_point = ray.point_at_parameter(distance)
                    # print(intersection_point)
                    # pixel_color = obj.shade(intersection_point, light)
                    # if isinstance(obj, Plane):
                    # # Handle plane shading
                    #     # Handle plane shading, this could be a simple uniform color or a more complex texture
                    #     # For now, let's just use a uniform gray color as an example
                    #     pixel_color = (100, 100, 100)  # Example gray color for the plane

                    if isinstance(obj, Plane):
                        pixel_color = obj.supersample_intersect(ray, supersample_level,light)
    
                    else:
                    # Make sure pixel_color is a tuple before setting it
                       
                        if not is_shadowed(intersection_point, light.position, objects):
                            pixel_color = obj.shade(intersection_point, light)
                        else:
                        # If it's in shadow, possibly darken the color or set it to shadow color
                            pixel_color = shadow_color(intersection_point, obj,light)
                        
                        if not isinstance(pixel_color, tuple):
                                pixel_color = tuple(pixel_color)
                # Set the pixel color

            image.putpixel((x, y), pixel_color)  # pixel_color should already be a tuple

    # Save or display the image
    image.save("rendered_scene.png")
    image.show()

def ask_color():
    # Ask the user for a color
    color_code = colorchooser.askcolor(title ="Choose color")[1]
    return color_code if color_code else "#000000"  # Default to black if no color is selected



def on_render_click():
    background_color = ask_color()
    r_intensity = r_scale.get() / 100.0
    g_intensity = g_scale.get() / 100.0
    b_intensity = b_scale.get() / 100.0
    x_pos = x_scale.get()
    y_pos = y_scale.get()
    z_pos = z_scale.get()
    light_position = Point(x_pos, y_pos, z_pos)
    light_intensity = (r_intensity, g_intensity, b_intensity)
    include_ground = bool(include_ground_var.get())
    render_scene(background_color, light_intensity, light_position, include_ground)


# GUI to select background color
root = tk.Tk()
root.title("Ray Tracing Configuration")

# Sliders for light intensity
r_scale = Scale(root, from_=0, to=200, orient="horizontal", label="Red Intensity")
r_scale.set(100)  # Default value
r_scale.pack()

g_scale = Scale(root, from_=0, to=200, orient="horizontal", label="Green Intensity")
g_scale.set(100)  # Default value
g_scale.pack()

b_scale = Scale(root, from_=0, to=200, orient="horizontal", label="Blue Intensity")
b_scale.set(100)  # Default value
b_scale.pack()

# Sliders for light position
x_scale = Scale(root, from_=-20, to=20, orient="horizontal", label="Light X Position")
x_scale.set(10)
x_scale.pack()

y_scale = Scale(root, from_=-20, to=20, orient="horizontal", label="Light Y Position")
y_scale.set(10)
y_scale.pack()

z_scale = Scale(root, from_=-20, to=20, orient="horizontal", label="Light Z Position")
z_scale.set(10)
z_scale.pack()

# Checkbox for including ground plane
include_ground_var = IntVar()
include_ground_checkbox = Checkbutton(root, text="Include Ground Plane", variable=include_ground_var)
include_ground_checkbox.pack()


render_button = tk.Button(root, text="Render Scene", command=on_render_click)
render_button.pack(pady=20)

root.mainloop()


