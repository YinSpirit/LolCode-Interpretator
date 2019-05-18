
class LOLCodeInterpreter(object):

    def __init__(self, tree):
        self.__tree = tree
        self.__variables = dict()

    def execute_program(self):
        self.__variables['IT'] =  None
        self.__execute_statement_list(self.__tree)
        #print(self.__variables)

    def __execute_statement_list(self, statement_list):
        if statement_list:
            try:
                for statement in statement_list:
                    self.__execute_statement(statement)
            except Exception as e:
                print(e)

    def __execute_statement(self, statement):
        if not statement:
            return
        elif statement[0] == 'print':
            print(str(self.__evaluate_expression(statement[1])))
        elif statement[0] == 'get':
            self.__set_variable(statement[1], input())
        elif statement[0] == 'declare':
            self.__declare_variable(statement[1])
        elif statement[0] == 'define':
            self.__declare_variable(statement[1])
            self.__set_variable(statement[1], self.__evaluate_expression(statement[2]))
        elif statement[0] == 'assign':
            self.__set_variable(statement[1], self.__evaluate_expression(statement[2]))
        elif statement[0] == 'convert':
            if   statement[2] == 'YARN':
                self.__set_variable(statement[1], str(self.__get_variable(statement[1])))
            elif statement[2] == 'NUMBR':
                self.__set_variable(statement[1], int(self.__get_variable(statement[1])))
            elif statement[2] == 'NUMBAR':
                self.__set_variable(statement[1], float(self.__get_variable(statement[1])))
            elif statement[2] == 'TROOF':
                self.__set_variable(statement[1], bool(self.__get_variable(statement[1])))
            else:
                raise Exception("Cannot convert identifier: %s to type %s" % (statement[1], statement[2]))
        elif statement[0] == 'if':
            if self.__get_variable('IT'):
                self.__execute_statement_list(statement[1])
            elif len(statement) == 3:
                self.__execute_statement_list(statement[2])
        elif statement[0] == 'it':
            self.__set_variable('IT', self.__evaluate_expression(statement[1]))

    def __evaluate_expression(self, expression):
        try:
            if not isinstance(expression,list):
                return expression
            elif expression[0] == 'not':
                return not self.__evaluate_expression([1])
            elif expression[0] == 'logic':
                if expression[1] == 'BOTH OF':
                    return self.__evaluate_expression(expression[2]) and self.__evaluate_expression(expression[3])
                elif expression[1] == 'EITHER OF':
                    return self.__evaluate_expression(expression[2]) or self.__evaluate_expression(expression[3])
                elif expression[1] == 'WON OF':
                    return not (self.__evaluate_expression(expression[2]) and self.__evaluate_expression(expression[3]))
                elif expression[1] == 'BOTH SAEM':
                    return self.__evaluate_expression(expression[2]) == self.__evaluate_expression(expression[3])
                elif expression[1] == 'DIFFRINT':
                    return self.__evaluate_expression(expression[2]) != self.__evaluate_expression(expression[3])
            elif expression[0] == 'OP':
                if expression[1] == 'SUM OF':
                    return self.__evaluate_expression(expression[2]) + self.__evaluate_expression(expression[3])
                elif expression[1] == 'DIFF OF':
                    return self.__evaluate_expression(expression[2]) - self.__evaluate_expression(expression[3])
                elif expression[1] == 'PRODUKT OF':
                    return self.__evaluate_expression(expression[2]) * self.__evaluate_expression(expression[3])
                elif expression[1] == 'QUOSHUNT OF':
                    return self.__evaluate_expression(expression[2]) / self.__evaluate_expression(expression[3])
                elif expression[1] == 'MOD OF':
                    return self.__evaluate_expression(expression[2]) % self.__evaluate_expression(expression[3])
                elif expression[1] == 'BIGGR OF':
                    return max(self.__evaluate_expression(expression[2]), self.__evaluate_expression(expression[3]))
                elif expression[1] == 'SMALLR OF':
                    return min(self.__evaluate_expression(expression[2]), self.__evaluate_expression(expression[3]))
            elif expression[0] == 'ALL OF':
                return all([self.__evaluate_expression(expr) for expr in expression[1]])
            elif expression[0] == 'ANY OF':
                return any([self.__evaluate_expression(expr) for expr in expression[1]])
            elif expression[0] == 'value':
                return self.__get_variable(expression[1])
        except TypeError:
            raise Exception("Unsupported operand type ")

    def __get_variable(self, name):
        try:
            return self.__variables[name]
        except KeyError:
            raise Exception("Undeclared identifier: %s" % name)

    def __set_variable(self, name, value):
        if name in self.__variables:
            self.__variables[name] = value
        else:
            raise Exception("Undeclared identifier: %s" % name)

    def __declare_variable(self, name):
        if name not in self.__variables:
            self.__variables[name] = None
        else:
            raise Exception("Multiple declaration of identifier: %s" % name)
