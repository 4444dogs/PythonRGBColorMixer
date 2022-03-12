from tkinter import *
window=Tk()

finalrgb = "Please Enter RGB Values"

r1=Entry(window, width=5)
r1.place(x=80, y=150)
g1=Entry(window, width=5)
g1.place(x=140, y=150)
b1=Entry(window, width=5)
b1.place(x=200, y=150)

r2=Entry(window, width=5)
r2.place(x=80, y=210)
g2=Entry(window, width=5)
g2.place(x=140, y=210)
b2=Entry(window, width=5)
b2.place(x=200, y=210)

def clicked():
   global finalrgb
   rcalc = int((int(r1.get()) + int(r2.get())) / 2)
   gcalc = int((int(g1.get()) + int(g2.get())) / 2)
   bcalc = int((int(b1.get()) + int(b2.get())) / 2)
   finalrgb = rcalc, gcalc, bcalc
   rgb = '#%02x%02x%02x' % (rcalc, gcalc, bcalc)
   finalrgblbl.configure(text=finalrgb, fg=rgb)
   print(finalrgb)

btn = Button(window, text="Calculate", command=clicked)
btn.place(x=80, y=120)

finalrgblbl=Label(window, text=finalrgb)
finalrgblbl.place(x=80, y=90)

window.title('RGB Color Mixer')
window.state('zoomed')

window.mainloop()