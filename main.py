import wx
import wx.grid
from datetime import date # used to get current date
import calendar # used to get current date


class GridFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        # Create a wxGrid object
        grid = wx.grid.Grid(self, -1)

    def OnSize(self, evt):
        if self.GetAutoLayout():
            self.Layout()
        #github test
        # Then we call CreateGrid to set the dimensions of the grid
        # (10 rows and 7 columns)

        grid.CreateGrid(10, 7)
        my_date = date.today()
        index = my_date.weekday()
        for i in range(0, 7):
            if index == 7:
                index = 0
            grid.SetColLabelValue(i, calendar.day_name[index])
            index = index + 1
        time_label = 9
        for i in range(0, 10):
            grid.SetRowLabelValue(i,(str(time_label)+":00"))
            time_label = time_label + 1
        # We can set the sizes of individual rows and columns
        # in pixels
        grid.SetRowSize(0, 60)
        grid.SetColSize(0, 120)

        # And set grid cell contents as strings
        grid.SetCellValue(0, 0, 'wxGrid is good')
        testString = "Hello" #Read from xml file
        # We can specify that some cells are read.only
        grid.SetCellValue(0, 3, testString)
        grid.SetReadOnly(0, 3)


        # We can specify the some cells will store numeric
        # values rather than strings. Here we set grid column 5
        # to hold floating point values displayed with width of 6
        # and precision of 2
        grid.SetColFormatFloat(5, 6, 2)
        grid.SetCellValue(0, 6, '3.1415')

        self.Show()


if __name__ == '__main__':

    app = wx.App(0)
    frame = GridFrame(None)
    app.MainLoop()
