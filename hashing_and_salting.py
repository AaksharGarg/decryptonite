import hashlib
import os

def salted_hash(password):
    # Generate a random salt
    salt = os.urandom(32)

    # Add the salt to the password and hash it using SHA-256
    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()

    # Return the salt and hashed password as a tuple
    return (salt, hashed_password)

# Example usage
password = "mypassword12456"
salt, hashed_password = salted_hash(password)

print("Salt: ", salt)
print("Hashed password: ", hashed_password)
