#file for the backend
import pyodbc
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFrame, QMessageBox, QTreeWidgetItem, QInputDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from datetime import datetime
from market_basket_analysis import run_mba

transactions_array = []
#for UI buttons
def UI_bttns(ui):
    #navigation selection (home, add order, files tab)
        ui.bttn_home.clicked.connect(lambda: navigation(ui, 1))
        ui.bttn_addOrder.clicked.connect(lambda: navigation(ui, 2))
        ui.bttn_files.clicked.connect(lambda: navigation(ui, 3))
        

        #services choices (hair, nail, eyelash, others)
        ui.bttn_hair.clicked.connect(lambda: services_category(ui, 1))
        ui.bttn_nail.clicked.connect(lambda: services_category(ui, 2))
        ui.bttn_eyelash.clicked.connect(lambda: services_category(ui, 3))
        ui.bttn_others.clicked.connect(lambda: services_category(ui, 4))

        #add order buttons
        #hair
        ui.bttn_cut.clicked.connect(lambda: info_check(ui, ui.label_cut.text(), ui.cut_price.toPlainText(), ui.stylist_choice_cut.currentText(), ui.cut_note.toPlainText()))
        ui.bttn_hairRebond.clicked.connect(lambda: info_check(ui, ui.label_hairRebond.text(), ui.hairRebond_price.toPlainText(), ui.stylist_choice_hairRebond.currentText(), ui.hairRebond_note.toPlainText()))
        ui.bttn_hairColor.clicked.connect(lambda: info_check(ui, ui.label_hairColor.text(), ui.hairColor_price.toPlainText(), ui.stylist_choice_hairColor.currentText(), ui.hairColor_note.toPlainText()))
        ui.bttn_highlights.clicked.connect(lambda: info_check(ui, ui.label_highlights.text(), ui.highlights_price.toPlainText(), ui.stylist_choice_highlights.currentText(), ui.highlights_note.toPlainText()))
        
        #nail
        ui.bttn_manicure.clicked.connect(lambda: info_check(ui, ui.label_manicure.text(), ui.manicure_price.toPlainText(), ui.tech_choice_manicure.currentText(), ui.manicure_note.toPlainText()))
        ui.bttn_pedicure.clicked.connect(lambda: info_check(ui, ui.label_pedicure.text(), ui.pedicure_price.toPlainText(), ui.tech_choice_pedicure.currentText(), ui.pedicure_note.toPlainText()))
        ui.bttn_gelPolish.clicked.connect(lambda: info_check(ui, ui.label_gelPolish.text(), ui.gelPolish_price.toPlainText(), ui.tech_choice_gelPolish.currentText(), ui.gelPolish_note.toPlainText()))
        ui.bttn_nailArt.clicked.connect(lambda: info_check(ui, ui.label_nailArt.text(), ui.nailArt_price.toPlainText(), ui.tech_choice_nailArt.currentText(), ui.nailArt_note.toPlainText()))
        ui.bttn_polyGel.clicked.connect(lambda: info_check(ui, ui.label_polyGel.text(), ui.polyGel_price.toPlainText(), ui.tech_choice_polyGel.currentText(), ui.polyGel_note.toPlainText()))
        ui.bttn_softGel.clicked.connect(lambda: info_check(ui, ui.label_softGel.text(), ui.softGel_price.toPlainText(), ui.tech_choice_softGel.currentText(), ui.softGel_note.toPlainText()))
        
        #eyelash
        ui.bttn_classic.clicked.connect(lambda: info_check(ui, ui.label_classic.text(), ui.classic_price.toPlainText(), ui.stylist_choice_classic.currentText(), ui.classic_note.toPlainText()))
        ui.bttn_hybrid.clicked.connect(lambda: info_check(ui, ui.label_hybrid.text(), ui.hybrid_price.toPlainText(), ui.stylist_choice_hybrid.currentText(), ui.hybrid_note.toPlainText()))
        ui.bttn_volume.clicked.connect(lambda: info_check(ui, ui.label_volume.text(), ui.volume_price.toPlainText(), ui.stylist_choice_volume.currentText(), ui.volume_note.toPlainText()))
        ui.bttn_mega.clicked.connect(lambda: info_check(ui, ui.label_mega.text(), ui.mega_price.toPlainText(), ui.stylist_choice_mega.currentText(), ui.mega_note.toPlainText()))

        #others
        ui.bttn_footSpa.clicked.connect(lambda: info_check(ui, ui.label_footSpa.text(), ui.footSpa_price.toPlainText(), ui.stylist_choice_footSpa.currentText(), ui.footSpa_note.toPlainText()))
        ui.bttn_hmu.clicked.connect(lambda: info_check(ui, ui.label_hmu.text(), ui.hmu_price.toPlainText(), ui.stylist_choice_hmu.currentText(), ui.hmu_note.toPlainText()))
        ui.bttn_eyebrow.clicked.connect(lambda: info_check(ui, ui.label_eyebrow.text(), ui.eyebrow_price.toPlainText(), ui.stylist_choice_eyebrow.currentText(), ui.eyebrow_note.toPlainText()))

        #payment method
        ui.bttn_cash.clicked.connect(lambda: payment_method(ui, 1))
        ui.bttn_points.clicked.connect(lambda: payment_method(ui, 2))
        ui.bttn_wallet.clicked.connect(lambda: payment_method(ui, 3))

        ui.bttn_reset.clicked.connect(lambda: initialize_scroll_widget(ui))
        ui.bttn_checkout.clicked.connect(lambda: checkout(ui))

        #admin page
        ui.bttn_accNext.clicked.connect(lambda: admin_navigation(ui,1))
        ui.bttn_orderNext.clicked.connect(lambda: admin_navigation(ui,2))
        ui.bttn_deleteOrder.clicked.connect(lambda: handle_deleteOrder(ui))
        ui.bttn_deleteAcc.clicked.connect(lambda: handle_deleteAcc(ui))
        ui.bttn_addAcc.clicked.connect(lambda: addAccDB(ui))
        ui.bttn_editAcc.clicked.connect(lambda: editAccDB(ui))
        ui.bttn_addBalance.clicked.connect(lambda: addBalance(ui))
        ui.bttn_generateMBA.clicked.connect(lambda: run_mba())

# Initialize text fields
def initialize_ui(ui):
    ui.cut_price.setPlainText("100")
    ui.cut_note.setPlainText("")

    ui.hairRebond_price.setPlainText("")
    ui.hairRebond_note.setPlainText("")

    ui.hairColor_price.setPlainText("")
    ui.hairColor_note.setPlainText("")

    ui.highlights_price.setPlainText("")
    ui.highlights_note.setPlainText("")

    ui.manicure_price.setPlainText("100")
    ui.manicure_note.setPlainText("")

    ui.pedicure_price.setPlainText("100")
    ui.pedicure_note.setPlainText("")

    ui.gelPolish_price.setPlainText("")
    ui.gelPolish_note.setPlainText("")

    ui.nailArt_price.setPlainText("")
    ui.nailArt_note.setPlainText("")

    ui.polyGel_price.setPlainText("")
    ui.polyGel_note.setPlainText("")

    ui.softGel_price.setPlainText("")
    ui.softGel_note.setPlainText("")

    ui.classic_price.setPlainText("399")
    ui.classic_note.setPlainText("")

    ui.hybrid_price.setPlainText("499")
    ui.hybrid_note.setPlainText("")

    ui.volume_price.setPlainText("699")
    ui.volume_note.setPlainText("")

    ui.mega_price.setPlainText("799")
    ui.mega_note.setPlainText("")

    ui.footSpa_price.setPlainText("350")
    ui.footSpa_note.setPlainText("")

    ui.hmu_price.setPlainText("1000")
    ui.hmu_note.setPlainText("")

    ui.eyebrow_price.setPlainText("1000")
    ui.eyebrow_note.setPlainText("")

    # Initialize combo boxes
    ui.stylist_choice_cut.setCurrentIndex(-1)
    ui.stylist_choice_hairRebond.setCurrentIndex(-1)
    ui.stylist_choice_hairColor.setCurrentIndex(-1)
    ui.stylist_choice_highlights.setCurrentIndex(-1)
    
    ui.tech_choice_manicure.setCurrentIndex(-1)
    ui.tech_choice_pedicure.setCurrentIndex(-1)
    ui.tech_choice_gelPolish.setCurrentIndex(-1)
    ui.tech_choice_nailArt.setCurrentIndex(-1)
    ui.tech_choice_polyGel.setCurrentIndex(-1)
    ui.tech_choice_softGel.setCurrentIndex(-1)
    
    ui.stylist_choice_classic.setCurrentIndex(-1)
    ui.stylist_choice_hybrid.setCurrentIndex(-1)
    ui.stylist_choice_volume.setCurrentIndex(-1)
    ui.stylist_choice_mega.setCurrentIndex(-1)
    
    ui.stylist_choice_footSpa.setCurrentIndex(-1)
    ui.stylist_choice_hmu.setCurrentIndex(-1)
    ui.stylist_choice_eyebrow.setCurrentIndex(-1)

    #initialize mop buttons
    ui.tabs_cash.setStyleSheet("border-radius: 15px; background-color: #ffffff")
    ui.tabs_points.setStyleSheet("border-radius: 15px; background-color: #ffffff")
    ui.tabs_wallet.setStyleSheet("border-radius: 15px; background-color: #ffffff")
    

#navigation (home, add order, admin tab)
def navigation(ui, x):
    if x == 1:
        ui.menu_stackedWidget.setCurrentWidget(ui.home_page)
        ui.tabs_home.setStyleSheet("background-color: rgb(188,54,79); border-radius: 15px")
        ui.label_home.setStyleSheet("color: rgba(254,250,249,255)")
        ui.label_addOrder.setStyleSheet("color: rgb(188,54,79)")
        ui.tabs_addOrder.setStyleSheet("border-radius: 15px")
        ui.label_files.setStyleSheet("color: rgb(188,54,79)")
        ui.tabs_files.setStyleSheet("border-radius: 15px")
    elif x == 2:
        ui.menu_stackedWidget.setCurrentWidget(ui.addorder_page)
        ui.tabs_addOrder.setStyleSheet("background-color: rgb(188,54,79); border-radius: 15px")
        ui.label_addOrder.setStyleSheet("color: rgba(254,250,249,255)")
        ui.label_home.setStyleSheet("color: rgb(188,54,79)")
        ui.tabs_home.setStyleSheet("border-radius: 15px")
        ui.label_files.setStyleSheet("color: rgb(188,54,79)")
        ui.tabs_files.setStyleSheet("border-radius: 15px")
    elif x == 3:
        ui.menu_stackedWidget.setCurrentWidget(ui.admin_page)
        ui.tabs_files.setStyleSheet("background-color: rgb(188,54,79); border-radius: 15px")
        ui.label_files.setStyleSheet("color: rgba(254,250,249,255)")
        ui.label_home.setStyleSheet("color: rgb(188,54,79)")
        ui.tabs_home.setStyleSheet("border-radius: 15px")
        ui.label_addOrder.setStyleSheet("color: rgb(188,54,79)")
        ui.tabs_addOrder.setStyleSheet("border-radius: 15px")
        
        populate_order_list(ui)
        populate_accounts_list(ui)
        initialize_tableText(ui)
        ui.searchOrder.textChanged.connect(lambda: perform_searchOrder(ui))
        ui.searchAccount.textChanged.connect(lambda: perform_searchAcc(ui))

#services choices (hair, nail, eyelash, others)
def services_category(ui, x):
    if x == 1:
        ui.services_stackedWidget.setCurrentWidget(ui.hair_page)
        ui.tabs_hair.setStyleSheet("border-radius: 15px; border: 1.5px solid rgb(188,54,79); background-color: #fff5f6")
        ui.tabs_nailcare.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        ui.tabs_eyelash.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        ui.tabs_others.setStyleSheet("border-radius: 15px; background-color: #ffffff")
    if x == 2:
        ui.services_stackedWidget.setCurrentWidget(ui.nail_page)
        ui.tabs_nailcare.setStyleSheet("border-radius: 15px; border: 1.5px solid rgb(188,54,79); background-color: #fff5f6")
        ui.tabs_hair.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        ui.tabs_eyelash.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        ui.tabs_others.setStyleSheet("border-radius: 15px; background-color: #ffffff")
    if x == 3:
        ui.services_stackedWidget.setCurrentWidget(ui.eyelash_page)
        ui.tabs_eyelash.setStyleSheet("border-radius: 15px; border: 1.5px solid rgb(188,54,79); background-color: #fff5f6")
        ui.tabs_nailcare.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        ui.tabs_hair.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        ui.tabs_others.setStyleSheet("border-radius: 15px; background-color: #ffffff")
    if x == 4:
        ui.services_stackedWidget.setCurrentWidget(ui.others_page)
        ui.tabs_others.setStyleSheet("border-radius: 15px; border: 1.5px solid rgb(188,54,79); background-color: #fff5f6")
        ui.tabs_nailcare.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        ui.tabs_eyelash.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        ui.tabs_hair.setStyleSheet("border-radius: 15px; background-color: #ffffff")

def info_check(ui, product, price, stylist, note):
    if price.isdigit() and price != "" and stylist != "":
        create_panel(ui, product, price, stylist, note)
        subTotal = float(price)
        compute_total(ui, subTotal)

    else:
        show_warning_message_box("Invalid input detected", "Error")

# Create a new panel for Bills tabs
def create_panel(ui, product, price, stylist, note):
    panel = QFrame()
    panel.setFrameStyle(QFrame.Box | QFrame.Raised)
    panel.setStyleSheet("border-radius: 15px; border: 1.5px solid rgb(188,54,79);")
    panel.setFixedSize(380, 120)  # Set the fixed size of the panel

    panel_layout = QVBoxLayout()

    # Add components to the panel
    font = QFont()
    font.setFamily("Classy Vogue")
    font.setPointSize(11)
    
    font.setBold(True)
    label_product = QLabel(product)
    label_product.setFont(font)
    label_product.setStyleSheet("border: 0px;")
    label_product.setAlignment(Qt.AlignCenter)
    panel_layout.addWidget(label_product)

    font.setBold(False)
    stylist_label = QLabel("Stylist: " + stylist)
    stylist_label.setFont(font)
    stylist_label.setStyleSheet("border: 0px;")
    stylist_label.setAlignment(Qt.AlignLeft)
    panel_layout.addWidget(stylist_label)

    note_label = QLabel("Note: " + note)
    note_label.setFont(font)
    note_label.setStyleSheet("border: 0px;")
    note_label.setAlignment(Qt.AlignLeft)
    panel_layout.addWidget(note_label)

    price_label = QLabel("₱ " + price)
    price_label.setFont(font)
    price_label.setStyleSheet("border: 0px;")
    price_label.setAlignment(Qt.AlignRight)
    panel_layout.addWidget(price_label)

    panel.setLayout(panel_layout)

    orders= [product, stylist, note, price]
    transactions_array.append(orders)

    # Add the panel to the scroll area's layout
    if not ui.scrollAreaWidgetContents.layout():
        scroll_area_layout = QVBoxLayout()
        ui.scrollAreaWidgetContents.setLayout(scroll_area_layout)

    ui.scrollAreaWidgetContents.layout().addWidget(panel)
    initialize_ui(ui)

#message box
def show_warning_message_box(message, title):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.setDefaultButton(QMessageBox.Ok)

    button_ok = msg_box.button(QMessageBox.Ok)
    button_ok.clicked.connect(msg_box.reject)  # Prevent UI exit on 'OK' button click

    msg_box.exec_()

def show_info_message_box(message, title):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)

        button_ok = msg_box.button(QMessageBox.Ok)
        button_ok.clicked.connect(msg_box.reject) 

        msg_box.exec_()
    

#function that computes Total
def compute_total(ui, subtotal):
    total_amt = float(ui.label_total.text().replace("₱ ", "")) 
    total_amt += subtotal
    ui.label_total.setText("₱ " + str(total_amt))


#function for payment method
def payment_method(ui, x):
    if x == 1:
        ui.tabs_cash.setStyleSheet("border-radius: 15px; background-color: #F0D8DB")
        ui.tabs_points.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        ui.tabs_wallet.setStyleSheet("border-radius: 15px; background-color: #ffffff")
    if x == 2:
        ui.tabs_points.setStyleSheet("border-radius: 15px; background-color: #F0D8DB")
        ui.tabs_cash.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        ui.tabs_wallet.setStyleSheet("border-radius: 15px; background-color: #ffffff")
    if x == 3:
        ui.tabs_wallet.setStyleSheet("border-radius: 15px; background-color: #F0D8DB")
        ui.tabs_points.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        ui.tabs_cash.setStyleSheet("border-radius: 15px; background-color: #ffffff")


# Clear existing content in the bills scroll area
def initialize_scroll_widget(ui):
    if ui.scrollAreaWidgetContents.layout():  # Check if layout exists
        while ui.scrollAreaWidgetContents.layout().count():
            child = ui.scrollAreaWidgetContents.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    else:
        scroll_area_layout = QVBoxLayout()  # Create a new layout if it doesn't exist
        ui.scrollAreaWidgetContents.setLayout(scroll_area_layout)

    ui.label_total.setText("0.0")
    ui.text_name.setText("")
    global transactions_array  # Declare transactions_array as global
    transactions_array = []  # Initialize transactions_array as an empty list


#admin page navigation
def admin_navigation(ui, x):
    if x == 1:
        ui.admin_stackedWidget.setCurrentWidget(ui.allAccounts_page)
    elif x == 2:
        ui.admin_stackedWidget.setCurrentWidget(ui.allOrders_page)

#database handling
def create_connection():
    conn = None
    try:
        # Replace 'path/to/your/database.accdb' with the actual path to your Access database file
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\julia\Documents\Soft. Eng (POS)\salondb.accdb')
    except pyodbc.Error as e:
        print(f"Error creating database connection: {e}")

    return conn

#market basket database
def insert_mba(conn, orders_array):
    try:
        cur = conn.cursor()
        
        # Prepare the data for MBA table
        items = [''] * 15  # Initialize a list with 15 empty strings
        for i in range(len(orders_array)):
            if i < 15:
                items[i] = orders_array[i][0]  # Assuming transactions_array[i][0] is the product
        
        # Construct the SQL insert statement
        sql = """
        INSERT INTO MBA (
            [Service 1], [Service 2], [Service 3], [Service 4], [Service 5], [Service 6], [Service 7], [Service 8], [Service 9], 
            [Service 10], [Service 11], [Service 12], [Service 13], [Service 14], [Service 15]
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        cur.execute(sql, (*items,))
        conn.commit()
    except pyodbc.Error as e:
        print(f"Error inserting into MBA: {e}")


def fetch_latest_order_num(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT MAX(OrderNum) FROM OrderList")
        max_order_num = cur.fetchone()[0]
        return max_order_num if max_order_num is not None else 0
    except pyodbc.Error as e:
        print(f"Error fetching latest order number: {e}")
        return 0
    
def insert_order(conn, ui, date, time, name, pay_method):
    try:
        cur = conn.cursor()

        # Insert each transaction into OrderList with the new OrderNum
        for order in transactions_array:
            latest_order_num = fetch_latest_order_num(conn)
            new_order_num = latest_order_num + 1
            cur.execute("INSERT INTO OrderList ([OrderNum], [CusName], [OrderDate], [OrderTime], [Product], [Stylist], [Note], [Price], [Mode of Payment]) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                        (new_order_num, name, date, time, order[0], order[1], order[2], order[3], pay_method))
            
        # If the length of transactions_array is more than one, insert into MBA
        if len(transactions_array) > 1:
            insert_mba(conn, transactions_array)
        
        show_info_message_box("Order saved.", "Success")
        initialize_ui(ui)
        initialize_scroll_widget(ui)
            
    except pyodbc.Error as e:
        print(f"Error inserting order: {e}")


def checkout(ui):
    if ui.tabs_cash.styleSheet().startswith("border-radius: 15px; background-color: #ffffff") and ui.tabs_points.styleSheet().startswith("border-radius: 15px; background-color: #ffffff") and ui.tabs_wallet.styleSheet().startswith("border-radius: 15px; background-color: #ffffff"):
        show_warning_message_box("Please enter mode of payment", "Error")
    else:
        if ui.text_name.text() == "":
            show_warning_message_box("Please enter customer's name", "Error")
        else:
            conn = create_connection()
            if conn:
                now = datetime.now()
                current_date = now.strftime("%m-%d-%Y")  # Change the date format to mm-dd-yyyy
                current_time = ui.lblTime.text()
                cusName = ui.text_name.text()

                if ui.tabs_cash.styleSheet().startswith("border-radius: 15px; background-color: #F0D8DB"):
                    pay_method = "Cash"
                    insert_order(conn, ui, current_date, current_time, cusName, pay_method)
                elif ui.tabs_points.styleSheet().startswith("border-radius: 15px; background-color: #F0D8DB"):
                    pay_method = "D-Eliz Points"
                    useBalance(ui, current_date, current_time, cusName, pay_method)
                elif ui.tabs_wallet.styleSheet().startswith("border-radius: 15px; background-color: #F0D8DB"):
                    pay_method = "E-Wallet"
                    insert_order(conn, ui, current_date, current_time, cusName, pay_method)

                conn.commit()
                conn.close()

#salon d-eliz points mop
def useBalance(ui, current_date, current_time, cusName, pay_method):
    conn = create_connection()
    if conn:
        try:
            acc_key, ok = QInputDialog.getInt(None, "Account Key", "Enter Account Key:")
            if ok:
                if acc_key_exists(conn, acc_key):
                    current_balance = fetch_balance_points(conn, acc_key)
                    if current_balance is not None:
                        current_balance = float(current_balance) 
                        total_amt = float(ui.label_total.text().replace("₱ ", "")) 
                        if current_balance >= total_amt:
                            new_balance = current_balance - total_amt
                            # Update the balance points of the existing account
                            cur = conn.cursor()
                            cur.execute("""
                                UPDATE AccountsList 
                                SET Balance = ?
                                WHERE AccKey = ?
                            """, (new_balance, acc_key))
                            conn.commit()
                            show_info_message_box(f"New balance: {new_balance}", "Transaction Successful")
                            insert_order(conn, ui, current_date, current_time, cusName, pay_method)
                        else:
                            show_warning_message_box("Insufficient balance.", "Transaction Error")
                    else:
                        show_warning_message_box("Current balance is None.", "Transaction Error")
                else:
                    show_warning_message_box("Account key not found.", "Transaction Error")
        except pyodbc.Error as e:
            show_warning_message_box(f"Transaction Error: {e}", "Error")

#displaying orders in UI table
def fetch_orders(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT [OrderNum], [CusName], [OrderDate], [OrderTime], [Product], [Stylist], [Note], [Price], [Mode of Payment] FROM OrderList")
        rows = cur.fetchall()
        return rows
    except pyodbc.Error as e:
        print(f"Error fetching orders: {e}")
        return []

def populate_order_list(ui):
    conn = create_connection()
    if conn:
        orders = fetch_orders(conn)
        conn.close()
        
        ui.orderList.clear()  # Clear any existing items
        
        for order in orders:
            # Convert each row to a QTreeWidgetItem
            item = QTreeWidgetItem([str(field) for field in order])
            ui.orderList.addTopLevelItem(item)

    ui.orderList.itemClicked.connect(lambda item, column: order_item_clicked(ui, item))

def order_item_clicked(ui, item):
    # Update labels with the item data from the clicked row
    ui.lblOrder.setText(f'{item.text(0)}')
    ui.lblName.setText(f'{item.text(1)}')
    ui.lblOrderDate.setText(f'{item.text(2)}')
    ui.lblOrderTime.setText(f'{item.text(3)}')
    ui.lblService.setText(f'{item.text(4)}')
    ui.lblStylist.setText(f'{item.text(5)}')
    ui.lblNote.setText(f'{item.text(6)}')
    ui.lblTotal.setText(f'{item.text(7)}')

def initialize_tableText(ui):
    ui.lblOrder.setText("")
    ui.lblName.setText("")
    ui.lblOrderDate.setText("")
    ui.lblOrderTime.setText("")
    ui.lblService.setText("")
    ui.lblStylist.setText("")
    ui.lblNote.setText("")
    ui.lblTotal.setText("")
    ui.text_accKey.setText("")
    ui.text_dateReg.setText("")
    ui.text_fname.setText("")
    ui.text_lname.setText("")
    ui.text_contact.setText("")
    ui.text_email.setText("")
    ui.lblBalance.setText("0")

def perform_searchOrder(ui):
        initialize_tableText(ui)
        text = ui.searchOrder.text().lower().strip()

        if not text:
            ui.orderList.clear()
            populate_order_list(ui)
            return
        
        for i in range(ui.orderList.topLevelItemCount()):
            item = ui.orderList.topLevelItem(i)
            item.setHidden(True)

            for column in range(item.columnCount()):
                if text in item.text(column).lower():
                    item.setHidden(False)
                    break

#delete order function
def delete_order(conn, order_num):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM OrderList WHERE OrderNum = ?", (order_num,))
        conn.commit()
        print(f"Order {order_num} deleted successfully.")
    except pyodbc.Error as e:
        show_warning_message_box("Error deleting order", "Error")

def update_order_numbers(conn, deleted_order_num):
    try:
        cur = conn.cursor()
        cur.execute("UPDATE OrderList SET OrderNum = OrderNum - 1 WHERE OrderNum > ?", (deleted_order_num,))
        conn.commit()
    except pyodbc.Error as e:
        print(f"Error updating order numbers: {e}")

def handle_deleteOrder(ui):
    selected_items = ui.orderList.selectedItems()
    if not selected_items:
        QMessageBox.warning(ui, "Delete Order", "Please select an order to delete.")
        return
    
    selected_item = selected_items[0]
    order_num = int(selected_item.text(0))  # Convert to integer to maintain consistency
    
    reply = QMessageBox.question(ui, "Delete Order", "Are you sure you want to delete the selected order?", 
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    
    if reply == QMessageBox.Yes:
        conn = create_connection()
        if conn:
            delete_order(conn, order_num)
            update_order_numbers(conn, order_num)
            conn.close()
            
            populate_order_list(ui)
            QMessageBox.information(ui, "Delete Order", "Order deleted successfully.")
    else:
        QMessageBox.information(ui, "Delete Order", "Order deletion canceled.")
        populate_order_list(ui)
        initialize_tableText(ui)

#displaying accounts in UI table
def fetch_accounts(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT [AccKey], [DateReg], [FName], [LName], [ContactNum], [Email], [Balance] FROM AccountsList")
        rows = cur.fetchall()
        return rows
    except pyodbc.Error as e:
        print(f"Error fetching accounts: {e}")
        return []

def populate_accounts_list(ui):
    conn = create_connection()
    if conn:
        orders = fetch_accounts(conn)
        conn.close()
        
        ui.accountsList.clear()
        
        for order in orders:
            item = QTreeWidgetItem([str(field) for field in order])
            ui.accountsList.addTopLevelItem(item)

    ui.accountsList.itemClicked.connect(lambda item, column: accounts_item_clicked(ui, item))

def accounts_item_clicked(ui, item):
    ui.text_accKey.setText(f'{item.text(0)}')
    ui.text_dateReg.setText(f'{item.text(1)}')
    ui.text_fname.setText(f'{item.text(2)}')
    ui.text_lname.setText(f'{item.text(3)}')
    ui.text_contact.setText(f'{item.text(4)}')
    ui.text_email.setText(f'{item.text(5)}')
    ui.lblBalance.setText(f'{item.text(6)}')

def perform_searchAcc(ui):
        initialize_tableText(ui)
        text = ui.searchAccount.text().lower().strip()

        if not text:
            ui.accountsList.clear()
            populate_order_list(ui)
            return
        
        for i in range(ui.accountsList.topLevelItemCount()):
            item = ui.accountsList.topLevelItem(i)
            item.setHidden(True)

            for column in range(item.columnCount()):
                if text in item.text(column).lower():
                    item.setHidden(False)
                    break

#delete account function
def delete_account(conn, acc_key):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM AccountsList WHERE AccKey = ?", (acc_key,))
        conn.commit()
    except pyodbc.Error as e:
        print(f"Error deleting account: {e}")

def handle_deleteAcc(ui):
    selected_items = ui.accountsList.selectedItems()
    if not selected_items:
        QMessageBox.warning(ui, "Delete Account", "Please select an account to delete.")
        return
    
    selected_item = selected_items[0]
    acc_key = selected_item.text(0)
    
    reply = QMessageBox.question(ui, "Delete Account", "Are you sure you want to delete the selected account?", 
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    
    if reply == QMessageBox.Yes:
        conn = create_connection()
        if conn:
            delete_account(conn, acc_key)
            conn.close()
            
            populate_accounts_list(ui)
            initialize_tableText(ui)
            QMessageBox.information(ui, "Delete Account", "Account deleted successfully.")
    else:
        QMessageBox.information(ui, "Delete Account", "Account deletion canceled.")
        populate_accounts_list(ui)
        initialize_tableText(ui)

#add and update account
def acc_key_exists(conn, acc_key):
    try:
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM AccountsList WHERE AccKey = ?", (acc_key,))
        row = cur.fetchone()
        return row is not None
    except pyodbc.Error as e:
        print(f"Error checking AccKey: {e}")
        return False

def editAccDB(ui):
    conn = create_connection()
    if conn:
        try:
            acc_key = ui.text_accKey.text()
            date_reg = ui.text_dateReg.text()
            f_name = ui.text_fname.text()
            l_name = ui.text_lname.text()
            contact_num = ui.text_contact.text()
            email = ui.text_email.text()
            balance = ui.lblBalance.text()

            if acc_key_exists(conn, acc_key):
                # Update the existing account
                cur = conn.cursor()
                cur.execute("""
                    UPDATE AccountsList 
                    SET DateReg = ?, FName = ?, LName = ?, ContactNum = ?, Email = ?, Balance = ? 
                    WHERE AccKey = ?
                """, (date_reg, f_name, l_name, contact_num, email, balance, acc_key))
                conn.commit()
                show_info_message_box(f"Account with AccKey {acc_key} updated successfully.", "Update Account")
                populate_accounts_list(ui)
                initialize_tableText(ui)
            else:
                show_warning_message_box("Account key not found.", "Update Account Error")
        except pyodbc.Error as e:
            show_warning_message_box(f"Error updating account: {e}", "Error")
        finally:
            conn.close()

def addAccDB(ui):
    conn = create_connection()
    if conn:
        try:
            acc_key = ui.text_accKey.text()
            date_reg = ui.text_dateReg.text()
            f_name = ui.text_fname.text()
            l_name = ui.text_lname.text()
            contact_num = ui.text_contact.text()
            email = ui.text_email.text()
            balance = ui.lblBalance.text()

            if acc_key_exists(conn, acc_key):
                show_warning_message_box("Account key not available.", "Add Account Error")
            else:
                # Insert a new account
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO AccountsList (AccKey, DateReg, FName, LName, ContactNum, Email, Balance) 
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (acc_key, date_reg, f_name, l_name, contact_num, email, balance))
                conn.commit()
                show_info_message_box(f"New account with AccKey {acc_key} inserted successfully.", "Add Account")
                populate_accounts_list(ui)
                initialize_tableText(ui)
        except pyodbc.Error as e:
            show_warning_message_box(f"Error saving new account: {e}", "Error")
        finally:
            conn.close()


def fetch_balance_points(conn, acc_key):
    try:
        cur = conn.cursor()
        cur.execute("SELECT Balance FROM AccountsList WHERE AccKey = ?", (acc_key,))
        row = cur.fetchone()
        if row:
            return row[0]  # Return the balance points if the account is found
        else:
            return None  # Return None if the account is not found
    except pyodbc.Error as e:
        print(f"Error fetching balance points: {e}")
        return None

def addBalance(ui):
    conn = create_connection()
    if conn:
        try:
            acc_key = ui.text_accKey.text()
            current_balance = fetch_balance_points(conn, acc_key)
            points, ok = QInputDialog.getInt(None, "Add Points", "Enter the amount of points to add:")
            if ok:
                if current_balance is not None:
                    current_balance = float(current_balance) 
                    new_balance = current_balance + points
                    # Update the balance points of the existing account
                    cur = conn.cursor()
                    cur.execute("""
                        UPDATE AccountsList 
                        SET Balance = ?
                        WHERE AccKey = ?
                    """, (new_balance, acc_key))
                    conn.commit()
                    show_info_message_box(f"Added {points} points to the account with AccKey {acc_key}. New balance: {new_balance}", "Balance Added Successfully")
                    populate_accounts_list(ui)
                    initialize_tableText(ui)
            else:
                show_warning_message_box("Account key not found.", "Add Balance Points Error")
        except pyodbc.Error as e:
            show_warning_message_box(f"Error updating balance points: {e}", "Error")
