import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def get_number(prompt):
    """ask the user for a number and return it as float. Supports 'q' to quit."""
    while True:
        s = input(prompt).strip()
        if s.lower() in ('q', 'quit', 'exit'):
            print("exiting, bye!")
            exit()
        try:
            return float(s)
        except ValueError:
            print("invalid input - a number is required, try again or 'q' to quit")


def get_operation(prompt):
    """ask for an operation and return '+', '-', '*', '/'."""
    while True:
        op = input(prompt).strip()
        if op in ops or op.lower() == 'done':
            return op
        if op.lower() in ('q', 'quit', 'exit'):
            print("exiting, bye!")
            exit()
        print("invalid operation. use +, -, *, /, or 'done' to finish (or 'q' to quit)")


def main():
    print("hey thats just an calculator\n")  # теперь выводится при запуске

    while True:
        result = get_number("enter the first number: ")

        while True:
            op = get_operation("choose an operation (+, -, *, /) or 'done' to finish: ")
            if op.lower() == 'done':
                break

            num = get_number("enter the next number: ")

            if op == '/' and num == 0:
                print("error: division by zero is not allowed.")
                continue

            result = ops[op](result, num)

            # print result nicely
            if isinstance(result, float) and result.is_integer():
                print("current result:", int(result))
            else:
                print("current result:", result)

        print("final result:", result, "\n")

        again = input("another calculation? (Enter = yes, q = no): ").strip().lower()
        if again in ('q', 'quit', 'exit'):
            print("bye!")
            break


# вот эта строка — главное отличие!
if __name__ == "__main__":
    main()
