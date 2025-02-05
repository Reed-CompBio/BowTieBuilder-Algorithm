# BowTieBuilder-Algorithm
This repository contains an implementation of the BowTieBuilder Algorithm.

# BowTieBuilder Docker image

Available on [DockerHub](https://hub.docker.com/repository/docker/reedcompbio/bowtiebuilder).

A simple pathway reconstruction algorithm that attempts to join sources and targets into a BowTie shape. The algorithm takes a network and 2 lists of nodes (source and target sets) as input. It outputs all edges in the network that are on the shortest paths from source to target sets.

# Usage 
Implemented into the Signaling Pathway Reconstruction Streamliner [(SPRAS)](https://github.com/Reed-CompBio/spras).

Command Line Test:
```
python btb.py --edges ./input/edges.txt --sources ./input/source.txt --targets ./input/target.txt --output ./output/output.txt
```

Example Output:
![BTB Output](https://github.com/Reed-CompBio/BowTieBuilder-Algorithm/blob/5138085aee9bdcaa0fc3f870731df4c6b5207b7d/btb.png)

## Original Paper

The original paper for BowTieBuilder can be accessed here:

Supper, J., Spangenberg, L., Planatscher, H. et al. BowTieBuilder: modeling signal transduction pathways. BMC Syst Biol 3, 67 (2009). https://doi.org/10.1186/1752-0509-3-67
