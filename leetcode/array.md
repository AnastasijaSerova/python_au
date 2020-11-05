# Arrays

+ [Squares of a Sorted Array](#squares-of-a-sorted-array)
+ [Move Zeroes](#move-zeroes)
+ [Transpose Matrix](#transpose-matrix)
+ [Flipping an Image](#flipping-an-image)
+ [Image Smoother](#image-smoother)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Max Consecutive Ones](#max-consecutive-ones)

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)
```

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
class Solution(object):
    def moveZeroes(self, nums):
        j = count = 0
        while count < len(nums):
            if nums[j] == 0:
                nums.pop(j)
                nums.append(0)
            else:
                j += 1
            count += 1
```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
class Solution(object):
    def transpose(self, A):
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in xrange(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans
```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
class Solution(object):
    def flipAndInvertImage(self, A):
        for row in A:
            for i in xrange((len(row) + 1) / 2):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A
```

## Image Smoother

https://leetcode.com/problems/image-smoother/

```python
class Solution(object):
    def aver(self, M, i, j):
        count = 0
        _sum = 0
        for a in [i-1, i, i+1]:
            if a < 0 or a >= len(M):
                continue
            for b in [j-1, j, j+1]:
                if b < 0 or b >= len(M[0]):
                    continue
                _sum += M[a][b]
                count += 1
        return int(floor(_sum/count))

    def imageSmoother(self, M):
        M2 = [[0 for i in range(len(M[0]))] for i in range(len(M))]
        for i in range(len(M2)):
            for j in range(len(M2[0])):
                M2[i][j] = self.aver(M, i, j)
        return M2
```

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
class Solution(object):
    def yielder(self, nums):
        for row in nums:
            for x in row:
                yield x

    def matrixReshape(self, nums, r, c):
        if not nums:
            return []
        if len(nums) * len(nums[0]) != r * c:
            return nums
        gen = self.yielder(nums)
        return [[next(gen) for _ in range(c)] for _ in range(r)]
```

## Non-overlapping Intervals

https://leetcode.com/problems/max-consecutive-ones/

```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        _max = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            if _max < count:
                _max = count
        return _max
```