import random

"""
Runs the befunge code

code: list - The code list to run. Should be a list of strings, each string being a row
input: list - The input given to the code
row: int - The starting row
column: int - The starting column
direction: str - The starting direction
string_mode: boolean - Start in string mode
stack: list - The starting stack

Returns the stack at end of program
"""
def run(code: list, input: list=[], row: int=0, column: int=0, direction: str="right", string_mode: bool=False, stack: list=[]):

    end = False
    skip = False

    try:
        cmd = code[row][column]
    except IndexError:
        raise RuntimeError(f"Invalid instruction")

    # Commands

    if not string_mode or cmd == "\"":

        match cmd:
            
            case ">":
                direction = "right"

            case "<":
                direction = "left"

            case "^":
                direction = "up"

            case "v":
                direction = "down"

            case "@":
                end=True

            case "#":
                skip=True
            
            case "+":
                stack.append(stack.pop() + stack.pop())
            
            case "-":
                stack.append(stack.pop() - stack.pop())
            
            case "*":
                stack.append(stack.pop() * stack.pop())
            
            case "/":
                stack.append(stack.pop() // stack.pop())
            
            case "%":
                stack.append(stack.pop() % stack.pop())
            
            case "!":
                value = stack.pop()
                if value == 0 or value == None:
                    stack.append(1)
                else:
                    stack.append(0)
            
            case "`":
                if stack.pop() <= stack.pop():
                    stack.append(1)
                else:
                    stack.append(0)
            
            case "?":
                rand_direction = random.randint(1, 4)

                if rand_direction == 1:
                    direction = "right"
                elif rand_direction == 2:
                    direction = "left"
                elif rand_direction == 3:
                    direction = "up"
                elif rand_direction == 4:
                    direction = "down"
            
            case "_":
                value = stack.pop()
                if value == 0 or value == None:
                    direction = "right"
                else:
                    direction = "left"
            
            case "|":
                value = stack.pop()
                if value == 0 or value == None:
                    direction = "down"
                else:
                    direction = "up"
            
            case "\"":
                if string_mode:
                    string_mode = False
                else:
                    string_mode = True
            
            case ":":
                try:
                    value = stack.pop()
                    stack.append(value)
                    stack.append(value)
                except IndexError:
                    stack.append(0)
            
            case "\\":
                value1 = stack.pop()
                value2 = stack.pop()
                stack.append(value1)
                stack.append(value2)
            
            case "$":
                stack.pop()
            
            case ".":
                print(stack.pop(), end=" ")
            
            case ",":
                print(chr(stack.pop()), end="")

            case "&":
                try:
                    stack.append(int(input.pop(0)))
                except IndexError:
                    raise RuntimeError("Unexpected end of input")
            
            case "~":
                try:
                    stack.append(ord(input.pop(0)))
                except IndexError:
                    raise RuntimeError("Unexpected end of input")
            
            case "p":
                y = stack.pop()
                x = stack.pop()
                value = stack.pop()

                code_list = list(code[y])
                code_list[x] = chr(value)

                code_str = ""
                for i in code_list:
                    code_str += str(i)
                
                code[y] = code_str
            
            case "g":
                y = stack.pop()
                x = stack.pop()

                stack.append(code[y][x])
            
            case " ":
                pass
            
            case _:
                try:
                    stack.append(int(cmd))
                except ValueError:
                    raise RuntimeError(f"Invalid instruction \"{cmd}\"")
    
    # String mode
    else:
        stack.append(ord(cmd))
    
    # End
    if end:
        return stack
    
    # Right
    if direction == "right":

        if skip:
            return run(code, input, row, column+2, direction, string_mode, stack)
        
        return run(code, input, row, column+1, direction, string_mode, stack)
    
    # Left
    elif direction == "left":

        if skip:
            return run(code, input, row, column-2, direction, string_mode, stack)
        
        return run(code, input, row, column-1, direction, string_mode, stack)
    
    # Down
    elif direction == "down":

        if skip:
            return run(code, input, row+2, column, direction, string_mode, stack)
        
        return run(code, input, row+1, column, direction, string_mode, stack)
    
    # Up
    elif direction == "up":

        if skip:
            return run(code, input, row-2, column, direction, string_mode, stack)
        
        return run(code, input, row-1, column, direction, string_mode, stack)