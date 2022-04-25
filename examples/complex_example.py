import tkinter
import tkinter.messagebox
import customtkinter
import sys
from tkinter import ttk

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

customtkinter.CTkSettings.preferred_drawing_method = "font_shapes"



class App(customtkinter.CTk):

    APP_NAME = "final project"
    WIDTH = 1000
    HEIGHT = 700


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        if sys.platform == "darwin":
            self.bind("<Command-q>", self.on_closing)
            self.bind("<Command-w>", self.on_closing)
            self.createcommand('tk::mac::Quit', self.on_closing)

        # ============ create two CTkFrames ============

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self,
                                                  width=700,
                                                  height=App.HEIGHT-40,
                                                  corner_radius=12)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.grid_columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(0, minsize=10)
     #   self.frame_left.grid_rowconfigure(5, weight=1)
        self.frame_left.grid_rowconfigure(8, minsize=10)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="CustomTkinter",
                                              fg_color=None)
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.loadEEGDataSetbtn = customtkinter.CTkButton(master=self.frame_left,
                                                text="Load EEG data set",
                                                command=self.loadEEGDataSet_event,
                                                border_width=0,
                                                width=150,
                                                corner_radius=8)
        self.loadEEGDataSetbtn.grid(row=2, column=0, pady=10, padx=20)

        self.trainModelbtn = customtkinter.CTkButton(master=self.frame_left,
                                                text="Train model",
                                                command=self.trainModel_event,
                                                border_width=0,
                                                width=150,
                                                corner_radius=8)
        self.trainModelbtn.grid(row=3, column=0, pady=10, padx=20)

        self.runModelbtn = customtkinter.CTkButton(master=self.frame_left,
                                                text="Run model",
                                                command=self.runModel_event,
                                                border_width=0,
                                                width =150,
                                                corner_radius=8)

        self.runModelbtn.grid(row=4, column=0, pady=10, padx=20)
        #  n = tkinter.StringVar()
        #
        # self.comboBox = ttk.Combobox(master=self.frame_left ,width = 27 , textvariable = n)
        #
        # self.comboBox['values'] = (' Show matrix by frequency band',
        #                   ' Show graphs by signal',
        #                   ' Show graph by patient',
        #                   ' Show trained data')
        #
        # self.comboBox.grid(row=5, column=0, pady=10, padx=20)

        self.analyzeDataBtn = customtkinter.CTkButton(master=self.frame_left,
                                                text="Analyze data",
                                                command=self.analyzeData_event,
                                                border_width=0,
                                                width =150,
                                                corner_radius=8)

        self.analyzeDataBtn.grid(row=5, column=0, pady=10, padx=20)


        #self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_left,
         #                                            text="CTkCheckBox")
        #self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

#        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_left,
 #                                                    text="Dark Mode",
  #                                                   command=self.change_mode)
   #     self.check_box_2.grid(row=7, column=0, pady=10, padx=20, sticky="w")


        # ============ frame_right ============

        self.frame_right.rowconfigure(0, weight=200)
        # self.frame_right.rowconfigure(1, weight=1)
        self.frame_right.columnconfigure(0, weight=1)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right,
                                                 width=380,
                                                 height=200)
        self.frame_info.grid(row=0, column=0,  columnspan=3, pady=20, padx=20, sticky="wens")
        #try to build place for all the parts
        self.frame_info.columnconfigure(0, weight=200)
        self.frame_info.columnconfigure(1, weight=200)
        self.frame_info.columnconfigure(2, weight=200)
        self.frame_info.rowconfigure(0, weight=200)
        self.frame_info.rowconfigure(1, weight=200)
        # ============ frame_right -> frame_info ============




        # self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
        #                                            text="CTkLabel: Lorem ipsum dolor sit,\n" +
        #                                                 "amet consetetur sadipscing elitr,\n" +
        #                                                 "sed diam nonumy eirmod tempor\n" +
        #                                                 "invidunt ut labore",
        #                                            width=250,
        #                                            height=100,
        #                                            fg_color=("white", "gray38"),  # <- custom tuple-color
        #                                            justify=tkinter.LEFT)
        # self.label_info_1.place(relx=0.5, rely=0.15, anchor=tkinter.N)
        #
        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        self.progressbar.place(relx=0.5, rely=0.85, anchor=tkinter.S)
        #
        # # ============ frame_right <- ============
        #
        # self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
        #                                         height=16,
        #                                         border_width=0,
        #                                         from_=1,
        #                                         to=0,
        #                                         number_of_steps=3,
        #                                         command=self.progressbar.set)
        # self.slider_1.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky="we")
        # self.slider_1.set(0.5)
        #
        self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
                                                width=160,
                                                height=16,
                                                command=self.progressbar.set)
        self.slider_2.grid(row=2, column=0, columnspan=2, pady=10, padx=20, sticky="we")
        self.slider_2.set(0.7)
        #
        self.label_info_2 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text="CTkLabel: Lorem ipsum",
                                                   fg_color=None,
                                                   width=180,
                                                   height=20,
                                                   justify=tkinter.CENTER)
        self.label_info_2.grid(row=1, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.button_4 = customtkinter.CTkButton(master=self.frame_right,
        #                                         height=25,
        #                                         text="CTkButton",
        #                                         command=self.button_event,
        #                                         border_width=0,
        #                                         corner_radius=8)
        # self.button_4.grid(row=2, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.entry = customtkinter.CTkEntry(master=self.frame_right,
        #                                     width=120,
        #                                     height=30,
        #                                     corner_radius=10,
        #                                     border_width=2,
        #                                     placeholder_text="CTkEntry")
        # self.entry.grid(row=4, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        # self.button_5 = customtkinter.CTkButton(master=self.frame_right,
        #                                         height=26,
        #                                         text="CTkButton",
        #                                         command=self.button_event,
        #                                         fg_color="gray30",
        #                                         border_width=2,
        #                                         border_color=("gray30", "gray50"),
        #                                         corner_radius=13)
        # self.button_5.grid(row=4, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # self.progressbar.set(0.2)

    def button_event(self):
        print("Button pressed")

    def trainModel_event(self):
        print("trainModel pressed")

    def loadEEGDataSet_event(self):
        self.EEGData = customtkinter.CTkFrame(master=self.frame_info,
                               width=180,
                               corner_radius=0)
        print("loadEEGDataSet pressed")
        self.lbl = tkinter.Label(self.frame_info, text="List of Programming Languages")

        self.lbl.grid(row=2, column=2, columnspan=1, pady=10, padx=20, sticky="we")
        self.listbox = tkinter.Listbox(self.frame_info)
        self.listbox.grid(row=1, column=1, columnspan=1, pady=10, padx=20, sticky="we")
        self.listbox.insert(1, "Python")

        self.listbox.insert(2, "Java")

        self.listbox.insert(3, "C")

        self.listbox.insert(4, "C++")

        self.lbl.pack()
        self.listbox.pack()
        self.inputtxt = tkinter.Text(self.frame_info,
                           height=1,
                           width=20)
        self.inputtxt.grid(row=0, column=0, columnspan=1, pady=10, padx=20, sticky="we")

        self.inputtxt.pack()

    def runModel_event(self):
        print("runModel pressed")
        self.frame_info.pack_forget()


    def analyzeData_event(self):
        print("analyzeData pressed")

        # self.frame_info.winfo_children
        children_widgets = self.frame_info.winfo_children()
        for child_widget in children_widgets:
            y = child_widget.winfo_class() == 'TNotebook'
            if child_widget.winfo_class() == 'TNotebook':#delete the old one
                child_widget.destroy()

        style = ttk.Style(self.frame_info)
        style.configure('lefttab.TNotebook', tabposition='wn')

        tabControl = ttk.Notebook(master=self.frame_info, style='lefttab.TNotebook')
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)

        tabControl.add(tab1, text='Tab 1')
        tabControl.add(tab2, text='Tab 2')
        tabControl.pack(expand=1, fill="both")

        ttk.Label(tab1,
                  text="Welcome to \
                         GeeksForGeeks").grid(column=0,
                                              row=0,
                                              padx=30,
                                              pady=30)
        ttk.Label(tab2,
                  text="Lets dive into the\
                         world of computers").grid(column=0,
                                                   row=0,
                                                   padx=30,
                                                   pady=30)




    def change_mode(self):
        if self.check_box_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
