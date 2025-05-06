# Paste in the requested functions from your Coded Messages assignment.
# If you didn't complete that assignment, use the code from the
# LCHS-web-form-part-2 GitHub repository: https://github.com/LaunchCodeEducation/LCHS-web-form-part-2

def encrypt(text, rot):
    """
    Encrypts the given text using the Caesar cipher with the specified rotation.
    
    Args:
        text (str): The text to encrypt
        rot (int): The rotation value (0-25)
    
    Returns:
        str: The encrypted text
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Convert to 0-25 range, apply rotation, and wrap around
            rotated = (ord(char) - ascii_offset + rot) % 26
            # Convert back to ASCII
            result += chr(rotated + ascii_offset)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result
