import itertools
import string
import time

class SecuritySystem:
    def __init__(self):
        self.failed_attempts = 0
        self.max_limit = 5

    def check_password(self, guess, actual):
        # Defender Logic
        if self.failed_attempts >= self.max_limit:
            return "LOCKED"
        
        if guess == actual:
            self.failed_attempts = 0
            return "MATCHED"
        else:
            self.failed_attempts += 1
            return "WRONG"