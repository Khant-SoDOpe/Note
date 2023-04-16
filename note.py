from tkinter import END,Label,Button,Tk,Entry,Text
import csv
alreadyna = 0
passdas = 0

class main():

    global window
    window = Tk()
    window.minsize(width=450, height=150)
    window.config(padx=50, pady=50)
    window.title('Note Login')
    code_for_pass = 0
    
    def append_data():#this will append data of user_name and password
        with open("username-password.csv",mode='a') as file:
            global username,password
            username = entry_log.get()
            password = pas_entry.get()
            file.write(f"{username},{password}\n")
            entry_log.delete(0, END)
            pas_entry.delete(0, END)

    def filecheck():#this will check that username and password file will create
        try:
            with open("username-password.csv",mode='r')as fall:
                pass

        except FileNotFoundError:
            with open('username-password.csv', 'a') as csvfile:
                global code_for_pass 
                fieldnames = ['username','password']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                usname = entry_log.get()
                passw = pas_entry.get()
                csvfile.write(f"{usname},{passw}\n")
                entry_log.delete(0, END)
                pas_entry.delete(0, END)
                window.quit()

    def check(search_with,search_data):#this will check username and password for signup and login
        with open("username-password.csv", "r") as data_file:
            players_data = csv.DictReader(data_file)
            players_datas = []
            b = 0
            num = 0
            vot = []

            for player in players_data:
                if appdata == 1:

                    players_datas.append(player['username'])
                    
                    if search_data in players_datas:
                        showerror.delete(0,END)
                        showerror.insert(37,'This username have been already used')

                    else:
                        passw = pas_entry.get()
                        if len(passw) > 2:
                            main.append_data()
                            window.quit()

                        elif len(passw) < 3:
                            showerror.delete(0,END)
                            showerror.insert(37,'Password must be at least more than 2')
                            
                elif gotonote == 1:
                    if player['username'] == search_data:
                        if player['password'] != pas_entry.get():
                            showerror.delete(0,END)
                            showerror.insert(18,'Incorrect Password')

                        elif player['password'] == pas_entry.get():
                            label.grid_forget()
                            usn.destroy()
                            entry_log.destroy()
                            pas.destroy()
                            pas_entry.destroy()
                            signu.destroy()
                            logi.destroy()
                            showerror.destroy()
                            main.notess(search_data)
                        
    #if user click signup go to check
    def signup():
        main.filecheck()
        global gotonote,appdata
        gotonote = 0
        appdata = 1
        main.check('username',entry_log.get())

    #if user click login go to check
    def login():
        main.filecheck()
        global gotonote,appdata
        gotonote = 1
        appdata = 0
        main.check('username',entry_log.get())

    def Start():#this will show button,label and entry on gui
        global label,usn,entry_log,pas,pas_entry,signu,logi,showerror

        #Heading
        label = Label(text='Note Login',font=('Arial',24,'bold'),)
        label.grid(row=0,column=1)
        
        #FOR USERNAME
        usn = Label(text='User name',font=('Arial',15,'bold'))
        usn.grid(row=1,column=0)

        entry_log = Entry()
        entry_log.grid(row=1,column=1)

        #FOR PASSWORD
        pas = Label(text='Password',font=('Arial',15,'bold'))
        pas.grid(row=2,column=0)

        pas_entry = Entry(show='*')
        pas_entry.grid(row=2,column=1)

        #FOR LOGIN AND SIGNUP
        signu = Button(text = 'Signup',command=main.signup)
        signu.grid(row=4,column=1)  

        logi = Button(text = 'Login',command=main.login)
        logi.grid(row=5,column=1)
           
        #for showing error
        showerror = Entry(width=40)
        showerror.grid(row=3,columnspan=2)
        showerror.insert(17,'for showing error')

        window.mainloop()
     
    #-------------------Note and data---------------------------
    def printle():#this will write note in note
        filename = aa+'.txt'
        with open(filename,mode='r')as letter:
            a = letter.read()
            writenote.insert(1.0,a)

    def savefile(name):#this will save file that writing letters
        filename = name+'.txt'
        with open(filename,mode='w')as newfile:
            inp = writenote.get(1.0, "end-1c")
            newfile.write(inp)

    def pp():
        main.savefile(aa)

    def quit():
        window.quit()
    
    def notess(name):#this will manage all about note
        global writenote,aa
        aa = name
        writenote = Text(height = 10,width = 45)
        writenote.grid(row=0,column=0)
        try:
            main.printle()
        except FileNotFoundError:
            main.savefile(name)
        
        Savebutton = Button(text = 'Save', command = main.pp)
        Savebutton.grid(row=1,column=0)

        quitbutton = Button(text = 'Quit', command = main.quit)
        quitbutton.grid(row=2,column=0)

main.Start()