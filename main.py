import tkinter
from tkinter import *


def application():
    # Initializing the GUI application window
    new_window = tkinter.Tk()
    new_window.title("Calculator")
    window_width = 340
    window_height = 400
    # Lines 10-16 are for centering the GUI window without having to type specific numbers for the dimensions
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    new_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Lines 21-23 are for making the window a fixed size, assuring it appears at the top of the stack of
    # open applications, and assigning an icon to the window from the asset folder, respectively
    new_window.resizable(False, False)
    new_window.attributes('-topmost', 1)
    new_window.iconbitmap('./assets/Calc.ico')

    # Code to initialize the input screen frame
    input_frame = Frame(new_window, width=window_width,
                        height=50,
                        bd=0,
                        highlightbackground="black",
                        highlightcolor="black",
                        highlightthickness=2)

    input_frame.pack(side=TOP)

    # Code to initialize the input screen widget
    global input_text
    input_text = StringVar(new_window, value="")

    input_field = Entry(input_frame,
                        font=('arial', 18, 'bold'),
                        textvariable=input_text,
                        width=50,
                        fg="#eee",
                        bg="#000",
                        bd=0,
                        justify=RIGHT)

    input_field.grid(row=0,
                     column=0)

    input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of input field

    # Code to initialize the button frame
    btn_height = 4
    btn_frame = Frame(new_window,
                      width=400,
                      height=350)
    btn_frame.pack()

    # First row of buttons
    btn_clear = Button(btn_frame, text="C", fg="black", width=32, height=btn_height,
                       bd=1, bg ="#d4d4d2", cursor="hand2", command=lambda: clear())
    btn_clear.grid(row=0, column=0, columnspan=3, sticky='nesw')
    btn_div = Button(btn_frame, font=("Helvetica", 13, 'bold'), text="/", fg="#eee", width=10, height=3,
                     bd=1, bg="#ff9500", cursor="hand2", command=lambda: write('/'))
    btn_div.grid(row=0, column=3)

    # Second row of buttons
    btn_clear = Button(btn_frame, text="7", fg="black", height=btn_height,
                       bd=1, bg="#eee", cursor="hand2", command=lambda: write('7'))
    btn_clear.grid(row=1, column=0, sticky='nesw')
    btn_clear = Button(btn_frame, text="8", fg="black", height=btn_height,
                       bd=1, bg="#eee", cursor="hand2", command=lambda: write('8'))
    btn_clear.grid(row=1, column=1, sticky='nesw')
    btn_div = Button(btn_frame, text="9", fg="black", height=btn_height,
                     bd=1, bg="#eee", cursor="hand2", command=lambda: write('9'))
    btn_div.grid(row=1, column=2, sticky='nesw')
    btn_div = Button(btn_frame, font=("Helvetica", 13, 'bold'), text="+", fg="#eee", height=3,
                     bd=1, bg="#ff9500", cursor="hand2", command=lambda: write('+'))
    btn_div.grid(row=1, column=3, sticky='nesw')

    # Third row of buttons
    btn_clear = Button(btn_frame, text="4", fg="black", height=btn_height,
                       bd=1, bg="#eee", cursor="hand2", command=lambda: write('4'))
    btn_clear.grid(row=2, column=0, sticky='nesw')
    btn_clear = Button(btn_frame, text="5", fg="black", height=btn_height,
                       bd=1, bg="#eee", cursor="hand2", command=lambda: write('5'))
    btn_clear.grid(row=2, column=1, sticky='nesw')
    btn_div = Button(btn_frame, text="6", fg="black", height=btn_height,
                     bd=1, bg="#eee", cursor="hand2", command=lambda: write('6'))
    btn_div.grid(row=2, column=2, sticky='nesw')
    btn_div = Button(btn_frame, font=("Helvetica", 13, 'bold'), text="-", fg="#eee", height=3,
                     bd=1, bg="#ff9500", cursor="hand2", command=lambda: write('-'))
    btn_div.grid(row=2, column=3, sticky='nesw')

    # Third row of buttons
    btn_clear = Button(btn_frame, text="1", fg="black", height=btn_height,
                       bd=1, bg="#eee", cursor="hand2", command=lambda: write('1'))
    btn_clear.grid(row=3, column=0, sticky='nesw')
    btn_clear = Button(btn_frame, text="2", fg="black", height=btn_height,
                       bd=1, bg="#eee", cursor="hand2", command=lambda: write('2'))
    btn_clear.grid(row=3, column=1, sticky='nesw')
    btn_div = Button(btn_frame, text="3", fg="black", height=btn_height,
                     bd=1, bg="#eee", cursor="hand2", command=lambda: write('3'))
    btn_div.grid(row=3, column=2, sticky='nesw')
    btn_div = Button(btn_frame, font=("Helvetica", 13, 'bold'), text="*", fg="#eee", height=3,
                     bd=1, bg="#ff9500", cursor="hand2", command=lambda: write('*'))
    btn_div.grid(row=3, column=3, sticky='nesw')

    # Third row of buttons
    btn_clear = Button(btn_frame, text="0", fg="black", height=btn_height,
                       bd=1, bg="#eee", cursor="hand2", command=lambda: write('0'))
    btn_clear.grid(row=4, column=0, columnspan=2, sticky='nesw')
    btn_clear = Button(btn_frame, text=".", fg="black", height=btn_height,
                       bd=1, bg="#eee", cursor="hand2", command=lambda: write('.'))
    btn_clear.grid(row=4, column=2, sticky='nesw')
    btn_div = Button(btn_frame, font=("Helvetica", 13, 'bold'), text="=", fg="#eee", height=3, bd=1,
                     bg="#ff9500", cursor="hand2", command=lambda: result(input_text.get()))
    btn_div.grid(row=4, column=3, sticky='nesw')

    new_window.mainloop()


def clear():
    input_text.set("")


def write(text):
    new_text = input_text.get() + text
    input_text.set(new_text)


def result(expression):
    exp_result = eval(expression)
    input_text.set(str(exp_result))


if __name__ == "__main__":
    application()
