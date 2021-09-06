import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
import os
def append_df_to_excel(filename, df, sheet_name='Sheet1', startrow=None,
                       truncate_sheet=False, 
                       **to_excel_kwargs):
    # Excel file doesn't exist - saving and exiting
    if not os.path.isfile(filename):
        df.to_excel(
            filename,
            sheet_name=sheet_name, 
            startrow=startrow if startrow is not None else 0, 
            **to_excel_kwargs)
        return
    
    # ignore [engine] parameter if it was passed
    if 'engine' in to_excel_kwargs:
        to_excel_kwargs.pop('engine')

    writer = pd.ExcelWriter(filename, engine='openpyxl', mode='a')

    # try to open an existing workbook
    writer.book = load_workbook(filename)
    
    # get the last row in the existing Excel sheet
    # if it was not specified explicitly
    if startrow is None and sheet_name in writer.book.sheetnames:
        startrow = writer.book[sheet_name].max_row

    # truncate sheet
    if truncate_sheet and sheet_name in writer.book.sheetnames:
        # index of [sheet_name] sheet
        idx = writer.book.sheetnames.index(sheet_name)
        # remove [sheet_name]
        writer.book.remove(writer.book.worksheets[idx])
        # create an empty sheet [sheet_name] using old index
        writer.book.create_sheet(sheet_name, idx)
    
    # copy existing sheets
    writer.sheets = {ws.title:ws for ws in writer.book.worksheets}

    if startrow is None:
        startrow = 0

    # write out the new sheet
    df.to_excel(writer, sheet_name, startrow=startrow, **to_excel_kwargs)

    # save the workbook
    writer.save()
def get_property():
    page = 1
    ls= []
    url = 'https://www.auhouseprices.com/sold/list/NSW/2127/Wentworth+Point/'
    for page in range(1, 15):
        response = requests.get(url=url+str(page))
        c = response.content
        soup = BeautifulSoup(c, "html.parser")
        all_c = soup.findAll("div", {"class": "caption"})
        for item in all_c:
            d={}
            d["price"]=item.find("span",{"class":"pull-right"}).text
            d["address"]=item.find("h4").text
            d["bed"]= item.find("big").text
            d["date"] = item.find("li").text
            ls.append(d)
        page=+1
        
    df = pd.DataFrame(ls)
    print(df)
    return df
timeD=time.strftime("%Y-%m-%d-%H-%S",time.localtime())
append_df_to_excel(timeD+"-get_previous_price.xlsx", get_property())
