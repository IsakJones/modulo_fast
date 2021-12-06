
with open("modulo/divisible.py", "w") as file:
    text = ""
    for i in range(2, 1000):
        text += f"from divisible{i} import divisible{i}\n"
    text += "\n"

    text += "def div(x, i):\n"
    for i in range(2, 1000):
        text += f"\tif i == {i}:\n\t\treturn divisible{i}(x)\n"

    text += "\tprint(f'help, something went wrong with i={i}')\n"
    text += "\treturn False"

    file.write(text)
