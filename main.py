import pandas as pd
import tkinter as tk
from pandastable import Table
import os

class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Aplication')
        self.master.geometry("1000x500")
        self.master.resizable(False, False)
        self.global_df = None

        orders_name = os.listdir("../Dane/Zamowienia")
        button_labels = [str(name[:10] + " " + name[10:-4]) for name in orders_name]

        """
            ORDER FRAME
        """
        # ORDER FRAME
        self.order_frame = tk.LabelFrame(self.master, width=0)
        self.order_frame.pack(side=tk.LEFT, fill="both", padx=40, pady=20)
        #self.order_frame.pack_propagate(False)

        # ORDER CANVAS
        self.order_canvas = tk.Canvas(self.order_frame, width=130)
        self.order_inside_frame = tk.Frame(self.order_canvas)
        self.order_canvas.pack(side=tk.LEFT, fill="y")
        self.order_canvas.pack_propagate(False)
        self.order_inside_frame.pack(fill="both", padx=20)

        self.order_inside_frame.place(relx=0.5, rely=0.5, anchor="center")
        # SCROLL
        order_scrollbar = tk.Scrollbar(self.order_frame, orient="vertical", command=self.order_canvas.yview)
        order_scrollbar.pack(side=tk.RIGHT, fill="both")
        self.order_canvas.configure(yscrollcommand=order_scrollbar.set)

        # INSIDE OF ORDER FRAME
        self.order_canvas.create_window((0, 0), window=self.order_inside_frame, anchor=tk.NW)
        self.order_inside_frame.bind("<Configure>", lambda e: self.order_canvas.configure(scrollregion=self.order_canvas.bbox("all")))

        for label in sorted(button_labels, key=self.extract_number):
            tk.Button(self.order_inside_frame, text=label, command=lambda l=label: self.button_clicked(l), height=3, width=15, font='Helvetica 10 bold').pack()

        """
            ANALYSIS BUTTON
        """
        self.button_frame  = tk.Frame(self.master)
        self.button_frame.pack(side= "top", fill="x", pady=5)
        button4frame = tk.Button(self.button_frame, text = "Analisys", command= lambda x = 1: print("TUTAJ BEDZIE FUNKCJA ANALIZUJACA"),height=3, width=15, font='Helvetica 10 bold')
        button4frame.pack()

        """
            DATA FRAME FRAME
        """
        # DATA Frame
        self.data_frame_frame = tk.LabelFrame(self.master)
        self.data_frame_frame.pack(fill="both", padx=20, pady=20)
        self.data_frame_frame.pack_propagate(True)

        

    def button_clicked(self, label):
        with open("../Dane/Zamowienia/" + str(label).replace(" ", "") + ".csv", "r") as file:
            self.global_df = pd.read_csv(file)
            self.global_df = self.global_df.rename(columns={self.global_df.columns[-1]: 'Ilosc'})

        # Clear existing content in the data_frame_frame
        for widget in self.data_frame_frame.winfo_children():
            widget.destroy()

        # Display the Pandas DataFrame using pandastable
        pt = Table(self.data_frame_frame, dataframe=self.global_df)
        pt.show()

    @staticmethod
    def extract_number(item):
        return int(item.split('Zamowienie')[1])

def main():
    root = tk.Tk()
    MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
