FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04

MAINTAINER Anqi Xu <ax@elementai.com>

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates libglib2.0-0
RUN apt-get install -y git mercurial subversion

# TODO: need these packages? libxext6 libsm6 libxrender1
#RUN apt-get install -y libhdf5-dev
#RUN conda install -y numpy pymongo scipy pandas jupyter pillow requests matplotlib h5py

# Use Tini to manage entrypoint and prevent zombie processes
#RUN apt-get install -y curl grep sed dpkg && \
#    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
#    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
#    dpkg -i tini.deb && \
#    rm tini.deb && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

# Fix Python-3 compatibility (see http://bugs.python.org/issue19846)
ENV LANG C.UTF-8

RUN pip install --upgrade pip
RUN pip install numpy scipy pandas jupyter pillow requests matplotlib h5py
RUN pip install tensorflow-gpu keras chainer chainerrl
RUN pip install celery seaborn tqdm

# Setup jupyter notebook password (default: jupyter)
# IMPORTANT: read http://jupyter-notebook.readthedocs.io/en/latest/public_server.html#preparing-a-hashed-password and update sha1 below
RUN mkdir -p -m 777 /root/.jupyter/ && \
    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = 'sha1:6b3542cc9bdb:524bda3d2a35b7e31c57744b655e5252549eedeb'" >> /root/.jupyter/jupyter_notebook_config.py

RUN jupyter nbextension enable --py widgetsnbextension

EXPOSE 8888
CMD ["jupyter", "notebook", "--allow-root", "--config", "/root/.jupyter/jupyter_notebook_config.py"]
