# Water Jugs Analysis

Summary observations:

- For the 3-jug (8,5,3) and 2-jug (3,5) instances both BFS and IDS find the same solution length (6 steps for the shown BFS/IDS outputs).
- IDS explores far more nodes than BFS for these problems (e.g., 847 vs 46 for the (3,5) case and 13817 vs 522 for the (8,5,3) case), reflecting repeated depth-limited searches.
- Max frontier sizes are comparable and small relative to nodes generated, showing that memory is modest for these instances.
- The trivial (2,4) target=2 instance is immediately solvable by a single fill action; both algorithms handle it efficiently.

Conclusions:

- BFS is generally more efficient in nodes generated/expanded for these small Water Jugs instances, while IDS trades CPU for constant memory.
- IDS may be preferable when memory is extremely constrained and solution depth is unknown, but here BFS is faster.

