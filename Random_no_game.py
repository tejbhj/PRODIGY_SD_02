import random as rd
import tkinter as tk

def game_window(a, b):
    root = tk.Tk()
    root.title("Random Number Guesser")
    root.geometry("300x200")

    no = rd.randint(a, b)

    def game():
        try:
            guess = int(guessno.get())
            result = ""
            if guess == no:
                result = "Good Job"
            else:
                if guess > no:
                    result = "Hint: Guess is bigger than no"
                else:
                    result = "Hint: Guess is lower than no"
            ans.config(text=result)
        except ValueError:
            ans.config(text="Please enter a valid number.")
        except Exception as e:
            ans.config(text="Something went wrong. Please try again")

    label = tk.Label(root, text="Enter your Guess")
    label.pack(pady=5)
    guessno = tk.Entry(root)
    guessno.pack(pady=5)
    gameon = tk.Button(root, text="Guess", command=game)
    gameon.pack(pady=5)
    ans = tk.Label(root, text="")
    ans.pack(pady=10)
    root.mainloop()

def start_game():
    try:
        a = int(mini_input.get())
        b = int(maxi_input.get())
        game_window(a, b)
    except ValueError:
        print("Please enter valid integers for the range.")
    except Exception as e:
        print("Something went wrong:", e)

window = tk.Tk()
window.title("Enter Range")
window.geometry("300x200")
mini_label = tk.Label(window, text="Enter Minimum")
mini_label.pack(pady=5)
mini_input = tk.Entry(window)
mini_input.pack(pady=5)
maxi_label = tk.Label(window, text="Enter Maximum")
maxi_label.pack(pady=5)
maxi_input = tk.Entry(window)
maxi_input.pack(pady=5)
windowon = tk.Button(window, text="Submit", command=start_game)
windowon.pack(pady=5)
window.mainloop()
