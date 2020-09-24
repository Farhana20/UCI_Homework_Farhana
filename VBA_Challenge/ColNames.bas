Attribute VB_Name = "Module1"
'Declaring a variable
Sub ColumnNames():

Dim h As Integer
Dim ws_num As Integer
Dim ws As Worksheet

ws_num = ThisWorkbook.Worksheets.count


For h = 1 To ws_num
     ThisWorkbook.Worksheets(h).Activate

     Worksheets(h).Activate
     ActiveSheet.Cells(1, 9).Value = "Ticker"
     ActiveSheet.Cells(1, 10).Value = "Yearly Change"
     ActiveSheet.Cells(1, 11).Value = "Percent Change"
     ActiveSheet.Cells(1, 12).Value = "Total Stock Volume"
     ActiveSheet.Cells(1, 15).Value = "Ticker"
     ActiveSheet.Cells(1, 16).Value = "Value"
     ActiveSheet.Cells(2, 14).Value = "Greatest % Increase"
     ActiveSheet.Cells(3, 14).Value = "Greatest % Decrease"
     ActiveSheet.Cells(4, 14).Value = "Greatest Total Value"





Next

     Worksheets("2016").Activate
     Worksheets("2016").Cells(1, 9).Select
     Worksheets("2016").Cells(1, 10).Select
     Worksheets("2016").Cells(1, 11).Select
     Worksheets("2016").Cells(1, 12).Select
     Worksheets("2016").Cells(1, 15).Select
     Worksheets("2016").Cells(1, 16).Select
     Worksheets("2016").Cells(2, 14).Select
     Worksheets("2016").Cells(3, 14).Select
     Worksheets("2016").Cells(4, 14).Select


End Sub

