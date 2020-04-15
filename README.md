# FaceToBMI

## Install python libraries

```
conda env create -f environment.yml
```

## activate environment with

```
source activate f2b
```

## stop

```
conda deactivate
```

## list all env

```
conda info --envs
```

## remove

```
conda remove --name f2b --all
```

## If fail to import cv2

```
pip install opencv-python==3.4.2.17
pip install opencv-contrib-python==3.4.2.17
```

## Ubuntu conflict with ROS

```
import sys
print(sys.path)
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
```
