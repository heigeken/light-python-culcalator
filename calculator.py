import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def get_number(prompt):
    while True:
        s = input(prompt).strip()
        if s.lower() in ('q', 'quit', 'exit'):
            exit()
        try:
            return float(s)
        except ValueError:
            print("invalid input")

def get_operation(prompt):
    while True:
        op = input(prompt).strip()
        if op in ops or op == 'done':
            return op
        if op.lower() in ('q', 'quit', 'exit'):
            exit()
        print("invalid operation")

def main():
    print("calculator\n")

    while True:
        result = get_number("first number: ")

        while True:
            op = get_operation("operation (+, -, *, /) or 'done': ")
            if op == 'done':
                break

            num = get_number("next number: ")

            if op == '/' and num == 0:
                print("division by zero")
                continue

            result = ops[op](result, num)
            print("result:", int(result) if result.is_integer() else result)

        print("final:", result, "\n")

        if input("again? (q = no): ").strip().lower() in ('q', 'quit', 'exit'):
            break

if __name__ == "__main__":
    main()
