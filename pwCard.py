from random import randrange
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
   
def plot(allTuples):
    val1 = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZ'] 
    val2 = ["  {:X}  ".format(i) for i in range(1, 10)] 
    val3 = [[],[],[],[],[],[],[],[],[]]
    i, j = 0, 3
    for c in range(9):
        for r in range(9):
            val3[c].append(allTuples[i:j])
            i += 3
            j += 3

    fig, ax = plt.subplots() 
    ax.set_axis_off() 
    table = ax.table( 
        cellText = val3,  
        rowLabels = val2,  
        colLabels = val1, 
        rowColours =["palegreen"] * 9,  
        colColours =["palegreen"] * 9, 
        cellLoc ='center',  
        loc ='upper left') 
    
    ax.set_title('Password Card', fontweight ="bold") 
    pdf = PdfPages('pwCard.pdf')
    pdf.savefig(fig)
    pdf.close()
    plt.show() 

def main():
    symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%1234567890'
    allTuples = ''
    for tuples in range(9*9):
        rdmTuple = ''
        for tuple in range(3):
            rdmInt = randrange(0, len(symbols))
            rdmSymb = symbols[rdmInt]
            rdmTuple += rdmSymb
        allTuples += rdmTuple
    plot(allTuples)
        
main()