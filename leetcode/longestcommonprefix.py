def longestCommonPrefix(strs):
    """
    Finds the longest common prefix string amongst an array of strings.

    Args:
        strs: A list of strings.

    Returns:
        The longest common prefix string, or "" if there is no common prefix.
    """

    # Handle the edge case of an empty list
    if not strs:
        return ""

    # Use the first string as our reference point
    first_string = strs[0]

    # Iterate through the characters of the first string
    for i in range(len(first_string)):
        char = first_string[i]

        # Compare this character with the character at the same position
        # in all other strings
        for j in range(1, len(strs)):
            # Check for two conditions:
            # 1. The current string is shorter than our current prefix length (i)
            # 2. The characters at position i don't match
            if i >= len(strs[j]) or strs[j][i] != char:
                # If a mismatch is found, return the prefix we've built so far
                return first_string[:i]

    # If the loop completes without finding any mismatches,
    # it means the entire first string is the common prefix.
    return first_string

# Example usage:
strs1 = ["flower", "flow", "flight"]
print(f"Input: {strs1}, Output: {longestCommonPrefix(strs1)}")

strs2 = ["dog", "racecar", "car"]
print(f"Input: {strs2}, Output: {longestCommonPrefix(strs2)}")

strs3 = ["apple", "apricot", "application"]
print(f"Input: {strs3}, Output: {longestCommonPrefix(strs3)}")

strs4 = ["a"]
print(f"Input: {strs4}, Output: {longestCommonPrefix(strs4)}")