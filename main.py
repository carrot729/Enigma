from simple_replace import simple_replace, rotors


def main():
    r_word1 = ''
    r_word2 = ''
    r_word3 = ''
    with open("replace_word1.txt", "r") as f:
        for line in f:
            r_word1 += line.strip()
        f.close()
    with open("replace_word2.txt", "r") as f:
        for line in f:
            r_word2 += line.strip()
        f.close()
    with open("replace_word3.txt", "r") as f:
        for line in f:
            r_word3 += line.strip()
        f.close()
    password = input("Enter password: ")
    rotor1 = input("Enter rotor 1: ")
    rotor2 = input("Enter rotor 2: ")
    rotor3 = input("Enter rotor 3: ")
    rotor1 = ord(rotor1) - ord('A')
    rotor2 = ord(rotor2) - ord('A')
    rotor3 = ord(rotor3) - ord('A')
    for i in range(rotor1):
        r_word1=rotors(r_word1)
    for i in range(rotor2):
        r_word2=rotors(r_word2)
    for i in range(rotor3):
        r_word3=rotors(r_word3)
    print('Running:', end='')
    new_pass = simple_replace(password, r_word1, r_word2, r_word3)
    print('New password:', end='')
    print(new_pass)


if __name__ == '__main__':
    main()
