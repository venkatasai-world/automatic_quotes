import random

with open("quotes.txt", "r", encoding="utf-8") as file:
    quotes = [line.strip() for line in file if line.strip()]

quote = random.choice(quotes)
print(f'"{quote}"')
