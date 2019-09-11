
def banner(subject, author):
    subject_length = len(subject)
    by_line = f"By {author}"
    banner_length = subject_length + 4
    print("=" * banner_length)
    print(f" {subject}")
    print(f" By {author}")
    print("=" * banner_length)
    print("")

if __name__ == "__main__":
    banner("BANNER", "Skyler")
    subject = input("What's the subject?")
    author = input("Who's the author?")
    banner(subject, author)