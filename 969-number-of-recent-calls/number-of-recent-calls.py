# from collections import deque

# class RecentCounter:

#     def __init__(self):
#         self.q = deque()

#     def ping(self, t: int) -> int:
#         self.q.append(t)

#         while self.q and self.q[0] < t - 3000:
#             self.q.popleft()

#         return len(self.q)
class RecentCounter:
    def __init__(self):
        self.records = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.records.append(t)
        while self.records[self.start] < t - 3000:
            self.start += 1
        return len(self.records) - self.start