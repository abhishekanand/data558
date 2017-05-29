

## Configuring Local envrionment
 
Created a Github private repo 
Downloaded all files from the Kagggle Comptiotion
extracted them locally
and commited to master branch 

cd /mnt/c/Users/abhanand/Documents/GitHub/data558/competition/
tar -xvzf test.tgz
tar -xvzf train.tgz


## Login to AWS Instance 

# abhanand@AASurgace:/mnt/c/Users/abhanand/Downloads$ ssh -i "midt.pem" ubuntu@ec2-52-71-137-76.compute-1.amazonaws.com
# The authenticity of host 'ec2-52-71-137-76.compute-1.amazonaws.com (52.71.137.76)' can't be established.
# ECDSA key fingerprint is SHA256:EHbv1COsk56R5SqdHxDg9O2NhDxqyrNQIRkc+CfTUrY.
# Are you sure you want to continue connecting (yes/no)? yes
# Warning: Permanently added 'ec2-52-71-137-76.compute-1.amazonaws.com,52.71.137.76' (ECDSA) to the list of known hosts.
# ===================================
# Deep Learning AMI for Ubuntu
# ===================================
# The README file for the AMI : /home/ubuntu/src/AMI.README.md

# Tests for deep learning frameworks ➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜➜ /home/ubuntu/src/bin

# Welcome to Ubuntu 14.04.5 LTS (GNU/Linux 3.13.0-107-generic x86_64)

 # * Documentation:  https://help.ubuntu.com/

  # System information as of Mon May 29 18:10:55 UTC 2017

  # System load: 0.0                Memory usage: 0%   Processes:       105
  # Usage of /:  68.5% of 49.08GB   Swap usage:   0%   Users logged in: 0

  # Graph this data and manage this system at:
    # https://landscape.canonical.com/

  # Get cloud support with Ubuntu Advantage Cloud Guest:
    # http://www.ubuntu.com/business/services/cloud

# 9 packages can be updated.
# 8 updates are security updates.

# New release '16.04.2 LTS' available.
# Run 'do-release-upgrade' to upgrade to it.


# Last login: Sun May 28 22:13:01 2017 from 131.107.147.93

# ubuntu@ip-172-31-43-70:~$ ls -l
# total 4
# drwxrwxr-x 22 ubuntu ubuntu 4096 Feb 16 17:52 src

# ubuntu@ip-172-31-43-70:~$ cd src/tensorflow
# ubuntu@ip-172-31-43-70:~/src/tensorflow$ cd tensorflow/models/image/imagenet/

# ubuntu@ip-172-31-43-70:~/src/tensorflow/tensorflow/models/image/imagenet$ ls
# BUILD  classify_image.py

# ubuntu@ip-172-31-43-70:~/src/tensorflow/tensorflow/models/image/imagenet$ python classify_image.py --model_dir TUTORIAL_DIR/imagenet
# I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcublas.so.7.5 locally
# I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcudnn.so.5 locally
# I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcufft.so.7.5 locally
# I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcuda.so.1 locally
# I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcurand.so.7.5 locally
# >> Downloading inception-2015-12-05.tgz 100.0%
# Succesfully downloaded inception-2015-12-05.tgz 88931400 bytes.
# I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
# I tensorflow/core/common_runtime/gpu/gpu_device.cc:885] Found device 0 with properties:
# name: Tesla K80
# major: 3 minor: 7 memoryClockRate (GHz) 0.8235
# pciBusID 0000:00:1e.0
# Total memory: 11.17GiB
# Free memory: 11.11GiB
# I tensorflow/core/common_runtime/gpu/gpu_device.cc:906] DMA: 0
# I tensorflow/core/common_runtime/gpu/gpu_device.cc:916] 0:   Y
# I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Tesla K80, pci bus id: 0000:00:1e.0)
# W tensorflow/core/framework/op_def_util.cc:332] Op BatchNormWithGlobalNormalization is deprecated. It will cease to work in GraphDef version 9. Use tf.nn.batch_normalization().
# giant panda, panda, panda bear, coon bear, Ailuropoda melanoleuca (score = 0.88493)
# indri, indris, Indri indri, Indri brevicaudatus (score = 0.00878)
# lesser panda, red panda, panda, bear cat, cat bear, Ailurus fulgens (score = 0.00317)
# custard apple (score = 0.00149)
# earthstar (score = 0.00127)

cd src/tensorflow
cd tensorflow/models/image/imagenet/
python classify_image.py --model_dir TUTORIAL_DIR/imagenet


# ubuntu@ip-172-31-43-70:~/src/tensorflow/tensorflow/models/image/imagenet$ ls -l
# total 16
# -rw-rw-r-- 1 ubuntu ubuntu  566 Feb 15 01:40 BUILD
# -rw-rw-r-- 1 ubuntu ubuntu 7743 Feb 15 01:40 classify_image.py
# drwxrwxr-x 3 ubuntu ubuntu 4096 May 29 18:14 TUTORIAL_DIR


# ubuntu@ip-172-31-43-70:~/src/tensorflow/tensorflow/models/image/imagenet$


Copying file from AWS to Local Instance 

# abhanand@AASurgace:/mnt/c/Users/abhanand/Documents/GitHub/data558/competition$ scp -i /mnt/c/Users/abhanand//Downloads/midt.pem -r ubuntu@ec2-52-71-137-76.compute-1.amazonaws.com:/home/ubuntu/src/tensorflow/tensorflow/models/image/imagenet/TUTORIAL_DIR .
# imagenet_synset_to_human_label_map.txt                                100%  724KB 724.0KB/s   00:01
# classify_image_graph_def.pb                                           100%   91MB   4.8MB/s   00:19
# inception-2015-12-05.tgz                                              100%   85MB   2.8MB/s   00:30
# imagenet_2012_challenge_label_map_proto.pbtxt                         100%   63KB  63.5KB/s   00:00
# LICENSE                                                               100%   11KB  11.2KB/s   00:01
# cropped_panda.jpg                                                     100% 2683     2.6KB/s   00:00
# abhanand@AASurgace:/mnt/c/Users/abhanand/Documents/GitHub/data558/competition$


scp -i /mnt/c/Users/abhanand//Downloads/midt.pem -r ubuntu@ec2-52-71-137-76.compute-1.amazonaws.com:/home/ubuntu/src/tensorflow/tensorflow/models/image/imagenet/TUTORIAL_DIR .

Copied all files to Github Repo and commited that to master branch 