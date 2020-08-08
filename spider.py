import mechanize
import datetime
import sys
from html_handeling import data_getter,save_file
from parameters import data_gen 
# API = https://mechanize.readthedocs.io/en/latest/index.html


"""
info_name={
    "ctl00$ContentPlaceHolder1$ddlAcademicSession": academic_year,      # academic session
    "ctl00$ContentPlaceHolder1$ddlSem": sem,                            # semester
    "ctl00$ContentPlaceHolder1$ddlResultCategory": res_cat,             #result_category 
    "ctl00$ContentPlaceHolder1$txtRollno": roll_no,                     # roll_number
    "ctl00_ContentPlaceHolder1_cmdPrintTR": "View",                   #button print(view)
}
"""



def run(filename):
    academic_year, sem, res_cat, rollno_min, rollno_max, codes =data_gen(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
    sr_no=1
    for code in codes:
        for roll_no in range(rollno_min,rollno_max+1):
            br =mechanize.Browser()
            br.open("http://www.bietjhs.ac.in/studentresultdisplay/frmprintreport.aspx")
            br.select_form(name="aspnetForm")
            br.find_control("ctl00$ContentPlaceHolder1$ddlAcademicSession").get(academic_year).selected=True
            br.find_control("ctl00$ContentPlaceHolder1$ddlSem").get(sem).selected=True
            br.find_control("ctl00$ContentPlaceHolder1$ddlResultCategory").get(res_cat).selected=True      
            br["ctl00$ContentPlaceHolder1$txtRollno"]=str(roll_no+code)           
            #redirecting to resulting site which we want to scrape so then we will scrape the data and save in csv
            response = br.submit()
            
            data = data_getter(response.read(),sr_no)
            s = save_file(filename,data)
            if s:
                print(f"Done:{code+roll_no}")
                sr_no+=1
            else:
                print(f"Skipped{code+roll_no}")
            br.close()



if __name__ == "__main__":
    date    =   datetime.datetime.now()
    run(f"{date.year}{date.month}{date.day}{date.hour}{date.minute}{date.second}.csv")