def hamming_dist(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")

    # Count differing positions
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))


s1 = "karolin"
s2 = "kathrin"

dist = hamming_dist(s1, s2)

print(f"Hamming Distance between '{s1}' and '{s2}': {dist}")