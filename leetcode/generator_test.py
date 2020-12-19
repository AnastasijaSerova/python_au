import unittest
from generate_md import LeetcodeSolution
from generate_md import *

class TestLeetcodeSolution(unittest.TestCase):

    def setUp(self):
        self.solution = LeetcodeSolution('Solution Name',
                'https://leetcode.com/problems/solution-name/',
                '''class Solution(object):
    def solutionName(self):
        return 5+5
''')

    def test_title(self):
        self.assertEqual(self.solution.Title(),
                         '## Solution Name\n')

    def test_menu_link(self):
        self.assertEqual(self.solution.MenuLink(),
                         '+ [Solution Name](#solution-name)\n')

    def test_link(self):
        self.assertEqual(self.solution.Link(),
                         'https://leetcode.com/problems/solution-name/')

    def test_code(self):
        self.assertEqual(self.solution.Code(),
                         '''```python
class Solution(object):
    def solutionName(self):
        return 5+5
```
''')


class TestReadNewSolution(unittest.TestCase):

    def test_read_new_solution(self):
        self.assertEqual(read_new_solution('test_add_solution.txt'),
                         ('Solution Name',
                         'https://leetcode.com/problems/aolution-name/'
                         ,
                         '''class Solution(object):
    def mySolution(self):
        return 1+1
'''))


class TestReadMdFile(unittest.TestCase):

    def test_read_md_file(self):
        self.assertEqual(read_md_file('test_md_file.md'),
                         ('''+ [Test1](#test1)
+ [Test2](#test2)
''',
                         '''## Test1

https://leetcode.com/problems/test1/

```python
test1 code
```

## Test2

https://leetcode.com/problems/test2/

```python
test2 code
```

'''))


if __name__ == '__main__':
    unittest.main()

