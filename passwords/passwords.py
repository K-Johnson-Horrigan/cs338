# Author: Kai Johnson


###### COPIED FROM JEFF ONDICH, CARLETON COLLEGE ######
import hashlib
import binascii


words = [line.strip().lower() for line in open('words.txt')]

def get_hash(password): #copied code from Jeff!
    encoded_password = password.encode('utf-8')
    hasher = hashlib.sha256(encoded_password)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string
    return digest_as_hex_string
###### END OF COPIED FROM JEFF ONDICH, CARLETON COLLEGE ######

def crack_passwords1():
    num_hashes_computed = 0
    num_passwords_cracked = 0

    hashed_words = {}
    for word in words:
        hashed_words[get_hash(word)] = word
        num_hashes_computed = num_hashes_computed + 1

    cracked1 = open("cracked1.txt", "w")
    hashed_logins = [line.strip().split(":") for line in open('passwords1.txt')]
    for hashed_login in hashed_logins:
        num_passwords_cracked = num_passwords_cracked + 1
        user = hashed_login[0]
        hashed_pwd = hashed_login[1]
        cracked_login = user + ":" + hashed_words[hashed_pwd] + "\n"
        cracked1.write(cracked_login)
    cracked1.close()

    print("num hashes computed: ", num_hashes_computed)
    print("num passwords cracked: ", num_passwords_cracked)

def crack_passswords2():
    num_hashes_computed = 0
    num_passwords_cracked = 0
    words.append("")
    cracked_file = open("cracked2.txt", "w")
    hashed_logins = [line.strip().split(":") for line in open('passwords2.txt')]
    hashed_logins_dict = {}
    for user in hashed_logins:
        hashed_logins_dict[user[1]] = user[0]

    for word in words:
        for word2 in words:
            word_combo = word + word2
            word_hash = get_hash(word_combo)
            num_hashes_computed = num_hashes_computed + 1
            if(word_hash in hashed_logins_dict):
                num_passwords_cracked = num_passwords_cracked + 1
                cracked_login = hashed_logins_dict[word_hash] + ":" + word_combo + "\n"
                cracked_file.write(cracked_login)

                print("cracked: ", num_passwords_cracked, "computed:", num_hashes_computed, cracked_login, end="")
                #just for my own sanity, print how many I've gotten so far
            #end user info if
        #end loop 2 for words
    #end loop 1 for words


    cracked_file.close()

    print("num hashes computed: ", num_hashes_computed)
    print("num passwords cracked: ", num_passwords_cracked)

def crack_passswords3():
    num_hashes_computed = 0
    num_passwords_cracked = 0

    cracked_file = open("cracked3.txt", "w")
    hashed_logins = []
    for line in open('passwords3.txt'):
        split_by_colon = line.strip().split(":")
        split_by_dollar = split_by_colon[1].split("$")
        hashed_logins.append([split_by_colon[0], split_by_dollar[2], split_by_dollar[3]])


    for hashed_login in hashed_logins:
        username = hashed_login[0]
        salt = hashed_login[1]
        hashed_pwd = hashed_login[2]
        for word in words:
            combo = salt + word
            num_hashes_computed = num_hashes_computed + 1
            if(get_hash(combo) == hashed_pwd):
                num_passwords_cracked = num_passwords_cracked + 1
                cracked_login = username + ":" + word + "\n"
                cracked_file.write(cracked_login)
                print(num_passwords_cracked, cracked_login, end="") # a sanity "program is still running" print, even though it slows it down
                break
    cracked_file.close()

    print("num hashes computed: ", num_hashes_computed)
    print("num passwords cracked: ", num_passwords_cracked)

#crack_passwords1()
#crack_passwords2()
#crack_passwords3()
