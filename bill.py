from tkinter import *
class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x790+0+0")
        self.root.title("Bill Software")
        bg_color="Lightskyblue1"
        title = Label(self.root,text="BILLING SOFTWARE",bd="5",bg=bg_color,fg="#000000",relief="groove",font=("times new roman",30,"bold"),pady=10).pack(fill=X)

        #####################################  CUSTOMER DETAILS ######################################################

        f1=LabelFrame(self.root,text="CUSTOMER DETAILS",bg=bg_color,fg="yellow4",bd=10,relief="groove",font=("times new roman",10,"bold"))
        f1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(f1,text="Customer Id",font=("times new roman",20,"bold"),padx=5,pady=20,bg=bg_color,fg="#000000").grid(row=0,column=0,padx=50,pady=5)
        cname_txt=Entry(f1,width=30,relief="sunken",bd=5).grid(row=0,column=1,padx=5,pady=15)

        cphone_lbl=Label(f1,text="Phone:no",bg=bg_color,fg="#000000",font=("times new roman",20,"bold")).grid(row=0,column=2,padx=50,pady=5)
        cphone_txt=Entry(f1,width=30,relief="sunken",bd=5).grid(row="0",column=3,padx=5,pady=15)

        cbill_lbl = Label(f1, text="Bill:no", bg=bg_color, fg="#000000", font=("times new roman",20, "bold")).grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(f1, width=30, relief="sunken", bd=5).grid(row="0", column=5,padx=5,pady=15)

        bill_btn=Button(f1,text="Search",width=15,bg="alice blue",fg="#000000",relief="raised",bd=2,font=("arial",15,"bold")).grid(row=0,column=6,padx=50,pady=5)

        ###################################################################### COSMETICS #########################################################################

        f2=LabelFrame(self.root,text="Cosmetics",bg=bg_color,fg="yellow4",bd=10,relief="groove",font=("times new roman",15,"bold"))
        f2.place(x=5,y=190,width=355,height=404)

        cbath_lbl = Label(f2, text="Bath Sope", bg=bg_color, fg="#000000", font=("times new roman", 20, "bold")).grid(row=0, column=2, padx=10, pady=5)
        cbath_txt = Entry(f2, width=20, relief="sunken", bd=5).grid(row=0, column=3, padx=5, pady=15)

        cfacecream_lbl = Label(f2, text="Face Cream", bg=bg_color, fg="#000000", font=("times new roman", 20, "bold")).grid(row=1, column=2, padx=10, pady=5)
        cfacecream_txt = Entry(f2, width=20, relief="sunken", bd=5).grid(row=1, column=3, padx=5, pady=15)

        cfaceqash_lbl = Label(f2, text="Facewash ", bg=bg_color, fg="#000000", font=("times new roman", 20, "bold")).grid(row=2, column=2, padx=10, pady=5)
        cfacewash_txt = Entry(f2, width=20, relief="sunken", bd=5).grid(row=2, column=3, padx=5, pady=15)

        chairspray_lbl = Label(f2, text="Hair Spray", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=3, column=2, padx=10, pady=5)
        chairspray_txt = Entry(f2, width=20, relief="sunken", bd=5).grid(row=3, column=3, padx=5, pady=15)

        chairgel_lbl = Label(f2, text="Hair Gel", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=4, column=2, padx=10, pady=5)
        chairgel_txt = Entry(f2, width=20, relief="sunken", bd=5).grid(row=4, column=3, padx=5, pady=15)

        cbodylotion_lbl = Label(f2, text="Body Lotion", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=5, column=2, padx=10, pady=5)
        cbodylotion_txt = Entry(f2, width=20, relief="sunken", bd=5).grid(row=5, column=3, padx=5, pady=15)

        ###################################################################### Groceries #########################################################################

        f3=LabelFrame(self.root,text="Grocery",bg=bg_color,fg="yellow4",bd=10,relief="groove",font=("times new roman",15,"bold"))
        f3.place(x=355,y=190,width=350,height=404)

        cgrain1_lbl = Label(f3, text="Rice", bg=bg_color, fg="#000000", font=("times new roman", 20, "bold")).grid(row=0, column=2, padx=10, pady=5)
        cgran1_txt = Entry(f3, width=20, relief="sunken", bd=5).grid(row=0, column=3, padx=5, pady=15)

        cgrain2_lbl = Label(f3, text="Food Oil", bg=bg_color, fg="#000000", font=("times new roman", 20, "bold")).grid(row=1, column=2, padx=10, pady=5)
        cgrain2_txt = Entry(f3, width=20, relief="sunken", bd=5).grid(row=1, column=3, padx=5, pady=15)

        cgrain3_lbl = Label(f3, text="Dhaal ", bg=bg_color, fg="#000000", font=("times new roman", 20, "bold")).grid(row=2, column=2, padx=10, pady=5)
        cgrain3_txt = Entry(f3, width=20, relief="sunken", bd=5).grid(row=2, column=3, padx=5, pady=15)

        cgrain4_lbl = Label(f3, text="Wheat", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=3, column=2, padx=10, pady=5)
        cgrain4_txt = Entry(f3, width=20, relief="sunken", bd=5).grid(row=3, column=3, padx=5, pady=15)

        chairgel_lbl = Label(f3, text="Sugar", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=4, column=2, padx=10, pady=5)
        chairgel_txt = Entry(f3, width=20, relief="sunken", bd=5).grid(row=4, column=3, padx=5, pady=15)

        cbodylotion_lbl = Label(f3, text="Tea", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=5, column=2, padx=10, pady=5)
        cbodylotion_txt = Entry(f3, width=20, relief="sunken", bd=5).grid(row=5, column=3, padx=5, pady=15)

        ###################################################################### COSMETICS #########################################################################

        f4=LabelFrame(self.root,text="Cool Drinks",bg=bg_color,fg="yellow4",bd=10,relief="groove",font=("times new roman",15,"bold"))
        f4.place(x=700,y=190,width=350,height=404)

        cc1_lbl = Label(f4, text="Mazza", bg=bg_color, fg="#000000", font=("times new roman", 20, "bold")).grid(row=0, column=2, padx=10, pady=5)
        cc2_txt = Entry(f4, width=20, relief="sunken", bd=5).grid(row=0, column=3, padx=5, pady=15)

        cc2_lbl = Label(f4, text="Thumbsup", bg=bg_color, fg="#000000", font=("times new roman", 20, "bold")).grid(row=1, column=2, padx=10, pady=5)
        cc2_txt = Entry(f4, width=20, relief="sunken", bd=5).grid(row=1, column=3, padx=5, pady=15)

        cc3_lbl = Label(f4, text="Sprite", bg=bg_color, fg="#000000", font=("times new roman", 20, "bold")).grid(row=2, column=2, padx=10, pady=5)
        cc3_txt = Entry(f4, width=20, relief="sunken", bd=5).grid(row=2, column=3, padx=5, pady=15)

        cc4_lbl = Label(f4, text="Appie Fizz", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=3, column=2, padx=10, pady=5)
        cc4_txt = Entry(f4, width=20, relief="sunken", bd=5).grid(row=3, column=3, padx=5, pady=15)

        cc5 = Label(f4, text="Kingfisher", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=4, column=2, padx=10, pady=5)
        cc5_txt = Entry(f4, width=20, relief="sunken", bd=5).grid(row=4, column=3, padx=5, pady=15)

        cc6_lbl = Label(f4, text="RedBull", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=5, column=2, padx=10, pady=5)
        cc6_txt = Entry(f4, width=20, relief="sunken", bd=5).grid(row=5, column=3, padx=5, pady=15)

        ################################################################  BILL AREA  #############################################################################
        f5=LabelFrame(self.root,fg="black",bd=10,relief="groove")
        f5.place(x=1050,y=190,width=475,height=404)
        bill_lbl=Label(f5,text="Bill Area",fg="black",bd=10,relief=GROOVE,font=("arial",15,"bold"),padx=20).pack(fill=X)
        scrol_y=Scrollbar(f5,orient=VERTICAL)

        ################################################################ BILL MENU ################################################################################
        f6 = LabelFrame(self.root,bg=bg_color,text="Bill Menu",fg="yellow4",relief="groove",bd=10,font=("times ew roman",15,"bold"),padx=10,pady=10)
        f6.place(x=0,y=590,relwidth=1,height=200)
        m_lbl  = Label(f6, text="Total Cosmetic Price",bg=bg_color,fg="#000000",font=("times new roman",20,"bold")).grid(row=0,column=0)
        m_txt  = Entry(f6, width=20,relief="sunken",bd=5).grid(row=0,column=1,padx=20,pady=10)

        m1_lbl = Label(f6, text="Total Grocery Price", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=1, column=0)
        m1_txt = Entry(f6, width=20, relief="sunken", bd=5).grid(row=1, column=1, padx=25, pady=10)

        m2_lbl = Label(f6, text="Total Cold Drink Price", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=2, column=0)
        m2_txt = Entry(f6, width=20, relief="sunken", bd=5).grid(row=2, column=1, padx=25, pady=10)

        m3_lbl = Label(f6, text="Cosmetic Tax", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=0, column=3)
        m3_txt = Entry(f6, width=20, relief="sunken", bd=5).grid(row=0, column=4, padx=35, pady=10,sticky="w")

        m4_lbl = Label(f6, text="Grocery Tax", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=1, column=3)
        m4_txt = Entry(f6, width=20, relief="sunken", bd=5).grid(row=1, column=4, padx=35, pady=10,sticky="w")

        m5_lbl = Label(f6, text="Cold drink Tax", bg=bg_color, fg="#000000",font=("times new roman", 20, "bold")).grid(row=2, column=3)
        m5_txt = Entry(f6, width=20, relief="sunken", bd=5).grid(row=2, column=4, padx=35, pady=10,sticky="w")

        btm_lbl= Frame(f6,bd=7,relief="groove",pady=0,padx=0)
        btm_lbl.place(x=825,width=680,height=150)
        total_btn = Button(btm_lbl, text="Total", bg="light steel blue", bd=10, relief="groove", pady=30,padx=20,font=("arial",20,"bold")).grid(row=0,column=0,padx=10)

        Gbill_btn = Button(btm_lbl, text="G_Bill", bg="light steel blue", bd=10, relief="groove", pady=30, padx=20,font=("arial", 20, "bold")).grid(row=0, column=1, padx=10)

        clear_btn = Button(btm_lbl, text="Clear",bg="light steel blue", bd=10, relief="groove", pady=30 , padx=20,font=("arial", 20, "bold")).grid(row=0, column=2, padx=10)

        Exit_btn = Button(btm_lbl, text="Exit", bg="light steel blue", bd=10, relief="groove", pady=30, padx=20,font=("arial", 20, "bold")).grid(row=0, column=3, padx=10)


root=Tk()
BillApp(root)
root.mainloop()

