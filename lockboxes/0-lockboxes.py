#!/usr/bin/python3
"""Solves the boxes problem."""


def canUnlockAll(boxes):
    """Checks if all boxes can be unlocked.

    Args:
        boxes: A list of lists, where each inner list represents the keys held
               by a box.

    Returns:
        True if all boxes can be unlocked, False otherwise.
    """

    for key in range(1, len(boxes)):
        can_be_unlocked = False
        for box_index in range(len(boxes)):
            if key in boxes[box_index] and box_index != key:
                can_be_unlocked = True
                break
        if not can_be_unlocked:
            return False
    return True
