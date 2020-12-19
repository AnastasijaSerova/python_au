class New_part:
    def __init__(self, file):
        title = file.readline()
        title = title[:-1]
        self.title = "## " + title
        self.link = file.readline()
        self.menulink = "+ ["+title+"](#"+self.link.split('/')[-2]+")"
        self.code = []
        self.code.append('```python\n')
        for i in file.readlines():
            self.code.append(i)
        self.code.append('```\n\n')

class MdFile:
    def __init__(self, file):
        self.title = file.readline()
        self.menu = []
        file.readline()
        cur_line = file.readline()
        while cur_line and cur_line[0] == '+':
            self.menu.append(cur_line)
            cur_line = file.readline()
        self.code = []
        self.code.append(cur_line)
        for i in file.readlines():
            self.code.append(i)

source = open("add_new_leetcode_problem.txt", 'r')
part = New_part(source)
source.close()

name = input("Type name of file:")
md_open = open(name+".md", 'r')
md_file = MdFile(md_open)
md_open.close()

output_file = open(name+".md", 'w')
output_file.write('# ' + name + '\n\n')
for i in range(len(md_file.menu)):
    output_file.write(md_file.menu[i])
output_file.write(part.menulink + '\n')
for i in range(len(md_file.code)):
    output_file.write(md_file.code[i])
output_file.write(part.title + '\n\n')
output_file.write(part.link + '\n')
for i in part.code:
    output_file.write(i)
output_file.close()
