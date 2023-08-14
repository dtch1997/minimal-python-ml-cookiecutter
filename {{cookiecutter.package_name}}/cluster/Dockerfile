# Reference: https://github.com/ethanluoyc/cdrl/blob/main/cluster/Dockerfile

# Usage:
#
#   Build image:
#     DOCKER_BUILDKIT=1 docker build -t cdrl -f  cluster/Dockerfile .
#   Run image:
#     docker run --gpus all --rm -it -v ${PWD}:/workdir cdrl:latest
#   Convert to Singularity image:
#     singularity build cluster/cdrl.sif docker-daemon://cdrl:latest
#
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04
ARG USERNAME=docker
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV LANG=C.UTF-8

# Needed by nvidia-container-runtime, if used
ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
        ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics,compat32,utility

# Install system dependencies
# Does a few things
# * Install rendering dependencies for dm_control
# * Enable EGL support via libglvnd, see
#   https://gitlab.com/nvidia/container-images/opengl/blob/ubuntu20.04/glvnd/runtime/Dockerfile

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -q -y --no-install-recommends \
        cuda-command-line-tools-11-6 \
        cuda-minimal-build-11-6 \
        ffmpeg \
        git \
        libegl1 \
        libgl1 \
        libgl1-mesa-glx \
        libgles2 \
        libglew2.1 \
        libglfw3 \
        libglvnd0 \
        libglx0 \
        libosmesa6 \
        patchelf \
        sudo \
        unzip \
        wget \
        python3.9 \
        python3.9-dev \
        python3.9-venv \
        python3.9-distutils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/bin/python3.9 /usr/bin/python3 \
    && ln -sf /usr/bin/python3.9 /usr/bin/python

# See
#   https://gitlab.com/nvidia/container-images/opengl/-/blob/ubuntu20.04/glvnd/runtime/Dockerfile
# and
#   https://github.com/apptainer/singularity/issues/1635
#
RUN wget -q https://gitlab.com/nvidia/container-images/opengl/-/raw/ubuntu20.04/glvnd/runtime/10_nvidia.json \
    -O /usr/share/glvnd/egl_vendor.d/10_nvidia.json

# Create the user
RUN echo $USER_GID $USER_UID \
    && groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# ENV MUJOCO_DIR=/opt/mujoco
# ENV MUJOCO_PY_MUJOCO_PATH=/opt/mujoco/mujoco210
# RUN mkdir -p ${MUJOCO_DIR} && \
#     wget https://github.com/deepmind/mujoco/releases/download/2.1.0/mujoco210-linux-x86_64.tar.gz && \
#     tar -C ${MUJOCO_DIR} -xvzf mujoco210-linux-x86_64.tar.gz

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir -p /workdir
ENV VIRTUAL_ENV=/opt/venv
RUN python3.9 -m venv $VIRTUAL_ENV
ENV PATH=$VIRTUAL_ENV/bin:$PATH

COPY ./requirements /tmp/requirements
RUN python3 -m pip --no-cache-dir install -U pip wheel setuptools \
    && python3 -m pip --no-cache-dir install -r /tmp/requirements/dev.txt \
    && rm -r /tmp/requirements

WORKDIR /workdir
USER $USERNAME