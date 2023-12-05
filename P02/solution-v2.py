import re


def solution():
    with open("input.txt", "r") as f:
        # Read first line
        line = f.readline()
        sum = 0

        while line:
            # We need to get the minimal valid set of cubes
            min_cubes = [0, 0, 0]

            # Check each set of cubes
            for s in line.split(":")[1].split(";"):
                s = s.strip()

                # Examine each cube color
                for c in s.split(","):
                    c = c.strip()

                    # Remove all non-numeric characters
                    num = int(re.sub("[^0-9]", "", c))

                    if "red" in c:
                        min_cubes[0] = max(num, min_cubes[0])
                    elif "green" in c:
                        min_cubes[1] = max(num, min_cubes[1])
                    elif "blue" in c:
                        min_cubes[2] = max(num, min_cubes[2])

            # Compute game power
            power = min_cubes[0] * min_cubes[1] * min_cubes[2]

            # Add to total power
            sum += power

            # Read next line
            line = f.readline()

        return sum


if __name__ == "__main__":
    print(f"Solution: {solution()}")
