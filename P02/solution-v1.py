import re


def solution():
    with open("input.txt", "r") as f:
        # Read first line
        line = f.readline()
        sum = 0

        # Valid cubes (R,G,B)
        cubes = [12, 13, 14]

        while line:
            # Do something with line
            id = line.split(" ")[1].replace(":", "")
            valid = True

            # Check each set of cubes
            for s in line.split(":")[1].split(";"):
                s = s.strip()

                draw_cubes = [0, 0, 0]

                # Examine each cube color
                for c in s.split(","):
                    c = c.strip()

                    # Remove all non-numeric characters
                    num = int(re.sub("[^0-9]", "", c))

                    if "red" in c:
                        draw_cubes[0] += num
                    elif "green" in c:
                        draw_cubes[1] += num
                    elif "blue" in c:
                        draw_cubes[2] += num

                # Check if game is valid
                for i in range(3):
                    if draw_cubes[i] > cubes[i]:
                        valid = False
                        break

            if valid:
                sum += int(id)

            # Read next line
            line = f.readline()

        return sum


if __name__ == "__main__":
    print(f"Solution: {solution()}")
