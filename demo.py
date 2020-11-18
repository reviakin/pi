def upper_case_word(word):
    return word.upper()

print(__name__)

if __name__ == '__main__':

    greetings = ["hello", 'bonjour', 'hola']

    for greeting in greetings:
        print(f"greeting: {upper_case_word(greeting)}")

    name = "Dima"
    print(name)

    upper_case_name = upper_case_word(name)
    print(f"upper case name is {upper_case_name}")