







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

for something in line:
    for match in re.match("opening_regex_here",line):
        count += 1
    for match in re.match("closing_regex_here",line):
        count2 += 1

    return count

def run_event_loop():
    while True:
        filename = input("Please enter the name of HTML file: ")

        tags = 0
        data = load(filename)
        for line in data:
            tags = tags + count_tags(line)
        print(tags)
        cont = input("would you like to count another html file (Y/N)? ")
        if cont == "N":
            print("Thank you for using the HTML Tag counter. Goodbye!")


print("Welcome to the HTML counter")
print("")

run_event_loop()
main()

