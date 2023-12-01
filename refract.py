import numpy as np
# def refract(ray_direction, normal, eta):
#     cosi = -max(-1, min(1, ray_direction.dot(normal)))
#     etai = 1
#     etat = eta
#     if cosi < 0:
#         cosi = -cosi
#         etai, etat = etat, etai
#         normal = -normal
#     eta = etai / etat
#     k = 1 - eta * eta * (1 - cosi * cosi)
#     if k < 0:
#         return None
#     else:
#         return eta * ray_direction + (eta * cosi - np.sqrt(k)) * normal
    
    # def refract(ray_direction, normal, eta):
    # cosi = -max(-1, min(1, ray_direction.dot(normal)))
    # k = 1 - eta**2 * (1 - cosi**2)
    # if k < 0:
    #     return None  # Total internal reflection
    # else:
    #     return eta * ray_direction + (eta * cosi - np.sqrt(k)) * normal

def refract(incoming_ray_direction, normal, index_of_refraction_ratio):
    # Convert Point to numpy array if not already
    if not isinstance(incoming_ray_direction, np.ndarray):
        incoming_ray_direction = np.array([incoming_ray_direction.x, incoming_ray_direction.y, incoming_ray_direction.z])
    if not isinstance(normal, np.ndarray):
        normal = np.array([normal.x, normal.y, normal.z])

    # Normalize the vectors to be safe
    incoming_ray_direction = incoming_ray_direction / np.linalg.norm(incoming_ray_direction)
    normal = normal / np.linalg.norm(normal)

    # Assumes incoming_ray_direction and normal are numpy arrays and normalized
    cos_theta = -np.dot(normal, incoming_ray_direction)
    sin_theta2 = index_of_refraction_ratio**2 * (1 - cos_theta**2)
    
    if sin_theta2 > 1:
        return None  # Total internal reflection
    
    cos_theta_t = np.sqrt(1 - sin_theta2)
    return index_of_refraction_ratio * incoming_ray_direction + (index_of_refraction_ratio * cos_theta - cos_theta_t) * normal
