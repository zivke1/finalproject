import tkinter
import time

from customtkinter.customtkinter_label import CTkLabel
from customtkinter.customtkinter_button import CTkButton
from customtkinter.customtkinter_entry import CTkEntry
from customtkinter.customtkinter_theme_manager import CTkThemeManager


class CTkDialog:
    def __init__(self,
                 master=None,
                 title="CTkDialog",
                 text="CTkDialog",
                 fg_color="default_theme",
                 hover_color="default_theme",
                 border_color="default_theme"):
        self.master = master

        self.user_input = None
        self.running = False

        self.height = len(text.split("\n"))*20 + 150

        self.fg_color = CTkThemeManager.theme["color"]["button"] if fg_color == "default_theme" else fg_color
        self.hover_color = CTkThemeManager.theme["color"]["button_hover"] if hover_color == "default_theme" else hover_color
        self.border_color = CTkThemeManager.theme["color"]["button_hover"] if border_color == "default_theme" else border_color

        self.top = customtkinter.CTkToplevel()
        self.top.geometry(f"280x{self.height}")
        self.top.resizable(False, False)
        self.top.title(title)
        self.top.lift()
        self.top.focus_force()
        self.top.grab_set()

        self.label_frame = customtkinter.CTkFrame(master=self.top,
                                                  corner_radius=0,
                                                  width=300,
                                                  height=self.height-100)
        self.label_frame.place(relx=0.5, rely=0, anchor=tkinter.N)

        self.button_and_entry_frame = customtkinter.CTkFrame(master=self.top,
                                                             corner_radius=0,
                                                             width=300,
                                                             height=100)
        self.button_and_entry_frame.place(relx=0.5, rely=1, anchor=tkinter.S)

        self.myLabel = CTkLabel(master=self.label_frame,
                                text=text,
                                width=300,
                                fg_color=None,
                                height=self.height-100)
        self.myLabel.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.entry = CTkEntry(master=self.button_and_entry_frame,
                              width=230)
        self.entry.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        self.ok_button = CTkButton(master=self.button_and_entry_frame,
                                   text='Ok',
                                   width=100,
                                   command=self.ok_event,
                                   fg_color=self.fg_color,
                                   hover_color=self.hover_color,
                                   border_color=self.border_color)
        self.ok_button.place(relx=0.28, rely=0.65, anchor=tkinter.CENTER)

        self.cancel_button = CTkButton(master=self.button_and_entry_frame,
                                       text='Cancel',
                                       width=100,
                                       command=self.cancel_event,
                                       fg_color=self.fg_color,
                                       hover_color=self.hover_color,
                                       border_color=self.border_color)
        self.cancel_button.place(relx=0.72, rely=0.65, anchor=tkinter.CENTER)

        self.entry.entry.focus_force()
        self.entry.bind("<Return>", self.ok_event)

    def ok_event(self, event=None):
        self.user_input = self.entry.get()
        self.running = False

    def cancel_event(self):
        self.running = False

    def get_input(self):
        self.running = True

        while self.running:
            self.top.update()
            time.sleep(0.01)

        time.sleep(0.05)
        self.top.destroy()
        return self.user_input


if __name__ == "__main__":
    import customtkinter
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("dark-blue")

    app = customtkinter.CTk()
    app.geometry("400x300")
    app.title("CTkDialog Test")

    def button_click_event():
        dialog = CTkDialog(master=None, text="Type in a number:", title="Test")
        print("Number:", dialog.get_input())

    button = CTkButton(master=app, text="Open Dialog", command=button_click_event)
    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    app.mainloop()
