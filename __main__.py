import urllib.request
import json

import tkinter as tk

VERSION = "0.0.1a"

WINDOW_TITLE = "TWiLightMenu Updater v{0}".format(VERSION)

GITHUB_API = "https://api.github.com/repos/%S/releases"
GITHUB_REPO = "DS-Homebrew/TWiLightMenu"

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master

        self.pack(fill=tk.BOTH, expand=1)

        exit_button = tk.Button(self, text="Exit", command=self.click_exit_button)
        menu = tk.Menu(master)
        file_menu = tk.Menu(menu)

        exit_button.place(x=0, y=0)
        master.config(menu=menu)
        menu.add_cascade(label="File", menu=file_menu)

    def click_exit_button(self):
        exit()

WINDOW = Window(tk.Tk())
WINDOW.master.title(WINDOW_TITLE)
WINDOW.master.geometry("320x240")

def get_github_repo_releases():
    with urllib.request.urlopen(GITHUB_API.replace("%S", GITHUB_REPO)) as repo:
        for release in json.loads(repo.read().decode("utf-8")):
            print(release["tag_name"])

def main():
    print("Contacting the repo...")
    get_github_repo_releases()
    WINDOW.mainloop()

if __name__ == "__main__":
    main()