from point import Point
from ray import Ray
from rgb_float import RGBFloat
from light import Light
import numpy as np


class Plane:
    def __init__(self, point, normal, color):
        self.point = point
        self.normal = normal.normalize()
        self.color = color

    def intersect(self, ray):
        # Calculate denominator to check if ray is parallel to the plane
        denom = self.normal.dot(ray.direction)
        if abs(denom) > 1e-6: # The threshold for considering the ray and the plane not parallel
            # The vector from a point on the ray (origin) to a point on the plane
            p0l0 = self.point - ray.origin
            # Calculate t, the distance along the ray at which it intersects the plane
            t = p0l0.dot(self.normal) / denom
            if t >= 0: # If t is positive, there's an intersection
                # Calculate the exact point of intersection
                
                return True, t
        # If the ray is parallel to the plane or the intersection is behind the ray's origin
        return False, None
    
    def shade(self, intersection_point, light):
        # The light vector points from the intersection point to the light source
        light_vector = (light.position - intersection_point).normalize()
        
        # The diffuse component is the dot product of the light vector and the plane's normal,
        # clamped to the range [0, 1]
        diffuse = max(self.normal.dot(light_vector), 0)
        
        # The color of the plane is modulated by the diffuse component and the light's color
        # Assuming light.color is an RGBFloat or has 'r', 'g', 'b' attributes
        light_intensity_np = np.array(light.intensity)
        shaded_color = RGBFloat(self.color.r * light_intensity_np[0] * diffuse,
                                self.color.g * light_intensity_np[1] * diffuse,
                                self.color.b * light_intensity_np[2] * diffuse)
       
        
        # Convert the shaded color to a tuple with values scaled between 0 and 255
        return (int(shaded_color.r * 255), int(shaded_color.g * 255), int(shaded_color.b * 255))
    
    def supersample_intersect(self, ray, supersample_level,light):
        """
        Perform supersampling to compute anti-aliased color for the plane.
        
        :param ray: The initial ray from the camera to the pixel.
        :param supersample_level: The square root of number of samples per pixel.
        :return: The average color computed from all samples.
        """
        step = 1.0 / supersample_level
        color_accumulator = RGBFloat(200, 200, 200)
        samples = supersample_level ** 2

        for dx in np.linspace(-0.5, 0.5, supersample_level, endpoint=False):
            for dy in np.linspace(-0.5, 0.5, supersample_level, endpoint=False):
                # Adjust the ray direction for supersampling
                supersample_ray = Ray(ray.origin, ray.direction + Point(dx * step, dy * step, 0))
                hit, t = self.intersect(supersample_ray)
                if hit:
                    intersection_point = supersample_ray.point_at_parameter(t)
                    shade_color_tuple = self.shade(intersection_point, light)
                    # Convert the tuple to RGBFloat before adding
                    shade_color = RGBFloat(*shade_color_tuple)
                    color_accumulator += shade_color
        # Average the accumulated color
        averaged_color = color_accumulator / samples
        return (int(averaged_color.r * 255), int(averaged_color.g * 255), int(averaged_color.b * 255))
    