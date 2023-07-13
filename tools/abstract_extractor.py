input_filename = "abstract_input.txt"
output_filename = "abstract_output.txt"

with open(input_filename, "r") as f:
    text = f.read()

strings = []

for line in text.split('\n'):
    if line.startswith("AB - "):
        strings.append(line[5:])

with open(output_filename, "w") as f:
    f.write("\n".join(strings))

