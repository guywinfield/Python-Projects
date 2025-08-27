import re

def main():
    print(um_count(input("Input: ")))

def um_count(string):
    string = string.lower().strip()
    um_pattern = re.findall(r"(\bum\b)", string.strip(), re.IGNORECASE)

    count = 0
    for _ in um_pattern:
        count += 1

    return count

if __name__ == "__main__":
    main()
