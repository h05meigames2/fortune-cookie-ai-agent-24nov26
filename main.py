#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — writes one fortune line to /output/entry.txt."""

import os

FORTUNE = "You will meet a tall, dark stranger: a prompt with no context, no examples, and a deadline of now."

def main():
    assert 1 <= len(FORTUNE) <= 140, "fortune must be 1-140 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")
    print(FORTUNE)

if __name__ == "__main__":
    main()
