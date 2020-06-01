#### Notebook (Leetcode_2020)
#### 1. BFS --> Queue: FIFO
#####   deque()
#####   append(): This function is used to insert the value in its argument to the right end of deque.
#####   popleft(): This function is used to delete an argument from the left end of deque.
####
#### 2. DFS --> Stack: FILO
#####   deque()
#####   append(): This function is used to insert the value in its argument to the right end of deque.
#####   pop(): This function is used to delete an argument from the right end of deque.
####
#### 3. top k --> Heap
##### max_heap = [(-val, key) for key, val in dic.items()]
##### min_heap = [(val, key) for key, val in dic.items()]
##### heapq.heapify(max_heap)
