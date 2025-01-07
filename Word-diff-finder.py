def compare_texts(content1, content2):
    # Convert the content into sets of unique words
    words1 = set(content1.split())
    words2 = set(content2.split())

    # Find differences
    only_in_file1 = words1 - words2
    only_in_file2 = words2 - words1

    # Print the results
    print("Words only in the first text:")
    for word in sorted(only_in_file1):
        print(f"  {word}")
    print("\nTotal differences:", len(only_in_file1))
    print("\n//////////////////////////////////////////////")
    print("\nWords only in the second text:")
    for word in sorted(only_in_file2):
        print(f"  {word}")
    print("\nTotal differences:", len(only_in_file2))

def get_multiline_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)

if __name__ == "__main__":
    print("Welcome to Word-diff-finder!")
    keep_going = True

    while keep_going:
        print("\n Please enter the first text than add an empty line:")
        text1 = get_multiline_input("> ")

        print("\n Please enter the second text than add an empty line:")
        text2 = get_multiline_input("> ")

        compare_texts(text1, text2)

        print("\nDo you want to compare another texts? (yes/no)")
        if input().strip().lower() != "yes":
            keep_going = False
