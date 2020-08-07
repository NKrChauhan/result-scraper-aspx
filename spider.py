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
    bases = [160431300,] #codes for all branches if needed to loop through
    base=1604313000
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
        print(f"done:{base+roll_no}")
        save_file(filename,data)
        br.close()


if __name__ == "__main__":
    date    =   datetime.datetime.now()
    run(f"{date}.csv")