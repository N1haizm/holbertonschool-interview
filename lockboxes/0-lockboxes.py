#!/usr/bin/python3
"""I wrote this code to solve the boxes problem"""

def canUnlockAll(boxes):
    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False
    return True
