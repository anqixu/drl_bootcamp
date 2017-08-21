FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04

MAINTAINER Anqi Xu <ax@elementai.com>

# Configure environment
ENV TERM=xterm
# Fix Python-3 compatibility (see http://bugs.python.org/issue19846)
ENV LANG C.UTF-8

# Upgrade packages in base image
RUN sed -i'' 's/archive\.ubuntu\.com/ca\.archive\.ubuntu\.com/' /etc/apt/sources.list # switch to a more trusted and stable mirror
RUN apt-get -y update
RUN apt-get -y dist-upgrade

# Install platform utilities
RUN apt-get -y update --fix-missing && apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libhdf5-dev
RUN apt-get -y update --fix-missing && apt-get install -y libcupti-dev
RUN apt-get -y update --fix-missing && apt-get install -y git mercurial subversion
RUN apt-get -y update --fix-missing && apt-get install -y python3-dev python3-pip
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.5 1
RUN update-alternatives --install /usr/bin/python python /usr/bin/python2.7 2

# Upgrade CUDNN to v6 to match compiled version of Tensorflow v1.3
RUN echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list
ENV CUDNN_VERSION 6.0.21
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"
RUN apt-get update && apt-get install -y --no-install-recommends \
            libcudnn6=$CUDNN_VERSION-1+cuda8.0 \
            libcudnn6-dev=$CUDNN_VERSION-1+cuda8.0

# Install ML frameworks and dependencies
RUN pip3 install --upgrade pip
RUN pip3 install numpy scipy pandas jupyter pillow requests matplotlib h5py
RUN pip3 install tensorflow-gpu keras
RUN pip3 install cupy chainer chainerrl
RUN pip3 install celery seaborn tqdm

# Compile and install RoboSchool
WORKDIR /opt/
RUN git clone https://github.com/openai/roboschool.git
RUN git clone https://github.com/olegklimov/bullet3 -b roboschool_self_collision
ENV ROBOSCHOOL_PATH=/opt/roboschool
RUN apt-get update --fix-missing && apt-get install -y cmake ffmpeg pkg-config qtbase5-dev libqt5opengl5-dev libassimp-dev libpython3.5-dev libboost-python-dev libtinyxml-dev
RUN pip3 install pyopengl
RUN mkdir bullet3/build
WORKDIR /opt/bullet3/build
RUN cmake -DBUILD_SHARED_LIBS=ON -DUSE_DOUBLE_PRECISION=1 -DCMAKE_INSTALL_PREFIX:PATH=$ROBOSCHOOL_PATH/roboschool/cpp-household/bullet_local_install -DBUILD_CPU_DEMOS=OFF -DBUILD_BULLET2_DEMOS=OFF -DBUILD_EXTRAS=OFF  -DBUILD_UNIT_TESTS=OFF -DBUILD_CLSOCKET=OFF -DBUILD_ENET=OFF -DBUILD_OPENGL3_DEMOS=OFF ..
RUN make -j8
RUN make install
RUN pip3 install -e $ROBOSCHOOL_PATH

# Setup jupyter notebook password (default: jupyter)
# IMPORTANT: read http://jupyter-notebook.readthedocs.io/en/latest/public_server.html#preparing-a-hashed-password and update sha1 below
RUN mkdir -p -m 777 /root/.jupyter/ && \
    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = 'sha1:6b3542cc9bdb:524bda3d2a35b7e31c57744b655e5252549eedeb'" >> /root/.jupyter/jupyter_notebook_config.py

# Configure Jupyter
RUN jupyter nbextension enable --py widgetsnbextension

# Setup user-specific utilities
RUN apt-get -y update --fix-missing && apt-get install -y nano screen

# Configure image
EXPOSE 8888
CMD ["jupyter", "notebook", "--allow-root", "--config", "/root/.jupyter/jupyter_notebook_config.py"]