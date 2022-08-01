class Evaluate:
 #This class validates and evaluate postfix expression.
 #Attributes:
 # top: An integer which denotes the index of the element at the top of the stack currently.
 # size_of_stack: An integer which represents the size of stack.
 # stack: A List which acts as a Stack.


  def __init__(self, size):
  #Inits Evaluate with top, size_of_stack and stack.
  # Arguments:
  # size_of_stack: An integer to set the size of stack.
    self.top = -1
    self.size_of_stack = size
    self.stack = []


  def isEmpty(self):
    #Check whether the stack is empty.
    #Returns:
    # True if it is empty, else returns False
      return len(self.stack) == 0


  def pop(self):
    #Do pop operation if the stack is not empty.
    #Returns:
    # The data which is popped out if the stack is not empty.
    if not self.isEmpty():
      self.top -= 1
      return self.stack.pop(-1)
    


  def push(self, operand):
   #Push the operand to stack if the stack is not full.
   #Arguments:
   # operand: The operand to be pushed.
    if len(self.stack) < self.size_of_stack:
      self.top += 1
      self.stack.append(operand)
      


  def validate_postfix_expression(self, expression):
    #Check whether the expression is a valid postfix expression.
    #Arguments:
    # expression: A list which represents the expression to be validated.
    #Returns:
    # True if the expression is valid, else returns False
    operands = [element for element in expression if element.isdigit()]
    operators = [element for element in expression if element in ["+", "-", "*", "/", "^"]]
    if (len(operands) + len(operators)) == len(expression) and len(operands) == len(operators) + 1:
        return expression[0] not in operators and expression[1] not in operators


  def evaluate_postfix_expression(self, expression):
    #Evaluate the postfix expression
    #Arguments:
    # expression: A list which represents the the expression to be evaluated
    #Returns:
    # The result of evaluated postfix expression.
    self.stack = []
    for element in expression:
      if element.isdigit():
        self.push(int(element))
      elif element in ["+", "-", "*", "/", "^"]:
        if element == "+":
          result = self.stack[-2] + self.stack[-1]
        elif element == "-":
          result = self.stack[-2] - self.stack[-1]
        elif element == "*":
          result = self.stack[-2] * self.stack[-1]
        elif element == "/":
          result = self.stack[-2] // self.stack[-1]
        elif element == "^":
          result = self.stack[-2] ** self.stack[-1]
        self.pop()
        self.pop()
        self.push(result)
    return self.pop()


# Do not change the following code
postfix_expression = input() # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
 
    
