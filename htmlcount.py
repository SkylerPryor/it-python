
import os
from banner import banner
banner(" HTML TAG COUNTER"," Skyler")



def load(filename):
    data = []

    if os.path.exists(filename):
        print(f"..... loading from {filename}")
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def main():
    run_event_loop()

def count_tags(line):
    count = 0
    previous_char = None
    for char in line:
        if char  != "/" and previous_char == "<":
            count += 1
        previous_char = char





    return count

def run_event_loop():
    while True:
        filename = input("Please enter the name of HTML file: ")

        tags = 0
        data = load(filename)
        for line in data:
            line_tags = count_tags(line)
            tags = tags + count_tags(line)
        print(f"The file {filename} contains {tags} tags.")
        name = input("would you like to count another html file (Y/N)? ")
        if name == "N":
            print("Thank you for using the HTML Tag counter. Goodbye!")
            break


print("Welcome to the HTML counter")
print("")


main()