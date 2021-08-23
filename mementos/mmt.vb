Sub reConditionFormatting()
    Cells.FormatConditions.Delete
    
    'Condition (1) - For all Cells with value "0", font color set to white
    ActiveSheet.usedRange.FormatConditions.Add Type:=xlCellValue, Operator:=xlEqual, Formula1:="=0"
    With ActiveSheet.usedRange.FormatConditions(1)
        .Font.Color = RGB(255, 255, 255)
        .StopIfTrue = False
    End With
    
    'Condition (2) - For row with JS cell "}", row background set to light grey
    ActiveSheet.usedRange.FormatConditions.Add Type:=xlExpression, Formula1:="=IFERROR($AM1,1)"
    With ActiveSheet.usedRange.FormatConditions(2)
        .Interior.Color = RGB(255, 255, 0)
        .StopIfTrue = False
    End With
    
    'Condition (3) - For row with JS cell "}", row background set to light grey
    ActiveSheet.usedRange.FormatConditions.Add Type:=xlExpression, Formula1:="=IF($AN1=CHAR(125),1)"
    With ActiveSheet.usedRange.FormatConditions(3)
        .Interior.Color = RGB(231, 230, 230)
        .StopIfTrue = False
    End With
    
End Sub
Sub refreshCalcField()
    Dim lastRow As Long
    
    Worksheets("Mementos").Activate
    lastRow = Cells.Find("*", SearchOrder:=xlByRows, SearchDirection:=xlPrevious).Row - 2
    
    Range("I3").Copy Range("I3:I" & lastRow)
    Range("M3").Copy Range("M3:M" & lastRow)
    Range("W3").Copy Range("W3:W" & lastRow)
    Range("AJ3").Copy Range("AJ3:AJ" & lastRow)
    Range("AM3:AP3").Copy Range("AM3:AP" & lastRow)
    
    Call reConditionFormatting
End Sub
Sub importMmtList()
    Dim TextFile As Integer
    Dim FilePath As String
    Dim FileContent As String
	Dim lastRow As Long
    Dim lastMmt As Long
    
    Worksheets("Mementos").Activate
    
    'File Path of Text File
    FilePath = Local_Workbook_Path(ActiveWorkbook) & "mmtList.txt"
    
    'Determine the next file number available for use by the FileOpen function
    TextFile = FreeFile
    
    'Open the text file
    Open FilePath For Input As TextFile
    
    'Store file content inside a variable
    FileContent = Input(LOF(TextFile), TextFile)
    
    lastRow = Cells.Find("*", SearchOrder:=xlByRows, SearchDirection:=xlPrevious).Row
    
    'Paste Text File Contents and create dummy columns to highlight new rows
    SetClipboard (FileContent)
    Range("B:C").Insert
    Range("B3").Select
    ActiveSheet.Paste
	lastMmt = Cells.Find("*", SearchOrder:=xlByRows, SearchDirection:=xlPrevious).Row
	Range("AO" & lastRow & ":AP" & lastRow).Copy Range("AO" & lastMmt + 2 & ":AP" & lastMmt + 2)
    Range("C3").Value = "=IF(COUNTIF(A:A,B3)=0,1,0)"
    Range("C3").Copy Range("C3:C" & lastMmt)
    
    'Search for new rows
    For currentRow = 3 To lastRow
        If ActiveSheet.Cells(currentRow, 3) = 1 Then
            'Insert 1 row on the active cell
            Range("A" & currentRow).EntireRow.Insert
            
            'Then move remaining mementos name to 1 row above
            Range("A" & currentRow + 1 & ":C" & lastMmt + 1).Copy Range("A" & currentRow)
            Range("A" & lastMmt + 1).EntireRow.Delete
        End If
    Next currentRow
    
    'Replace with new mmtList and delete dummy columns
    Range("B2:B" & lastMmt).Copy Range("A2")
    Range("B:C").EntireColumn.Delete
    
    'Close Text File
    Close TextFile
    
    Call refreshCalcField
    
End Sub
Sub copyHTML()
    Dim lastRow As Long
    
    Worksheets("Mementos").Activate
    lastRow = Cells.Find("*", SearchOrder:=xlByRows, SearchDirection:=xlPrevious).Row
    
    Dim strClip As String
    strClip = Range("AN2:AN" & lastRow).Copy
    strClip = GetClipboard()
    
    On Error Resume Next
    strClip = Replace(strClip, Chr(34), "")
    
    On Error GoTo 0
    SetClipboard (strClip)
End Sub
Sub copyJS()
    Dim lastRow As Long
    lastRow = Cells.Find("*", SearchOrder:=xlByRows, SearchDirection:=xlPrevious).Row
    
    Dim strClip As String
    strClip = Range("AO2:AO" & lastRow).Copy
    strClip = GetClipboard()
    
    On Error Resume Next
    strClip = Replace(strClip, Chr(34), "")
    
    On Error GoTo 0
    SetClipboard (strClip)
End Sub