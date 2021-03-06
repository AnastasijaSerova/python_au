class LeetcodeSolution:

    def __init__(self, title, link, code):
        self.title = title
        self.link = link
        self.code = code

    def Title(self):
        return '## {}\n'.format(self.title)

    def MenuLink(self):
        return '+ [{}](#{})\n'.format(self.title, self.link.split('/')[-2])

    def Link(self):
        return self.link

    def Code(self):
        return "```python\n{}```\n".format(self.code)


class MdFile:

    def __init__(self, menu, solutions):
        self.menu = menu
        self.solutions = solutions

    def Menu(self):
        return self.menu

    def Solutions(self):
        return self.solutions


def read_new_solution(filename):
    file = open(filename)
    title = file.readline()
    link = file.readline()
    code = file.read()
    file.close()
    return (title[:-1], link[:-1], code)


def read_md_file(filename):
    file = open(filename)
    menu = ''
    solutions = ''
    checker = False
    while True:
        line = file.readline()
        if line != '' and line[0] == '+':
            menu = menu + line
            if not checker:
                checker = True
        elif checker:
            break
    solutions = file.read()
    return (menu, solutions)


def generate_final_data(section, md_file, new_solution):
    res = "# {}\n\n".format(section)
    res = '{}{}{}\n'.format(res, md_file.Menu(),
                            new_solution.MenuLink())
    res = res + md_file.Solutions() + new_solution.Title() \
        + new_solution.Link() + new_solution.Code()
    return res


def write_to_md(filename, data):
    file = open(filename, 'w')
    file.write(data)
    file.close


if __name__ == '__main__':
    data = read_new_solution('add_new_leetcode_problem.txt')
    new_solution = LeetcodeSolution(data[0], data[1], data[2])
    section = input('Type name md file: ')
    data = read_md_file(section + '.md')
    md_file = MdFile(data[0], data[1])
    write_to_md(section + '.md', generate_final_data(section, md_file,
                new_solution))
