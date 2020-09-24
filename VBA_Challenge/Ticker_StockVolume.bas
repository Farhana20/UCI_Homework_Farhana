Attribute VB_Name = "Module2"
Sub FindTicker():


Dim t As Long
Dim Lastrow As Long
Dim count

CurrentValue = Cells(2, 1)
counter = 2
Cells(2, 9) = CurrentValue
last_record = Cells(Rows.count, 1).End(xlUp).Row


'Find Ticker


 For t = 3 To last_record
 
     If Cells(t, 1).Value <> CurrentValue Then
     
     Cells(counter, 9) = CurrentValue
     
     CurrentValue = Cells(t, 1).Value
     
     counter = counter + 1
     
   
End If

Next t

'The total stock volume of the stock.'

For i = 2 To counter

  For J = 2 To last_record

        If (Cells(i, 9) = Cells(J, 1)) Then

        Total_volume = Total_volume + Cells(J, 7).Value

        End If

  Next J
  
  Cells(i, 12).Value = Total_volume
  Total_volume = 0

Next i



End Sub

