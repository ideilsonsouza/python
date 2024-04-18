from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

def set_data_table(data, table_widget):
    
    if not isinstance(table_widget, QTableWidget):
        raise ValueError("O argumento 'table_widget' deve ser uma instância de QTableWidget.")
    
    if not data:
        table_widget.setRowCount(1)
        table_widget.setColumnCount(1)
        table_widget.setItem(0, 0, QTableWidgetItem("Sem dados para exibir"))
        
    else:
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(len(data[0]))
        
        for row, item in enumerate(data):
            for col, value in enumerate(item.values()):
                table_widget.setItem(row, col, QTableWidgetItem(str(value)))
        
        table_widget.setHorizontalHeaderLabels(data[0].key())