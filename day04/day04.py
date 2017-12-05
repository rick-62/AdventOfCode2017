# day 4

def check_validity(passphrase):
    """check none of words in passphrase don't match"""
    word_list = []
    passphrase = passphrase.strip('\n')
    for word in passphrase.split():
        if word in word_list:
            return 0
        word_list.append(word)
    return 1
    
def reorder_words(passphrase):
    """reorder words before checking validity"""
    ordered_passphrase = []
    for word in passphrase.split():
        ordered_word = ''.join(sorted(word))
        ordered_passphrase.append(ordered_word)
    return ' '.join(ordered_passphrase)

if __name__ == '__main__':
    with open("input.txt") as f:
        counter1 = 0
        counter2 = 0
        for passphrase in f:
            counter1 += check_validity(passphrase)
            counter2 += check_validity(reorder_words(passphrase))
            
        print("part1:",counter1)
        print("part2:",counter2)

        

