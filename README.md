Duplicate Outline Object - Blender Add-on
This Blender add-on allows users to duplicate an object and automatically create an outline for it using the Solidify modifier. It also applies the Surface Deform modifier, binding the outline to the original object for deformation. This is particularly useful for creating stylized outlines or other effects in Blender.

Features
Duplicate an existing object in the scene.
Add an Outline using the Solidify modifier.
Set up and bind the Surface Deform modifier to link the duplicated outline with the original object.
Automatically create a custom outline material with backface culling enabled.
Requirements
Blender 3.1 or newer.
Installation
Download the duplicate_outline_object.py file from this repository.
Open Blender.
Go to Edit > Preferences > Add-ons.
Click the Install button at the top and navigate to where you downloaded duplicate_outline_object.py.
Select the file and click Install Add-on.
Check the box next to the add-on's name to enable it.
How to Use
In the 3D Viewport, select an object that you want to duplicate and outline.
Go to the Object menu in the top bar of the 3D Viewport.
Select Duplicate Outline Object.
A new object will be created with an outline based on the original object, and a custom outline material will be applied.
Example
Select any mesh object, such as a cube or sphere.
From the Object menu, choose Duplicate Outline Object.
The add-on will create a duplicate object with an outline and link it to the original mesh for deformation.
Customization
After using the add-on, you can adjust the outline's thickness by modifying the Solidify modifier on the duplicated object. You can also modify the material created for the outline by editing the material in the Materials tab of the Properties panel.

Troubleshooting
Ensure that you have selected an active object before running the add-on. If no object is selected, the add-on will not work and a warning will be displayed.
The add-on uses the Surface Deform modifier, which requires the original object to remain in the scene for the outline to follow any deformations.
License
This add-on is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to fork this repository and submit pull requests with any improvements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.

Author
Created by oki75.