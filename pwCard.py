from random import randrange
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
   
def plot(col, row, cell):
    fig, ax = plt.subplots(1, figsize=(3.5,3))
    ax.set_axis_off() 
    ax.table(
        cellText = cell,  
        rowLabels = row,  
        colLabels = col, 
        rowColours =["palegreen"] * 9,  
        colColours =["palegreen"] * 9, 
        cellLoc ='center',  
        loc ='upper left') 
    ax.set_title('Password Card', fontweight ="bold") 
    pdf = PdfPages('pwCard.pdf')
    pdf.savefig(fig)
    pdf.close()

def fillCells(tuples):
    col = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZ'] 
    row = []
    for rowNr in range(1, 10):
        row.append(f"  {rowNr}  ")
    cell = []
    for rowNr, colNr in enumerate(range(0,243,27)):
        cell.append([])
        for colIdx in range(0,27,3):
            colIdx += colNr
            cell[rowNr].append(tuples[colIdx:colIdx+3])
    return col, row, cell

def createTuples():
    symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%1234567890'
    tuples = ''
    for _ in range(9*9):
        cellTuple = ''
        for _ in range(3):
            cellTuple += symbols[randrange(0, len(symbols))]
        tuples += cellTuple
    return tuples

tuples = createTuples()
col, row, cell = fillCells(tuples)
plot(col, row, cell)