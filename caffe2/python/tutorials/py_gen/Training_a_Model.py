#########################################################
#
# DO NOT EDIT THIS FILE. IT IS GENERATED AUTOMATICALLY. #
# PLEASE LOOK INTO THE README FOR MORE INFORMATION.     #
#
#########################################################


# coding: utf-8

# ### Dataset Formats
# 
# When you look at a model and its dataset, one of the things that will be specified is how the dataset is organized. Additionally, within Caffe2 when you load the data you will need to relay this specification. When trying to optimize training and increase its speed you may find discussions related to changing this format. For the purposes of this tutorial you don't need to worry about that, but it is good to recognize the different flavors and the fact the the raw data is loaded into temporary databases to facilitate the network's training and testing.
# 
# #### Data Ordering
# 
# * NCHW: [description]
# * Others: [description]
# 
# #### Databases
# 
# * minidb: [description]
# * leveldb: [descrption]
# * others...
# 
