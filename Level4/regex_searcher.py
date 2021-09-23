# Write a Python regex function to find sequences of lowercase letters joined with an underscore.
import re


def regex_snake_case(text):
    found_seqs = []
    regex = r"[a-z]+_[a-z]+"

    matches = re.finditer(regex, text, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        # print("Match {} was found at {}-{}: {}".format(matchNum, match.start(), match.end(), match.group()))
        found_seqs.append(match.group())
    return found_seqs


if __name__ == "__main__":
    test_text = "asdv_123feq_vfdfwer12_3w_2_3qwe_t"
    print(regex_snake_case(test_text))
