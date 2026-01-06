import customtkinter as ctk


win = ctk.CTk()

win.geometry("300x400")

save_btn = ctk.CTkButton(win,text="save")
save_btn.place(x=40,y=50)


win.mainloop()