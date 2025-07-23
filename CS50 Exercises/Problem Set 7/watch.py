
import re

def main():
    print(parse(input("HTML: ")))

def parse(string):
    if string := re.search(r"<iframe.+src=['\"](https?://(www\.)?youtube\.com/embed/[0-9a-z]+)['\"].+", string, re.IGNORECASE):
        yt_link = string.group(1)
        embed_code = re.search(r"https?://(?:www\.)?youtube\.com/embed/([0-9a-z]+)", yt_link, re.IGNORECASE)
        embed_code = embed_code.group(1)

        return f"https://youtu.be/{embed_code}"


if __name__ == "__main__":
    main()
