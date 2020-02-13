FaceToBMI

# Install python libraries

conda env create -f environment.yml

# activate environment with

source activate facetobmi

# Solve conflict with ROS

**macOS and Linux**

1. Locate the directory for the conda environment in your terminal window by running in the terminal `{echo \$CONDA_PREFIX}`

2. Enter that directory and create these subdirectories and files:

`cd \$CONDA_PREFIX mkdir -p ./etc/conda/activate.d mkdir -p ./etc/conda/deactivate.d touch ./etc/conda/activate.d/env_vars.sh touch ./etc/conda/deactivate.d/env_vars.sh`
Edit ./etc/conda/activate.d/env_vars.sh as follows:

#!/bin/sh

export MY_KEY='secret-key-value'
export MY_FILE=/path/to/my/file/
Edit ./etc/conda/deactivate.d/env_vars.sh as follows:

#!/bin/sh

unset MY_KEY
unset MY_FILE

When you run conda activate analytics, the environment variables MY_KEY and MY_FILE are set to the values you wrote into the file. When you run conda deactivate, those variables are erased.
