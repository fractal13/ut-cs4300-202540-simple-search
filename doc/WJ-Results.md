# Water Jugs Report Outputs

## BFS

Running WaterJugsProblem capacities=(3, 5) target=4
Domain: WaterJugsProblem | Algorithm: BFS
Solution cost: 9.0 | Depth: 6
Nodes generated: 46 | Nodes expanded: 13 | Max frontier: 3
Path:
  1) ('fill', 1)     capacities=(3,5) volumes=(0,0) -> capacities=(3,5) volumes=(0,5)
  2) ('pour', 1, 0)  capacities=(3,5) volumes=(0,5) -> capacities=(3,5) volumes=(3,2)
  3) ('empty', 0)    capacities=(3,5) volumes=(3,2) -> capacities=(3,5) volumes=(0,2)
  4) ('pour', 1, 0)  capacities=(3,5) volumes=(0,2) -> capacities=(3,5) volumes=(2,0)
  5) ('fill', 1)     capacities=(3,5) volumes=(2,0) -> capacities=(3,5) volumes=(2,5)
  6) ('pour', 1, 0)  capacities=(3,5) volumes=(2,5) -> capacities=(3,5) volumes=(3,4)

Running WaterJugsProblem capacities=(8, 5, 3) target=4
Domain: WaterJugsProblem | Algorithm: BFS
Solution cost: 9.0 | Depth: 6
Nodes generated: 522 | Nodes expanded: 72 | Max frontier: 25
Path:
  1) ('fill', 1)     capacities=(8,5,3) volumes=(0,0,0) -> capacities=(8,5,3) volumes=(0,5,0)
  2) ('pour', 1, 2)  capacities=(8,5,3) volumes=(0,5,0) -> capacities=(8,5,3) volumes=(0,2,3)
  3) ('empty', 2)    capacities=(8,5,3) volumes=(0,2,3) -> capacities=(8,5,3) volumes=(0,2,0)
  4) ('pour', 1, 2)  capacities=(8,5,3) volumes=(0,2,0) -> capacities=(8,5,3) volumes=(0,0,2)
  5) ('fill', 1)     capacities=(8,5,3) volumes=(0,0,2) -> capacities=(8,5,3) volumes=(0,5,2)
  6) ('pour', 1, 2)  capacities=(8,5,3) volumes=(0,5,2) -> capacities=(8,5,3) volumes=(0,4,3)

Running WaterJugsProblem capacities=(2, 4) target=2
Domain: WaterJugsProblem | Algorithm: BFS
Solution cost: 1.0 | Depth: 1
Nodes generated: 2 | Nodes expanded: 1 | Max frontier: 2
Path:
  1) ('fill', 0)     capacities=(2,4) volumes=(0,0) -> capacities=(2,4) volumes=(2,0)


## IDS

Running WaterJugsProblem capacities=(3, 5) target=4
Domain: WaterJugsProblem | Algorithm: IDS
Solution cost: 9.0 | Depth: 6
Nodes generated: 847 | Nodes expanded: 843 | Max frontier: 13
Path:
  1) ('fill', 1)     capacities=(3,5) volumes=(0,0) -> capacities=(3,5) volumes=(0,5)
  2) ('pour', 1, 0)  capacities=(3,5) volumes=(0,5) -> capacities=(3,5) volumes=(3,2)
  3) ('empty', 0)    capacities=(3,5) volumes=(3,2) -> capacities=(3,5) volumes=(0,2)
  4) ('pour', 1, 0)  capacities=(3,5) volumes=(0,2) -> capacities=(3,5) volumes=(2,0)
  5) ('fill', 1)     capacities=(3,5) volumes=(2,0) -> capacities=(3,5) volumes=(2,5)
  6) ('pour', 1, 0)  capacities=(3,5) volumes=(2,5) -> capacities=(3,5) volumes=(3,4)

Running WaterJugsProblem capacities=(8, 5, 3) target=4
Domain: WaterJugsProblem | Algorithm: IDS
Solution cost: 9.0 | Depth: 6
Nodes generated: 13817 | Nodes expanded: 13808 | Max frontier: 23
Path:
  1) ('fill', 1)     capacities=(8,5,3) volumes=(0,0,0) -> capacities=(8,5,3) volumes=(0,5,0)
  2) ('pour', 1, 2)  capacities=(8,5,3) volumes=(0,5,0) -> capacities=(8,5,3) volumes=(0,2,3)
  3) ('empty', 2)    capacities=(8,5,3) volumes=(0,2,3) -> capacities=(8,5,3) volumes=(0,2,0)
  4) ('pour', 1, 2)  capacities=(8,5,3) volumes=(0,2,0) -> capacities=(8,5,3) volumes=(0,0,2)
  5) ('fill', 1)     capacities=(8,5,3) volumes=(0,0,2) -> capacities=(8,5,3) volumes=(0,5,2)
  6) ('pour', 1, 2)  capacities=(8,5,3) volumes=(0,5,2) -> capacities=(8,5,3) volumes=(0,4,3)

Running WaterJugsProblem capacities=(2, 4) target=2
Domain: WaterJugsProblem | Algorithm: IDS
Solution cost: 1.0 | Depth: 1
Nodes generated: 4 | Nodes expanded: 3 | Max frontier: 2
Path:
  1) ('fill', 0)     capacities=(2,4) volumes=(0,0) -> capacities=(2,4) volumes=(2,0)
