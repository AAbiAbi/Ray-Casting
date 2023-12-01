def reflect(ray_direction, normal):
    return ray_direction - normal * 2 * ray_direction.dot(normal)
