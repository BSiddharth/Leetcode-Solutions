name_of_file = input("Provide name of file in {Num. Name} format: ")
dot_index = name_of_file.find(".")
name_of_file = name_of_file[dot_index + 2 :]
name_of_file = name_of_file.lower()
leetcode_naming = name_of_file.replace(" ", "-")
name_of_file = name_of_file.replace(" ", "_")


with open(f"{name_of_file}.py", "w") as f:
    f.write(f"# https://leetcode.com/problems/{leetcode_naming}/description/")
    f.write("\n")
    f.write(f'# git add . && git commit -m "completed {name_of_file}" && git push')

print(f"{name_of_file}.py generated")
