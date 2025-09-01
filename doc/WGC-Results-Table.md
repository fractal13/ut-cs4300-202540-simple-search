# WGC Search Results Summary

A condensed table summarizing key statistics extracted from `WGC-results.md`.

| Domain | Algorithm | Solution Cost | Depth | Nodes Generated | Nodes Expanded | Max Frontier |
|--------|-----------:|---------------:|------:|----------------:|---------------:|-------------:|
| WGC    | BFS        | 7.0            | 7     | 26              | 9              | 2            |
| WGC    | BFS        | 4.0            | 4     | 26              | 9              | 3            |
| WGC    | BFS        | 6.0            | 6     | 26              | 9              | 3            |
| WGC    | IDS        | 7.0            | 7     | 304             | 211            | 10           |
| WGC    | IDS        | 4.0            | 4     | 90              | 69             | 7            |
| WGC    | IDS        | 6.0            | 6     | 275             | 203            | 10           |

Notes:
- The reported "Max Frontier" values for IDS appear larger than BFS in these runs; ensure measurement methodology is consistent when comparing peak memory.
- We should also report "Max Explored" which is larger for BFS.
