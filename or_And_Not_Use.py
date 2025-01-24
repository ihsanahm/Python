
# A applicatent is eligiable for loan or not 
good_incom=False
good_credit= True

if good_incom and good_credit:
    print("The applicant is eligiable for loan ")
elif good_incom and not good_credit:
    print("The applicant is eligiable for loan ")
elif good_credit and not good_incom:
     print("The applicant is eligiable for loan ")
     print("not opration excute")
else:
    print("Not elegiable for loan ")

