from deep_translator import GoogleTranslator

# deep_translator has its own languages dict
LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)
# returns {'afrikaans': 'af', 'albanian': 'sq', 'english': 'en', ...}
# NOTE: this is flipped from googletrans — name:code instead of code:name

languages_codes = set(LANGUAGES.values())               # {'af', 'sq', 'en', ...}
languages_names = {k.lower(): v for k, v in LANGUAGES.items()}  # {'english': 'en', ...}

def resolve_language(user_input):
    user_input = user_input.strip().lower()
    if user_input in languages_codes:
        return user_input
    elif user_input in languages_names:
        return languages_names[user_input]
    return None

def show_supported_languages():
    print("\nSupported languages:")
    for name, code in LANGUAGES.items():
        print(f"  {code}: {name}")

def main():
    print("=== Google Translator ===\n")

    src_input = input("Translate FROM (language name or code): ").strip()
    src_code = resolve_language(src_input)
    if not src_code:
        print(f"[Error] '{src_input}' is not a recognized language.")
        show_supported_languages()
        return

    text = input("Enter the word or phrase to translate: ").strip()
    if not text:
        print("[Error] No text entered.")
        return

    dest_input = input("Translate TO (language name or code): ").strip()
    dest_code = resolve_language(dest_input)
    if not dest_code:
        print(f"[Error] '{dest_input}' is not a recognized language.")
        show_supported_languages()
        return

    try:
        result = GoogleTranslator(source=src_code, target=dest_code).translate(text)
        print(f"\nOriginal  ({src_input.title()}): {text}")
        print(f"Translated ({dest_input.title()}): {result}")
    except Exception as e:
        print(f"[Translation Error] {e}")
        print("Tip: Try again shortly.")

if __name__ == "__main__":
    main()