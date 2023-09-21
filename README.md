# COCO synthetic data generation using BlenderProc



## Getting started

Install BleederProc from [here](https://github.com/DLR-RM/BlenderProc) and clone this repositary.

This repo consists of .blend file for the basic generation and the imports .obj files from a folder to create synthetic data and saves the corresponding generated images along with COCO styed annotations in the output folder.

## Usage

Run the following command in CLI to start data generation 

```
blenderproc run main.py 
/home/rushabh/Thesis/data-synthesis/resources/camera_positions 
/home/rushabh/Thesis/data-synthesis/object_files
/home/rushabh/Thesis/data-synthesis/output/
20
```

camera: default="/home/rushabh/Thesis/data-synthesis/resources/camera_positions": Path to the camera .txt file with position and orienattion of camera\
obj_files: default="/home/rushabh/Thesis/data-synthesis/object_files": Path to the stored .obj files\
output_dir: default="/home/rushabh/Thesis/data-synthesis/output/": Path to where the final files will be saved\
no_of_frames: Number of images to be generated for each object
