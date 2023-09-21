import blenderproc as bproc
import argparse
import os
import glob
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--camera', nargs='?', default="/home/au321555/Thesis/code/data-synthesis/resources/camera_positions", help="Path to the camera file")
parser.add_argument('-obj', '--obj_files', nargs='?', default="/home/au321555/Thesis/code/data-synthesis/object_files", help="Path to the stored .obj file")
parser.add_argument('-o', '--output_dir', nargs='?', default="/home/rushabh/Thesis/code/data-synthesis/output/", help="Path to where the final files will be saved ")
parser.add_argument('-n', '--no_of_frames', type=int, default=5, required=False, help="Number of images to be generated for each object")
args = parser.parse_args()

def add_key_frame(frame=0):

    # read the camera positions file and convert into homogeneous camera-world transformation
        with open(args.camera, "r") as f:
            for line in f.readlines():
                line = [float(x) for x in line.split()]
                position, euler_rotation = line[:3], line[3:6]
                matrix_world = bproc.math.build_transformation_mat(position, euler_rotation)
                bproc.camera.add_camera_pose(matrix_world, frame=frame)

def render():

    # activate seg_map rendering
    bproc.renderer.enable_segmentation_output(map_by=["category_id", "instance", "name"], default_values={'category_id': 0})
        
    # render the whole pipeline
    data = bproc.renderer.render()

    # Write data to coco file
    bproc.writer.write_coco_annotations(os.path.join(args.output_dir, 'coco_data'),
                                    instance_segmaps=data["instance_segmaps"],
                                    instance_attribute_maps=data["instance_attribute_maps"],
                                    colors=data["colors"],
                                    color_file_format="JPEG")

bproc.init()

# get the list of .obj files
obj_files = glob.glob(args.obj_files + "/*.obj")

for i in range(len(obj_files)):

    bproc.utility.reset_keyframes()

    scene = bproc.loader.load_blend("new_scene.blend")

    # define a light and set its location and energy level
    light = bproc.types.Light()

    # load the objects into the scene
    objs = bproc.loader.load_obj(obj_files[i])

    # Set some category ids for loaded objects
    for j, obj in enumerate(objs):
        obj.set_cp("category_id", i + 1)
        obj.set_location([0,0,0.5])

    light.set_type("POINT")
    light.set_location([-500, 3000, 100])
    light.set_energy(1e8)

    light.set_type("POINT")
    light.set_location([500, 3000, 100])
    light.set_energy(1e8)

    # define the camera intrinsics
    bproc.camera.set_resolution(1280, 720)

    # set the camera intrinsics
    bproc.camera.set_intrinsics_from_blender_params(lens=107/2*np.pi, lens_unit="FOV") # for ZED 2 camera, taken from the website - dedpends on the resolution 

    add_key_frame()
    render()
    bproc.utility.reset_keyframes()

    for n in range(args.no_of_frames-1):
        
        add_key_frame(frame=n)

        x = np.random.randint(-300,300)
        y = np.random.randint(-250,120)
        z = np.random.randint(50, 400)
        obj.set_location([x, y, z], frame=n)
        obj.set_rotation_euler([np.random.random()*np.pi, np.random.random()*np.pi, np.random.random()*np.pi], frame=n)

    render()

    bproc.clean_up()
