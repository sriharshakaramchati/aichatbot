import re
from io import StringIO

def parse_chat(file):
    messages = []

    content = file.stream.read().decode("utf-8")
    lines = content.split('\n')

    for line in lines:
        match = re.match(r'\[(.*?)\] (.*?): (.*)', line)
        if match:
            timestamp, sender, message = match.groups()
            messages.append((timestamp, sender, message))

    return messages

