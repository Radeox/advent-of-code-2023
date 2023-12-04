import re


def solution():
    sum = 0

    with open("input.txt", "r") as f:
        # Read the first line
        line = f.readline()

        while line:
            # Remove all non-digits
            line = re.sub("[^0-9]", "", line)

            # Get digits we need and sum them to total
            num = int(line[0] + line[-1])
            sum += num

            # Read the next line
            line = f.readline()

    return sum


if __name__ == "__main__":
    print(f"Solution: {solution()}")
