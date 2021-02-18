from  __future__ import annotations

import math
from typing import List, Union

class SeqmentTree:
    def __init__(self, size: int) -> None:
        self.size = size
        self.seqment_tree = [0 for i in range(0, 4 * size)]
        self.lazy = [0 for i in range(0, 4 * size)]
        self.flag = [0 for i in range(0, 4 * size)]
        

    def left(self, index: int) -> int:
        return index * 2
    
    def right(self, index: int) -> int:
        return index * 2 + 1

    def build(
        self, index: int, left_element: int, right_element: int, A: List[int]
    ) -> None:

        if left_element == right_element:
            self.seqment_tree[index] = A[left_element - 1]
        else:
            mid = (left_element + right_element) // 2
            self.build(self.left(index), left_element, mid, A)
            self.build(self.right(index), mid + 1, right_element, A)
            self.seqment_tree[index] = max(self.seqment_tree[self.left(index)], self.seqment_tree[self.right(index)])

    def update(
        self, index: int, left_element: int, right_element: int, a:int, b:int, val:int
    ) -> bool:
        if self.flag[index] is True:
            self.seqment_tree[index] = self.lazy[index]
            self.flag[index] = False
            if left_element != right_element:
                self.lazy[self.left(index)] = self.lazy[index]
                self.lazy[self.right(index)] = self.lazy[index]
                self.flag[self.left(index)] = True
                self.flag[self.right(index)] = True
        if right_element < a or left_element > b:
            return True
        if left_element >= a and right_element <= b:
            self.seqment_tree[index] = val
            if left_element != right_element:
                self.lazy[self.left(index)] = val
                self.lazy[self.right(index)] = val
                self.flag[self.left(index)] = True
                self.flag[self.right(index)] = True                
            return True
        mid = (left_element + right_element) // 2
        self.update(self.left(index), left_element, mid, a, b, val)
        self.update(self.right(index), mid + 1, right_element, a, b, val)
        self.seqment_tree[index] = max(
            self.seqment_tree[self.left(index)], self.seqment_tree[self.right(index)]
        )
        return True


    def query(
        self, index: int, left_element: int, right_element: int, a:int, b:int
    ) -> Union[int, float]:
        if self.flag[index] is True:
            self.seqment_tree[index] = self.lazy[index]
            self.flag[index] = False
            if left_element != right_element:                
                self.lazy[self.left(index)] = self.lazy[index]
                self.lazy[self.right(index)] = self.lazy[index]
                self.flag[self.left(index)] = True
                self.flag[self.right(index)] = True
        if right_element < a or right_element > b:
            return -math.inf
        if left_element >= a or left_element <= b:
            return self.seqment_tree[index]

        mid = (left_element + right_element) // 2
        q1 = self.query(self.left(index), left_element, mid, a, b)
        q2 = self.query(self.right(index), mid + 1, right_element, a, b)
        return max(q1, q2)

    def __str__(self) -> str:
        return str([self.query(1, 1, self.size, i, i) for i in range(1, self.size +1)])

if __name__ == "__main__":
    A = [1, 2, 5, 7]
    size = 4
    segt = SeqmentTree(size)
    segt.build(1, 1, size, A)
    segt.update(1, 1, size, 15, 25, 15)
    print(segt.query(1, 1, size, 1, 3))
    print(segt)
    segt.update(1, 1, size, 15, 25, 15)
    print(segt.query(1, 1, size, 1, 3))
    print(segt)
    print(A[3])
