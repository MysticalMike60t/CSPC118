# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///


import urllib.request


def main() -> None:
    url = "http://redefininggravity.com/web/web2"
    file = "index.html"
    urllib.request.urlretrieve(url, file)
    for line in open(file, "r"):
        print(line)


if __name__ == "__main__":
    main()
