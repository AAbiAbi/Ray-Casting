# Ray-Casting
implement ray casting algorithm
In this assignment, you will implement ray casting algorithm. 
Follow the lecture content, write a program to generate the ray casting result.
The objects in the scene are spheres.
You need to define in your program: 

```
the light source intensity (R, G, B),  
light source location (Lx, Ly, Lz),  
eye location (Ex, Ey, Ez),  
one plane and at least 2 spheres 
location/radius of spheres,  
surface property (K value in the lighting model), view plane size/location (perpendicular to z axis)
```
Your result should be showing 2 shaded spheres (or more), with one sphere casting a shadow on the other a ( after your program works, just change the sphere location or light location to get shadow)

Extra credit:   
- Ground plane. with sphere shadows on it   
- Reflection and refraction.    
- Environment map
A diagram image is provided for your reference.

Write comment to explain your code. submit program code and result image.
## Algorithm
- Setting up a view plane: The image shows a grid that represents the view plane (the screen), the eye (the viewer's point), and the light source. The axes X, Y, and 
Z define the 3D space.

- Ray casting: A ray is cast from the eye through each pixel on the screen.

- Intersection checks: For each ray, the algorithm checks for intersections with objects in the scene. This is done in the nested loop using two variables i and j which iterate over the window height (i<win_height) and window width (j<win_width), respectively.

- Color calculation: Once the closest intersection point of the ray with an object is found, the color at that point is calculated using a lighting model. The lighting model typically takes into account various factors such as the light's intensity, the material of the object, and the angle at which the light hits the object.

- Rendering: The color calculated is then used to render the pixel on the 2D screen.

![Alt text](image/alg1.png?raw=true "alg1")

![Alt text](image/alg2.png?raw=true "alg2")
![Alt text](image/alg3.png?raw=true "alg2")

### Features

- **Ray-Sphere Intersection**: Calculate intersections of rays with sphere objects to render solid spheres.
- **Ray-Plane Intersection**: Handle intersections with plane objects to create flat surfaces.
- **Shading**: Implement a simple lighting model with diffuse and specular shading.
- **Shadows**: Determine if points are in shadow and shade them accordingly.
- **Reflection**: Calculate reflection rays for reflective surfaces to create mirror-like effects.
- **Refraction**: Handle transparency and refraction for glass-like materials.
- **Anti-Aliasing**: Utilize supersampling anti-aliasing for smoother edges.



## Initializtion

You can try two different ray-casting function. main.py and reflection.py

commands like:
``` bash
/Users/a25076/bin/python3 /Users/a25076/Desktop/290/assignment4/Ray-Casting/reflection.py
```

``` bash
/Users/a25076/bin/python3 /Users/a25076/Desktop/290/assignment4/Ray-Casting/main.py
```
### Configration

To run the ray tracer, you need Python 3.10 and the following libraries:
- NumPy
- Pillow (PIL)

Install the required packages using pip:

### GUI Usage

Run the main script to launch the GUI configuration window:
![Alt text](image/gui1.png?raw=true "alg2")
![Alt text](image/gui2.png?raw=true "alg2")
From the GUI, you can:
- Select the background color for the scene.
- Adjust the light intensity and position.
- Choose whether to include a ground plane in the scene.

After configuring the settings, click the "Render Scene" button to generate the image. The rendered scene will be displayed and saved as `rendered_scene.png` in the script's directory.

### Scene Configuration

The scene is composed of spheres and an optional ground plane. You can define the properties of these objects, such as position, color, reflectivity, and transparency, within the script. The light source's properties can also be adjusted.
![Alt text](image/dc1.png?raw=true "alg2")
![Alt text](image/dc2.png?raw=true "alg2")
![Alt text](image/dc3.png?raw=true "alg2")


Also you can adjust the intensity of light.The intensity values are normalized within the ray tracing calculations, so values above 100 may result in brighter and more intense lighting effects.

Alternatively, you can directly modify the `light_intensity` tuple in the script if you prefer to set the intensity without using the GUI:
 
![Alt text](image/li1.png?raw=true "alg2")
![Alt text](image/li2.png?raw=true "alg2")

Besides, you can change the source of light.So you can see the shadow shown in different angles.

![Alt text](image/lp1.png?raw=true "alg2")
![Alt text](image/lp2.png?raw=true "alg2")



### Extendability

The script is modular, allowing for easy addition of new geometric primitives, materials, and more complex lighting models.

## Result


Ground shadow: When you put the light behind the sphere, you will notice that there is a huge shadow on the groundplane.

![Alt text](image/gs.png?raw=true "alg2")

Refract and reflection:
![Alt text](image/rr.png?raw=true "alg2")

## Contributer

Ningchen Liang: ningchenliang98@gmail.com


