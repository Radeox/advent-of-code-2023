def solution():
    sum = 0

    with open("input.txt", "r") as f:
        # Read the first line
        line = f.readline()
        line = line.strip()

        while line:
            letters = []
            first_digit = None
            last_digit = None

            # Start searching for first digit
            for c in line:
                letters.append(c)

                if c.isdigit():
                    first_digit = c
                    break
                elif "one" in "".join(letters):
                    first_digit = 1
                    break
                elif "two" in "".join(letters):
                    first_digit = 2
                    break
                elif "three" in "".join(letters):
                    first_digit = 3
                    break
                elif "four" in "".join(letters):
                    first_digit = 4
                    break
                elif "five" in "".join(letters):
                    first_digit = 5
                    break
                elif "six" in "".join(letters):
                    first_digit = 6
                    break
                elif "seven" in "".join(letters):
                    first_digit = 7
                    break
                elif "eight" in "".join(letters):
                    first_digit = 8
                    break
                elif "nine" in "".join(letters):
                    first_digit = 9
                    break

            # Start searching for last digit
            letters = []

            for c in line[::-1]:
                letters.insert(0, c)

                if c.isdigit():
                    last_digit = c
                    break
                elif "one" in "".join(letters):
                    last_digit = 1
                    break
                elif "two" in "".join(letters):
                    last_digit = 2
                    break
                elif "three" in "".join(letters):
                    last_digit = 3
                    break
                elif "four" in "".join(letters):
                    last_digit = 4
                    break
                elif "five" in "".join(letters):
                    last_digit = 5
                    break
                elif "six" in "".join(letters):
                    last_digit = 6
                    break
                elif "seven" in "".join(letters):
                    last_digit = 7
                    break
                elif "eight" in "".join(letters):
                    last_digit = 8
                    break
                elif "nine" in "".join(letters):
                    last_digit = 9
                    break

            # Get digits we need and sum them to total
            num = int(f"{first_digit}{last_digit}")
            sum += num

            # Read the next line
            line = f.readline()

    return sum


if __name__ == "__main__":
    print(f"Solution: {solution()}")
