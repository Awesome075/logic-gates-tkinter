from tkinter import *
from tkinter import messagebox
import AND_ADI as ad
import OR_ADI as ar
import NOT_ADI as at
import XNOR_ADI as anxr
import XOR_ADI as axr
import NOR_ADI as anr
import NAND_ADI as an
class Gates:
    def __init__(self,root):
        self.root=root
        root.title('Learning Logic Gates')
        a=Label(font=('arial',12,'bold'),padx=2,pady=3,text="LEARNING LOGIC GATES",fg="gray15",bg="#439093")
        a.pack()
        b=Label(root,font=('arial',12,'bold'),padx=2,pady=3,text='A logic gate is an idealized or physical device that performs a Boolean function, \na logical operation performed on one or more binary inputs that produces a single binary output.',fg='gray15',bg='#439093')
        b.pack()
        c=Label(font=('arial',12,'bold'),padx=2,pady=3,text="\nDepending on the context, the term may refer to an ideal logic gate, one that has for instance zero rise time and unlimited fan-out,\n or it may refer to a non-ideal physical device (see ideal and real op-amps for comparison).",fg="gray15",bg="#439093")
        c.pack()
        d=Label(font=('arial',12,'bold'),padx=2,pady=3,text="\nIn the real world, the primary way of building logic gates uses diodes or transistors acting as electronic switches.\n Today, most logic gates are made from MOSFETs, metal–oxide–semiconductor field-effect transistors.\n They can also be constructed using vacuum tubes, electromagnetic relays with\n relay logic, fluidic logic, pneumatic logic, optics, molecules, or even mechanical elements.",fg="gray15",bg="#439093")
        d.pack()
        e=Label(font=('arial',12,'bold'),padx=2,pady=3,text="\nWith amplification, logic gates can be cascaded in the same way that Boolean functions can be composed,\n allowing the construction of a physical model of all of Boolean logic, and therefore, all of the algorithms\nand mathematics that can be described with Boolean logic.",fg="gray15",bg="#439093")
        e.pack()
        root.geometry("500x500+0+0")
        self.root.config(bg="#439093")
        def And():
            root1=Toplevel(root)
            root1.geometry("400x400+0+0")
            root1.title('AND')
            root1.config(bg="#fcd0ba")
            a1=Label(root1,font=('arial',12,'bold'),padx=2,pady=3,text="The AND gate is a basic digital logic gate that implements logical conjunction (∧) from mathematical logic – AND gate behaves according to the truth table.\n A HIGH output (1) results only if all the inputs to the AND gate are HIGH (1). \n If not all inputs to the AND gate are HIGH, LOW output results. The function can be extended to any number of inputs.",fg="gray15",bg="#fcd0ba")
            a1.pack()
            x1=Label(root1,font=('arial',12,'bold'),padx=2,pady=3,text='ENTER FIRST NUMBER',fg='gray15',bg='#fcd0ba')
            x1.place(x=100,y=100)
            b1=Entry(root1,font=('arial',12,'bold'))
            b1.place(x=100,y=150)
            y1=Label(root1,font=('arial',12,'bold'),padx=2,pady=3,text='ENTER SECOND NUMBER',fg='gray15',bg='#fcd0ba')
            y1.place(x=100,y=200)
            c1=Entry(root1,font=('arial',12,'bold'))
            c1.place(x=100,y=250)
            
            def Get():
                n1=b1.get()
                n2=c1.get()
                try:
                    r1=ad.AND(int(n1),int(n2))
                    rL1.config(text=("RESULT:-   "+str(r1)))
                except:
                    messagebox.showinfo("error","please enter valid input")
                    
            z1=Button(root1,font=('arial',12,'bold'),padx=2,pady=3,text="AND OPERATION",bg="#fcd0ba",fg="gray15",command=Get)
            z1.place(x=100,y=300)
            rL1=Label(root1,font=('arial',12,'bold'),padx=2,pady=3,text="",fg='gray15',bg='#fcd0ba')
            rL1.place(x=100,y=350)
            i1=PhotoImage(name="img1",file="and.png")
            iL1=Label(root1,image=i1)
            iL1.place(x=400,y=150)
            t1=PhotoImage(name="img11",file="andt.png")
            tL1=Label(root1,image=t1)
            tL1.place(x=800,y=150)
            symbol1=Label(root1,font=('arial',12,'bold'),padx=2,pady=3,text="SYMBOL",fg='gray15',bg='#fcd0ba')
            symbol1.place(x=500,y=100)
            tt1=Label(root1,font=('arial',12,'bold'),padx=2,pady=3,text="TRUTH TABLE",fg='gray15',bg='#fcd0ba')
            tt1.place(x=840,y=100)
                
            root1.mainloop()
        def Not():
            root2=Toplevel(root)
            root2.geometry("400x400+0+0")
            root2.title('NOT')
            root2.config(bg="#fcd0ba")
            a2=Label(root2,font=('arial',12,'bold'),padx=2,pady=3,text="A NOT gate (also often called Inverter) is a logic gate. Each NOT gate has only one input signal.\n Logically with NOT gates, the input and the output swap, so if you input 1 it outputs as 0; likewise if you input 0 it outputs as 1.\nThe NOT gate negates the values of data or signal in its input. It will always output the opposite signal. Its main function is to interchange logic.",fg="gray15",bg="#fcd0ba")
            a2.pack()
            x2=Label(root2,font=('arial',12,'bold'),padx=2,pady=3,text='ENTER NUMBER',fg='gray15',bg='#fcd0ba')
            x2.place(x=100,y=100)
            b2=Entry(root2,font=('arial',12,'bold'))
            b2.place(x=100,y=150)
            
            
            def Get():
                n1=b2.get()
                
                try:
                    r2=at.NOT(int(n1))
                    rL2.config(text=("RESULT:-   "+str(r2)))
                except:
                    messagebox.showinfo("error","please enter valid input")
            z2=Button(root2,font=('arial',12,'bold'),padx=2,pady=3,text="NOT OPERATION",bg="#fcd0ba",fg="gray15",command=Get)
            z2.place(x=100,y=200)
            rL2=Label(root2,font=('arial',12,'bold'),padx=2,pady=3,text="",fg='gray15',bg='#fcd0ba')
            rL2.place(x=100,y=300)
            i2=PhotoImage(name="img2",file="not.png")
            iL2=Label(root2,image=i2)
            iL2.place(x=400,y=150)
            t2=PhotoImage(name="img22",file="nott.png")
            tL2=Label(root2,image=t2)
            tL2.place(x=800,y=150)
            symbol2=Label(root2,font=('arial',12,'bold'),padx=2,pady=3,text="SYMBOL",fg='gray15',bg='#fcd0ba')
            symbol2.place(x=500,y=100)
            tt2=Label(root2,font=('arial',12,'bold'),padx=2,pady=3,text="TRUTH TABLE",fg='gray15',bg='#fcd0ba')
            tt2.place(x=870,y=100)
            
            root2.mainloop()
        def Or():
            root3=Toplevel(root)
            root3.geometry("400x400+0+0")
            root3.title('OR')
            root3.config(bg="#fcd0ba")
            a3=Label(root3,font=('arial',12,'bold'),padx=2,pady=3,text="The OR gate is a logic gate that outputs 1 (true) when at least one of its inputs is 1 (true).That means that if both of its inputs are 0, the output will be 0.",fg="gray15",bg="#fcd0ba")
            a3.pack()
            x3=Label(root3,font=('arial',12,'bold'),padx=2,pady=3,text='ENTER NUMBER',fg='gray15',bg='#fcd0ba')
            x3.place(x=100,y=50)
            b3=Entry(root3,font=('arial',12,'bold'))
            b3.place(x=100,y=100)
            y3=Label(root3,font=('arial',12,'bold'),padx=2,pady=3,text='ENTER SECOND NUMBER',fg='gray15',bg='#fcd0ba')
            y3.place(x=100,y=150)
            c3=Entry(root3,font=('arial',12,'bold'))
            c3.place(x=100,y=200)
            def Get():
                n1=b3.get()
                n2=c3.get()
                try:
                    r3=ar.OR(int(n1),int(n2))
                    rL3.config(text=("RESULT:-   "+str(r3)))
                except:
                    messagebox.showinfo("error","please enter valid input")
            z3=Button(root3,font=('arial',12,'bold'),padx=2,pady=3,text="OR OPERATION",bg="#fcd0ba",fg="gray15",command=Get)
            z3.place(x=100,y=250)
            rL3=Label(root3,font=('arial',12,'bold'),padx=2,pady=3,text="",fg='gray15',bg='#fcd0ba')
            rL3.place(x=100,y=300)
            i3=PhotoImage(name="img3",file="or.png")
            iL3=Label(root3,image=i3)
            iL3.place(x=400,y=100)
            t3=PhotoImage(name="img33",file="ort.png")
            tL3=Label(root3,image=t3)
            tL3.place(x=800,y=100)
            symbol3=Label(root3,font=('arial',12,'bold'),padx=2,pady=3,text="SYMBOL",fg='gray15',bg='#fcd0ba')
            symbol3.place(x=500,y=50)
            tt3=Label(root3,font=('arial',12,'bold'),padx=2,pady=3,text="TRUTH TABLE",fg='gray15',bg='#fcd0ba')
            tt3.place(x=870,y=50)
            
            root3.mainloop()
        def Xor():
            root4=Toplevel(root)
            root4.geometry("400x400+0+0")
            root4.title('XOR')
            root4.config(bg="#fcd0ba")
            a4=Label(root4,font=('arial',12,'bold'),padx=2,pady=3,text="XOR gate (sometimes EOR, or EXOR and pronounced as Exclusive OR) is a digital logic gate that gives a true (1 or HIGH) output when the number of true inputs is odd.\n An XOR gate implements an exclusive or (from mathematical logic; that is, a true output results if one, and only one, of the inputs to the gate is true." ,fg="gray15",bg="#fcd0ba")
            a4.pack()
            x4=Label(root4,font=('arial',12,'bold'),padx=2,pady=3,text='ENTER FIRST NUMBER',fg='gray15',bg='#fcd0ba')
            x4.place(x=100,y=50)
            b4=Entry(root4,font=('arial',12,'bold'))
            b4.place(x=100,y=100)
            y4=Label(root4,font=('arial',12,'bold'),padx=2,pady=3,text='ENTER SECOND NUMBER',fg='gray15',bg='#fcd0ba')
            y4.place(x=100,y=150)
            c4=Entry(root4,font=('arial',12,'bold'))
            c4.place(x=100,y=200)
            def Get():
                n1=b4.get()
                n2=c4.get()
                try:
                    r4=axr.XOR(int(n1),int(n2))
                    rL4.config(text=("RESULT:-   "+str(r4)))
                except:
                    messagebox.showinfo("error","please enter valid input")
            z4=Button(root4,font=('arial',12,'bold'),padx=2,pady=3,text="XOR OPERATION",bg="#fcd0ba",fg="gray15",command=Get)
            z4.place(x=100,y=250)
            rL4=Label(root4,font=('arial',12,'bold'),padx=2,pady=3,text="",fg='gray15',bg='#fcd0ba')
            rL4.place(x=100,y=300)
            i4=PhotoImage(name="img4",file="xor.png")
            iL4=Label(root4,image=i4)
            iL4.place(x=400,y=100)
            t4=PhotoImage(name="img44",file="xort.png")
            tL4=Label(root4,image=t4)
            tL4.place(x=800,y=100)
            symbol4=Label(root4,font=('arial',12,'bold'),padx=2,pady=3,text="SYMBOL",fg='gray15',bg='#fcd0ba')
            symbol4.place(x=500,y=50)
            tt4=Label(root4,font=('arial',12,'bold'),padx=2,pady=3,text="TRUTH TABLE",fg='gray15',bg='#fcd0ba')
            tt4.place(x=870,y=50)

            root4.mainloop()
        def Xnor():
            root5=Toplevel(root)
            root5.geometry("400x400+0+0")
            root5.title('XNOR')
            root5.config(bg="#fcd0ba")
            a5=Label(root5,font=('arial',12,'bold'),padx=2,pady=3,text="The XNOR gate (sometimes ENOR, EXNOR or NXOR and pronounced as Exclusive NOR.\n Alternatively XAND, pronounced Exclusive AND) is a digital logic gate whose function is the logical complement of the Exclusive OR (XOR) gate.",fg="gray15",bg="#fcd0ba")
            a5.pack()
            x5=Label(root5,font=('arial',12,'bold'),padx=2,pady=3,text='ENTER FIRST NUMBER',fg='gray15',bg='#fcd0ba')
            x5.place(x=100,y=50)
            b5=Entry(root5,font=('arial',12,'bold'))
            b5.place(x=100,y=100)
            y5=Label(root5,font=('arial',12,'bold'),padx=2,pady=3,text='ENTER SECOND NUMBER',fg='gray15',bg='#fcd0ba')
            y5.place(x=100,y=150)
            c5=Entry(root5,font=('arial',12,'bold'))
            c5.place(x=100,y=200)
            def Get():
                n1=b5.get()
                n2=c5.get()
                try:
                    r5=anxr.XNOR(int(n1),int(n2))
                    rL5.config(text=("RESULT:-   "+str(r5)))
                except:
                    messagebox.showinfo("error","please enter valid input")
            z5=Button(root5,font=('arial',12,'bold'),padx=2,pady=3,text="XNOR OPERATION",bg="#fcd0ba",fg="gray15",command=Get)
            z5.place(x=100,y=250)
            rL5=Label(root5,font=('arial',12,'bold'),padx=2,pady=3,text="",fg='gray15',bg='#fcd0ba')
            rL5.place(x=100,y=300)
            i5=PhotoImage(name="img5",file="xnor.png")
            iL5=Label(root5,image=i5)
            iL5.place(x=400,y=100)
            t5=PhotoImage(name="img55",file="xnort.png")
            tL5=Label(root5,image=t5)
            tL5.place(x=800,y=100)
            symbol5=Label(root5,font=('arial',12,'bold'),padx=2,pady=3,text="SYMBOL",fg='gray15',bg='#fcd0ba')
            symbol5.place(x=500,y=50)
            tt5=Label(root5,font=('arial',12,'bold'),padx=2,pady=3,text="TRUTH TABLE",fg='gray15',bg='#fcd0ba')
            tt5.place(x=870,y=50)
            
            root5.mainloop()
        def Nor():
            root6=Toplevel(root)
            root6.geometry("400x400+0+0")
            root6.title('NOR')
            root6.config(bg="#fcd0ba")
            a6=Label(root6,font=('arial',12,'bold'),padx=2,pady=3,text="The NOR gate is a digital logic gate that implements logical NOR - it behaves according to the truth table to the right.\n A HIGH output (1) results if both the inputs to the gate are LOW (0); if one or both input is HIGH (1), a LOW output (0) results. NOR is the result of the negation of the OR operator.",fg="gray15",bg="#fcd0ba")
            a6.pack()
            x6=Label(root6,font=('arial',12,'bold'),padx=2,pady=3,text='ENTER FIRST NUMBER',fg='gray15',bg='#fcd0ba')
            x6.place(x=100,y=50)
            b6=Entry(root6,font=('arial',12,'bold'))
            b6.place(x=100,y=100)
            y6=Label(root6,font=('arial',12,'bold'),padx=2,pady=3,text='ENTER SECOND NUMBER',fg='gray15',bg='#fcd0ba')
            y6.place(x=100,y=150)
            c6=Entry(root6,font=('arial',12,'bold'))
            c6.place(x=100,y=200)
            def Get():
                n1=b6.get()
                n2=c6.get()
                try:
                    r6=anr.NOR(int(n1),int(n2))
                    rL6.config(text=("RESULT:-   "+str(r6)))
                except:
                    messagebox.showinfo("error","please enter valid input")
            z6=Button(root6,font=('arial',12,'bold'),padx=2,pady=3,text="NOR OPERATION",bg="#fcd0ba",fg="gray15",command=Get)
            z6.place(x=100,y=250)
            rL6=Label(root6,font=('arial',12,'bold'),padx=2,pady=3,text="",fg='gray15',bg='#fcd0ba')
            rL6.place(x=100,y=300)
            i6=PhotoImage(name="img6",file="nor.png")
            iL6=Label(root6,image=i6)
            iL6.place(x=400,y=100)
            t6=PhotoImage(name="img66",file="nort.png")
            tL6=Label(root6,image=t6)
            tL6.place(x=800,y=100)
            symbol6=Label(root6,font=('arial',12,'bold'),padx=2,pady=3,text="SYMBOL",fg='gray15',bg='#fcd0ba')
            symbol6.place(x=500,y=50)
            tt6=Label(root6,font=('arial',12,'bold'),padx=2,pady=3,text="TRUTH TABLE",fg='gray15',bg='#fcd0ba')
            tt6.place(x=870,y=50)
            
            root6.mainloop()
        def Nand():
            root7=Toplevel(root)
            root7.geometry("400x400+0+0")
            root7.title('NAND')
            root7.config(bg="#fcd0ba")
            a7=Label(root7,font=('arial',12,'bold'),padx=2,pady=3,text="In digital electronics, a NAND gate (NOT-AND) is a logic gate which produces an output which is false only if all its inputs are true;\n Thus its output is complement to that of an AND gate. A LOW (0) output results only if all the inputs to the gate are HIGH (1); if any input is LOW (0), a HIGH (1) output results. ",fg="gray15",bg="#fcd0ba")
            a7.pack()
            x7=Label(root7,font=('arial',12,'bold'),padx=2,pady=3,text='ENTER FIRST NUMBER',fg='gray15',bg='#fcd0ba')
            x7.place(x=100,y=50)
            b7=Entry(root7,font=('arial',12,'bold'))
            b7.place(x=100,y=100)
            y7=Label(root7,font=('arial',12,'bold'),padx=2,pady=3,text='ENTER SECOND NUMBER',fg='gray15',bg='#fcd0ba')
            y7.place(x=100,y=150)
            c7=Entry(root7,font=('arial',12,'bold'))
            c7.place(x=100,y=200)
            def Get():
                n1=b7.get()
                n2=c7.get()
                try:
                    r7=an.NAND(int(n1),int(n2))
                    rL7.config(text=("RESULT:-   "+str(r7)))
                except:
                    messagebox.showinfo("error","please enter valid input")
            z7=Button(root7,font=('arial',12,'bold'),padx=2,pady=3,text="NAND OPERATION",bg="#fcd0ba",fg="gray15",command=Get)
            z7.place(x=100,y=250)
            rL7=Label(root7,font=('arial',12,'bold'),padx=2,pady=3,text="",fg='gray15',bg='#fcd0ba')
            rL7.place(x=100,y=300)
            i7=PhotoImage(name="img7",file="nand.png")
            iL7=Label(root7,image=i7)
            iL7.place(x=400,y=100)
            t7=PhotoImage(name="img77",file="nandt.png")
            tL7=Label(root7,image=t7)
            tL7.place(x=800,y=100)
            symbol7=Label(root7,font=('arial',12,'bold'),padx=2,pady=3,text="SYMBOL",fg='gray15',bg='#fcd0ba')
            symbol7.place(x=500,y=50)
            tt7=Label(root7,font=('arial',12,'bold'),padx=2,pady=3,text="TRUTH TABLE",fg='gray15',bg='#fcd0ba')
            tt7.place(x=870,y=50)
            
            root7.mainloop()


            
        self.AND=Button(font=('arial',12,'bold'),padx=2,pady=3,text=" AND GATE",bg="#f4f0db",fg="gray15",command=And)
        self.AND.place(x=0,y=50)
        
        self.OR=Button(font=('arial',12,'bold'),padx=2,pady=3,text=" OR GATE ",bg="#f4f0db",fg="gray15",command=Or)
        self.OR.place(x=0,y=100)

        self.NOT=Button(font=('arial',12,'bold'),padx=2,pady=3,text=" NOT GATE",bg="#f4f0db",fg="gray15",command=Not)
        self.NOT.place(x=0,y=150)

        self.NOR=Button(font=('arial',12,'bold'),padx=2,pady=3,text=" NOR GATE",bg="#f4f0db",fg="gray15",command=Nor)
        self.NOR.place(x=0,y=200)

        self.XOR=Button(font=('arial',12,'bold'),padx=2,pady=3,text=" XOR GATE",bg="#f4f0db",fg="gray15",command=Xor)
        self.XOR.place(x=0,y=250)

        self.XNOR=Button(font=('arial',12,'bold'),padx=2,pady=3,text="XNOR GATE",bg="#f4f0db",fg="gray15",command=Xnor)
        self.XNOR.place(x=0,y=300)

        self.NAND=Button(font=('arial',12,'bold'),padx=2,pady=3,text="NAND GATE",bg="#f4f0db",fg="gray15",command=Nand)
        self.NAND.place(x=0,y=350)
        






if __name__=='__main__':
    root=Tk()
    app=Gates(root)
    root.mainloop()
