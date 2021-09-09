# Program to extract number
# of rows using Python
import xlrd
 
# Give the location of the file
loc = open("Book1.xlsx")
 
wb = xlrd.open_workbook(loc)
print(wb)