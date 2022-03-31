from tkinter import *
root = Tk()

root.title("Fibonacci")
root.geometry("400x400")
enter_no = Entry(root)
label_series = Label(root, text="Fibonacci Series: ")
label_sum = Label(root, text="Fibonacci Sum: ")

def Fibonacci():
    
    num = int(enter_no.get())
    label_series["text"] = ""
    first_number = 0
    second_number = 1
    sum = 0
    sum2 = 0
    counter = 1
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        label_sum["text"] ="Fibonacci Sum: " + str(sum2)
        counter = counter + 1
        first_number = second_number
        second_number = sum
        sum = first_number + second_number
        sum2 = sum2 + sum


btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)

enter_no.pack()

btn.pack()
label_series.pack()
label_sum.pack()

root.mainloop()