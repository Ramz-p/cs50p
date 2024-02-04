import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Use regular expression to extract YouTube URL from src attribute in iframe element
    match = re.search(r'<iframe .*?src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', s)

    if match:
        video_id = match.group(1)
        youtu_url = f"https://youtu.be/{video_id}"
        return youtu_url
    else:
        return None


if __name__ == "__main__":
    main()
