from point import Point
from ray import Ray
from rgb_float import RGBFloat



import numpy as np

class Sphere2:
    def __init__(self, center = None, radius=1.0, color=None, reflectivity=0.0, transparency=0.0, refractive_index=1.0):

        self.center = center if center is not None else Point()
        self.radius = radius
        self.color = color if color is not None else RGBFloat(0.0, 0.0, 0.0)
        self.reflectivity = reflectivity
        self.transparency = transparency
        self.refractive_index = refractive_index

    # Check for an intersection with the ray
    def intersect(self, ray):

        # Convert Point to numpy array
        ray_origin = np.array([ray.origin.x, ray.origin.y, ray.origin.z])
        ray_direction = np.array([ray.direction.x, ray.direction.y, ray.direction.z])
        sphere_center = np.array([self.center.x, self.center.y, self.center.z])

        # Vector from ray origin to sphere center
        oc = ray_origin - sphere_center
        # print("oc: ", oc)
        a = np.dot(ray_direction, ray_direction)
        # print("a: ", a)
        b = 2.0 * np.dot(oc, ray_direction)
        # print("b: ", b)
        c = np.dot(oc, oc) - self.radius * self.radius
        # print("c: ", c)
        discriminant = b*b - 4*a*c
        # print("discriminant: ", discriminant)
        
        if discriminant < 0:
            return False, None  # No intersection
        else:
            # Return the distance to the intersection
            dist = (-b - np.sqrt(discriminant)) / (2.0 * a)
            if dist < 0:
                # return None  # Intersection behind the ray origin
                return False, None  # Intersection behind the ray origin
            return True, dist
        
    def shade(self,intersection_point, light):
           # No need to call to_np() if it's already a numpy array
        # light_position_np = light.position  # Assuming light.position is a numpy array
        intersection_point_np = np.array([intersection_point.x, intersection_point.y, intersection_point.z])
        
        # Calculate normal
        normal_np = intersection_point_np - np.array([self.center.x, self.center.y, self.center.z])
        
        normal_np = normal_np / np.linalg.norm(normal_np)  # Normalize
        # Light direction
        light_position_np = light.position.to_np()
        light_dir_np = light_position_np - intersection_point_np
        # light_dir = light.position - intersection_point
        light_dir_np = light_dir_np / np.linalg.norm(light_dir_np)
        # light_dir = light_dir / np.linalg.norm(light_dir)
         # Assuming self.color is a RGBFloat object with 'r', 'g', 'b' attributes
    # Convert self.color to a NumPy array for the calculation

        # Calculate the light color at the intersection point
        # Assuming `self.color` is the inherent color of the sphere
        # and is also an RGB tuple like (R, G, B)
        light_intensity_np = np.array(light.intensity)
        # sphere_color_np = np.array(self.color)
        
        # Calculate diffuse shading using the dot product, etc.
        diffuse_intensity = max(np.dot(normal_np, light_dir_np), 0)
    
        color_np = np.array([self.color.r, self.color.g, self.color.b])
         # Diffuse shading
        # diffuse = max(np.dot(normal, light_dir), 0)
        diffuse = max(np.dot(normal_np, light_dir_np), 0)
        # diffuse_color = np.array(self.color) * light.color * diffuse
        # Assuming light.color is a NumPy array
        # diffuse_color = color_np * light.color * diffuse
        rgb_color = color_np * light_intensity_np * diffuse

        # Clamp and convert to an integer tuple for RGB
        clamped_color = np.clip(rgb_color, 0, 1)
        rgb_color = tuple((clamped_color * 255).astype(int))

        return rgb_color

        # # Ensure the resulting color is in the valid range [0, 1] and convert to [0, 255]
        # clamped_color = np.clip(diffuse_color, 0, 1)
        # rgb_color = tuple((clamped_color * 255).astype(int))
        

        # # return diffuse_color
        # return rgb_color  # Return a tuple of integers
        # # Ensure the resulting color is in the valid range [0, 255] for each channel
        # diffuse_color = np.clip(diffuse_color, 0, 255).astype(int)
        
        # return tuple(diffuse_color)
    def normal_at(self, point):
        # Calculate the normal vector at a point on the surface of the sphere
        # The normal vector is the normalized vector from the center of the sphere to the point
        object_to_point = point - self.center
        normal = object_to_point.normalize()  # Assuming there is a normalize method
        return normal