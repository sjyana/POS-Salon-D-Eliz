#file for the changes in UI when buttons are clicked

import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFrame, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


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
        show_warning_message_box("Invalid input detected")


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

    # Add the panel to the scroll area's layout
    if not ui.scrollAreaWidgetContents.layout():
        scroll_area_layout = QVBoxLayout()
        ui.scrollAreaWidgetContents.setLayout(scroll_area_layout)

    ui.scrollAreaWidgetContents.layout().addWidget(panel)
    initialize_ui(ui)

#message box
def show_warning_message_box(message):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setWindowTitle("Warning")
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.setDefaultButton(QMessageBox.Ok)

    button_ok = msg_box.button(QMessageBox.Ok)
    button_ok.clicked.connect(msg_box.reject)  # Prevent UI exit on 'OK' button click

    msg_box.exec_()

def show_info_message_box(message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Information")
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
        payment = "Cash"
    if x == 2:
        ui.tabs_points.setStyleSheet("border-radius: 15px; background-color: #F0D8DB")
        ui.tabs_cash.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        ui.tabs_wallet.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        payment = "D-Eliz Points"
    if x == 3:
        ui.tabs_wallet.setStyleSheet("border-radius: 15px; background-color: #F0D8DB")
        ui.tabs_points.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        ui.tabs_cash.setStyleSheet("border-radius: 15px; background-color: #ffffff")
        payment = "E-Wallet"

def checkout(ui):
    show_info_message_box("Order saved.")
    initialize_ui
    initialize_scroll_widget(ui)

# Clear existing content in the bills scroll area
def initialize_scroll_widget(ui):
    while ui.scrollAreaWidgetContents.layout().count():
        child = ui.scrollAreaWidgetContents.layout().takeAt(0)
        if child.widget():
            child.widget().deleteLater()

    ui.label_total.setText("0.0")

#admin page navigation
def admin_navigation(ui, x):
    if x == 1:
        ui.admin_stackedWidget.setCurrentWidget(ui.allAccounts_page)
    elif x == 2:
        ui.admin_stackedWidget.setCurrentWidget(ui.allOrders_page)