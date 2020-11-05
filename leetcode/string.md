# String

+ [To Lower Case](#to-lower-case)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [Reverse String](#reverse-string)
+ [Valid Anagram](#valid-anagram)

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
class Solution(object):
    def toLowerCase(self, str):
        for i in str:
            if 65 <= ord(i) <= 90:
                str = str.replace(i, chr(ord(i) + 32))
        return str
```

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
class Solution(object):
    def reverseString(self, s):
        s = list(s)

        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
        return "".join(s)

    def reverseWords(self, s):
        s = s.split(" ")
        for i in range(len(s)):
            s[i] = self.reverseString(s[i])
        return " ".join(s)
```

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        vowels = {'a', 'e', 'o', 'u', 'i', 'A', 'E', 'U', 'I', 'O'}

        def helper(left, right):
            if left < right:
                if s[left] in vowels and s[right] in vowels:
                    s[left], s[right] = s[right], s[left]
                    helper(left + 1, right - 1)
                    return
                if s[left] not in vowels:
                    left += 1
                if s[right] not in vowels:
                    right -= 1
                helper(left, right)

        helper(0, len(s) - 1)
        return "".join(s)

```

## Reverse String

https://leetcode.com/problems/reverse-string/

```python
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
```

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
class Solution:
    def isAnagram(self, s, t):
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i in t:
            if i in count:
                count[i] -= 1
            else:
                count[i] = 1
        for k in count:
            if count[k] != 0:
                return False
        return True
```