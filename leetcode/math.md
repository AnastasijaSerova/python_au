# Math

+ [Sqrt(x)](#sqrtx)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [Fibonacci Number](#fibonacci-number)
+ [Base 7](#base-7)
+ [Fizz Buzz](#fizz-buzz)
+ [Palindrome Number](#palindrome-number)
+ [Reverse Integer](#reverse-integer)

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
class Solution(object):
    def mySqrt(self, x):
        return int(sqrt(x))
```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
class Solution(object):
    def largestPerimeter(self, A):
        A.sort()
        for i in xrange(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
class Solution(object):
    def fib(self, N):
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)
```

## Base 7

https://leetcode.com/problems/base-7/

```python
class Solution(object):
    def convertToBase7(self, num):
        if not num:
            return str(num)

        sign = '-' if num < 0 else ''
        num = abs(num)
        result = []
        while num:
            result.append(str(num % 7))
            num //= 7
        result.append(sign)
        return ''.join(reversed(result))
```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
class Solution(object):
    def fizzBuzz(self, n):
        ans = []
        for num in range(1, n+1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)
            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            elif divisible_by_3:
                ans.append("Fizz")
            elif divisible_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(num))
        return ans
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        revrse = int(str(x)[::-1])
        return True if revrse == x else False
```

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
class Solution(object):
    def reverse(self, x):
        s = (x > 0) - (x < 0)
        r = int(str(x*s)[::-1])
        if s*r < -2**31 or s*r > 2**31 - 1:
            return 0
        else:
            return s * r
```