Attribute VB_Name = "Module3"
Sub YearlyChange():

Dim F As Double
Dim L As Double
Dim Change As Double
Dim YC As Double
Dim PC As Double
Dim X As Long
Dim ws As Worksheet

' Yearly Change

F = 0
L = 0
YC = 0

last_record = Cells(Rows.count, 1).End(xlUp).Row

For Each ws In Worksheets
    ws.Activate

For i = 2 To last_record
    ' First Price Finder
    If Cells(i - 1, 1).Value <> Cells(i, 1).Value Then
    F = Cells(i, 3).Value
    
   
    ' Last Price Finder
    
    ElseIf Cells(i, 1).Value <> Cells(i + 1, 1) Then
    L = Cells(i, 6).Value
    
    
    
    ' Yearly Change
    
    Change = (F - L)
    Cells(2 + YC, 10).Value = Change
    If F <> 0 Then
    PC = (Change / F) * 100

    Cells(2 + YC, 11).Value = PC
    
    End If
    
    YC = YC + 1
    
    
    End If
    
Next i

Next

End Sub


For i = 2 To counter

  If Cells(i, 10).Value > 0 Then

      Cells(i, 10).Interior.ColorIndex = 4

  Else

      Cells(i, 10).Interior.ColorIndex = 3
      Cells(i, 11).Value = 0 - Cells(i, 11).Value

  End If

Next i
Range("K:K").NumberFormat = "0%"
Range("q2:q3").NumberFormat = "0%"

