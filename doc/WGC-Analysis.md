# Wolf-Goat-Cabbage (WGC) — Search Analysis

This document compares and contrasts results obtained when solving three WGC-related problems with two search algorithms implemented in this repository (Breadth-First Search (BFS) and Iterative Deepening Search (IDS)). The three problems are: the canonical WGC puzzle and two variant problem instances (e.g., different initial or goal banks or altered safety rules). The following summarizes expected behavior, observed behavior, and notable findings.

## Summary of expectations
- BFS (uninformed breadth-first) should find optimal solutions in terms of number of steps for unit step costs. It explores level-by-level and therefore visits all shallow nodes before deeper ones.
- IDS (iterative deepening depth-first search) combines DFS's low memory with BFS-level optimality for unit-cost steps: IDS will also find an optimal solution (same solution depth as BFS) while using much less memory, but with higher node-generation overhead due to repeated depth-limited searches.
- For small finite problems like WGC, both algorithms should succeed quickly; BFS will typically generate fewer total node expansions for the shallow optimal solution, while IDS will re-generate nodes across iterations and therefore generate more nodes but use less peak memory.

## Observed behavior
- Optimality: Both BFS and IDS found solutions of equal depth (optimal number of crossings) for the canonical WGC instance. This matches expectations for unit-cost problems.
- Node generation / expansions:
  - BFS generated a moderate number of nodes but required larger frontier memory proportional to the branching factor at shallow depths.
  - IDS generated more total node visits due to repeated searches up to successive depth limits; the overhead increased with the solution depth but remained reasonable for the WGC state space.
- Memory usage: Based on largest frontier storage size, it looks like BFS is more memory efficient than IDS.

## Variants and robustness
- Variants with different starting banks behaved predictably: BFS and IDS still returned optimal-depth solutions.

## Surprises / notable findings
- Implementation details matter: one observed pitfall was that naive successor filtering can produce subtle differences in node counts between BFS and IDS if duplicate-checking is implemented differently (e.g., when BFS maintains a global visited set but IDS does not deduplicate across iterations). Ensuring consistent duplicate handling is important for fair comparison.
- For this repository's implementations, IDS's reported node-generated counts were higher than theory predicted in some runs due to how statistics were recorded (counting node-generation attempts at each depth iteration rather than unique states). This explains apparent discrepancies where IDS seemed disproportionately expensive.
- For extremely small state spaces like WGC, differences in memory and time are small; the pedagogical value is primarily in illustrating algorithmic trade-offs rather than exposing performance limits.

## Conclusions
- Both algorithms behave as expected: BFS returns optimal-depth solutions with higher memory, IDS returns optimal-depth solutions with lower memory but higher repeated work.
- In typical WGC instances, choose BFS for simplicity and slightly faster solves; choose IDS when memory is constrained or when scaling to deeper but still moderately branching problems.
- When comparing algorithms, ensure consistent definitions for node counting and duplicate handling to avoid misleading statistics.
- We should also consider "Max Explored" size when looking for total memory usage.
