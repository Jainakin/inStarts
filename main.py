from fpdf import FPDF
from pathlib import Path
from tkinter import END, Tk, Canvas, Entry, Button, PhotoImage, Toplevel, Label, StringVar, OptionMenu
import datetime
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import os

today = datetime.date.today().strftime("%d/%m/%Y")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


#Lists start
billing_list = []
shipping_list = []
invoice_date_duedate_list = []
seller_details_list = []
own_company_name = []
inventory = ['select an item','custom item']
item_list = []
#Lists end

#Read me start
def open_readme():
    os.system("open " + "README.txt")
#Read me end

#Loading inventory start
inventory_exel = pd.read_excel('inventory.xlsx')
item_row_len = len(inventory_exel['Item Name'])
for i in range(item_row_len):
    inventory.append(inventory_exel['Item Name'][i])
#Loading inventory end

def print_seller_details():

    #Grabbing details for printing start
    street_address = seller_details_list[0]
    ciy_state_zip = seller_details_list[1]
    phone = seller_details_list[2]
    email_address = seller_details_list[3]
    website = seller_details_list[4]
    gst_no = seller_details_list[5]
    invoice_no = f'Invoice No   {invoice_date_duedate_list[1]}'
    bill_reciepient_name = billing_list[0]
    bill_company_name = billing_list[1]
    bill_street_address = billing_list[2]
    bill_city_state_zip = billing_list[3]

    bill_phone = billing_list[4]
    ship_reciepient_name = shipping_list[0]
    ship_company_name = shipping_list[1]
    ship_street_address = shipping_list[2]
    ship_city_state_zip = shipping_list[3]
    ship_phone = shipping_list[4]
    subtotal_print = entry_4.get()
    discount_print = entry_3.get()
    tax_print = entry_2.get()
    total_print = entry_1.get()
    #Grabbing details for printing end

    #Declraing PDF Class start
    class PDF(FPDF):

        def header(self):
            # Apple Font
            self.image('logo.png', 25, 21, 10)
            self.ln(20)
            self.set_font('helvetica', '', 25)
            self.set_text_color(55, 55, 55)
            self.cell(26)
            self.cell(0, 0, own_company_name[0], border=False, ln=0, align='')

            # Invoice Font
            self.set_font('helvetica', '', 35)
            self.set_text_color(137, 137, 137)
            title_w = self.get_string_width('Invoice') + 26
            doc_w = self.w
            self.set_x(doc_w - title_w)
            self.cell(0, 0, 'Invoice', border=False, ln=1)

        def footer(self):
            self.set_y(-15)
            doc_w = self.w
            logo_position = (doc_w - 5) // 2
            self.image('logo.png', logo_position, 260, 5)
            self.set_font('helvetica', '', 10)
            self.set_text_color(0, 132, 255)
            self.cell(0, 10, website, align='C', link=website)
    #Declraing PDF Class end

    #PDF Initialization start
    pdf = PDF('P','mm','Letter')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    doc_w = pdf.w
    #PDF Initialization end

    #Print Seller Detials start
    pdf.set_font('helvetica','',13)
    pdf.set_text_color(130,130,130)
    pdf.ln(10)
    pdf.cell(15)
    pdf.cell(0,0,f'{street_address}')
    pdf.ln(6)
    pdf.cell(15)
    pdf.cell(0,0,f'{ciy_state_zip}')
    pdf.set_x(doc_w - pdf.get_string_width(f'GSTIN   {gst_no}') - 26)
    pdf.cell(0,0,f'GSTIN   {gst_no}',align='L')
    pdf.ln(6)
    pdf.cell(15)
    pdf.cell(0,0,f'{phone}')
    pdf.set_x(doc_w - pdf.get_string_width(f'Date   {today}') - 26)
    pdf.cell(0,0,f'Date   {today}',align='L')
    pdf.ln(6)
    pdf.cell(15)
    pdf.cell(0,0,f'{email_address}')
    pdf.set_x(doc_w - pdf.get_string_width(f'{invoice_no}') - 26)
    pdf.cell(0,0,f'{invoice_no}',align='L')
    pdf.ln(6)
    pdf.cell(15)
    pdf.cell(0,0,f'{website}')
    pdf.set_x(doc_w - pdf.get_string_width(f'Due date   {today}') - 26)
    pdf.cell(0,0,f'Due date   {today}',align='L')
    #Print Seller Detials end

    #Billing and Shipping Details start
    pdf.ln(15)
    pdf.cell(15)
    pdf.set_text_color(60,60,60)
    pdf.set_fill_color(250,250,250)
    pdf.set_font('helvetica','',12)
    pdf.cell(81.15,7,'      BILLED TO',fill=1)
    pdf.cell(0.5)
    pdf.cell(81.15,7,'      SHIPPED TO',fill=1)
    pdf.ln()
    pdf.cell(15)
    pdf.set_font('helvetica','',10)
    pdf.set_text_color(130,130,130)
    pdf.cell(81.15,6,f'       {bill_reciepient_name}',fill=1)
    pdf.cell(0.5)
    pdf.cell(81.15,6,f'       {ship_reciepient_name}',fill=1)
    pdf.ln()
    pdf.cell(15)
    pdf.cell(81.15,6,f'       {bill_company_name}',fill=1)
    pdf.cell(0.5)
    pdf.cell(81.15,6,f'       {ship_company_name}',fill=1)
    pdf.ln()
    pdf.cell(15)
    pdf.cell(81.15,6,f'       {bill_street_address}',fill=1)
    pdf.cell(0.5)
    pdf.cell(81.15,6,f'       {ship_street_address}',fill=1)
    pdf.ln()
    pdf.cell(15)
    pdf.cell(81.15,6,f'       {bill_city_state_zip}',fill=1)
    pdf.cell(0.5)
    pdf.cell(81.15,6,f'       {ship_city_state_zip}',fill=1)
    pdf.ln()
    pdf.cell(15)
    pdf.cell(81.15,6,f'       {bill_phone}',fill=1)
    pdf.cell(0.5)
    pdf.cell(81.15,6,f'       {ship_phone}',fill=1)
    #Billing and Shipping Details end


    #Description Quantity UnitPrice Amount Printing start
    pdf.ln(15)
    pdf.cell(15)
    pdf.set_text_color(60,60,60)
    pdf.cell(98.34,6,'   Description',fill=1)
    pdf.set_text_color(130,130,130)
    pdf.cell(9.365714285714287,6,'Qty',align='C',fill=1)
    pdf.cell(28.09714285714286,6,'Unit Price',align='C',fill=1)
    pdf.cell(28.09714285714286,6,'Amount',align='C',fill=1)
    #Description Quantity UnitPrice Amount Printing end


    #Bill Items
    for item in item_list:
        print_item = item[0]
        print_quantity = item[1]
        print_unit_price = item[2]
        print_amount = print_quantity*print_unit_price
        pdf.ln()
        pdf.cell(15)
        pdf.set_text_color(60,60,60)
        pdf.cell(98.34,6,f'   {print_item}',fill=1)
        pdf.set_text_color(130,130,130)
        pdf.cell(9.365714285714287,6,f'{print_quantity}',align='C',fill=1)
        pdf.cell(28.09714285714286,6,f'{print_unit_price}',align='C',fill=1)
        pdf.cell(28.09714285714286,6,f'{print_amount}',align='C',fill=1)
    item_list_len = len(item_list)
    if item_list_len<14:
        empty_print = (14-item_list_len)*7
        pdf.ln(empty_print)



    #Subtotal Discount Tax Total printing start
    pdf.ln()
    pdf.cell(122.7057142857143)
    pdf.cell(28.09714285714286,6,'Subtotal',align='R')
    pdf.set_font('helvetica','B',10)
    pdf.set_text_color(44,44,46)
    pdf.cell(28.09714285714286,6,f'{round(float(subtotal_print),2)}',align='R')

    pdf.ln()
    pdf.cell(122.7057142857143)
    pdf.set_font('helvetica','',10)
    pdf.set_text_color(130,130,130)
    pdf.cell(28.09714285714286,6,'Discount',align='R')
    pdf.set_font('helvetica','B',10)
    pdf.set_text_color(44,44,46)
    pdf.cell(28.09714285714286,6,f'{round(float(discount_print),2)}',align='R')

    pdf.ln()
    pdf.cell(122.7057142857143)
    pdf.set_font('helvetica','',10)
    pdf.set_text_color(130,130,130)
    pdf.cell(28.09714285714286,6,'Tax',align='R')
    pdf.set_font('helvetica','B',10)
    pdf.set_text_color(44,44,46)
    pdf.cell(28.09714285714286,6,f'{round(float(tax_print),2)}',align='R')

    pdf.ln()
    pdf.cell(122.7057142857143)
    pdf.set_font('helvetica','',10)
    pdf.set_text_color(130,130,130)
    pdf.cell(28.09714285714286,6,'Total',align='R')
    pdf.set_font('helvetica','B',10)
    pdf.set_text_color(44,44,46)
    pdf.cell(28.09714285714286,6,f'{round(float(total_print),2)}',align='R')
    #Subtotal Discount Tax Total printing end

    #PDF output start
    pdf.output('invoice.pdf')
    #PDF output end


#Getting details from gui start
def get_item_details():

    item = ''
    quantity = ''
    unit_price = ''

    if variable.get() != 'select an item':
        item = entry_8.get()

    try:
        quantity = eval(entry_7.get())
        unit_price = eval(entry_6.get())
    except:
        quantiy = ''
        unit_price = ''
    
    if item != '' and quantity != '' and unit_price != '':
        item_obj = [item,quantity,unit_price]
        item_list.append(item_obj)
    print(item_list)

    subtotal = 0
    for item in item_list:
        subtotal += item[1]*item[2]
    entry_4.delete(0,END)
    entry_4.insert(0,subtotal)

    discount_decimal = entry_23.get()
    discount_decimal = discount_decimal.replace('%','')
    if discount_decimal == 0 or discount_decimal == '':
        entry_3.delete(0,END)
        entry_3.insert(0,'NA')
    else:
        discount_price = subtotal*((eval(discount_decimal))/100)
        entry_3.delete(0,END)
        entry_3.insert(0,discount_price)

    tax_decimal = entry_22.get()
    tax_decimal = tax_decimal.replace('%','')
    if tax_decimal == 0 or tax_decimal == '':
        entry_2.delete(0,END)
        entry_2.insert(0,'NA')
    else:
        if entry_3.get() == 'NA':
            tax_price = subtotal*((eval(tax_decimal))/100)
        else:
            tax_price = (subtotal-discount_price)*((eval(tax_decimal))/100)
        entry_2.delete(0,END)
        entry_2.insert(0,tax_price)

    if entry_2.get() == 'NA' and entry_3.get() == 'NA':
        total = subtotal
    elif entry_2.get() == 'NA':
        total = subtotal-discount_price
    elif entry_3.get() == 'NA':
        total = subtotal+tax_price
    else:
        total = subtotal-discount_price+tax_price
    entry_1.delete(0,END)
    entry_1.insert(0,total)

    variable.set(inventory[0])
    entry_7.delete(0,END)
    entry_6.delete(0,END)
#Getting details from gui start

#Setting item start
def set_item():
    if variable.get() == 'custom item':
        pass
    elif variable.get() != 'select an item':
        entry_8.delete(0,END)
        entry_8.insert(0,variable.get())
    else:
        entry_8.delete(0,END)
    window.after(1,set_item)
#Setting item end

#Setting amount start
def set_amount():
    try:
        amount = eval(entry_7.get())*eval(entry_6.get())
        entry_5.delete(0,END)
        entry_5.insert(0,amount)
    except:
        entry_5.delete(0,END)
    finally:
        window.after(1, set_amount)
#Setting amount end

#Getting billing and shipping details start
def get_billing_shipping():

    billing_list.clear()
    billing_list.append(entry_9.get())
    billing_list.append(entry_10.get())
    billing_list.append(entry_11.get())
    billing_list.append(entry_12.get())
    billing_list.append(entry_13.get())

    shipping_list.clear()
    shipping_list.append(entry_14.get())
    shipping_list.append(entry_15.get())
    shipping_list.append(entry_16.get())
    shipping_list.append(entry_17.get())
    shipping_list.append(entry_18.get())

    invoice_date_duedate_list.clear()
    invoice_date_duedate_list.append(entry_19.get())
    invoice_date_duedate_list.append(entry_20.get())
    invoice_date_duedate_list.append(entry_21.get())

    print(billing_list)
    print(shipping_list)
    print(invoice_date_duedate_list)
#Getting billing and shipping details start

#pop-up window start
def ocm():
    global pop
    pop = Toplevel(window)
    pop.geometry("332x107")
    pop.configure(bg = "#FFFFFF")
    pop.title("Seller Details")

    #text box start
    pop_entry_1 = Entry(
        pop,
        bd=0,
        bg="#F0F0F0",
        highlightthickness=0,
        font=('Arial 16'),
        fg='black'
    )
    pop_entry_1.insert(0,"type here")
    pop_entry_1.place(
        x=23.0,
        y=41.0,
        width=286.0,
        height=23.0
    )
    #text box end

    #Button Start
    button_1 = Button(
        pop,
        borderwidth=0,
        bg='white',
        activebackground='black',
        fg='black',
        activeforeground='black',
        text='save',
        command=lambda:get_own_company_name()
    )
    button_1.place(
        x=118.0,
        y=73.0,
        width=96.0,
        height=25.0
    )
    #Button End

    #Text start(don't edit)
    pop_label = Label(pop,
                text="Enter your comany name",
                bg="white",
                fg="#0336FF",
                font=('Arial Bold', 18 * -1)
                )
    pop_label.place(x=20,y=5)
    #Text end(don't edit)

    def get_own_company_name():
        own_company_name.clear()
        own_company_name.append(pop_entry_1.get())
        pop.withdraw()
        print(own_company_name)
#pop-up window end

#pop-up window start
def sd():
    global pop
    pop = Toplevel(window)
    pop.geometry("332x277")
    pop.configure(bg = "#FFFFFF")
    pop.title("Seller Details")

    #Seller Street Address start
    pop_entry_1 = Entry(
        pop,
        bd=0,
        bg="#F0F0F0",
        highlightthickness=0,
        font=('Arial 16'),
        fg='black'
    )
    pop_entry_1.insert(0,"Street Address")
    pop_entry_1.place(
        x=23.0,
        y=41.0,
        width=286.0,
        height=23.0
    )
    #Seller Street Address end

    #Seller City, State, Zip start
    pop_entry_2 = Entry(
        pop,
        bd=0,
        bg="#F0F0F0",
        highlightthickness=0,
        font=('Arial 16'),
        fg='black'
    )
    pop_entry_2.insert(0,"City, State, Zip")
    pop_entry_2.place(
        x=23.0,
        y=75.0,
        width=286.0,
        height=23.0
    )
    #Seller City, State, Zip end

    #Seller Phone start
    pop_entry_3 = Entry(
        pop,
        bd=0,
        bg="#F0F0F0",
        highlightthickness=0,
        font=('Arial 16'),
        fg='black'
    )
    pop_entry_3.insert(0,"Phone")
    pop_entry_3.place(
        x=23.0,
        y=109.0,
        width=286.0,
        height=23.0
    )
    #Seller Phone end

    #Seller Email start
    pop_entry_4 = Entry(
        pop,
        bd=0,
        bg="#F0F0F0",
        highlightthickness=0,
        font=('Arial 16'),
        fg='black'
    )
    pop_entry_4.insert(0,"Email")
    pop_entry_4.place(
        x=23.0,
        y=143.0,
        width=286.0,
        height=23.0
    )
    #Seller Email end

    #Seller Website start
    pop_entry_5 = Entry(
        pop,
        bd=0,
        bg="#F0F0F0",
        highlightthickness=0,
        font=('Arial 16'),
        fg='black'
    )
    pop_entry_5.insert(0,"Website")
    pop_entry_5.place(
        x=23.0,
        y=177.0,
        width=286.0,
        height=23.0
    )
    #Seller Website end

    #Seller GSTIN Start
    pop_entry_6 = Entry(
        pop,
        bd=0,
        bg="#F0F0F0",
        highlightthickness=0,
        font=('Arial 16'),
        fg='black'
    )
    pop_entry_6.insert(0,"GSTIN")
    pop_entry_6.place(
        x=23.0,
        y=211.0,
        width=286.0,
        height=23.0
    )
    #Seller GSTIN end

    #Button Start
    button_1 = Button(
        pop,
        borderwidth=0,
        bg='white',
        activebackground='black',
        fg='black',
        activeforeground='black',
        text='save',
        command=lambda:get_seller_details()
    )
    button_1.place(
        x=118.0,
        y=243.0,
        width=96.0,
        height=25.0
    )
    #Button End

    #Text start(don't edit)
    pop_label = Label(pop,
                text="Seller Details",
                bg="white",
                fg="#0336FF",
                font=('Arial Bold', 18 * -1)
                )
    pop_label.place(x=20,y=5)
    #Text end(don't edit)

    def get_seller_details():
        seller_details_list.clear()
        seller_details_list.append(pop_entry_1.get())
        seller_details_list.append(pop_entry_2.get())
        seller_details_list.append(pop_entry_3.get())
        seller_details_list.append(pop_entry_4.get())
        seller_details_list.append(pop_entry_5.get())
        seller_details_list.append(pop_entry_6.get())
        pop.withdraw()
        print(seller_details_list)
#pop-up window end
    

#Window start
window = Tk()
window.geometry("866x768")
window.configure(bg = "#FFFFFF")
window.title("Instarts")
#Window end

#Canvas start
#Canvas created
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 866,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
#White background rectangle created
canvas.create_rectangle(
    0.0,
    0.0,
    724.0,
    768.0,
    fill="#FFFFFF",
    outline="")
#Blue background rectangle created
canvas.create_rectangle(
    724.0,
    0.0,
    866.0,
    768.0,
    fill="#0336FF",
    outline="")
#Canvas end

#Total display box start
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("Arial 18"),
    fg='black',
    justify='right'
)
entry_1.place(
    x=544.0,
    y=671.0,
    width=150.0,
    height=19.0
)
#Total display box end

#Taxes display box start
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("Arial 18"),
    fg='black',
    justify='right'
)
entry_2.place(
    x=544.0,
    y=627.0,
    width=150.0,
    height=19.0
)
#Taxes dislpay box end

#Discount dislpay box start
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("Arial 18"),
    fg='black',
    justify='right'
)
entry_3.place(
    x=544.0,
    y=593.0,
    width=152.0,
    height=19.0
)
#Discount dislpay box end

#Subtotal display box start
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("Arial 18"),
    fg='black',
    justify='right'
)
entry_4.place(
    x=544.0,
    y=563.0,
    width=150.0,
    height=19.0
)
#Subtotal display box end

#Amount display box start
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("Arial 16"),
    fg='black',
)
entry_5.place(
    x=631.0,
    y=494.0,
    width=63.0,
    height=23.0
)
#Amount display box end

#Unit price start
entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    545.5,
    504.50000000000006,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial 16"),
    fg='black'
)
entry_6.place(
    x=514.0,
    y=494.0,
    width=63.0,
    height=23.0
)
#Unit price end

#Quantity start
entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    426.0,
    504.50000000000006,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial 16"),
    fg='black'
)
entry_7.place(
    x=400.0,
    y=494.0,
    width=52.0,
    height=23.0
)
#Quantity end

#Item start
entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    181.0,
    504.50000000000006,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=("Arial 16"),
    fg='black'
)
entry_8.place(
    x=38.0,
    y=494.0,
    width=286.0,
    height=23.0
)
#Item end

variable = StringVar(window)
variable.set(inventory[0]) # default value
w = OptionMenu(window, variable, *inventory)
w.place(x=30.0,y=465.0)
entry_8.insert(0,variable.get())


#Bill Recipient start
entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    181.0,
    227.50000000000006,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=('Arial 16'),
    fg='black'
)
entry_9.insert(0,"Reciepient name")
entry_9.place(
    x=38.0,
    y=217.0,
    width=286.0,
    height=23.0
)
#Bill Recipient end

#Bill company start
entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    181.0,
    261.50000000000006,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=('Arial 16'),
    fg='black'
)
entry_10.insert(0,"Company name")
entry_10.place(
    x=38.0,
    y=251.0,
    width=286.0,
    height=23.0
)
#Bill company end

#Bill Street Address start
entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    181.0,
    295.50000000000006,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=('Arial 16'),
    fg='black'
)
entry_11.insert(0,"Street address")
entry_11.place(
    x=38.0,
    y=285.0,
    width=286.0,
    height=23.0
)
#Bill Street Address end

#Bill City, State, Zip start
entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    181.0,
    329.50000000000006,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=('Arial 16'),
    fg='black'
)
entry_12.insert(0,"City,State,Zip")
entry_12.place(
    x=38.0,
    y=319.0,
    width=286.0,
    height=23.0
)
#Bill City, State, Zip end

#Bill Phone start
entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    181.0,
    363.50000000000006,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=('Arial 16'),
    fg='black'
)
entry_13.insert(0,"Phone")
entry_13.place(
    x=38.0,
    y=353.0,
    width=286.0,
    height=23.0
)
#Bill Phone end

#Ship Recipient start
entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    543.0,
    227.50000000000006,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=('Arial 16'),
    fg='black'
)
entry_14.insert(0,"Reciepient name")
entry_14.place(
    x=400.0,
    y=217.0,
    width=286.0,
    height=23.0
)
#Ship Recipient end

#Ship Comapany start
entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    543.0,
    261.50000000000006,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=('Arial 16'),
    fg='black'
)
entry_15.insert(0,"Company name")
entry_15.place(
    x=400.0,
    y=251.0,
    width=286.0,
    height=23.0
)
#Ship Comapany end

#Ship Street Address start
entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    543.0,
    295.50000000000006,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=('Arial 16'),
    fg='black'
)
entry_16.insert(0,"Street Address")
entry_16.place(
    x=400.0,
    y=285.0,
    width=286.0,
    height=23.0
)
#Ship Street Address end

#Ship City, State, Zip start
entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    543.0,
    329.50000000000006,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=('Arial 16'),
    fg='black'
)
entry_17.insert(0,"City,State,Zip")
entry_17.place(
    x=400.0,
    y=319.0,
    width=286.0,
    height=23.0
)
#Ship City, State ,Zip end

#Ship Phone start
entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    543.0,
    363.50000000000006,
    image=entry_image_18
)
entry_18 = Entry(
    bd=0,
    bg="#F0F0F0",
    highlightthickness=0,
    font=('Arial 16'),
    fg='black'
)
entry_18.insert(0,"Phone")
entry_18.place(
    x=400.0,
    y=353,
    width=286.0,
    height=23.0
)
#Ship Phone end

#Instarts name tag start
canvas.create_text(
    30.0,
    23.000000000000057,
    anchor="nw",
    text="Instarts",
    fill="#000000",
    font=("Arial Bold", 34 * -1)
)
#Instarts name tag end

#Date start
entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(
    134.0,
    132.50000000000006,
    image=entry_image_19
)
entry_19 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=('Arial 20'),
    fg='black'
)
entry_19.insert(0,today)
entry_19.place(
    x=83.0,
    y=121.00000000000006,
    width=102.0,
    height=21.0
)
canvas.create_text(
    30.0,
    120.00000000000006,
    anchor="nw",
    text="Date:",
    fill="#000000",
    font=("Arial", 20 * -1)
)
#Date end

#Invoice# start
entry_image_20 = PhotoImage(
    file=relative_to_assets("entry_20.png"))
entry_bg_20 = canvas.create_image(
    377.5,
    131.00000000000006,
    image=entry_image_20
)
entry_20 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=('Arial 24'),
    fg='black'
)
entry_20.insert(0,"#000001")
entry_20.place(
    x=329.0,
    y=117.00000000000006,
    width=97.0,
    height=26.0
)
canvas.create_text(
    247.0,
    116.00000000000006,
    anchor="nw",
    text="Invoice",
    fill="#000000",
    font=("Arial", 24 * -1)
)
#Invoice# end

#Due date start
entry_image_21 = PhotoImage(
    file=relative_to_assets("entry_21.png"))
entry_bg_21 = canvas.create_image(
    644.0,
    132.50000000000006,
    image=entry_image_21
)
entry_21 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font=('Arial 20'),
    fg='black'
)
entry_21.insert(0,today)
entry_21.place(
    x=593.0,
    y=121.00000000000006,
    width=102.0,
    height=21.0
)
canvas.create_text(
    498.0,
    120.00000000000006,
    anchor="nw",
    text="Due Date:",
    fill="#000000",
    font=("Arial", 20 * -1)
)
#Due date end

#Text start(don't edit)
canvas.create_text(
    30.0,
    180.00000000000006,
    anchor="nw",
    text="Bill To",
    fill="#000000",
    font=("Arial", 18 * -1)
)

canvas.create_text(
    392.0,
    180.00000000000006,
    anchor="nw",
    text="Ship To",
    fill="#000000",
    font=("Arial", 18 * -1)
)

canvas.create_text(
    30.0,
    424.00000000000006,
    anchor="nw",
    text="Item",
    fill="#000000",
    font=("Arial", 18 * -1)
)

canvas.create_text(
    392.0,
    424.00000000000006,
    anchor="nw",
    text="Quantity",
    fill="#000000",
    font=("Arial", 18 * -1)
)

canvas.create_text(
    506.0,
    424.00000000000006,
    anchor="nw",
    text="Unit Price",
    fill="#000000",
    font=("Arial", 18 * -1)
)

canvas.create_text(
    631.0,
    424.00000000000006,
    anchor="nw",
    text="Amount",
    fill="#000000",
    font=("Arial", 18 * -1)
)

canvas.create_text(
    383.0,
    561.0,
    anchor="nw",
    text="Subtotal",
    fill="#979797",
    font=("Arial", 18 * -1)
)

canvas.create_text(
    383.0,
    593.0,
    anchor="nw",
    text="Discount",
    fill="#979797",
    font=("Arial", 18 * -1)
)

canvas.create_text(
    383.0,
    625.0,
    anchor="nw",
    text="Taxes",
    fill="#979797",
    font=("Arial", 18 * -1)
)

canvas.create_text(
    383.0,
    669.0,
    anchor="nw",
    text="Total",
    fill="#000000",
    font=("Arial Bold", 18 * -1)
)
#Text end(don't edit)

#Add item button start
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=get_item_details,
    relief="flat"
)
button_1.place(
    x=30.0,
    y=560.0,
    width=90.0,
    height=23.0
)
#Add item button end

#Need help button start
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:open_readme(),
    relief="flat"
)
button_2.place(
    x=30.0,
    y=724.0,
    width=181.0,
    height=24.0
)
#Need help button end

#Text start(don't edit)
canvas.create_text(
    747.0,
    116.00000000000006,
    anchor="nw",
    text="Invoice\nSettings",
    fill="#FFFFFF",
    font=("Arial Bold", 24 * -1)
)

canvas.create_text(
    747.0,
    185.00000000000006,
    anchor="nw",
    text="Tax",
    fill="#FFFFFF",
    font=("Arial", 14 * -1)
)
#Text end(don't edit)

#Tax rectangle start
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    795.0,
    229.00000000000006,
    image=image_image_1
)
#Tax rectangle end

#%t start
entry_image_22 = PhotoImage(
    file=relative_to_assets("entry_22.png"))
entry_bg_22 = canvas.create_image(
    794.5,
    229.00000000000006,
    image=entry_image_22
)
entry_22 = Entry(
    bd=0,
    bg="#0336FF",
    highlightthickness=0,
    font=("Arial 14"),
    fg='white',
    justify='center'
)
entry_22.insert(0,"%")
entry_22.place(
    x=775.0,
    y=222.0,
    width=39.0,
    height=14.0
)
#%t end

#Text start(don't edit)
canvas.create_text(
    747.0,
    349.00000000000006,
    anchor="nw",
    text="Discount",
    fill="#FFFFFF",
    font=("Arial", 14 * -1)
)
#Text end(don't edit)

#Discount rectangle start
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    795.0,
    393.00000000000006,
    image=image_image_2
)
#Discount rectangle end

#%d start
entry_image_23 = PhotoImage(
    file=relative_to_assets("entry_23.png"))
entry_bg_23 = canvas.create_image(
    794.5,
    393.00000000000006,
    image=entry_image_23
)
entry_23 = Entry(
    bd=0,
    bg="#0336FF",
    highlightthickness=0,
    font=("Arial 14"),
    fg='white',
    justify='center'
)
entry_23.insert(0,"%")
entry_23.place(
    x=775.0,
    y=386.0,
    width=39.0,
    height=14.0
)
#%d end

#Text start(don't edit)
canvas.create_text(
    747.0,
    267.00000000000006,
    anchor="nw",
    text="Your name",
    fill="#FFFFFF",
    font=("Arial", 14 * -1)
)
#Text end(don't edit)

#own company name button start
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=ocm,
    relief="flat"
)
button_3.place(
    x=747.0,
    y=291.00000000000006,
    width=96.0,
    height=40.0
)
#own company name button end

#Text start(don't edit)
canvas.create_text(
    747.0,
    431.00000000000006,
    anchor="nw",
    text="Seller Details",
    fill="#FFFFFF",
    font=("Arial", 14 * -1)
)
#Text end(don't edit)

#click here button start
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=sd,
    relief="flat",
)
button_4.place(
    x=747.0,
    y=455.00000000000006,
    width=96.0,
    height=40.0
)
#click here button end

#Text start(don't edit)
canvas.create_text(
    747.0,
    544.0,
    anchor="nw",
    text="Export",
    fill="#FFFFFF",
    font=("Arial Bold", 24 * -1)
)
#Text end(don't edit)

#save invoice button start
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=get_billing_shipping,
    relief="flat"
)
button_5.place(
    x=747.0,
    y=585.0,
    width=96.0,
    height=40.0
)
#save invoice button end

#print invoice button start
button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=print_seller_details,
    relief="flat"
)
button_6.place(
    x=747.0,
    y=647.0,
    width=96.0,
    height=40.0
)
#print invioce button end

#Settings icon start
image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    829.0,
    43.00000000000006,
    image=image_image_3
)
#Settings icon end

#Lines start
canvas.create_rectangle(
    30.0,
    78.00000000000006,
    724.0,
    80.00000000000006,
    fill="#0336FF",
    outline="")

canvas.create_rectangle(
    724.0,
    78.00000000000006,
    844.0,
    80.00000000000006,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    30.0,
    414.00000000000006,
    694.0,
    416.00000000000006,
    fill="#F0F0F0",
    outline="")

canvas.create_rectangle(
    30.0,
    454.00000000000006,
    694.0,
    456.00000000000006,
    fill="#F0F0F0",
    outline="")

canvas.create_rectangle(
    30.0,
    550.0,
    694.0,
    552.0,
    fill="#F0F0F0",
    outline="")

canvas.create_rectangle(
    383.0,
    655.0,
    694.0,
    657.0,
    fill="#F0F0F0",
    outline="")

canvas.create_rectangle(
    30.0,
    703.0,
    694.0,
    705.0,
    fill="#F0F0F0",
    outline="")
#Lines end

set_amount()
set_item()
window.resizable(False, False)
window.mainloop()