'''
Token Types

EOF (end-of-file) token is used to indicate that there is no more input left
for lexical analysis

'''

INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'EOF'

class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0,1,2,3,4,5,6,7,8,9,'+','-','*','/' or None
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
        return self.__str__()




######################################################################################

class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text
        #self.pos is an index into self.text
        self.pos = 0
        #current token instance
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error parsing input')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result=''
        while self.current_char is not None and self.current_char.isdigit():
            result =  result + self.current_char
            self.advance()
        #print("integer() called: "+ str(result))
        return int(result)

    def get_next_token(self):
        """
        Lexical Analyzer (also know as scanner or tokenizer)
        This method is responsible for breaking a sentence apart into tokens.
        One Token at a time.
        """

        #print(self.current_char)
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')
            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            if self.current_char == '*':
                self.advance()
                return Token(MULTIPLY, '*')
            if self.current_char == '/':
                self.advance()
                return Token(DIVIDE, '/')
            self.error()
        return Token(EOF, None)



        """
        is self.pos index past the end of self.text?
        if so, then return EOF TOKEN because there is no more input left
        to convert into tokens

        if self.pos > len(text) -1:
            return Token(EOF, None)


       "
        get a char at the position self.pos and decide what token to create
        based on the single char

       "
        current_char = text[self.pos]



       "
        if the character s a digit, then convert it to integer, create an integer
        TOKEN, increment self.pos index to point to the next character after the
        digit, and return the INTEGER TOKEN
        "
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
        """





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
        # expect curr token to be single digit integer
        left = self.current_token
        self.eat(INTEGER)

        while self.current_token.type != EOF :

            #expect curr token to be '+' or '-'
            op = self.current_token
            if op.type == PLUS:
                self.eat(PLUS)
            elif op.type == MINUS:
                self.eat(MINUS)
            elif op.type == MULTIPLY:
                self.eat(MULTIPLY)
            elif op.type == DIVIDE:
                self.eat(DIVIDE)
            else:
                self.error()

            # we expect the current token to be a single digit integer
            right=self.current_token
            self.eat(INTEGER)

            interResult = 0
            if op.type == PLUS:
                interResult = left.value + right.value
            elif op.type == MINUS:
                interResult = left.value - right.value
            elif op.type == MULTIPLY:
                interResult = left.value*right.value
            elif op.type == DIVIDE:
                interResult = left.value/right.value
            else:
                self.error()
            left = Token(INTEGER,interResult)
        return left.value


        # after the above call, self.current_token is set to EOF token


        """
        at this point we have successfully found INT PLUS INT sequence of tokens
        and we return the result of adding the two integers, thus effectively
        interpreting client input

        #pre-proccessing
        lnum = 0
        for i in range(0,len(left)):
            lnum = lnum*10 + left[i].value
        rnum = 0
        for i in range(0,len(right)):
            rnum = rnum*10 + right[i].value


        # update to handle subtractions
        if op.type == PLUS:
            result = left.value + right.value
        elif op.type == MINUS:
            result = left.value - right.value
        elif op.type == MULTIPLY:
            result = left.value * right.value
        elif op.type == DIVIDE:
            result = left.value / right.value
        else:
            self.error()
        return result
        """

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
        '''
        text = text.strip()
        text = text.split()
        tempText = ""
        for a in text:
            tempText = tempText + a
        text = tempText

        '''
        #print(text)
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()




