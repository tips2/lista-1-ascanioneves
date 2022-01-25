import sys

class rule:
    __head = 0
    __body = 0

    def __init__(self, body, head):
        self.__body = body
        self.__head = head

    def getHead(self):
        return self.__head

    def getBody(self):
        return self.__body

    def printRule(self):
        if len(self.__body) != 0:
            for i in range(len(self.__body)):
                print(self.__body[i], end = "")
                if i is not len(self.__body) - 1:
                    print("^", end = "")
            if len(self.__body) != 0:
                print("=>", end = "")
            print(self.__head, end="\t")
        else:
            print(self.__head, end="\t")


def parse(line):
    result = []
    thehead = ""
    for i in range(len(line)):
        if i == 1:
            thehead = line[i]
        else:
            if line[i].isalpha():
                result.append(line[i])
    return rule(result, thehead)


def solve(Goals, Rules, Solutions, Path, failedPartialPath):
    if len(Goals) == 0:
        return True
    goal = Goals.pop(0)
    for rule in Rules:
        if rule.getHead() == goal:
            Path.append(rule)
            temp = []
            temp.extend(rule.getBody())
            temp.extend(Goals)
            if solve(temp, Rules, Solutions, Path, failedPartialPath):
                Solutions.append(rule)
                return True
            else:
                failedPartialPath.append(rule)
    return False


def solutionForEachQuery(Rules, Goals):
    Solutions = []
    path = []
    failedPartialPath = []


    result = solve(Goals, Rules, Solutions, path, failedPartialPath)
    Solutions.reverse()
    failedPartialPath.reverse()

    if result is True:
        print("Encontrou corretamente o caminho para o objetivo... ", "\n")
        print("A solucao para o caminho eh: ")
        for i in Solutions:
            i.printRule()
        print("\n")

        if len(failedPartialPath) != 0:
            print("No entanto, houve um desperdicio de procurar um caminho com falha parcial:")
            for i in failedPartialPath:
                i.printRule()
            print("")
            print("entao o caminho procurado foi: ")
            for i in path:
                i.printRule()
            print("\n")

        else:
            print("o resultado foi encontrado sem nenhum desperdício de pesquisas com falha.")

    else:
        print("Nao foi encontrado o caminho para o objetivo... ", "\n")
        print("o caminho procurado foi: ")
        for i in path:
            i.printRule()
        print("")

## Main
filename = None
if len(sys.argv) >= 2:
    filename = sys.argv[1]

Rules = []
if filename is None:
    print("Necessario um nome de arquivo como parametro")
    exit()

if filename is not None:
    test_file = open(filename, "r")
    content = test_file.readlines()
    for line in content:
        Rules.append(parse(line))
    test_file.close()

print("As Regras sao :")
for i in Rules:
    i.printRule()
print("\n\n")

Goals = []
another = "yes"
while another != "no":
    theInput = input("Insira uma query: ")
    Goals.append(theInput)
    another = input("Gostaria de inserir outra query(yes/no): ")

print("Queries requisitadas pelo usuario: ")
print(Goals, sep = ',')


print("O algoritmo foi iniciado...", "\n\n")


for i in range(len(Goals)):
    goals = []
    goals.append(Goals[i]) 
    print("***resolvendo a query ", goals[0])
    print("\n")
    solutionForEachQuery(Rules, goals)
    print("\n\n")