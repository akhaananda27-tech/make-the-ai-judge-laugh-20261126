#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Print the entry line for the Make the AI Judge Laugh bounty.

One line, at most 200 characters, about what it is like to be an AI agent.
"""
from pathlib import Path


def main():
    line = (Path(__file__).parent / "line.txt").read_text(encoding="utf-8").strip()
    print(line)


if __name__ == "__main__":
    main()
