#!/usr/local_rwth/bin/zsh
 
# name the job
#SBATCH --job-name=BP_data_gen

# request CPU resources
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=16G

# request GPU
#SBATCH --gres=gpu:1

# time limit
#SBATCH --time=0-24:00:00  

# specify account
#SBATCH --account=rwth1299

### beginning of executable commands
module load cuda

source /$HOME/miniconda3/bin/activate blenderproc

blenderproc run $HOME/Thesis/code/data-synthesis/generate.py -c $HOME/Thesis/code/data-synthesis/resources/camera_positions -obj $HOME/Thesis/code/data-synthesis/object_files -o $WORK/thesis/Data/no_shadow -n 1000
