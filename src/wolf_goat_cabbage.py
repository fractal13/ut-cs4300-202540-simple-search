from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple

@dataclass(frozen=True)
class WolfGoatCabbageState:
    farmer: bool  # True = left bank, False = right bank
    wolf: bool
    goat: bool
    cabbage: bool

    def is_valid(self) -> bool:
        # goat alone with wolf without farmer -> invalid
        if self.goat == self.wolf and self.farmer != self.goat:
            return False
        # goat alone with cabbage without farmer -> invalid
        if self.goat == self.cabbage and self.farmer != self.goat:
            return False
        return True

    def as_tuple(self) -> Tuple[bool, bool, bool, bool]:
        return (self.farmer, self.wolf, self.goat, self.cabbage)


class WolfGoatCabbageProblem:
    def __init__(self, start: WolfGoatCabbageState | None = None, goal: WolfGoatCabbageState | None = None):
        self.start = start or WolfGoatCabbageState(True, True, True, True)
        self.goal = goal or WolfGoatCabbageState(False, False, False, False)

    def Actions(self, s: WolfGoatCabbageState) -> List[str]:
        # possible actions: farmer crosses alone or with wolf/goat/cabbage if on same side
        actions: List[str] = ["cross_alone"]
        if s.farmer == s.wolf:
            actions.append("take_wolf")
        if s.farmer == s.goat:
            actions.append("take_goat")
        if s.farmer == s.cabbage:
            actions.append("take_cabbage")
        return actions

    def Transition(self, s: WolfGoatCabbageState, a: str) -> WolfGoatCabbageState:
        # returns new state after action (does not check validity)
        f, w, g, c = s.as_tuple()
        new_f = not f
        new_w, new_g, new_c = w, g, c
        if a == "cross_alone":
            pass
        elif a == "take_wolf":
            new_w = not w
        elif a == "take_goat":
            new_g = not g
        elif a == "take_cabbage":
            new_c = not c
        else:
            raise ValueError(f"Unknown action: {a}")
        new_state = WolfGoatCabbageState(new_f, new_w, new_g, new_c)
        return new_state

    def GoalTest(self, s: WolfGoatCabbageState) -> bool:
        return s == self.goal

    def Cost(self, s1: WolfGoatCabbageState, a: str, s2: WolfGoatCabbageState) -> float:
        return 1.0
