import pandas as pd
from .models import Bank, Branches

def do_bank():

    a = open('indian_banks.sql','r',encoding="utf8")
    a = a.readlines()

    for i in range(41, 211):
        Bank.objects.create(
            name = a[i].split('\t')[0],
            b_id = int(a[i].split('\t')[1][:-1])
        )


def do_branch():
    df = pd.read_csv('bank_branches.csv')
    df = df.fillna('NA')
    idx = df.columns

    for i in range(len(df['ifsc'])):
        obj = Bank.objects.get(b_id = df[idx[1]][i])
        Branches.objects.create(
            ifsc = df[idx[0]][i],
            b_id = obj,
            branch = df[idx[2]][i],
            address = df[idx[3]][i],
            city = df[idx[4]][i],
            district = df[idx[5]][i],
            state = df[idx[6]][i]
        )
