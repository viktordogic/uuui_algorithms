import sys


def negate(x):
    if x[0] == "~":
        return x[1:]
    else:
        y = "~" + x
        return y


class Lab2:
    def __init__(self):
        self.resolution_path = ""
        self.clause_dict = {}
        self.nr_of_starting_clauses = int
        self.nr_of_clauses = int

        self.args = sys.argv[1:]

        try:
            if self.args[0] == "resolution":
                self.resolution_path = self.args[1]
                self.load_resolution(self.resolution_path)
        except:
            print("Error regarding command line arguments!")

        self.select_clauses()


    def load_resolution(self, resolution_path):
        with open(resolution_path, "r", encoding="utf8") as file:
            file_read = file.readlines()
            self.nr_of_clauses = sum(1 for x in file_read)
            nth_line = 1

            for line in file_read:  # PO LINIJI U FILE-U
                line_elements = line.strip().lower().split("v")
                literal_set = set()

                if nth_line == self.nr_of_clauses:  # AKO JE ZADNJI RED --> TREBA DE MORGANA
                    self.nr_of_starting_clauses = nth_line - 1
                    for line_element in line_elements:
                        line_element = line_element.strip()
                        negated_line_element = negate(line_element)
                        self.clause_dict.update({nth_line: {negated_line_element}})
                        nth_line += 1
                    print(self.clause_dict)
                    print(self.nr_of_starting_clauses)
                    return
                else:  # AKO NIJE ZADNJI RED --> PO ELEMENTIMA U LINIJI
                    for line_element in line_elements:
                        line_element = line_element.strip()
                        literal_set.add(line_element)
                    self.clause_dict.update({nth_line: literal_set})
                    nth_line += 1


    def select_clauses(self):
        for s1 in self.clause_dict:
            for s2 in self.clause_dict:
                print("The two clauses chosen are {}\n and {}".format(self.clause_dict[s1], s2))




    def refutation_resolution(self):
        new_clauses = set()
        while True:
            continue


if __name__ == "__main__":
    print("aaa")
    run = Lab2()

'''prvi = {
    1: {"~a", "e", "i"},
    2: {"b", "d"},
    3: {"c"},
    4: {"d", "f"}
}

drugi = {
    1: {"a", "e", "u"},
    2: {"b", "c"},
    3: {"c", "k"},
    4: {"d", "l"}
}

set_of_tuples = {
    (1, 2),
    (2, 3)
}

new_clause = set

char = "~"

print(str(char + "c"))

def custom_intersection(s1, s2):
    for x in s1:
        for y in s2:
            if x == str("~" + y):
                print("ovo je diff", s1.union(s2).difference(y))
                #napravimo uniju bez tog chara

for s1 in prvi.values():
    for s2 in drugi.values():
        if s1.intersection(s2) != set():
            if s1 != s2:
                custom_intersection(s1, s2)
                #print("{} is from s1[{}] and s2[{}]".format(s1.intersection(s2)))
            #new_clause = s1.intersection(s2)

print(new_clause)
'''