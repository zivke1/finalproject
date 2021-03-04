import tkinter
import customtkinter

customtkinter.enable_macos_darkmode()
#customtkinter.set_appearance_mode("Light")

app = tkinter.Tk()
app.geometry("400x240")
app.title("CustomTkinter Test")


def button_function():
    print("button pressed")


def slider_function(value):
    progressbar_1.set(value)


frame_1 = customtkinter.CTkFrame(master=app, width=300, height=200, corner_radius=15)
frame_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

label_1 = customtkinter.CTkLabel(master=frame_1)
label_1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
progressbar_1.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

button_1 = customtkinter.CTkButton(master=frame_1, corner_radius=10, command=button_function)
button_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_function)
slider_1.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

entry_1 = customtkinter.CTkEntry(master=frame_1)
entry_1.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

app.mainloop()
customtkinter.disable_macos_darkmode()