# Basic example

This repo uses ![LXM3](https://github.com/ethanluoyc/lxm3) to effortlessly submit jobs to the cluster. 

## Quickstart

Ensure that `~/.config/lxm3/config.toml` is created.
```
project = "" # Optional project name
# Configuration for running in local mode.
[local]
[local.storage]
staging = ".cache/lxm"

# Configuration for running on clusters.
[[clusters]]
# Set a name for this cluster, e.g., "cs"
name = "<TODO>"
# Replace with the server you normally use for ssh into the cluster, e.g. "beaker.cs.ucl.ac.uk"
server = "<TODO>"
# Fill in the username you use for this cluster.
user = "<TODO>"

[clusters.storage]
# Replace with the path to a staging directory on the cluster. lxm3 uses this directory for storing all files required to run your job.
staging = "<absolute path to your home directory>/lxm3-staging"
```

Build the Singularity container. 

```bash
cd cluster # this directory
make build-singularity
```

## Running Jobs

Launch locally:
```bash
lxm3 launch launcher.py 
```

Launch on cluster:
```bash
LXM_CLUSTER=cs lxm3 launch launcher.py --launch_on_cluster
```