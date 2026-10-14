def group_by_signature(words: list) -> list:
    head = []
    result = []

    for i in words:
        head.append("".join(sorted(i)))
    wordhead = list(set(head))
    for j in wordhead:
        chack = []
        for j in words:
            if i == "".join(sorted(j)):
                chack.append(j)
        result.append(chack)

    return result

if __name__ == "__main__":
    # Example 1
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # Output: [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]
    