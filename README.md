# COCO synthetic data generation using BlenderProc



## Getting started

Install BlenderProc from [here](https://github.com/DLR-RM/BlenderProc) and clone this repositary.

This repo consists of .blend file for the basic generation and the imports .obj files from a folder to create synthetic data and saves the corresponding generated images along with COCO styed annotations in the output folder.

## Usage

Run the following command in CLI to start data generation 

```
blenderproc run main.py -c -obj -o -n
```

-c: camera: Path to the camera .txt file with position and orienattion of camera\
-obj: obj_files: Path to the stored .obj files\
-o: output_dir: Path to where the final files will be saved\
-n: no_of_frames: Number of images to be generated for each object
