Function Main
    Declare Integer NUMNIGHT

    Input NUMNIGHT
    Declare Real TOTALPAYMENT

    If NUMNIGHT > 0
        Assign TOTALPAYMENT = (NUMNIGHT * 250 * 0.15)+250
    Else
        Assign TOTALPAYMENT = 0
    End
    Output TOTALPAYMENT
End
