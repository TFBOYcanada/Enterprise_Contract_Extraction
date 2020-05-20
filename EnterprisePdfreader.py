from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
import pandas as pd
import numpy as np

def read_pdf(pdf):
    # resource manager
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    # device
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdf)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    # grab all the lines
    lines = str(content)#.split("\n")logging.info('parsing %s',i)
    return lines

def get_index1(lst=None, item=''):  # get one item for all index

    return [index for (index, value) in enumerate(lst) if value == item]

def find_key(arr,item):  #  find the indes for all items
    location=[]
    for i in item:
        index=get_index1(arr,i)
        location.append(index)
    return location

def make_word(s2):  #  merge strings seprated with special signs
    ans=[]
    cc=''
    for i in s2:
        sign=['',':','/','&','#']
        if i not in sign :
            cc+=i
        elif cc!='':
            ans.append(cc)
            cc=''
        else:
            cc=''
    return ans

def find_word(arr,key,res):  # find the keyword according to index
    word=[]
    for i in key:
        if type(i) is int:
            word.append(arr[i+res])
        else:
            for j in i:
                word.append(arr[j+res])
    return word

def pdf_parse(filepath,keyafter= ['Start', 'End', 'Driven', 'Charged', 'Model', '(CAD)CAD', 'DISTANCECAD'],keybefore= ['Plate', 'DETAILSVEHICLE']):
    #filepath = '/Users/gaominhao/Downloads/20190418.pdf'
    #filepath = '/Users/gaominhao/Documents/Enterprise/MerBC300.pdf'
    with open(filepath, "rb") as my_pdf:
        s = 'start'
        for i in read_pdf(my_pdf):  # elimate space
            if i != ' ':
                s += i
        s2 = s.split('\n')  # elimate change line

        text_arr = make_word(s2)
        #print(text_arr)
        #keyafter = ['Start', 'End', 'Driven', 'Charged', 'Model', '(CAD)CAD', 'DISTANCECAD']  # find after
        #keybefore = ['Plate', 'DETAILSVEHICLE']  # find before
        location = '•'  # branch location
        branch = get_index1(text_arr, location)

        address = text_arr[branch[-2] + 1:branch[-1]]
        branch_ad = ''
        for i in address:
            branch_ad += i

        dat = 'Agreement'
        time_index = text_arr.index(dat)
        date = text_arr[time_index - 3:time_index]
        datefix = ''

        for i in date:
            datefix += i

        pkdate = datefix.strip('Rental')  # time fixed

        key1 = find_key(text_arr, keyafter)  # find the index for want1
        key2 = find_key(text_arr, keybefore)  # find the index for want2

        record = find_word(text_arr, key1, 1)
        record.extend(find_word(text_arr, key2, -1))
        record.append(branch_ad) # get the info for branch address
        record.append(pkdate)   # get the pick up date


        colname = ['Start', 'End', 'Class', 'Drive', 'Charge', 'Make', 'Total', 'Day', 'Model', 'Plate', 'Location',
                'Agreement']


        return record
def Save_record(record,Whole_record):


    whole_record = []
    whole_record.append(record)

    df = pd.DataFrame(np.array(whole_record), columns=colname)

    print(df)
filepath = '/Users/gaominhao/Documents/Enterprise/2019-03-02.pdf'
want1 = ['Start', 'End', 'Driven', 'Charged', 'Model', '(CAD)CAD', 'DISTANCECAD']  # find after
want2 = ['Plate', 'DETAILSVEHICLE']  # find before

a=pdf_parse(filepath)

#print(a)