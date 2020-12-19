import unittest
from generate_md import LeetcodeSolution
from generate_md import *

class TestLeetcodeSolution(unittest.TestCase):
		def setUp(self):
				self.solution = LeetcodeSolution("Solution Name", "https://leetcode.com/problems/solution-name/", "class Solution(object):\n    def solutionName(self):\n        return 5+5\n")
		def test_title(self):
				self.assertEqual(self.solution.get_md_title(), "## Solution Name\n")
		def test_menu_link(self):
				self.assertEqual(self.solution.get_md_menu_link(), "+ [Solution Name](#solution-name)\n")
		def test_link(self):
				self.assertEqual(self.solution.get_md_link(), "https://leetcode.com/problems/solution-name/")
		def test_code(self):
				self.assertEqual(self.solution.get_md_code(), "```python\nclass Solution(object):\n    def solutionName(self):\n        return 5+5\n```\n")

class TestReadNewSolution(unittest.TestCase):
		def test_read_new_solution(self):
				self.assertEqual(read_new_solution("test_add_solution.txt"), ('Solution Name', 'https://leetcode.com/problems/aolution-name/', 'class Solution(object):\n    def mySolution(self):\n        return 1+1\n'))

class TestReadMdFile(unittest.TestCase):
		def test_read_md_file(self):
				self.assertEqual(read_md_file("test_md_file.md"), ('+ [Test1](#test1)\n+ [Test2](#test2)\n', '## Test1\n\nhttps://leetcode.com/problems/test1/\n\n```python\ntest1 code\n```\n\n## Test2\n\nhttps://leetcode.com/problems/test2/\n\n```python\ntest2 code\n```\n\n'))

if __name__ == "__main__":
		unittest.main()

