def main():
    text = input("Enter some text: ").strip()
    print(f"Here's the text with (AEIOU) omitted: {shorten(text)}")

def shorten(word):
    final_text = ""
    for letter in word:
        if letter not in "AEIOUaeiou":
            final_text += letter

    return final_text

if __name__ == "__main__":
    main()