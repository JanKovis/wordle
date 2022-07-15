import itertools


if __name__ == "__main__":
    all_chars = set()
    czech_characters = "ěščřžýáíéůqwertyuiopasdfghjklzxcvbnm"
    for c in czech_characters:
        all_chars.add(c)

    # CHANGE HERE
    #
    # green characters must fit on position and be left-padded by spaces
    precise = " u e"

    # list of oranges along with zero-index position where it does not fit (3rd position is expressed as 2)
    orange_desc = {"l": [2], "c": [4]}

    # set the characters that do not belong to the word
    not_contained = set()
    for c in "žrtyiopad":
        not_contained.add(c)
    #
    # DO NOT CHANGE ANY FURTHER

    oranges = set(orange_desc.keys())
    orange_options = list(itertools.product("o", oranges, repeat=1))
    print(orange_options)

    free_chars = all_chars - not_contained - oranges
    unused_options = list(itertools.product("f", free_chars, repeat=1))
    print(unused_options)

    FINAL_LENGTH = 5
    while len(precise) < FINAL_LENGTH:
        precise += " "
    precise = precise[:FINAL_LENGTH]  # to be sure if someone is too eager on left blank padding

    word_count = 0
    fillings = itertools.permutations(
        orange_options + unused_options, r=precise.count(" ")
    )
    for f in fillings:
        contained_oranges = set()
        for subf in f:
            if subf[0] == "o":
                contained_oranges.add(subf[1])

        if contained_oranges != oranges:
            continue

        # complete the word into the blanks
        space_index = 0
        completed = ""
        for c in precise:
            if c == " ":
                completed += f[space_index][1]
                space_index += 1
            else:
                completed += c

        # exclude the known orange positions
        is_orange_in_forbidden_position = False
        for idx, c in enumerate(completed):
            if c in orange_desc:
                is_orange_in_forbidden_position = idx in orange_desc[c]
                if is_orange_in_forbidden_position:
                    break

        if is_orange_in_forbidden_position:
            continue

        print(completed)
        word_count += 1

    print(f"\nWord count is {word_count}")
