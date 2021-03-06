#!/usr/bin/env python
from src.utils import BaseResolution


class Resolution(BaseResolution):
    """Logics for resolving day 1."""
    day = 1

    def part_1(self, input_lines: list):
        """Run n**2 solution for part 1."""
        total = 2020
        for i, line in enumerate(input_lines):
            line = int(line)
            rest = total - line
            for candidate in input_lines[i+1:]:
                candidate = int(candidate)
                if rest == candidate:
                    print(line * candidate)
                    return

    def part_2(self, input_lines: list):
        """Run n**3 solution for part 2."""
        total = 2020
        for i, line in enumerate(input_lines):
            line = int(line)
            rest = total - line
            for candidate1 in input_lines[i+1:]:
                candidate1 = int(candidate1)
                rest2 = rest - candidate1
                for candidate2 in input_lines[i+2:]:
                    candidate2 = int(candidate2)
                    if rest2 == candidate2:
                        print(line * candidate1 * candidate2)
                        return
