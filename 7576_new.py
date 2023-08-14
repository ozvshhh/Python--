import time
from collections import deque
start = time.time()
list1 = [0 for i in range(100000)]
list1 = deque(list1)
for i in range(len(list1)):
    list1.popleft()
end = time.time()
print(end-start)