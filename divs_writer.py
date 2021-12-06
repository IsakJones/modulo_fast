

for i in range(2, 1000):
    with open(f"modulo/divisible{i}.py", "w") as f:
        header = f"def divisible{i}(x):\n"
        for j in range(0, 1000, i):
            header += f"\tif x == {j}:\n\t\treturn True\n"
        header += "\treturn False"
        f.write(header)
            
