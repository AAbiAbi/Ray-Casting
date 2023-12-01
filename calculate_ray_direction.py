import numpy as np
from point import Point

def calculate_ray_direction(eye, pixel_x, pixel_y, image_width, image_height, fov=90):
    """
    Calculate the direction of a ray from the eye through a pixel on the view plane.
    
    :param eye: The eye (camera) position as a Point object.
    :param pixel_x: The x-coordinate of the pixel.
    :param pixel_y: The y-coordinate of the pixel.
    :param image_width: The width of the image (view plane).
    :param image_height: The height of the image (view plane).
    :param fov: The field of view in degrees.
    :return: A normalized direction vector as a Point object.
    """
    # Convert field of view to radians for calculations
    fov_rad = np.radians(fov)
    
    # Calculate the width and height of the view plane
    aspect_ratio = image_width / image_height
    view_height = 2 * np.tan(fov_rad / 2)
    view_width = view_height * aspect_ratio
    
    # Calculate the pixel size
    pixel_size_x = view_width / image_width
    pixel_size_y = view_height / image_height
    
    # Calculate the position of the pixel on the view plane
    # in view plane coordinates where (0, 0) is the center of the view plane
    view_plane_x = (pixel_x - image_width / 2) * pixel_size_x
    view_plane_y = -(pixel_y - image_height / 2) * pixel_size_y  # Negative because pixel coordinates are top-down
    
    # Calculate the direction from the eye to the pixel on the view plane
    direction = Point(view_plane_x, view_plane_y, 1) - eye
    
    # Normalize the direction
    direction = direction.normalize()
    
    return direction
