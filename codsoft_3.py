import string
import secrets
import pyperclip

def get_user_preferences():
    print("\n--- Password Generator ---")
    length = int(input("Enter desired password length (min 8): "))
    if length < 8:
        print("Password should be at least 8 characters for better security.")
        return None

    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include special symbols? (y/n): ").lower() == 'y'

    if not any([include_upper, include_lower, include_digits, include_symbols]):
        print("❌ At least one character type must be selected.")
        return None

    return {
        'length': length,
        'upper': include_upper,
        'lower': include_lower,
        'digits': include_digits,
        'symbols': include_symbols
    }

def generate_password(settings):
    characters = ''
    if settings['upper']:
        characters += string.ascii_uppercase
    if settings['lower']:
        characters += string.ascii_lowercase
    if settings['digits']:
        characters += string.digits
    if settings['symbols']:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(settings['length']))
    return password

def check_strength(password):
    length = len(password)
    complexity = sum([
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password)
    ])
    if length >= 10 and complexity == 4:
        return "🟢 Strong"
    elif length >= 9 and complexity >= 3:
        return "🟡 Medium"
    else:
        return "🔴 Weak"

def main():
    settings = get_user_preferences()
    if not settings:
        return

    password = generate_password(settings)
    strength = check_strength(password)

    print(f"\n🔐 Your Password: {password}")
    print(f"📊 Strength: {strength}")

    try:
        pyperclip.copy(password)
        print("📋 Password copied to clipboard!")
    except Exception:
        print("⚠️ Could not copy to clipboard (pyperclip not installed).")

if __name__ == "__main__":
    main()
