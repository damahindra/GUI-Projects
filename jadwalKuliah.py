import  tkinter as tk

jadwalKuliah = ["senin", "selasa", "rabu", "kamis", "jumat"]

# customizable schedules

senin = {"subject" : "time"}

selasa = {"subject" : "time"}

rabu = {"subject" : "time"}

kamis = {"subject" : "time"}

jumat = {"subject" : "time"}

tag = {"senin" : senin,
       "selasa" : selasa,
       "rabu" : rabu,
       "kamis" : kamis,
       "jumat" : jumat}

screen = tk.Tk()

width = screen.winfo_screenwidth()
height = screen.winfo_screenheight()
screen.geometry(f"{width}x{height}+0+0")

screen.attributes("-transparentcolor", screen["bg"])
screen.overrideredirect(True)

labels = []

def destroyLabels(labels) :
    if len(labels) == 0 :
        pass
    else :
        for i in range(len(labels)) :
            if i % 2 == 1 :
                sub = labels[i]
                sub.destroy()
            elif i % 2 == 0 :
                line = labels[i]
                line.destroy()

def printSchedule(day) :
    x1 = 0.5
    y1 = 0.65
    x2 = 0.5
    y2 = 0.7

    if day.lower() == "clear" :
        destroyLabels(labels)

    for jadwal in jadwalKuliah :
        if day.lower() == jadwal :
            destroyLabels(labels)
            for subjects in tag[jadwal] :
                sub = tk.Label(master=screen, text=f"{subjects} || {tag[jadwal][subjects]}", fg="white", font=("Helvetica", 20))
                labels.append(sub)
                sub.pack()
                sub.place(relx=x1, rely=y1, anchor="center")
                line = tk.Label(master=screen, text="--------------------------------------", fg="white", font=("Helvetica", 20))
                labels.append(line)
                line.pack()
                line.place(relx=x2, rely=y2, anchor="center")
                y1 += 0.1
                y2 += 0.1

def clearEntry() :
    entry.delete(0, tk.END)

def key_pressed(event):
    day = entry.get()
    clearEntry()
    printSchedule(day)

capt = tk.Label(master=screen, text="College Schedule", foreground="#ffffff", font=("Helvetica", 40))
capt.pack()
capt.place(relx=0.5, rely=0.495, anchor="center")


entry = tk.Entry(master=screen, fg="#FF10F0", bg="white", font=("Helvetica", 12), borderwidth=0)
entry.pack()
entry.place(relx=0.5, rely=0.55, anchor="center", width=300, height=22)
entry.bind("<Return>", key_pressed)
screen.mainloop()




