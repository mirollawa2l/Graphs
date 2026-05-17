# Graph Algorithms Demo

This repository contains simple Python examples for fundamental graph algorithms.

## Files

- `graphs.py`
  - Demonstrates Prim's algorithm for computing a minimum spanning tree (MST) on a weighted undirected graph.
  - Prints the MST edges and total cost starting from the chosen node.

- `mst.py`
  - Implements the same Prim's MST example and prints the MST result.

- `topological.py`
  - Demonstrates topological sorting for a directed acyclic graph (DAG).
  - Builds a sample graph and prints a valid topological order.

## Usage

Run any example with Python:

```bash
python graphs.py
python mst.py
python topological.py
```

## Purpose

This project is intended to help understand and visualize:

- Prim's algorithm for minimum spanning trees
- Topological sorting of directed acyclic graphs
- Basic graph representation and traversal in Python

## Notes

- `graphs.py` and `mst.py` currently use the same sample graph for MST.
- `topological.py` uses a DAG example with vertex ordering computed using DFS.
