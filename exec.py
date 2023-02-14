print("Scanning Surrounding Area")

exec(open("Raddios.py").read())
with open("results.txt", "r") as file:
    print(file.read())
