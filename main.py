import os

ENTRY = 'You still fold the corner of every page you love, like the book might forget you — and every time I find one, I fall for you all over again.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
