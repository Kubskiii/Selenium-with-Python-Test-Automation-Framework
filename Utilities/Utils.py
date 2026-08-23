import inspect
import logging
import softest
from openpyxl import load_workbook
import csv

class Utils(softest.TestCase):

    def AssertListItems(self,list,value):

        for stop in list:
            print("The Text is: " + stop.text)
            # assert value in stop.text
            self.soft_assert(self.assertIn,value,stop.text)
            if value in stop.text:
                print("Assert Pass")
            else:
                print("Assert Fail")
        self.assert_all()

    def CustomLogger(logLevel=logging.DEBUG):
        # Set class/method name from where it is called
        loggerName = inspect.stack()[1][3]
        # Create Logger
        logger = logging.getLogger(loggerName)
        logger.setLevel(logLevel)
        # Create Console handler or file handler and set the log level
        fileHandler = logging.FileHandler("automation.log", mode='a')
        # create formatter - how you want logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%d/%b/%y %H:%M:%S %p')
        # add formatter to console or file handler
        fileHandler.setFormatter(formatter)
        # add console handler to loger
        logger.addHandler(fileHandler)
        return logger

    def ReadDataFromExcel(fileName,sheetName):

        dataList = []
        workbook = load_workbook(filename=fileName)
        sheet = workbook[sheetName]
        rowCount = sheet.max_row
        columnCount = sheet.max_column

        for i in range(2, rowCount + 1):
            row = []
            for j in range(1, columnCount + 1):
                row.append(sheet.cell(row=i, column=j).value)
            dataList.append(row)

        return dataList

    def ReadDataFromCSV(fileName):
        #create list
        dataList = []
        #Open File
        csvData = open(fileName,"r")
        #Create CSV Reader
        reader = csv.reader(csvData)
        #skip header
        next(reader)
        # Add CSV rows to list
        for row in reader:
            dataList.append(row)

        return dataList



