import customtkinter as ctk
from logic import SecuritySystem
import threading
import time
import itertools
import string

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cyber Security Simulator")
        self.geometry("500x600")
        
        # UI Elements
        self.label = ctk.CTkLabel(self, text="Password Security Simulator", font=("Helvetica", 20))
        self.label.pack(pady=20)

        self.target_input = ctk.CTkEntry(self, placeholder_text="Set Password (e.g. 12a)", width=250)
        self.target_input.pack(pady=10)

        self.start_btn = ctk.CTkButton(self, text="Launch Attack", command=self.run_sim)
        self.start_btn.pack(pady=10)

        self.logs = ctk.CTkTextbox(self, width=450, height=300)
        self.logs.pack(pady=20)

    def run_sim(self):
        # Threading taaki screen hang na ho
        threading.Thread(target=self.attack_logic).start()

    def attack_logic(self):
        system = SecuritySystem()
        target = self.target_input.get()
        chars = string.ascii_lowercase + string.digits
        
        self.logs.insert("end", f"[*] Starting attack on: {target}\n")
        
        for length in range(1, 5):
            for guess in itertools.product(chars, repeat=length):
                attempt = "".join(guess)
                result = system.check_password(attempt, target)

                if result == "LOCKED":
                    self.logs.insert("end", "[!!] DEFENDER: System Locked! Waiting 5s...\n", "red")
                    time.sleep(5)
                    system.failed_attempts = 0
                
                self.logs.insert("end", f"Trying: {attempt}\n")
                self.logs.see("end")
                time.sleep(0.05) # Speed control

                if result == "MATCHED":
                    self.logs.insert("end", f"\n[SUCCESS] Cracked: {attempt}\n")
                    return