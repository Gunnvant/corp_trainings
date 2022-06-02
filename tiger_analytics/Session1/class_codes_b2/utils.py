def check_number_present(s):
    flag = False
    for i in s:
        if i.isdigit():
            flag=True
            break
    return flag

def case_change(s):
    midpt = int(len(s)/2)
    s_new = s[0:midpt].lower()+s[midpt:].upper()
    return s_new