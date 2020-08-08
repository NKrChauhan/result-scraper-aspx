import mechanize
import datetime
import sys
# API = https://mechanize.readthedocs.io/en/latest/index.html
from html_handeling import data_getter,save_file

"""
info_name={
    "ctl00$ContentPlaceHolder1$ddlAcademicSession": academic_year,      # academic session
    "ctl00$ContentPlaceHolder1$ddlSem": sem,                            # semester
    "ctl00$ContentPlaceHolder1$ddlResultCategory": res_cat,             #result_category 
    "ctl00$ContentPlaceHolder1$txtRollno": roll_no,                     # roll_number
    "ctl00_ContentPlaceHolder1_cmdPrintTR": "View",                   #button print(view)
}
"""

def data_gen(min,max):
    """
    format:"2017-2018","1","R","1704313016"

    """
    return "2017-2018","3","R",min,max

def run(filename):
    academic_year,sem,res_cat,rollno_min,rollno_max=data_gen(int(sys.argv[1]),int(sys.argv[2]))
    #this is for 2016-2020(corona kaal) batch 
    bases = {
        "it":1604313000,
        "me":1604340000,
        "ee":1604320000,
        "cs":1604310000,
        "ec":1604331000,
        "ch":1604351000,
        "ce":1604300000,
        } #codes for all branches if needed to loop through
    base=bases[sys.argv[3]]
    # rollno_min+=base
    # rollno_max+=base
    for roll_no in range(rollno_min,rollno_max+1):
        br =mechanize.Browser()
        br.open("http://www.bietjhs.ac.in/studentresultdisplay/frmprintreport.aspx")
        br.select_form(name="aspnetForm")
        br.find_control("ctl00$ContentPlaceHolder1$ddlAcademicSession").get(academic_year).selected=True
        br.find_control("ctl00$ContentPlaceHolder1$ddlSem").get(sem).selected=True
        br.find_control("ctl00$ContentPlaceHolder1$ddlResultCategory").get(res_cat).selected=True      
        br["ctl00$ContentPlaceHolder1$txtRollno"]=str(roll_no+base)           
        #redirecting to resulting site which we want to scrape so then we will scrape the data and save in csv
        response = br.submit()
        
        data = data_getter(response.read(),roll_no)
        s = save_file(filename,data)
        if s:
            print(f"done:{base+roll_no}")
        else:
            print(f"skipped{base+roll_no}")
        br.close()


if __name__ == "__main__":
    date    =   datetime.datetime.now()
    run(f"{date.year}{date.month}{date.day}{date.hour}{date.minute}{date.second}.csv")