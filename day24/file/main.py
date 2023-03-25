with open("my_file.txt") as file:
    contents = file.read()
    mori = contents.replace("Zuko", "Kazu")
    print(mori)

