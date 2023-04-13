import re
english_words = ['hello', 'good', 'cats', 'dogs']
def is_strong_password(password: str):
    password = password.lower()
    result = re.findall("\D{4,}", password)
    for word in result:
        if word in english_words:
            return False
    return True

if __name__ == "__main__":
    print(is_strong_password("55hell33o44cat55s5"))