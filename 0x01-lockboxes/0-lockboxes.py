#!/usr/bin/python3
"""
Module documentation for 0-lockboxes.py
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    """


    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    visited.add(0)
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]

        for key in keys:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == n
