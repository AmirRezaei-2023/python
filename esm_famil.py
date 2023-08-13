import re
import csv
def ready_up():
    global participants_dict,true_dict,participants_list,esm_list,esm_list_dup,famil_list,famil_list_dup,keshvar_list,keshvar_list_dup,rang_list,rang_list_dup,ghaza_list,ghaza_list_dup,ashia_list,ashia_list_dup
    participants_dict={}
    participants_list=[]
    esm_list=[]
    esm_list_dup=[]
    famil_list=[]
    famil_list_dup=[]
    keshvar_list=[]
    keshvar_list_dup=[]
    rang_list=[]
    rang_list_dup=[]
    ghaza_list=[]
    ghaza_list_dup=[]
    ashia_list=[]
    ashia_list_dup=[]
    true_dict={'esm':[],'famil':[],'keshvar':[],'rang':[],'ashia':[],'ghaza':[]}
    file = open('esm_famil_data.csv', "r",encoding="utf8")
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        if row[0]!='esm':
            true_dict['esm'].append(row[0].replace(' ',''))
        if row[1]!='famil':
            true_dict['famil'].append(row[1].replace(' ',''))
        if row[2]!='keshvar':
            true_dict['keshvar'].append(row[2].replace(' ',''))
        if row[3]!='rang':
            true_dict['rang'].append(row[3].replace(' ',''))
        if row[4]!='ashia':
            true_dict['ashia'].append(row[4].replace(' ',''))
        if row[5]!='ghaza':
            true_dict['ghaza'].append(row[5].replace(' ',''))
    k=''
    while(k in true_dict['esm']):
        true_dict['esm'].remove(k)
    while(k in true_dict['famil']):
        true_dict['famil'].remove(k)
    while(k in true_dict['keshvar']):
        true_dict['keshvar'].remove(k)
    while(k in true_dict['rang']):
        true_dict['rang'].remove(k)
    while(k in true_dict['ghaza']):
        true_dict['ghaza'].remove(k)
    while(k in true_dict['ashia']):
        true_dict['ashia'].remove(k)
    file.close()
    print(true_dict['ashia'])
    return true_dict,participants_list,esm_list,esm_list_dup,famil_list,famil_list_dup,keshvar_list,keshvar_list_dup,rang_list,rang_list_dup,ghaza_list,ghaza_list_dup,ashia_list,ashia_list_dup

def add_participant(participant, answers):
    global participants_list
    participants_list.append(participant)
    if answers['esm'].replace(' ','')  in esm_list:
        esm_list_dup.append(answers['esm'].replace(' ',''))
    esm_list.append(answers['esm'].replace(' ',''))
    if answers['famil'].replace(' ','')  in famil_list:
        famil_list_dup.append(answers['famil'].replace(' ',''))
    famil_list.append(answers['famil'].replace(' ',''))
    if answers['keshvar'].replace(' ','')  in keshvar_list:
        keshvar_list_dup.append(answers['keshvar'].replace(' ',''))
    keshvar_list.append(answers['keshvar'].replace(' ',''))
    if answers['rang'].replace(' ','')  in rang_list:
        rang_list_dup.append(answers['rang'].replace(' ',''))
    rang_list.append(answers['rang'].replace(' ',''))
    if answers['ghaza'].replace(' ','')  in ghaza_list:
        ghaza_list_dup.append(answers['ghaza'].replace(' ',''))
    ghaza_list.append(answers['ghaza'].replace(' ',''))
    if answers['ashia'].replace(' ','') in ashia_list:
        ashia_list_dup.append(answers['ashia'].replace(' ',''))
    ashia_list.append(answers['ashia'].replace(' ',''))
    print(ashia_list)
    print(ashia_list_dup)
    return participants_list,esm_list,esm_list_dup,famil_list,famil_list_dup,keshvar_list,keshvar_list_dup,rang_list,rang_list_dup,ghaza_list,ghaza_list_dup,ashia_list,ashia_list_dup
def calculate_all():
    
    for ind, i in enumerate(participants_list):
        count_e=0
        count_f=0
        count_k=0
        count_r=0
        count_g=0
        count_s=0
        count=0
###esm##
        if ''  not in esm_list:
            if esm_list[ind] not in true_dict['esm']:
                count_e+=0
            elif (esm_list[ind]  in true_dict['esm']) and (esm_list[ind]  in esm_list_dup):
                count_e+=5
            elif (esm_list[ind]  in true_dict['esm']) and (esm_list[ind]  not in esm_list_dup):
                count_e+=10
        if ''  in esm_list:
            if (esm_list[ind]  not in true_dict['esm']) or (esm_list[ind]==' '):
                count_e+=0
            elif (esm_list[ind] in true_dict['esm']) and (esm_list[ind] in esm_list_dup):
                count_e+=10
            elif (esm_list[ind] in true_dict['esm']) and (esm_list[ind] not in esm_list_dup):
                count_e+=15
###famil##
        if '' not in famil_list:
            if famil_list[ind] not in true_dict['famil']:
                count_f+=0
            elif (famil_list[ind] in true_dict['famil']) and (famil_list[ind] in famil_list_dup):
                count_f+=5
            elif (famil_list[ind] in true_dict['famil']) and (famil_list[ind] not in famil_list_dup):
                count_f+=10
        if '' in famil_list:
            if (famil_list[ind] not in true_dict['famil']) or (famil_list[ind]==' '):
                count_f+=0
            elif (famil_list[ind] in true_dict['famil']) and (famil_list[ind] in famil_list_dup):
                count_f+=10
            elif (famil_list[ind] in true_dict['famil']) and (famil_list[ind] not in famil_list_dup):
                count_f+=15
##keshvar##
        if '' not in keshvar_list:
            if keshvar_list[ind] not in true_dict['keshvar']:
                count_k+=0
            elif (keshvar_list[ind]in true_dict['keshvar']) and (keshvar_list[ind] in keshvar_list_dup):
                count_k+=5
            elif (keshvar_list[ind] in true_dict['keshvar']) and (keshvar_list[ind] not in keshvar_list_dup):
                count_k+=10
        if '' in keshvar_list:
            if (keshvar_list[ind] not in true_dict['keshvar']) or (keshvar_list[ind]==' '):
                count_k+=0
            elif (keshvar_list[ind] in true_dict['keshvar']) and (keshvar_list[ind] in keshvar_list_dup):
                count_k+=10
            elif (keshvar_list[ind] in true_dict['keshvar']) and (keshvar_list[ind] not in keshvar_list_dup):
                count_k+=15
##rang##
        if '' not in rang_list:
            if rang_list[ind] not in true_dict['rang']:
                count_r+=0
            elif (rang_list[ind] in true_dict['rang']) and (rang_list[ind] in rang_list_dup):
                count_r+=5
            elif (rang_list[ind] in true_dict['rang']) and (rang_list[ind] not in rang_list_dup):
                count_r+=10
        if '' in rang_list:
            if (rang_list[ind] not in true_dict['rang']) or (rang_list[ind]==' '):
                count_r+=0
            elif (rang_list[ind] in true_dict['rang']) and (rang_list[ind] in rang_list_dup):
                count_r+=10
            elif (rang_list[ind] in true_dict['rang']) and (rang_list[ind] not in rang_list_dup):
                count_r+=15
##ghaza##
        if ''not in ghaza_list:
            if ghaza_list[ind] not in true_dict['ghaza']:
                count_g+=0
            elif (ghaza_list[ind] in true_dict['ghaza']) and (ghaza_list[ind] in ghaza_list_dup):
                count_g+=5
            elif (ghaza_list[ind] in true_dict['ghaza']) and (ghaza_list[ind] not in ghaza_list_dup):
                count_g+=10
        if '' in ghaza_list:
            if (ghaza_list[ind] not in true_dict['ghaza']) or (ghaza_list[ind]==' '):
                count_g+=0
            elif (ghaza_list[ind] in true_dict['ghaza']) and (ghaza_list[ind] in ghaza_list_dup):
                count_g+=10
            elif (ghaza_list[ind] in true_dict['ghaza']) and (ghaza_list[ind] not in ghaza_list_dup):
                count_g+=15
##ashia##
        if '' not in ashia_list:
            if ashia_list[ind] not in true_dict['ashia']:
                count_s+=0
            elif (ashia_list[ind] in true_dict['ashia']) and (ashia_list[ind] in ashia_list_dup):
                count_s+=5
            elif (ashia_list[ind] in true_dict['ashia']) and (ashia_list[ind] not in ashia_list_dup):
                count_s+=10
        if '' in ashia_list:
            if (ashia_list[ind] not in true_dict['ashia']) or (ashia_list[ind]==' '):
                count_s+=0
            elif (ashia_list[ind] in true_dict['ashia']) and (ashia_list[ind] in ashia_list_dup):
                count_s+=10
            elif (ashia_list[ind] in true_dict['ashia']) and (ashia_list[ind] not in ashia_list_dup):
                count_s+=15
        participants_dict[i]=count_s+count_r+count_g+count_k+count_e+count_f
    return participants_dict
        
