import fitz
from  pprint import pprint
import re
import numpy as np
import pandas as pd
import numpy_financial as npf

def extractTransactions(filePath='./MFCas.pdf'):
    doc = fitz.open(filePath)
    text = []
    for page in doc:
        text+=page.get_text().splitlines()
    MFmap={}
    val=""

    for i in range(len(text)):
        line=text[i]

        if "FOLIO NO:" in line:
            key,val=line.split(":")
            val=val.strip()
            MFmap[val]={}

        if "ISIN" in line or "ARN" in line :
            match = re.search(r'^([^(]*)', line)
            if match:
                result = match.group(1)
                new_key=result.strip()
                MFmap[val][new_key]=[]

        if "Purchase" in line or "Systematic" in line or "Lateral In" in line or "SIP" in line or "Switch In" in line :
            MFmap[val][new_key].append((text[i-1],-int(float(text[i+1].replace(",","")))))
        elif "Switch Out" in line:
            MFmap[val][new_key].append((text[i-1],int(float(text[i+1].replace(",","")[1:-1]))))
        if "Valuation" in  line:
            match = re.search(r'Valuation on (\d{2}-[A-Za-z]{3}-\d{4})\s:\s([A-Za-z]{3})\s([\d,\.]+)', line)
            if match:
                date = match.group(1)
                price = match.group(3)
                MFmap[val][new_key].append((date,int(float(price.replace(",","")))))

    modifiedMap={}
    for i in MFmap:
        for j in MFmap[i]:
            # print(MFmap[i][j])
            if j not in modifiedMap:
                modifiedMap[j]=MFmap[i][j]
            else:
                modifiedMap[j]+=MFmap[i][j]
    # pprint(modifiedMap)
    return modifiedMap

txn=extractTransactions()
pprint(txn)