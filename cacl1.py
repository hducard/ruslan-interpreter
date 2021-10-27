'''
Token Types

EOF (end-of-file) token is used to indicate that there is no more input left
for lexical analysis

'''

INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0,1,2,3,4,5,6,7,8,9,'+','-' or None
        self.value = value

    def __str__(self):
        """
        String Representation of class instance

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
        """
        return 'Token({type}, {value})'.format(
            type = self.type,
            value = repr(self.value)
        )

    def __repr__(self):
        return elf.__str__()

class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text
        #self.pos is an index into self.text
        self.pos = 0
        #current token instance
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """
        Lexical Analyzer (also know as scanner or tokenizer)
        This method is responsible for breaking a sentence apart into tokens.
        One Token at a time.
        """
        text = self.text




        """
        is self.pos index past the end of self.text?
        if so, then return EOF TOKEN because there is no more input left
        to convert into tokens
        """
        if self.pos > len(text) -1:
            return Token(EOF, None)


        """
        get a char at the position self.pos and decide what token to create
        based on the single char

        """
        current_char = text[self.pos]



        """
        if the character s a digit, then convert it to integer, create an integer
        TOKEN, increment self.pos index to point to the next character after the
        digit, and return the INTEGER TOKEN
        """
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token
        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token
        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        self.error()





    def eat(self, token_type):
        """
        compare the current token type with the passed token type and if they
        match then eat the current token and assign the next token to the
        self.current_token, otherwise raise an exception
        """
        if (self.current_token.type == token_type):
            self.current_token = self.get_next_token()
        else:
            self.error()






    def expr(self):
        """
        expr -> INTEGER PLUS INTEGER
        """
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        #expect curr token to be single digit integer
        #opcode value to handle more operations
        opcode = 0
        left=[]
        while self.current_token.type == INTEGER:
            left.append(self.current_token)
            self.eat(INTEGER)


        #expect curr token to be '+' or '-'
        op = self.current_token
        if op.type == PLUS:
            opcode = 1
            self.eat(PLUS)
        elif op.type == MINUS:
            opcode = 2
            self.eat(MINUS)
        else:
            self.error()

        # we expect the current token to be a single digit integer
        right=[]
        while self.current_token.type == INTEGER:
            right.append(self.current_token)
            self.eat(INTEGER)

        # after the above call, self.current_token is set to EOF token


        """
        at this point we have successfully found INT PLUS INT sequence of tokens
        and we return the result of adding the two integers, thus effectively
        interpreting client input
        """
        #pre-proccessing
        lnum = 0
        for i in range(0,len(left)):
            lnum = lnum*10 + left[i].value
        rnum = 0
        for i in range(0,len(right)):
            rnum = rnum*10 + right[i].value

        # update to handle subtractions
        result = 0
        if opcode == 1:
            result = lnum + rnum
        elif opcode == 2:
            result = lnum - rnum
        else:
            self.error()
        return result

###############################################################################


def main():
    while True:
        try:
            """
            to run python3 replace raw_input' call with input
            """
            text = input('calc> ')

        except EOFError:
            break
        if not text:
            continue
        if text == "q" or text == 'quit':
            return
        # edit to handle white space and graciously exit the interpreter
        text = text.strip()
        text = text.split()
        tempText = ""
        for a in text:
            tempText = tempText + a
        text = tempText

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()




