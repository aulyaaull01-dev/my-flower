def rpn_calculator():
    stack = []

    while True:
        cmd = input("integer, operator or 'print' ('stop' to stop): ").strip()

        if cmd.lower() == 'stop':
            print(f"Final stack: {stack}")
            break

        elif cmd.lower() == 'print':
            print(stack)

        # jika angka
        elif cmd.lstrip('-').isdigit(): # support angka negatif
            stack.append(int(cmd))
            print(stack)

        # jika operator
        elif cmd in ['+', '-', '*', '/', '^']:
            if len(stack) < 2:
                print("Error: stack butuh minimal 2 angka!")
                continue

            b = stack.pop()
            a = stack.pop()

            if cmd == '+':
                result = a + b
            elif cmd == '-':
                result = a - b # a yang bawah, b yang atas
            elif cmd == '*':
                result = a * b
            elif cmd == '/':
                result = a / b
            elif cmd == '^':
                result = a ** b

            stack.append(result)
            print(stack)

        else:
            print("Input tidak valid. Masukkan integer, +, -, *, /, atau 'stop'")

# jalankan
rpn_calculator()
