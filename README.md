FaceToBMI

# Install python libraries

conda env create -f environment.yml

# activate environment with

source activate facetobmi

# stop

conda deactivate

# remove

conda remove --name facetobmi --all

# Add dependencies

conda create -n facetobmi numpy requests

# Solve conflict with ROS

**Linux**

1. Locate the directory for the conda environment in your terminal window by running in the terminal:

```
echo $CONDA_PREFIX
```

2. Enter that directory and create these subdirectories and files:

```
cd $CONDA_PREFIX
mkdir -p ./etc/conda/activate.d
mkdir -p ./etc/conda/deactivate.d
touch ./etc/conda/activate.d/env_vars.sh
touch ./etc/conda/deactivate.d/env_vars.sh
```

3. Edit **./etc/conda/activate.d/env_vars.sh** as follows:

```
#!/bin/sh
export MY_KEY='secret-key-value'
export MY_FILE=/path/to/my/file/
```

4. Edit ./etc/conda/deactivate.d/env_vars.sh as follows:

```
#!/bin/sh
unset MY_KEY
unset MY_FILE
```

When you run conda activate analytics, the environment variables _MY_KEY_ and _MY_FILE_ are set to the values you wrote into the file. When you run conda deactivate, those variables are erased.
