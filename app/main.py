def copy_file(command: str) -> None:
    lines = command.split()
    if len(lines) != 3 or lines[0] != "cp":
        print("Invalid command")
        return

    source_file, target_file = lines[1], lines[2]
    if source_file == target_file:
        return
    try:
        with open(source_file, "r") as file_in, \
                open(target_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
