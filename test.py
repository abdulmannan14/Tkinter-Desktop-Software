# 1: toggle button q jb start ka button rkh skte
#   2: p wale buttons ki jaga radio button laga dete
#   3: output bottom mai show kra dete




import tkinter as tk

# from test import delete,delete1
lista=[]
root = tk.Tk(className="Python Calculator")
canvas1 = tk.Canvas(root, width=1370, height=900, relief='raised',bg="#043C74")
canvas1.pack()

def delete():
    tokenentry1.delete(0,'end')
def delete1():
    thresholdentry.delete(0, 'end')

tokenInpuT = tk.Label(root, text='Token Value:')
tokenInpuT.config(font=('helvetica', 20),bg='#043C74',fg='white')
canvas1.create_window(685, 20, window=tokenInpuT)
tokenentry1 = tk.Entry(root)
canvas1.create_window(685, 100, window=tokenentry1,height = 130,width=500)
thresholdinpuT = tk.Label(root, text='Threshold:')
thresholdinpuT.config(font=('helvetica', 15),bg='#043C74',fg='white')
canvas1.create_window(1010, 120, window=thresholdinpuT)
thresholdentry = tk.Entry(root)
canvas1.create_window(1020, 150, window=thresholdentry,height = 30,width=150)
clear_token = tk.Button(root, text ="clear token", command =delete ,bg='#043C74',fg='white')
canvas1.create_window(350, 150, window=clear_token,height = 30,width=150)
clear_threshold = tk.Button(root, text ="clear threshold", command =delete1 ,bg='#043C74',fg='white')
canvas1.create_window(1182, 150, window=clear_threshold,height = 30,width=150)










def start():
    token=0
    if tokenentry1.get():
        if thresholdentry.get():
            if len(lista)!=0:
                token =tokenentry1.get()
                threshold=thresholdentry.get()
                total_of_lista=sum(lista)
                while int(token) > int(threshold):
                    token =int(token)-total_of_lista
                qs = tk.Label(root, text='The Final Output value is:')
                qs.config(font=('helvetica', 20), bg='#043C74', fg='white')
                canvas1.create_window(730, 500, window=qs)
                qs = tk.Label(root, text=token)
                print("this is the token",token)
                qs.config(font=('helvetica', 20), bg='#043C74', fg='white')
                canvas1.create_window(730, 550, window=qs)
            else:
                pass
                # qs3 = tk.Label(root, text='Please press some "P" Button to get value ')
                # qs3.config(font=('helvetica', 20), bg='#043C74', fg='white')
                # canvas1.create_window(730, 500, window=qs3)
        else:
            qs1 = tk.Label(root, text='Please enter some threshold value ')
            qs1.config(font=('helvetica', 20), bg='#043C74', fg='white')
            canvas1.create_window(730, 500, window=qs1)
    else:
        qs2 = tk.Label(root, text='Please enter some token value ')
        qs2.config(font=('helvetica', 20), bg='#043C74', fg='white')
        canvas1.create_window(730, 500, window=qs2)




def B1_presser():
    lista.append(1000)
def B2_presser():
    lista.append(2000)
def B3_presser():
    lista.append(3000)
def B4_presser():
    lista.append(4000)
def B5_presser():
    lista.append(5000)
def B6_presser():
    lista.append(6000)
def B7_presser():
    lista.append(7000)
def B8_presser():
    lista.append(8000)
def B9_presser():
    lista.append(9000)
def B10_presser():
    lista.append(10000)

# B1 = tk.Button.bind("<ButtonPress>",
B1 = tk.Button(root, text ="P1 = 1000", command = B1_presser,bg='#043C74',fg='white')
canvas1.create_window(410, 250, window=B1,height = 30,width=150)
B2 = tk.Button(root, text ="P2 = 2000", command = B2_presser,bg='#043C74',fg='white')
canvas1.create_window(570, 250, window=B2,height = 30,width=150)
B3 = tk.Button(root, text ="P3 = 3000", command = B3_presser,bg='#043C74',fg='white')
canvas1.create_window(730, 250, window=B3,height = 30,width=150)
B4 = tk.Button(root, text ="P4 = 4000", command = B4_presser,bg='#043C74',fg='white')
canvas1.create_window(890, 250, window=B4,height = 30,width=150)
B5 = tk.Button(root, text ="P5 = 5000", command = B5_presser,bg='#043C74',fg='white')
canvas1.create_window(1050, 250, window=B5,height = 30,width=150)
B6 = tk.Button(root, text ="P6 = 6000", command = B6_presser,bg='#043C74',fg='white')
canvas1.create_window(410, 300, window=B6,height = 30,width=150)
B7 = tk.Button(root, text ="P7 = 7000", command = B7_presser,bg='#043C74',fg='white')
canvas1.create_window(570, 300, window=B7,height = 30,width=150)
B8 = tk.Button(root, text ="P8 = 8000", command = B8_presser,bg='#043C74',fg='white')
canvas1.create_window(730, 300, window=B8,height = 30,width=150)
B9 = tk.Button(root, text ="P9 = 9000", command = B9_presser,bg='#043C74',fg='white')
canvas1.create_window(890, 300, window=B9,height = 30,width=150)
B10 = tk.Button(root, text ="P10 = 10,000", command = B10_presser,bg='#043C74',fg='white')
canvas1.create_window(1050, 300, window=B10,height = 30,width=150)
start = tk.Button(root, text ="Start", command = start,bg='#043C74',fg='white')
canvas1.create_window(730, 400, window=start,height = 30,width=250)


root.mainloop()