#======== Designing second menu page========================
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from barcode import EAN13
import random
import time
from tkinter import filedialog, messagebox
import requests







new = Tk()
new.title("Restaurant Management System")
new.geometry("1600x940")
new.resizable(False, False)
#====================Function in project========================
def pay():
    paywindow=Tk()
    paywindow.title("Pay")
    paywindow.geometry("1400x1400")
    img = Image.open("scan and pay.jpg")
    photo = ImageTk.PhotoImage(img)
    image_label = Label(paywindow, text="Hey i dont know why image is not working ", bg="firebrick4", image=photo).pack()
    paywindow.mainloop()
def sahipanner():
    if cinsp.get()==1:
        text_sp.config(state=NORMAL)
        text_sp.delete(0,END)
        text_sp.focus()
    else:
        text_sp.config(state=DISABLED)
        e_sp.set('0')
def mixveg():
    if cinmv.get()==1:
        text_mv.config(state=NORMAL)
        text_mv.delete(0, END)
        text_mv.focus()
    else:
        text_mv.config(state=DISABLED)
        e_mv.set('0')
def dalmakhni():
    if cindm.get()==1:
        text_dm.config(state=NORMAL)
        text_dm.delete(0, END)
        text_dm.focus()
    else:
        text_dm.config(state=DISABLED)
        e_dm.set('0')
def kadaipanner():
    if cinkp.get()==1:
        text_kp.config(state=NORMAL)
        text_kp.delete(0, END)
        text_kp.focus()
    else:
        text_kp.config(state=DISABLED)
        e_kp.set('0')
def pannertikka():
    if cinpt.get()==1:
        text_pt.config(state=NORMAL)
        text_pt.delete(0, END)
        text_pt.focus()
    else:
        text_pt.config(state=DISABLED)
        e_pt.set('0')
def aloojerra():
    if cinaj.get()==1:
        text_aj.config(state=NORMAL)
        text_aj.delete(0, END)
        text_aj.focus()
    else:
        text_aj.config(state=DISABLED)
        e_aj.set('0')
def bhindimasala():
    if cinbm.get()==1:
        text_bm.config(state=NORMAL)
        text_bm.delete(0, END)
        text_bm.focus()
    else:
        text_bm.config(state=DISABLED)
        e_bm.set('0')
def rajmatadka():
    if cinrt.get()==1:
        text_rt.config(state=NORMAL)
        text_rt.delete(0, END)
        text_rt.focus()
    else:
        text_rt.config(state=DISABLED)
        e_rt.set('0')
def mushroommattar():
    if cinmm.get()==1:
        text_mm.config(state=NORMAL)
        text_mm.delete(0, END)
        text_mm.focus()
    else:
        text_mm.config(state=DISABLED)
        e_mm.set('0')
def soyachap():
    if cinsc.get()==1:
        text_sc.config(state=NORMAL)
        text_sc.delete(0, END)
        text_sc.focus()
    else:
        text_sc.config(state=DISABLED)
        e_sc.set('0')
def baiganbharta():
    if cinbb.get()==1:
        text_bb.config(state=NORMAL)
        text_bb.delete(0, END)
        text_bb.focus()
    else:
        text_bb.config(state=DISABLED)
        e_bb.set('0')
def roti():
    if cinr.get()==1:
        text_r.config(state=NORMAL)
        text_r.delete(0, END)
        text_r.focus()
    else:
        text_r.config(state=DISABLED)
        e_r.set('0')
def butterroti():
    if cinbr.get()==1:
        text_br.config(state=NORMAL)
        text_br.delete(0, END)
        text_br.focus()
    else:
        text_br.config(state=DISABLED)
        e_br.set('0')


def butternaan():
    if cinbn.get() == 1:
        text_bn.config(state=NORMAL)
        text_bn.delete(0, END)
        text_bn.focus()
    else:
        text_bn.config(state=DISABLED)
        e_bn.set('0')

def alooparatha():
    if cinap.get()==1:
        text_ap.config(state=NORMAL)
        text_ap.delete(0, END)
        text_ap.focus()
    else:
        text_ap.config(state=DISABLED)
        e_ap.set('0')
def eggroll():
    if ciner.get()==1:
        text_er.config(state=NORMAL)
        text_er.delete(0, END)
        text_er.focus()
    else:
        text_er.config(state=DISABLED)
        e_er.set('0')

def eggcurry():
    if cinec.get()==1:
        text_ec.config(state=NORMAL)
        text_ec.delete(0, END)
        text_ec.focus()
    else:
        text_ec.config(state=DISABLED)
        e_ec.set('0')

def chickentikka():
    if cinct.get()==1:
        text_ct.config(state=NORMAL)
        text_ct.delete(0, END)
        text_ct.focus()
    else:
        text_ct.config(state=DISABLED)
        e_ct.set('0')

def chickenbutter():
    if cincb.get()==1:
        text_cb.config(state=NORMAL)
        text_cb.delete(0, END)
        text_cb.focus()
    else:
        text_cb.config(state=DISABLED)
        e_cb.set('0')

def chickensoup():
    if cchcs.get()==1:
        txt_chcs.config(state=NORMAL)
        txt_chcs.delete(0,END)
        txt_chcs.focus()
    else:
        txt_chcs.config(state=DISABLED)
        e_ch_cs.set('0')
def vegsoup():
    if cchvs.get()==1:
        txt_chvs.config(state=NORMAL)
        txt_chvs.delete(0,END)
        txt_chvs.focus()
    else:
        txt_chvs.config(state=DISABLED)
        e_ch_vs.set('0')
def friedrice():
    if cchfr.get()==1:
        txt_chfr.config(state=NORMAL)
        txt_chfr.delete(0,END)
        txt_chfr.focus()
    else:
        txt_chfr.config(state=DISABLED)
        e_ch_fr.set('0')

def manchurian():
    if cchm.get()==1:
        txt_chm.config(state=NORMAL)
        txt_chm.delete(0, END)
        txt_chm.focus()
    else:
        txt_chm.config(state=DISABLED)
        e_ch_m.set('0')
def chillipot():
    if cchcp.get()==1:
        txt_chi_pot.config(state=NORMAL)
        txt_chi_pot.delete(0, END)
        txt_chi_pot.focus()
    else:
        txt_chi_pot.config(state=DISABLED)
        e_ch_cp.set('0')
def chickennood():
    if cchcn.get()==1:
        txt_chi_nood.config(state=NORMAL)
        txt_chi_nood.delete(0,END)
        txt_chi_nood.focus()
    else:
        txt_chi_nood.config(state=DISABLED)
        e_ch_cn.set('0')
def chillicheese():
    if cchcc.get()==1:
        txt_chi_che.config(state=NORMAL)
        txt_chi_che.delete(0,END)
        txt_chi_che.focus()
    else:
        txt_chi_che.config(state=DISABLED)
        e_ch_cc.set('0')

def kadaichicken():
    if cchkc.get()==1:
        txt_kad_pann.config(state=NORMAL)
        txt_kad_pann.delete(0,END)
        txt_kad_pann.focus()
    else:
        txt_kad_pann.config(state=DISABLED)
        e_ch_kc.set('0')

def tea():
    if cdt.get()==1:
        txt_d_t.config(state=NORMAL)
        txt_d_t.delete(0, END)
        txt_d_t.focus()
    else:
        txt_d_t.config(state=DISABLED)
        e_d_t.set('0')

def cofee():
    if cdc.get()==1:
        txt_d_c.config(state=NORMAL)
        txt_d_c.delete(0, END)
        txt_d_c.focus()
    else:
        txt_d_c.config(state=DISABLED)
        e_d_c.set('0')

def mojito():
    if cdm.get()==1:
        txt_d_m.config(state=NORMAL)
        txt_d_m.delete(0, END)
        txt_d_m.focus()
    else:
        txt_d_m.config(state=DISABLED)
        e_d_m.set('0')

def orange():
    if cdo.get()==1:
        txt_d_o.config(state=NORMAL)
        txt_d_o.delete(0, END)
        txt_d_o.focus()
    else:
        txt_d_o.config(state=DISABLED)
        e_d_o.set('0')

def strawberry():
    if cds.get()==1:
        txt_d_s.config(state=NORMAL)
        txt_d_s.delete(0, END)
        txt_d_s.focus()
    else:
        txt_d_s.config(state=DISABLED)
        e_d_s.set('0')


def mango():
    if cdma.get() == 1:
        txt_d_ma.config(state=NORMAL)
        txt_d_ma.delete(0, END)
        txt_d_ma.focus()
    else:
        txt_d_ma.config(state=DISABLED)
        e_d_ma.set('0')

def watermellon():
    if cdwm.get()==1:
        txt_d_wm.config(state=NORMAL)
        txt_d_wm.delete(0, END)
        txt_d_wm.focus()
    else:
        txt_d_wm.config(state=DISABLED)
        e_d_wm.set('0')












def totalcost():
    raw_text = u"\u20B9"
    item1a, item1b, item1c = cinsp.get(), pinsp.get(), int(text_sp.get())
    item2a, item2b, item2c = cinmv.get(), pinmv.get(), int(text_mv.get())
    item3a, item3b, item3c = cindm.get(), pindm.get(), int(text_dm.get())
    item4a, item4b, item4c = cinkp.get(), pinkp.get(), int(text_kp.get())
    item5a, item5b, item5c = cinpt.get(), pinpt.get(), int(text_pt.get())
    item6a, item6b, item6c = cinaj.get(), pinaj.get(), int(text_aj.get())
    item7a, item7b, item7c = cinbm.get(), pinbm.get(), int(text_bm.get())
    item8a, item8b, item8c = cinrt.get(), pinrt.get(), int(text_rt.get())
    item9a, item9b, item9c = cinmm.get(), pinmm.get(), int(text_mm.get())
    item10a, item10b, item10c = cinsc.get(), pinsc.get(), int(text_sc.get())
    item11a, item11b, item11c = cinbb.get(), pinbb.get(), int(text_bb.get())
    item12a, item12b, item12c = cinr.get(), pinr.get(), int(text_r.get())
    item13a, item13b, item13c = cinbr.get(), pinbr.get(), int(text_br.get())
    item14a, item14b, item14c = cinbn.get(), pinbn.get(), int(text_bn.get())
    item15a, item15b, item15c = cinap.get(), pinap.get(), int(text_ap.get())
    item16a, item16b, item16c = ciner.get(), piner.get(), int(text_er.get())
    item17a, item17b, item17c = cinec.get(), pinec.get(), int(text_ec.get())
    item18a, item18b, item18c = cinct.get(), pinct.get(), int(text_ct.get())
    item19a, item19b, item19c = cincb.get(), pincb.get(), int(text_cb.get())
    global price_of_indian
    price_of_indian = (item1a*item1b*item1c) + (item2a*item2b*item3c)+(item3a*item3b*item3c)+(item4a*item4b*item4c)+(item5a*item5b*item5c)+(item6a*item6b*item6c)+(item7a*item7b*item7c)+(item8a*item8b*item8c)+(item9a*item9b*item9c)+(item10a*item10b*item10c)+(item11a*item11b*item11c)+(item12a*item12b*item12c)+(item13a*item13b*item13c)+(item14a*item14b*item14c)+(item15a*item15b*item15c)+(item16a*item16b*item16c)+(item17a*item17b*item17c)+(item18a*item18b*item18c) + (item19a*item19b*item19c)
    print(price_of_indian)
    indianprice.set(raw_text+str(price_of_indian))
    item1x, item1y, item1z = cchcs.get(), pchcs.get(), int(txt_chcs.get())
    item2x, item2y, item2z = cchvs.get(), pchvs.get(), int(txt_chvs.get())
    item3x, item3y, item3z = cchfr.get(), pchfr.get(), int(txt_chfr.get())
    item4x, item4y, item4z = cchm.get(), pchm.get(), int(txt_chm.get())
    item5x, item5y, item5z = cchcp.get(), pchcp.get(), int(txt_chi_pot.get())
    item6x, item6y, item6z = cchcn.get(), pchcn.get(), int(txt_chi_nood.get())
    item7x, item7y, item7z = cchcc.get(), pchcc.get(), int(txt_chi_che.get())
    item8x, item8y, item8z = cchkc.get(), pchkc.get(), int(txt_kad_pann.get())
    price_of_chinese = ((item1x*item1y*item1z)+(item2x*item2y*item2z)+(item3x*item3y*item3z)+(item4x*item4y*item4z)+(item5x*item5y*item5z)+(item6x*item6y*item6z)+(item7x*item7y*item7z)+(item8x*item8y*item8z))
    chinesprice.set(raw_text+str(price_of_chinese))

    item1l, item1m, item1n = cdt.get(), pdt.get(), int(txt_d_t.get())
    item2l, item2m, item2n = cdc.get(), pdc.get(), int(txt_d_c.get())
    item3l, item3m, item3n = cdm.get(), pdm.get(), int(txt_d_m.get())
    item4l, item4m, item4n = cdo.get(), pdo.get(), int(txt_d_o.get())
    item5l, item5m, item5n = cds.get(), pds.get(), int(txt_d_s.get())
    item6l, item6m, item6n = cdma.get(), pdma.get(), int(txt_d_ma.get())
    item7l, item7m, item7n = cdwm.get(), pdwm.get(), int(txt_d_wm.get())
    price_of_drink =((item1l*item1m*item1n) + (item2l*item2m*item2n) + (item3l*item3m*item3n) + (item4l*item4m*item4n) + (item5l*item5m*item5n) + (item6l*item6m*item6n) + (item7l*item7m*item7n))
    drinkprice.set(raw_text+str(price_of_drink))
    global subtotal
    subtotal = (price_of_drink+price_of_chinese+price_of_indian)
    subtotalprice.set(raw_text+str(subtotal))

    totaldam = ((subtotal*5)/100+subtotal)
    totalprice.set(raw_text+str(totaldam))

def receipt():
    raw_text = u"\u20B9"
    receipt_area.delete(1.0,END)
    x=random.randint(100, 10000)
    y = "BILL "+str(x)
    data = time.strftime('%d/%m/%Y')
    receipt_area.insert(END,"Receipt Ref:\t\t\t"+y+"\t\t\t"+data+'\n\n')
    receipt_area.insert(END, "**************************************************************\n")
    receipt_area.insert(END,'Item:\t\t\t\tCost Of Item'+"\n\n")
    receipt_area.insert(END, "**************************************************************\n\n")
    if(cinsp.get()==1):
         receipt_area.insert(END,"Shahi Panner\t\t\t\t\t"+raw_text+str(int(text_sp.get())*pinsp.get())+'\n\n')
    if (cinmv.get() == 1):
        receipt_area.insert(END, "Mix Veg      \t\t\t\t\t" + raw_text + str(int(text_mv.get()) * pinmv.get())+'\n\n')
    if (cindm.get() == 1):
        receipt_area.insert(END, "Dal Makhni   \t\t\t\t\t" + raw_text + str(int(text_dm.get()) * pindm.get()) + '\n\n')
    if (cinkp.get() == 1):
        receipt_area.insert(END, "Kadhai Panner\t\t\t\t\t" + raw_text + str(int(text_kp.get()) * pinkp.get()) + '\n\n')
    if (cinpt.get() == 1):
        receipt_area.insert(END, "Panner Tikka \t\t\t\t\t" + raw_text + str(int(text_pt.get()) * pinpt.get()) + '\n\n')
    if (cinaj.get() == 1):
        receipt_area.insert(END, "Aloo Jerra   \t\t\t\t\t" + raw_text + str(int(text_aj.get()) * pinaj.get()) + '\n\n')
    if (cinbm.get() == 1):
        receipt_area.insert(END, "Bhindi Masala\t\t\t\t\t" + raw_text + str(int(text_bm.get()) * pinbm.get()) + '\n\n')
    if (cinrt.get() == 1):
        receipt_area.insert(END, "Rajma Tadka  \t\t\t\t\t" + raw_text + str(int(text_rt.get()) * pinrt.get()) + '\n\n')
    if (cinmm.get() == 1):
        receipt_area.insert(END, "Mushroom Mutter\t\t\t\t\t" + raw_text + str(int(text_mm.get()) * pinmm.get()) + '\n\n')
    if (cinsc.get() == 1):
        receipt_area.insert(END, "Soya Chap     \t\t\t\t\t" + raw_text + str(int(text_sc.get()) * pinsc.get()) + '\n\n')
    if (cinbb.get() == 1):
        receipt_area.insert(END, "Baigan Bharta \t\t\t\t\t" + raw_text + str(int(text_bb.get()) * pinbb.get()) + '\n\n')
    if (cinr.get() == 1):
        receipt_area.insert(END, "Roti          \t\t\t\t\t" + raw_text + str(int(text_r.get()) * pinr.get()) + '\n\n')
    if (cinbr.get() == 1):
        receipt_area.insert(END, "Butter Roti   \t\t\t\t\t" + raw_text + str(int(text_br.get()) * pinbr.get()) + '\n\n')
    if (cinbn.get() == 1):
        receipt_area.insert(END, "Baigan Naann  \t\t\t\t\t" + raw_text + str(int(text_bn.get()) * pinbn.get()) + '\n\n')
    if (cinap.get() == 1):
        receipt_area.insert(END, "Aloo Paratha  \t\t\t\t\t" + raw_text + str(int(text_ap.get()) * pinap.get()) + '\n\n')
    if (ciner.get() == 1):
        receipt_area.insert(END, "Egg Roll      \t\t\t\t\t" + raw_text + str(int(text_er.get()) * piner.get()) + '\n\n')
    if (cinec.get() == 1):
        receipt_area.insert(END, "Egg Curry     \t\t\t\t\t" + raw_text + str(int(text_ec.get()) * pinec.get()) + '\n\n')
    if (cinct.get() == 1):
        receipt_area.insert(END, "Chicken Tikka \t\t\t\t\t" + raw_text + str(int(text_ct.get()) * pinct.get()) + '\n\n')
    if (cincb.get() == 1):
        receipt_area.insert(END, "Chicken Butter \t\t\t\t\t" + raw_text + str(int(text_bb.get()) * pinbb.get()) + '\n\n')
    if (cchcs.get() == 1):
        receipt_area.insert(END, "Chicken Soup   \t\t\t\t\t" + raw_text + str(int(txt_chcs.get()) * pchcs.get()) + '\n\n')
    if (cchvs.get() == 1):
        receipt_area.insert(END, "Veg Soup      \t\t\t\t\t" + raw_text + str(int(txt_chvs.get()) * pchvs.get()) + '\n\n')
    if (cchfr.get() == 1):
        receipt_area.insert(END, "Fried Rice    \t\t\t\t\t" + raw_text + str(int(txt_chfr.get()) * pchfr.get()) + '\n\n')
    if (cchm.get() == 1):
        receipt_area.insert(END, "Manchurian    \t\t\t\t\t" + raw_text + str(int(txt_chm.get()) * pchm.get()) + '\n\n')
    if (cchcp.get() == 1):
        receipt_area.insert(END, "Chilli Potatoe \t\t\t\t\t" + raw_text + str(int(txt_chi_pot.get()) * pchcp.get()) + '\n\n')
    if (cchcn.get() == 1):
        receipt_area.insert(END, "Chicken Noodle  \t\t\t\t\t" + raw_text + str(int(txt_chi_nood.get()) * pchcn.get()) + '\n\n')
    if (cchcc.get() == 1):
        receipt_area.insert(END, "Chilli Cheese   \t\t\t\t\t" + raw_text + str(int(txt_chi_che.get()) * pchcc.get()) + '\n\n')
    if (cchkc.get() == 1):
        receipt_area.insert(END, "Kadhai Chicken  \t\t\t\t\t" + raw_text + str(int(txt_kad_pann.get()) * pchkc.get()) + '\n\n')
    if(cdt.get()==1):
        receipt_area.insert(END,"Tea              \t\t\t\t\t" +raw_text + str(int(txt_d_t.get()) * pdt.get())+'\n\n')
    if (cdc.get() == 1):
        receipt_area.insert(END,"Coffee            \t\t\t\t\t" + raw_text + str(int(txt_d_c.get()) * pdc.get()) + '\n\n')
    if (cdm.get() == 1):
        receipt_area.insert(END,"Mojito            \t\t\t\t\t" + raw_text + str(int(txt_d_m.get()) * pdm.get()) + '\n\n')
    if (cdo.get() == 1):
        receipt_area.insert(END,"Orange            \t\t\t\t\t" + raw_text + str(int(txt_d_o.get()) * pdo.get()) + '\n\n')
    if (cds.get() == 1):
        receipt_area.insert(END,"Strawberry        \t\t\t\t\t" + raw_text + str(int(txt_d_s.get()) * pds.get()) + '\n\n')
    if (cdma.get() == 1):
        receipt_area.insert(END,"Mango            \t\t\t\t\t" + raw_text + str(int(txt_d_ma.get()) * pdma.get()) + '\n\n')
    if (cdwm.get() == 1):
        receipt_area.insert(END,"Watermelon       \t\t\t\t\t" + raw_text + str(int(txt_d_wm.get()) * pdwm.get()) + '\n\n')
    receipt_area.insert(END,"Sub Total            \t\t\t\t\t" + str(subtotalprice.get())+'\n\n')
    receipt_area.insert(END,"GST                  \t\t\t\t\t"+ '%5' + '\n\n')
    receipt_area.insert(END, "**************************************************************\n\n")
    receipt_area.insert(END,"Total Price          \t\t\t\t\t"+ str(totalprice.get())+'\n\n\n\n')
    receipt_area.insert(END,"\t\t\t    THANK YOU    ")



def save():
    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    bill_data = receipt_area.get(1.0, END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information', 'Your File Is Saved Successfully')

def sendmessege():
    message = str(receipt_area.get(1.0, END))
    number = str(numberentry.get())
    auth ='9kICSlcTw12FiPKbJomGa0Hs8y36ZL4jh5xdgNezR7qfunWDMpBuR3dQvFXtLY9nATS6JMwaliHI2ymk'
    url = "https://www.fast2sms.com/dev/bulkV2"
    params = {
        'authorization': auth,
        'message': message,
        'numbers': number,
        'route': 'q',
        'language': 'english'
    }
    response = requests.get(url, params=params)
    dic = response.json()
    result = dic.get('return')
    if(result==True):
        messagebox.showinfo("Send Successfully", "Message Sent Successfully")
    else:
        messagebox.showerror('Error', 'Message not sent successfully')



def send():
    new = Toplevel()
    new.title("Send")
    new.geometry('400x400')
    new.config(bg="black")
    imageobject = PhotoImage(file="resize-1638162761600905400sendmessege.png")
    label = Label(new, image=imageobject, bg='firebrick4')
    label.pack()
    numberlabel = Label(new, text='Number ', bd=6, relief='ridge')
    numberlabel.place(x=50, y=200)
    numbervariable = StringVar()
    global numberentry
    numberentry = Entry(new, relief='sunken', bd=5, textvariable=numbervariable)
    numberentry.place(x=190, y=200)

    sendbutton = Button(new,text="SEND", fg="black", bg="red", font=("Helvetica",20,"bold"), command=sendmessege)
    sendbutton.place(x=170, y=350)




    new.mainloop()

def pay():
    newpay = Toplevel()
    newpay.title("Scan and Pay")
    newpay.geometry('400x600')
    imageobject = PhotoImage(file="payimage.png")
    imagelabel = Label(newpay, image=imageobject)
    imagelabel.pack()
    newpay.mainloop()

def reset():
    in_sahi_panner.deselect()
    e_sp.set('0')
    text_sp.config(state=DISABLED)
    in_mix_veg.deselect()
    e_mv.set('0')
    text_mv.config(state=DISABLED)
    in_dal_makhni.deselect()
    e_dm.set('0')
    text_dm.config(state=DISABLED)
    in_kadai_panner.deselect()
    e_kp.set('0')
    text_kp.config(state=DISABLED)
    in_panner_tikka.deselect()
    e_pt.set('0')
    text_pt.config(state=DISABLED)
    in_aloo_jerra.deselect()
    e_aj.set('0')
    text_aj.config(state=DISABLED)
    in_bhindi_masala.deselect()
    e_bm.set('0')
    text_bm.config(state=DISABLED)
    in_rajma_tadka.deselect()
    e_rt.set('0')
    text_rt.config(state=DISABLED)
    in_mushroom_mutter.deselect()
    e_mm.set('0')
    text_mm.config(state=DISABLED)
    in_soya_chap.deselect()
    e_sc.set('0')
    text_sc.config(state=DISABLED)
    in_baigan_bharta.deselect()
    e_bb.set('0')
    text_bb.config(state=DISABLED)
    in_roti.deselect()
    e_r.set('0')
    text_r.config(state=DISABLED)
    in_butter_roti.deselect()
    e_br.set('0')
    text_br.config(state=DISABLED)
    in_butter_nann.deselect()
    e_bn.set('0')
    text_bn.config(state=DISABLED)
    in_aloo_paratha.deselect()
    e_ap.set('0')
    text_ap.config(state=DISABLED)

    ch_chicken_soup.deselect()
    e_ch_cs.set('0')
    txt_chcs.config(state=DISABLED)
    ch_veg_soup.deselect()
    e_ch_vs.set('0')
    txt_chvs.config(state=DISABLED)
    ch_fried_rice.deselect()
    e_ch_fr.set('0')
    txt_chfr.config(state=DISABLED)
    ch_manch.deselect()
    e_ch_m.set('0')
    txt_chm.config(state=DISABLED)
    ch_chi_pot.deselect()
    e_ch_cp.set('0')
    txt_chi_pot.config(state=DISABLED)
    ch_chi_nood.deselect()
    e_ch_cn.set('0')
    txt_chi_nood.config(state=DISABLED)
    ch_chi_che.deselect()
    e_ch_cc.set('0')
    txt_chi_che.config(state=DISABLED)
    ch_kad_pann.deselect()
    e_ch_kc.set('0')
    txt_kad_pann.config(state=DISABLED)

    d_tea.deselect()
    e_d_t.set('0')
    txt_d_t.config(state=DISABLED)
    d_cof.deselect()
    e_d_c.set('0')
    txt_d_c.config(state=DISABLED)
    d_moj.deselect()
    e_d_m.set('0')
    txt_d_m.config(state=DISABLED)
    d_ora.deselect()
    e_d_o.set('0')
    txt_d_o.config(state=DISABLED)
    d_straw.deselect()
    e_d_s.set('0')
    txt_d_s.config(state=DISABLED)
    d_mango.deselect()
    e_d_ma.set('0')
    txt_d_ma.config(state=DISABLED)
    d_water_mel.deselect()
    e_d_wm.set('0')
    txt_d_wm.config(state=DISABLED)

    indianprice.set('0')
    chinesprice.set('0')
    drinkprice.set('0')
    subtotalprice.set('0')
    totalprice.set('0')
    receipt_area.delete(1.0, END)
    
# ==================Restaurant name in frame======================
name_frame = Frame(new, width=1600, height=50, bg="black", bd=7, relief="ridge")
name_frame.place(x=0)
name_label = Label(name_frame, text="ASG FOOD'S", bg="black", fg="yellow", font=("Courier", 49, "italic"), underline=1)
name_label.place(x=700, y=0)
# =================Designing menu frames===================================
menu_frame = Frame(new, width=1100, height=860, bg="black", bd=10, relief="ridge")
menu_frame.place(y=50)

food_frame = Frame(menu_frame, width=1100, height=870, bg="white", bd=15, relief="ridge")
food_frame.pack()



indian_frame = Frame(food_frame, width=370, height=840, bg="firebrick4", bd=7, relief="sunken")
indian_frame.place(x=0, y=0)

chinese_frame = Frame(food_frame, width=370, height=840, bg="firebrick4", bd=7, relief="sunken")
chinese_frame.place(x=370, y=0)

drink_frame = Frame(food_frame, width=330, height=840, bg="firebrick4", bd=7, relief="sunken")
drink_frame.place(x=740, y=0)

billing_frame = Frame(new, width=480, height=890, bg="firebrick4", bd=7, relief="sunken").place(x=1120, y=50)
cost_frame = Frame(billing_frame, width=480, height=300, bg="firebrick4", bd=7, relief="sunken").place(x=1120, y=50)
global indianprice
indianprice = StringVar()
indianprice.set('0')
label_indian_cost = Label(cost_frame, text="Cost of Indian Food", fg="white", bg="firebrick4", font=("Helvetica", 18, "bold")).place(x=1127, y=60)
entry_indian_cost = Entry(billing_frame,bg="white", fg="black", textvariable=indianprice)
entry_indian_cost.place(x=1335, y=60, width=80, height=30)
global chinesprice
chinesprice = StringVar()
chinesprice.set('0')
label_chinese_cost = Label(cost_frame, text="Cost of Chinese Food", fg="white", bg="firebrick4", font=("Helvetica", 18, "bold")).place(x=1127, y=100)
entry_chinese_cost = Entry(billing_frame,bg="white", fg="black", textvariable=chinesprice)
entry_chinese_cost.place(x=1335, y=100, width=80, height=30)

global drinkprice
drinkprice = StringVar()
drinkprice.set('0')

label_drink_cost = Label(cost_frame, text="Cost of Drink's", fg="white", bg="firebrick4", font=("Helvetica", 18, "bold")).place(x=1127, y=140)
entry_drink_cost = Entry(billing_frame, bg="white", fg="black",textvariable=drinkprice)
entry_drink_cost.place(x=1335, y=140, width=80, height=30)

global subtotalprice
subtotalprice = StringVar()
subtotalprice.set('0')

label_sub_total = Label(cost_frame, text="Sub Total", fg="white", bg="firebrick4", font=("Helvetica", 18, "bold")).place(x=1127, y=180)
entry_sub_total = Entry(billing_frame,bg="white", fg="black", textvariable=subtotalprice)
entry_sub_total.place(x=1335, y=180, width=80, height=30)


label_gst_cost = Label(cost_frame, text=" GST ", fg="white", bg="firebrick4", font=("Helvetica", 18, "bold")).place(x=1127, y=220)
entry_gst_cost = Label(billing_frame,text="5%", font=("arial",17,"bold"), bg="white", fg="black")
entry_gst_cost.place(x=1335, y=220, width=80, height=30)
global totalprice
totalprice = StringVar()
totalprice.set('0')

label_total_cost = Label(cost_frame, text="Total", fg="white", bg="firebrick4", font=("Helvetica", 18, "bold")).place(x=1127, y=260)
entry_total_cost = Entry(billing_frame,bg="white", fg="black", textvariable=totalprice)
entry_total_cost.place(x=1335, y=260, width=80, height=30)

pay_button = Button(cost_frame, text=" PAY ", fg="black", bg="firebrick4", command=pay, relief="sunken",)
pay_button.place(x=1450, y=300)

global receipt_area
receipt_area = Text(billing_frame, width=64, height=35, bg="white", bd=7, relief="sunken")
receipt_area.place(x=1120, y=350)

total = Button(billing_frame, text="TOTAL", bg="red", fg="black", relief="sunken", bd=20, activeforeground="red", font=("Helvetica", 20, "bold"), command=totalcost)
total.place(x=1130, y=835, width=80, height=40)
receipt = Button(billing_frame, text="RECEIPT", bg="red", fg="black", relief="sunken", bd=20, activeforeground="red", font=("Helvetica", 20, "bold"), command=receipt)
receipt.place(x=1220, y=835, width=93, height=40)
save = Button(billing_frame, text="SAVE", bg="red", fg="black", relief="sunken", bd=20, activeforeground="red", font=("Helvetica", 20, "bold"), command=save)
save.place(x=1325, y=835, width=80, height=40)
send = Button(billing_frame, text="SEND", bg="red", fg="black", relief="sunken", bd=20, activeforeground="red", font=("Helvetica", 20, "bold"), command=send)
send.place(x=1420, y=835, width=80, height=40)
reset = Button(billing_frame, text="RESET", bg="red", fg="black", relief="sunken", bd=20, activeforeground="red", font=("Helvetica", 20, "bold"), command=reset)
reset.place(x=1510, y=835, width=80, height=40)

#==============Payment section==========================










# ========ADDING FOOD IN MENU SECTION====================================
    # 1.======ADDING FOOD IN INDIAN FRAME SECTION============================
       #====VARIABLES=========
indian_menu = Label(indian_frame, text="INDIAN", fg="yellow", bg="black", font=("SUNDAY", 20))
indian_menu.place(x=140, y=0)
indian_menu_veg = Label(indian_frame, text="MAIN COURSE", underline=0, bg="black", fg="yellow", font=("Helvetica", 13))
indian_menu_veg.place(x=0, y=40)
indian_menu_half = Label(indian_frame, text=" PRICE", bg="black", fg="yellow", font=("Helvetica", 13))
indian_menu_half.place(x=180, y=40)
india_menu_full = Label(indian_frame, text="QUANTITY", bg="black", fg="yellow", font=("Helvetica", 13))
india_menu_full.place(x=265, y=40)


cinsp = IntVar() # sahi panne, the first letter represent check box, then 2nd and 3rd is cusine(eg.in-indian)

cinmv = IntVar() # Mix veg
cindm = IntVar() # Dal Makhni
cinkp = IntVar() # Kadai Panner
cinpt = IntVar() # Panner Tikka
cinaj = IntVar() # Aloo Jerra
cinbm = IntVar() # Bhindi Masala
cinrt = IntVar() # Rajma Tadka
cinmm = IntVar() #Mushroom mutter
cinsc = IntVar() #Soya chap
cinbb = IntVar() # Baigan Bharta

cinr = IntVar() #Roti
cinbr = IntVar() #Butter roti
cinbn = IntVar() #Butter Nann

cinap = IntVar() #Aloo paratha

ciner = IntVar() #Egg roll
cinec = IntVar() #egg curry

cinct = IntVar() #Chicken Tandoor
cincb = IntVar() #Chicken Butter Masala

# ================price Variable=====================

pinsp = IntVar() # sahi panner,Rs-150 the first letter represent check box, then 2nd and 3rd is cusine(eg.in-indian)
pinsp.set(150)

pinmv = IntVar() # Mix veg 100
pinmv.set(100)

pindm = IntVar() # Dal Makhni 80
pindm.set(80)

pinkp = IntVar() # Kadai Panner 160
pinkp.set(160)

pinpt = IntVar() # Panner Tikka 200
pinpt.set(200)

pinaj = IntVar() # Aloo Jerra  120
pinaj.set(120)

pinbm = IntVar() # Bhindi Masala 110
pinbm.set(110)

pinrt = IntVar() # Rajma Tadka  140
pinrt.set(140)

pinmm = IntVar() #Mushroom mutter 160
pinmm.set(160)

pinsc = IntVar() #Soya chap 120
pinsc.set(120)

pinbb = IntVar() # Baigan Bharta 130
pinbb.set(130)

pinr = IntVar() #Roti 5
pinr.set(5)

pinbr = IntVar() #Butter roti 15
pinbr.set(15)

pinbn = IntVar() #Butter Nann 25
pinbn.set(25)

pinap = IntVar() #Aloo paratha 30
pinap.set(30)

piner = IntVar() #Egg roll 45
piner.set(45)

pinec = IntVar() #egg curry 90
pinec.set(90)

pinct = IntVar() #Chicken Tandoor 180
pinct.set(180)

pincb = IntVar() #Chicken Butter Masala 220
pincb.set(220)

#================================== variable for entry widget=============================
e_sp = StringVar()
e_sp.set('0')
e_mv = StringVar()
e_mv.set('0')
e_dm = StringVar()
e_dm.set('0')
e_kp = StringVar()
e_kp.set('0')
e_pt = StringVar()
e_pt.set('0')
e_aj = StringVar()
e_aj.set('0')
e_bm = StringVar()
e_bm.set('0')
e_rt = StringVar()
e_rt.set('0')
e_mm = StringVar()
e_mm.set('0')
e_sc = StringVar()
e_sc.set('0')
e_bb = StringVar()
e_bb.set('0')
e_r = StringVar()
e_r.set('0')
e_br = StringVar()
e_br.set('0')
e_bn = StringVar()
e_bn.set('0')
e_ap = StringVar()
e_ap.set('0')
e_er = StringVar()
e_er.set('0')
e_ec = StringVar()
e_ec.set('0')
e_ct = StringVar()
e_ct.set('0')
e_cb = StringVar()
e_cb.set('0') 








# =============FOOD MENUS=========
in_sahi_panner = Checkbutton(indian_frame, selectcolor="purple", text=" Shahi Panner          Rs-150", font=("ariel", 17, "bold"), variable=cinsp, onvalue=1, offvalue=0, bd=4, relief="ridge", bg="firebrick4", fg="white", command=sahipanner)
in_sahi_panner.place(x=0, y=70)

in_mix_veg = Checkbutton(indian_frame, selectcolor="purple", text=" Mix Veg                     Rs-100", font=("ariel", 17, "bold"), variable=cinmv, onvalue=1, offvalue=0, bd=4, relief="ridge", bg="firebrick4", fg="white", command=mixveg)
in_mix_veg.place(x=0, y=105)

in_dal_makhni = Checkbutton(indian_frame, selectcolor="purple", text=" Dal Makhni               Rs-80", font=("ariel", 17, "bold"),variable=cindm, onvalue=1, offvalue=0,bd=4, relief="ridge", bg="firebrick4", fg="white", command=dalmakhni)
in_dal_makhni.place(x=0, y=140)

in_kadai_panner = Checkbutton(indian_frame, selectcolor="purple", text=" Kadai Panner          Rs-160", font=("ariel", 17, "bold"), variable=cinkp, onvalue=1, offvalue=0, bd=4, relief="ridge", bg="firebrick4", fg="white",command=kadaipanner)
in_kadai_panner.place(x=0, y=175)

in_panner_tikka = Checkbutton(indian_frame, selectcolor="purple", text=" Panner Tikka          Rs-200", font=("ariel", 17, "bold"), variable=cinpt, onvalue=1, offvalue=0, bd=4, relief="ridge", bg="firebrick4", fg="white", command=pannertikka)
in_panner_tikka.place(x=0, y=210)

in_aloo_jerra = Checkbutton(indian_frame, selectcolor="purple", text=" Aloo Jerra                Rs-120", font=("ariel", 17, "bold"), variable=cinaj, onvalue=1, offvalue=0,bd=4, relief="ridge", bg="firebrick4", fg="white", command=aloojerra)
in_aloo_jerra.place(x=0, y=245)

in_bhindi_masala = Checkbutton(indian_frame, selectcolor="purple", text=" Bhindi Masala         Rs-110", font=("ariel", 17, "bold"), variable=cinbm, onvalue=1, offvalue=0,bd=4, relief="ridge", bg="firebrick4", fg="white", command=bhindimasala)
in_bhindi_masala.place(x=0, y=280)

in_rajma_tadka = Checkbutton(indian_frame, selectcolor="purple", text=" Rajma Tadka           Rs-140", font=("ariel", 17, "bold"), variable=cinrt, onvalue=1, offvalue=0, bd=4, relief="ridge", bg="firebrick4", fg="white", command=rajmatadka)
in_rajma_tadka.place(x=0, y=315)

in_mushroom_mutter = Checkbutton(indian_frame, selectcolor="purple", text=" Mushroom Mutter Rs-160", font=("ariel", 17, "bold"),variable=cinmm, onvalue=1, offvalue=0, bd=4, relief="ridge", bg="firebrick4", fg="white", command=mushroommattar)
in_mushroom_mutter.place(x=0, y=350)

in_soya_chap = Checkbutton(indian_frame, selectcolor="purple", text=" Soya Chapp             Rs-120", font=("ariel", 17, "bold"), variable=cinsc, onvalue=1, offvalue=0, bd=4, relief="ridge", bg="firebrick4", fg="white", command=soyachap)
in_soya_chap.place(x=0, y=385)

in_baigan_bharta = Checkbutton(indian_frame, selectcolor="purple", text=" Baigan Bharta         Rs-130", font=("ariel", 17, "bold"), variable=cinbb, onvalue=1, offvalue=0, bd=4, relief="ridge", bg="firebrick4", fg="white", command=baiganbharta)
in_baigan_bharta.place(x=0, y=420)

#====Adding Roti and Paratha================
indian_menu_rp= Label(indian_frame, text="Roti & Paratha", underline=0, bg="black", fg="yellow", font=("Helvetica", 15))
indian_menu_rp.place(x=0, y=455)

in_roti = Checkbutton(indian_frame, selectcolor="purple", text=" Roti                              Rs-5", font=("ariel", 17, "bold"),variable=cinr, onvalue=1, offvalue=0,bd=4, relief="ridge", bg="firebrick4", fg="white", command=roti)
in_roti.place(x=0, y=490)

in_butter_roti = Checkbutton(indian_frame, selectcolor="purple", text=" Butter Roti                Rs-15", font=("ariel", 17, "bold"), variable=cinbr, onvalue=1, offvalue=0,bd=4, relief="ridge", bg="firebrick4", fg="white", command=butterroti)
in_butter_roti.place(x=0, y=525)

in_butter_nann = Checkbutton(indian_frame, selectcolor="purple", text=" Butter Nann             Rs-25", font=("ariel", 17, "bold"), variable=cinbn, onvalue=1, offvalue=0,bd=4, relief="ridge", bg="firebrick4", fg="white", command=butternaan)
in_butter_nann.place(x=0, y=560)

in_aloo_paratha = Checkbutton(indian_frame, selectcolor="purple", text="Aloo Paratha            Rs-130", font=("ariel", 17, "bold"), variable=cinap, onvalue=1, offvalue=0,bd=4, relief="ridge", bg="firebrick4", fg="white", command=alooparatha)
in_aloo_paratha.place(x=0, y=595)

indian_menu_chicke = Label(indian_frame, text=" CHICKEN", underline=0, bg="black", fg="yellow", font=("Helvetica", 15))
indian_menu_chicke.place(x=0, y=630)

in_egg_roll = Checkbutton(indian_frame, selectcolor="purple", text=" Egg Roll                  Rs-45", font=("ariel", 17, "bold"), variable=ciner, onvalue=1, offvalue=0,bd=4, relief="ridge", bg="firebrick4", fg="white", command=eggroll)
in_egg_roll.place(x=0, y=665)

in_egg_curry = Checkbutton(indian_frame, selectcolor="purple", text=" Egg Curry              Rs-90", font=("ariel", 17, "bold"), variable=cinec, onvalue=1, offvalue=0,bd=4, relief="ridge", bg="firebrick4", fg="white", command=eggcurry)
in_egg_curry.place(x=0, y=700)

in_chic_tikka = Checkbutton(indian_frame, selectcolor="purple", text=" Chicken Tikka      Rs-180", font=("ariel", 17, "bold"), variable=cinct, onvalue=1, offvalue=0,bd=4, relief="ridge", bg="firebrick4", fg="white", command=chickentikka)
in_chic_tikka.place(x=0, y=735)

in_chic_butter = Checkbutton(indian_frame, selectcolor="purple", text=" Chicken Butter    Rs-220", font=("ariel", 17, "bold"), variable=cincb, onvalue=1, offvalue=0,bd=4, relief="ridge", bg="firebrick4", fg="white", command=chickenbutter)
in_chic_butter.place(x=0, y=770)

#==============Adding Entry  Label to Indian menu============

text_sp = Entry(indian_frame, bg="white", fg="black", bd=3, relief="sunken", state=DISABLED, textvariable=e_sp)
text_sp.place(x=274, y=70, width=60, height=25)

text_mv = Entry(indian_frame, bg="white", fg="black", bd=3, state=DISABLED, textvariable=e_mv, relief="sunken")
text_mv.place(x=274, y=105, width=60, height=25)

text_dm = Entry(indian_frame, bg="white", fg="black", bd=3, state=DISABLED, textvariable=e_dm, relief="sunken")
text_dm.place(x=274, y=140, width=60, height=25)

text_kp = Entry(indian_frame, bg="white", fg="black", bd=3, state=DISABLED, textvariable=e_kp, relief="sunken")
text_kp.place(x=274, y=175, width=60, height=25)

text_pt = Entry(indian_frame, bg="white", fg="black", bd=3, state=DISABLED, textvariable=e_pt, relief="sunken")
text_pt.place(x=274, y=210, width=60, height=25)

text_aj = Entry(indian_frame, bg="white", fg="black", bd=3, state=DISABLED, textvariable=e_aj, relief="sunken")
text_aj.place(x=274, y=245, width=60, height=25)

text_bm = Entry(indian_frame, bg="white", fg="black", bd=3, state=DISABLED, textvariable=e_bm, relief="sunken")
text_bm.place(x=274, y=280, width=60, height=25)

text_rt = Entry(indian_frame, bg="white", fg="black", bd=3, state=DISABLED, textvariable=e_rt, relief="sunken")
text_rt.place(x=274, y=315, width=60, height=25)

text_mm = Entry(indian_frame, bg="white", fg="black", bd=3, state=DISABLED, textvariable=e_mm, relief="sunken")
text_mm.place(x=274, y=350, width=60, height=25)

text_sc = Entry(indian_frame, bg="white", fg="black", bd=3, state=DISABLED, textvariable=e_sc, relief="sunken")
text_sc.place(x=274, y=385, width=60, height=25)

text_bb = Entry(indian_frame, bg="white", fg="black", bd=3, state=DISABLED, textvariable=e_bb, relief="sunken")
text_bb.place(x=274, y=420, width=60, height=25)

text_r = Entry(indian_frame, bg="white", fg="black", bd=3, state=DISABLED, textvariable=e_r, relief="sunken")
text_r.place(x=274, y=490, width=60, height=25)

text_br = Entry(indian_frame, bg="white", fg="black", bd=3, state=DISABLED, textvariable=e_br, relief="sunken")
text_br.place(x=274, y=525, width=60, height=25)

text_bn = Entry(indian_frame, bg="white", fg="black", bd=3,state=DISABLED, textvariable=e_bn, relief="sunken")
text_bn.place(x=274, y=560, width=60, height=25)

text_ap = Entry(indian_frame, bg="white", fg="black", bd=3,state=DISABLED, textvariable=e_ap, relief="sunken")
text_ap.place(x=274, y=595, width=60, height=25)

text_er = Entry(indian_frame, bg="white", fg="black", bd=3,state=DISABLED, textvariable=e_er, relief="sunken")
text_er.place(x=274, y=665, width=60, height=25)

text_ec = Entry(indian_frame, bg="white", fg="black", bd=3,state=DISABLED, textvariable=e_ec, relief="sunken")
text_ec.place(x=274, y=700, width=60, height=25)

text_ct = Entry(indian_frame, bg="white", fg="black", bd=3,state=DISABLED, textvariable=e_ct, relief="sunken")
text_ct.place(x=274, y=735, width=60, height=25)

text_cb = Entry(indian_frame, bg="white", fg="black", bd=3,state=DISABLED, textvariable=e_cb, relief="sunken")
text_cb.place(x=274, y=770, width=60, height=25)







# ===================================Adding chinese menu=======================
chinese_menu = Label(chinese_frame, text="CHINESE", fg="yellow", bg="black", font=("SUNDAY", 20)).place(x=120, y=5)
item_menu = Label(chinese_frame, text="ITEM'S", bg="black", fg="yellow", font=("Helvetica", 13)).place(x=3, y=42)
chinese_menu_price = Label(chinese_frame, text=" PRICE", bg="black", fg="yellow", font=("Helvetica", 13)).place(x=187, y=40)
chinese_menu_quan = Label(chinese_frame, text="QUANTITY", bg="black", fg="yellow", font=("Helvetica", 13)).place(x=275, y=40)

#========================VARIABLE FOR CHINESE MENU ITEM'S==========================
cchcs = IntVar() #chicken soup
cchvs = IntVar() #veg soup
cchfr = IntVar() #Fried rice
cchm = IntVar() # Manchurian
cchcp = IntVar() #chillie potatoe
cchcn = IntVar() #chicke noodle
cchcc = IntVar() # chile cheese

cchkc = IntVar() #Kadhai chicken
#===================================Price Variable============

pchcs = IntVar() #price of chicken soup
pchcs.set(70)
pchvs= IntVar() # Price of veg soup
pchvs.set(60)
pchfr = IntVar()# Price of Fried Rice
pchfr.set(100)
pchm = IntVar() # Price of Manchurian
pchm.set(100)
pchcp = IntVar() #Price of  chille potatoe
pchcp.set(100)
pchcn = IntVar() #Price of chicken noddle
pchcn.set(150)
pchcc = IntVar() #Price of chilie cheese
pchcc.set(250)

pchkc = IntVar() #Price of Kadhai chicken
pchkc.set(280)

#========================variable for entry box===============
e_ch_cs = StringVar()
e_ch_cs.set('0')
e_ch_vs = StringVar()
e_ch_vs.set('0')
e_ch_fr = StringVar()
e_ch_fr.set('0')
e_ch_m = StringVar()
e_ch_m.set('0')
e_ch_cp = StringVar()
e_ch_cp.set('0')
e_ch_cn = StringVar()
e_ch_cn.set('0')
e_ch_cc = StringVar()
e_ch_cc.set('0')
e_ch_kc = StringVar()
e_ch_kc.set('0')




#========= Adding food to menu using above variable in checkbox=============

ch_chicken_soup = Checkbutton(chinese_frame,command=chickensoup ,text="Chicken Soup    Rs-70", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cchcs, onvalue=1, offvalue=0)
ch_chicken_soup.place(x=0, y=75)

txt_chcs = Entry(chinese_frame, bg="white", bd=3,relief="sunken", state=DISABLED, textvariable=e_ch_cs)
txt_chcs.place(x=280, y=75, width=70, height=25)

ch_veg_soup = Checkbutton(chinese_frame,command=vegsoup ,text="Veg Soup             Rs-60", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cchvs, onvalue=1, offvalue=0)
ch_veg_soup.place(x=0, y=130)

txt_chvs = Entry(chinese_frame, bg="white", bd=3, relief="sunken", state=DISABLED, textvariable=e_ch_vs)
txt_chvs.place(x=280, y=130, width=70, height=25)

ch_fried_rice = Checkbutton(chinese_frame,command=friedrice,text="Fried Rice            Rs-100", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cchfr, onvalue=1, offvalue=0)
ch_fried_rice.place(x=0, y=185)

txt_chfr = Entry(chinese_frame, bg="white", bd=3, relief="sunken", state=DISABLED, textvariable=e_ch_fr)
txt_chfr.place(x=280, y=185, width=70, height=25)

ch_manch = Checkbutton(chinese_frame,command=manchurian ,text="Manchurian        Rs-100", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cchm, onvalue=1, offvalue=0)
ch_manch.place(x=0, y=240)
txt_chm = Entry(chinese_frame, bg="white", bd=3, relief="sunken",state=DISABLED, textvariable=e_ch_m)
txt_chm.place(x=280, y=240, width=70, height=25)

ch_chi_pot = Checkbutton(chinese_frame,command=chillipot ,text="Chilli Potatoe     Rs-100", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cchcp, onvalue=1, offvalue=0)
ch_chi_pot.place(x=0, y=295)
txt_chi_pot = Entry(chinese_frame, bg="white", bd=3, relief="sunken",state=DISABLED, textvariable=e_ch_cp)
txt_chi_pot.place(x=280, y=295, width=70, height=25)

ch_chi_nood = Checkbutton(chinese_frame,command=chickennood ,text="Chicken Noodle Rs-150", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cchcn, onvalue=1, offvalue=0)
ch_chi_nood.place(x=0, y=350)
txt_chi_nood = Entry(chinese_frame, bg="white", bd=3, relief="sunken",state=DISABLED, textvariable=e_ch_cn)
txt_chi_nood.place(x=280, y=350, width=70, height=25)

ch_chi_che = Checkbutton(chinese_frame, command=chillicheese,text="Chilli Chesse       Rs-250", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cchcc, onvalue=1, offvalue=0)
ch_chi_che.place(x=0, y=405)
txt_chi_che = Entry(chinese_frame, bg="white", bd=3, relief="sunken",state=DISABLED, textvariable=e_ch_cc)
txt_chi_che.place(x=280, y=405, width=70, height=25)

ch_kad_pann = Checkbutton(chinese_frame,command=kadaichicken,text="Kadai Chicken    Rs-280", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cchkc, onvalue=1, offvalue=0)
ch_kad_pann.place(x=0, y=460)
txt_kad_pann = Entry(chinese_frame, bg="white", bd=3, relief="sunken", state=DISABLED, textvariable=e_ch_kc)
txt_kad_pann.place(x=280, y=460, width=70, height=25)


#=====================Add drink to Drink menu===========================
drink_menu = Label(drink_frame, text="DRINK'S", fg="yellow", bg="black", font=("SUNDAY", 20)).place(x=120, y=5)
ditem_menu = Label(drink_frame, text="ITEM'S", bg="black", fg="yellow", font=("Helvetica", 13)).place(x=3, y=42)
drink_menu_price = Label(drink_frame, text=" PRICE", bg="black", fg="yellow", font=("Helvetica", 13)).place(x=147, y=40)
drink_menu_quan = Label(drink_frame, text="QUANTITY", bg="black", fg="yellow", font=("Helvetica", 13)).place(x=235, y=40)

# ========variable for drink menu items================================
cdt = IntVar() # Tea
cdc = IntVar() # cofee
cdm = IntVar() # mojito
cdo = IntVar() #orange
cds = IntVar() #strawberry
cdma = IntVar() # Mango
cdwm = IntVar() #Watermellon
#===========Variable for price of drink=================================
pdt = IntVar()
pdt.set(15)
pdc = IntVar()
pdc.set(30)
pdm = IntVar()
pdm.set(100)
pdo = IntVar()
pdo.set(60)
pds = IntVar()
pds.set(120)
pdma = IntVar()
pdma.set(140)
pdwm = IntVar()
pdwm.set(120)
# ==================== variable for entry in drink============
e_d_t = StringVar()
e_d_t.set('0')
e_d_c = StringVar()
e_d_c.set('0')
e_d_m = StringVar()
e_d_m.set('0')
e_d_o = StringVar()
e_d_o.set('0')
e_d_s = StringVar()
e_d_s.set('0')
e_d_ma = StringVar()
e_d_ma.set('0')
e_d_wm = StringVar()
e_d_wm.set('0')

#=========================Adding menu in drink section======================

d_tea = Checkbutton(drink_frame, text="Tea                Rs-15", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cdt, onvalue=1, offvalue=0, command=tea)
d_tea.place(x=0, y=75)
txt_d_t = Entry(drink_frame, bg="white", bd=3, relief="sunken", state=DISABLED, textvariable=e_d_t)
txt_d_t.place(x=240, y=75, width=70, height=25)

d_cof = Checkbutton(drink_frame, text="Coffee          Rs-15", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cdc, onvalue=1, offvalue=0, command=cofee)
d_cof.place(x=0, y=140)
txt_d_c = Entry(drink_frame, bg="white", bd=3, relief="sunken", state=DISABLED, textvariable=e_d_c)
txt_d_c.place(x=240, y=140, width=70, height=25)

d_moj = Checkbutton(drink_frame, text="Mojito          Rs-100", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cdm, onvalue=1, offvalue=0, command=mojito)
d_moj.place(x=0, y=205)
txt_d_m = Entry(drink_frame, bg="white", bd=3, relief="sunken", state=DISABLED, textvariable=e_d_m)
txt_d_m.place(x=240, y=205, width=70, height=25)

d_ora = Checkbutton(drink_frame, text="Orange          Rs-60", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cdo, onvalue=1, offvalue=0, command=orange)
d_ora.place(x=0, y=270)
txt_d_o = Entry(drink_frame, bg="white", bd=3, relief="sunken", state=DISABLED, textvariable=e_d_o)
txt_d_o.place(x=240, y=270, width=70, height=25)

d_straw = Checkbutton(drink_frame, text="Strawberry  Rs-120", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cds, onvalue=1, offvalue=0, command=strawberry)
d_straw.place(x=0, y=335)
txt_d_s = Entry(drink_frame, bg="white", bd=3, relief="sunken", state=DISABLED, textvariable=e_d_s)
txt_d_s.place(x=240, y=335, width=70, height=25)

d_mango = Checkbutton(drink_frame, text="Mango      Rs-140", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cdma, onvalue=1, offvalue=0, command=mango)
d_mango.place(x=0, y=400)
txt_d_ma = Entry(drink_frame, bg="white", bd=3, relief="sunken", state=DISABLED, textvariable=e_d_ma)
txt_d_ma.place(x=240, y=400, width=70, height=25)

d_water_mel = Checkbutton(drink_frame, text="Watermelon  Rs-120", fg="white", bg="firebrick4", relief="ridge", font=("ariel", 22, "bold"), variable=cdwm, onvalue=1, offvalue=0, command=watermellon)
d_water_mel.place(x=0, y=465)
txt_d_wm = Entry(drink_frame, bg="white", bd=3, relief="sunken", state=DISABLED, textvariable=e_d_wm)
txt_d_wm.place(x=240, y=465, width=70, height=25)


new.mainloop()
