import re



def main():
    print(parse(input("HTML: ")))


def parse(s):
    # sample : "http://www.youtube.com/embed/xvFZjo5PgG0"
    # sample : <iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>...
    matches = re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z_0-9]+)\"",s)
    if matches:
        video_id = matches.group(1)

        return('https://youtu.be/'+ video_id)
        # return('https://youtu.be/'+matches.group(1))


if __name__ == "__main__":
    main()
