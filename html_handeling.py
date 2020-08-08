from requests_html import HTML
from csv import DictWriter
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def data_getter(html_page,i,sem):
    page    = HTML(html=html_page)    
    if not page.find("#ctl00_ContentPlaceHolder1_rollno"):
        return {"index":i,"roll_no":"","name":"","fname":"","branch":"","marks":"","result":""}
    information ={
    "index"   : i,
    "roll_no" : page.find("#ctl00_ContentPlaceHolder1_rollno")[0].text,
    "name"    : page.find("#ctl00_ContentPlaceHolder1_sName")[0].text,
    "fname"   : page.find("#ctl00_ContentPlaceHolder1_fName")[0].text,
    "branch"  : page.find("#ctl00_ContentPlaceHolder1_bname")[0].text,
    "marks_o" : eval(page.find("#ctl00_ContentPlaceHolder1_omk")[0].text)*100,
    } 
    if int(sem)%2==0:
        information["marks_e"]     = eval(page.find("#ctl00_ContentPlaceHolder1_emk")[0].text)*100
        information["total_marks"] = eval(page.find("#ctl00_ContentPlaceHolder1_YTTO")[0].text)*100
        year = int(sem)/2
        if year==1:
            information["result"]      = page.find("#ctl00_ContentPlaceHolder1_fst")[0].text
        elif year ==2:
            information["result"]      = page.find("#ctl00_ContentPlaceHolder1_snd")[0].text
        elif year ==3:
            information["result"]      = page.find("#ctl00_ContentPlaceHolder1_thrd")[0].text
        else:
            information["result"]      = page.find("#ctl00_ContentPlaceHolder1_frt")[0].text
    else:
        information["result"]      = page.find("#ctl00_ContentPlaceHolder1_oResult")[0].text

    return information

def append_row(filename, dict_of_elem):
    field_names = dict_of_elem.keys()
    with open(filename, 'a+', newline='') as write_obj:
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        dict_writer.writerow(dict_of_elem)

def save_file(filename,dictionary):
    file_path = os.path.join(BASE_DIR,filename)
    if dictionary["roll_no"]=="":
        return False
    else:
        df = pd.DataFrame(dictionary,index=[0])
        if not os.path.exists(file_path):
            df.to_csv(filename,index=False,header=True)
        else:
            df.to_csv(filename, mode='a', header=False,index=False)
        return True