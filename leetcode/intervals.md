# Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
+ [Insert Interval](insert-interval)

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        remove = 0
        intervals = sorted(intervals, key=lambda x: x[1])
        endP = intervals[0][1]
        for i in range(1, len(intervals)):
            startN = intervals[i][0]
            endN = intervals[i][1]
            if startN < endP:
                remove += 1
            else:
                endP = intervals[i][1]
        return remove
```

## Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
```

## Insert Interval

https://leetcode.com/problems/insert-interval/

```python
class Solution(object):
    def insert(self, intervals, newInterval):
        ans = []
        added = False
        nx1, nx2 = newInterval
        for x1, x2 in intervals:
            if not (x2 < nx1 or x1 > nx2):
                nx1 = min(x1, nx1)
                nx2 = max(x2, nx2)
            else:
                if x1 > nx2 and not added:
                    ans.append([nx1, nx2])
                    added = True
                ans.append([x1, x2])
        if not added:
            ans.append([nx1, nx2])
        return ans if ans else [newInterval]
```