import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import pyodbc
from PyQt5.QtWidgets import QMessageBox

def convert_accdb_to_csv():
    # Establish connection to the Access database
    conn_str = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\julia\Documents\Soft. Eng (POS)\salondb.accdb'
    conn = pyodbc.connect(conn_str)

    # Fetch data from the specified table
    query = f"SELECT * FROM MBA"
    data = pd.read_sql(query, conn)

    # Close the database connection
    conn.close()

    output_csv = r'C:\Users\julia\Documents\Soft. Eng (POS)\MBA.csv'
    # Write the data to a CSV file
    csv_file = data.to_csv(output_csv, index=False)

# Function to load the file and perform MBA
def run_mba():
    convert_accdb_to_csv()
    file_path = r'C:\Users\julia\Documents\Soft. Eng (POS)\MBA.csv'
    if not file_path:
        show_warning_message_box("File error", "Error")
        return

    try:
        # Load the dataset
        df = pd.read_csv(file_path)

        # Data preprocessing
        df1 = pd.get_dummies(df)
        df2 = df1.iloc[:, 1:]
        
        # Fill NaN values with 0
        df2 = df2.fillna(0)
        
        # Apply Apriori algorithm
        frequent_items = apriori(df2, min_support=0.01, use_colnames=True)
        
        # Generate association rules
        rules = association_rules(frequent_items, metric="lift", min_threshold=1)
        
        # Post-process the rules to remove prefix from items
        for i in range(1, 7):
            prefix = f'item {i}_'
            rules['antecedents'] = rules['antecedents'].apply(lambda x: frozenset([item.replace(prefix, '') for item in x]))
            rules['consequents'] = rules['consequents'].apply(lambda x: frozenset([item.replace(prefix, '') for item in x]))
        
        # Filtered rules based on given criteria
        filtered_rules = rules[(rules['lift'] >= 2) &
                               (rules['confidence'] >= 0.5) &
                               (rules['support'] >= 0.02)]
        
        # Save filtered results to the database
        store_association_rules_to_database(filtered_rules)

    except Exception as e:
        show_warning_message_box(str(e), "Error")


def store_association_rules_to_database(rules):
    import re
    
    # Establish connection to the Access database
    conn_str = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\julia\Documents\Soft. Eng (POS)\salondb.accdb'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    try:
        # Clear existing data from the MarketBasketResults table
        cursor.execute("DELETE FROM MarketBasketResults")
        conn.commit()

        # Define a function to remove the "Service X_" prefix from items
        def remove_prefix(items):
            return frozenset([re.sub(r'Service \d+_', '', item) for item in items])

        # Apply the prefix removal function to antecedents and consequents using .loc
        rules.loc[:, 'antecedents'] = rules['antecedents'].apply(remove_prefix)
        rules.loc[:, 'consequents'] = rules['consequents'].apply(remove_prefix)

        # Insert association rules into the MarketBasketResults table
        for index, row in rules.iterrows():
            antecedents = ', '.join(row['antecedents'])
            consequents = ', '.join(row['consequents'])
            support = row['support']
            confidence = row['confidence']
            lift = row['lift']
            cursor.execute("INSERT INTO MarketBasketResults (Antecedent, Consequent, Support, Confidence, Lift) VALUES (?, ?, ?, ?, ?)",
                           (antecedents, consequents, support, confidence, lift))
        
        # Commit the transaction
        conn.commit()
        show_info_message_box("Market Basket Analysis completed and results saved to MarketBasketResults table", "Information")

    except Exception as e:
        show_warning_message_box(str(e), "Error")
        conn.rollback()

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

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