#!/usr/bin/python3
'''Local boxes module
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    '''
    n = len(boxes)
    se_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in s_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            se_boxes.add(boxIdx)
    return n == len(se_boxes)
