class StringUtility:
    def vowels(self, s):
        # Initialize the vowel counter to 0
        vowel_count = 0

        # Loop through each character in the string
        for ch in s:
            # Check if the character is a vowel
            if ch in 'aeiouAEIOU':
                # If it is, increment the vowel counter
                vowel_count += 1

        # Check if the vowel count is 5 or more
        if vowel_count >= 5:
            # If it is, return 'many'
            return 'many'
        else:
            # Otherwise, return the vowel count as a string
            return str(vowel_count)

   
    def bothEnds(self, s):
        # Check if the length of the string is less than or equal to 2
        if len(s) <= 2:
            # If it is, return an empty string
            return ''
        else:
            # Otherwise, return a new string made up of the first two and last two characters of the original string
            return s[:2] + s[-2:]

    def fixStart(self, s):
        # Check if the length of the string is less than or equal to 1
        if len(s) <= 1:
            # If it is, return the original string
            return s
        else:
            # Otherwise, initialize a new string to hold the modified string
            new_s = ''

            # Loop through each character in the string, starting from the second character
            for i in range(1, len(s)):
                # Check if the character matches the first character of the string
                if s[i] == s[0]:
                    # If it does, replace it with an asterisk
                    new_s += '*'
                else:
                    # Otherwise, add the character to the modified string as is
                    new_s += s[i]

            # Return the modified string with the first character of the original string appended to the front
            return s[0] + new_s

    def asciiSum(self, s):
        # Initialize the total to 0
        total = 0

        # Loop through each character in the string
        for ch in s:
            # Add the ASCII value of the character to the total
            total += ord(ch)

        # Return the total
        return total

    def cipher(self, s):
        # Initialize a new string to hold the encoded string
        encoded_s = ''

        # Loop through each character in the string
        for ch in s:
            # Check if the character is a letter
            if ch.isalpha():
                # If it is, increment its ASCII value by the length of the string, and make sure to account for wrap around
                if ch.islower():
                    encoded_s += chr((ord(ch) - ord('a') + len(s)) % 26 + ord('a'))
                else:
                    encoded_s += chr((ord(ch) - ord('A') + len(s)) % 26 + ord('A'))
            else:
                # If the character is not a letter, add it to the encoded string as is
                encoded_s += ch
        
        # Return the encoded string
        return encoded_s
