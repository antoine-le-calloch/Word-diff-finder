from collections import Counter

def display_result(words, only_in_text, file_place):
    print(f"Words only in the {file_place} text:")
    print("Total differences:", len(only_in_text))
    for word in sorted(only_in_text):
        print(f"  {word}")
    print("Words that are duplicated in the text:")
    for key, value in Counter(words).items():
        if value > 1: print(f" {value}: {key}")

    print("\nResults as a list:")
    print(" ".join(only_in_text))


def compare_texts(text1, text2):
    words1 = text1.split()
    words2 = text2.split()

    # Find differences
    only_in_text1 = set(words1) - set(words2)
    only_in_text2 = set(words2) - set(words1)

    display_result(words1, only_in_text1, "first")
    print("\n//////////////////////////////\n")
    display_result(words2, only_in_text2, "second")


def get_multiline_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return " ".join(lines)


if __name__ == "__main__":
    print("Welcome to Word-diff-finder!")
    keep_going = True

    while keep_going:
        print("\n Please enter the first text than add an empty line:")
        multiline_input_1 = get_multiline_input("> ")

        print("\n Please enter the second text than add an empty line:")
        multiline_input_2 = get_multiline_input("> ")

        compare_texts(multiline_input_1, multiline_input_2)

        print("\nDo you want to compare another texts? (yes/no)")
        if input().strip().lower() != "yes":
            keep_going = False
