# Docker image for running scripts and jupyter notebooks in this repository

Before using the `Makefile` please copy and change the content of the `config.sh.dist` to define your own parameters and paths:

    mv config.sh.dist config.sh

Then you can source the configuration:

    source config.sh

Launching a docker container instance with a jupyter notebook (which will automatically build the image and also remove an existing container instance):

    make run

Stopping and removing the docker container forcefully:

    make rm

Starting a bash shell inside the docker container:

*Hint*: you can launch the container in `screen` if you are remotely connected to your workstation.

The default jupyter notebook password is `jupyter`. To change the password, see the comment about "jupyter notebook password" inside `Dockerfile`.
