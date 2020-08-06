import mechanize
# API = https://mechanize.readthedocs.io/en/latest/index.html

br = mechanize.Browser()
br.open("http://www.bietjhs.ac.in/studentresultdisplay/frmprintreport.aspx")
print(br.title())
print(br.geturl())
br.select_form(name="aspnetForm")
academic_year,sem,res_cat,roll_no="2017-2018","3","R","1604313016"

info_name={
    "ctl00$ContentPlaceHolder1$ddlAcademicSession": academic_year,      # academic session
    "ctl00$ContentPlaceHolder1$ddlSem": sem,                            # semester
    "ctl00$ContentPlaceHolder1$ddlResultCategory": res_cat,             #result_category 
    "ctl00$ContentPlaceHolder1$txtRollno": roll_no,                     # roll_number
    # "ctl00_ContentPlaceHolder1_cmdPrintTR": "View",                     #button print(view)
}
br.find_control("ctl00$ContentPlaceHolder1$ddlAcademicSession").get(academic_year).selected=True
br.find_control("ctl00$ContentPlaceHolder1$ddlSem").get(sem).selected=True
br.find_control("ctl00$ContentPlaceHolder1$ddlResultCategory").get(res_cat).selected=True      
br["ctl00$ContentPlaceHolder1$txtRollno"]=roll_no           
#redirecting to resulting site which we want to scrape so then we will scrape the data and save in csv
response = br.submit()

with open('some.html',"wb") as f:
    f.write(response.read())