import sys

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Side(self, a, b):
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

    def isTriangle(self):
        s1 = self.Side(self.a, self.b)
        s2 = self.Side(self.b, self.c)
        s3 = self.Side(self.c, self.a)

        return (s1+s2>s3) and (s2+s3>s1) and (s3+s1>s2)

    def isIsosceles(self):
        s1 = self.Side(self.a, self.b)
        s2 = self.Side(self.b, self.c)
        s3 = self.Side(self.c, self.a)

        return (s1 == s2 or s2 == s3 or s3 == s1)

    def Square(self):
        s1 = self.Side(self.a, self.b)
        s2 = self.Side(self.b, self.c)
        s3 = self.Side(self.c, self.a)
        p = (s1 + s2 + s3) / 2
        return (p * (p - s1) * (p - s2) * (p - s3)) ** 0.5


class File:
    def __init__(self, filename):
        self.filename = filename

    def get_all_lines(self):
        file = open(self.filename, 'r')
        result = file.readlines()
        file.close()
        return result

    def write_result(self, string):
        file = open(self.filename, 'w')
        file.write(string)
        file.close()


def main():
    name_input_file = sys.argv[1]
    name_output_file = sys.argv[2]

    res = []
    in_file = File(name_input_file)
    lines = in_file.get_all_lines()

    if lines:
        for line in lines:
            crd = line.split(" ")
            if len(crd) == 6:
                A = Point(crd[0], crd[1])
                B = Point(crd[2], crd[3])
                C = Point(crd[4], crd[5])
                T = Triangle(A, B, C)
                if T.isTriangle() and T.isIsosceles():
                    res.append(T.Square())
                else:
                    res.append(-1)

        output = File(name_output_file)
        i = res.index(max(res))
        if max(res) != -1:
            output.write_result(lines[i])


if __name__ == "__main__":
    main()
