FaceToBMI

# Install python libraries

conda env create -f environment.yml

# activate environment with

source activate f2b

# stop

conda deactivate

# list all env

conda info --envs

# remove

conda remove --name f2b --all