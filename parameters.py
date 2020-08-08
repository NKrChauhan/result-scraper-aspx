def data_gen(min,max,branch):
    """
    form-format:"2017-2018","1","R","1604313016"

    """
    all_codes = {
        "it":1604313000,
        "me":1604340000,
        "ee":1604320000,
        "cs":1604310000,
        "ec":1604331000,
        "ch":1604351000,
        "ce":1604300000,
        } 
        #codes for all branches if needed to loop through    
    codes = []
    if branch!="all":
        try:
            codes = [all_codes[branch]]
        except:
            raise Exception(f"{branch} does not exist as valid inputs are (it/cs/ee/ec/me/ch/ce/all)") 
    else:
        codes = all_codes.values()    
    # rollno_min+=code
    # rollno_max+=code
    return "2017-2018","3","R",min,max,codes
