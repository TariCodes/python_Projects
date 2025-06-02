import tkinter as tk
import secrets

app = tk.Tk()
app.title("OTP Generator")

app.geometry("500x500")

def generator_otp(length=6) -> None:
    print(''.join(str(secrets.randbelow(10))
                   for _ in range(length)))

def otp():
    label = tk.Label(app, text=generator_otp()).pack()  #I want the generated otp to be printed onto the label widget


genOtp = tk.Button(app, text="Generate OTP", bg="#333", padx=20, pady=12, fg="#fff", command=otp).pack()

app.mainloop()
