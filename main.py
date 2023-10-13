import tkinter as tk
import source

def main():

    fullName = ""
    window = tk.Tk()
    window.title("Name Generator")
    window.geometry("350x200")
    window.rowconfigure(0, minsize=20)
    window.columnconfigure([0, 1], minsize=20)
    
    newlabel = tk.Label(text=" Press button to generate name!")
    newlabel.grid(row=0, column=0)

    
    btn = tk.Button(
        text="Clic me to generate name!",
        width=20,
        height=15,
        bg="black",
        fg="white",
    )
    btn.grid(row=0, column=0, sticky="nsew")
    
    label1 = tk.Label(
        text=fullName,
        width=25,
        height=15,
        bg="black",
        fg="white",
    )
    label1.grid(row=0, column=1, sticky="nsew")
    def handle_click(event):
        fullName=source.sourced_data()
        print(fullName)
        label1["text"]=fullName


    btn.bind("<Button-1>", handle_click)
    window.mainloop()

main()