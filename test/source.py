import csv
from collections import Counter

esm_data = [] # dictionary bood behtar bood badan search tosh sari tar bood
famil_data = []
Keshvar_data = []
rang_data = []
ashia_data = []
ghaza_data = []
data_participants = []

def ready_up():
    with open('esm_famil_data.csv' , newline='' , encoding='utf-8') as csv_file:
        game_data = csv.DictReader(csv_file , delimiter=',' )
        # header = next(game_data)
        for col in game_data:
            esm_data.append(col['esm'])
            famil_data.append(col['famil'])
            Keshvar_data.append(col['keshvar'])
            rang_data.append(col['rang'])
            ashia_data.append(col['ashia'])
            ghaza_data.append(col['ghaza'])

def add_participant(participant, answers):
    # esm_famil_participants = []
    participants_dict = {participant : answers}
    data_participants.append(participants_dict)
    return data_participants

def check_in_list( name_data , o_answer ):
    stripped_answer = o_answer.replace(" ","")
    stripped_name_data = []
    for data in name_data:
        stripped_data = data.replace(" ", "")
        stripped_name_data.append(stripped_data)
    if stripped_answer == "" :
        result = 0
    elif stripped_answer in stripped_name_data:
        result = 10
    else:
        result = 0
    return result

particants_esm = {}
particants_famil = {}
particants_keshvar = {}
particants_rang = {}
particants_ashia = {}
particants_ghaza = {}

def compare_participants(o_compare_list , o_initial_score):
    value_count = Counter(o_compare_list.values())
    # print(value_count)
    for people, value in o_compare_list.items():
        if None not in value_count :
             if value_count[value] > 1:
                o_initial_score[people] = o_initial_score[people] - 5
                continue
        else:
            if o_compare_list[people] == None :
                o_initial_score[people] = o_initial_score[people]
            if value_count[value] > 1:
                o_initial_score[people] = o_initial_score[people]
                continue
            elif value_count[value] == 1 and o_compare_list[people] != None:
                o_initial_score[people] = o_initial_score[people] + 5


def score_calculator(score_dict):
    sum_score=0
    for value in score_dict:
        sum_score = score_dict[value] + sum_score
    return sum_score

def calculate_all():
    score_dict = {}
    initial_score = {}
    for sheet in data_participants:
        for participant in sheet:
            for item in sheet[participant]:
                answer = sheet[participant][item]
                if item == 'esm':
                    score_esm = check_in_list((esm_data), answer)
                    if score_esm == 0:
                        score_dict[item] = score_esm
                        particants_esm [participant] = None
                    else :
                        score_dict[item] = score_esm
                        particants_esm[participant] = answer
                elif item == 'famil':
                    score_famil = check_in_list((famil_data), answer )
                    if score_famil == 0:
                        score_dict[item] = score_famil
                        particants_famil [participant] = None
                    else :
                        score_dict[item] = score_famil
                        particants_famil[participant] = answer
                    # score_dict[item] = score_famil
                    # particants_famil [participant] = answer
                elif item == 'keshvar':
                    score_keshvar = check_in_list((Keshvar_data), answer )
                    if score_keshvar == 0:
                        score_dict[item] = score_keshvar
                        particants_keshvar [participant] = None
                    else :
                        score_dict[item] = score_keshvar
                        particants_keshvar[participant] = answer
                    # score_dict[item] = score_keshvar
                    # particants_keshvar [participant] = answer
                elif item == 'rang':
                    score_rang = check_in_list((rang_data), answer )
                    if score_rang == 0:
                        score_dict[item] = score_rang
                        particants_rang [participant] = None
                    else :
                        score_dict[item] = score_rang
                        particants_rang[participant] = answer
                    # score_dict[item] = score_rang
                    # particants_rang [participant] = answer
                elif item == 'ashia':
                    score_ashia = check_in_list((ashia_data), answer )
                    if score_ashia == 0:
                        score_dict[item] = score_ashia
                        particants_ashia [participant] = None
                    else :
                        score_dict[item] = score_ashia
                        particants_ashia[participant] = answer
                    # score_dict[item] = score_ashia
                    # particants_ashia [participant] = answer
                elif item == 'ghaza':
                    score_ghaza = check_in_list((ghaza_data), answer )
                    if score_ghaza == 0:
                        score_dict[item] = score_ghaza
                        particants_ghaza [participant] = None
                    else :
                        score_dict[item] = score_ghaza
                        particants_ghaza[participant] = answer
                    # score_dict[item] = score_ghaza
                    # particants_ghaza [participant] = answer
            # print(score_dict)
            initial_score[participant] = score_calculator(score_dict)
            # print(initial_score)

    compare_participants(particants_esm , initial_score)
    compare_participants(particants_famil , initial_score)
    compare_participants(particants_keshvar , initial_score)
    compare_participants(particants_rang , initial_score)
    compare_participants(particants_ashia , initial_score)
    compare_participants(particants_ghaza , initial_score)
    print(initial_score)


if __name__=='__main__':
    ready_up()
    add_participant(participant = 'salib',
    answers = {'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس',
    'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
    add_participant(participant = 'kianoush',
    answers = {'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل',
    'rang': 'بلوطی', 'ashia': 'بیل', 'ghaza': 'به   پلو'})
    add_participant(participant = 'sajjad',
    answers = {'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما',
    'rang': 'بژ', 'ashia': '        ', 'ghaza': 'برنج خورشت'})
    add_participant(participant = 'farhad',
    answers = {'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب',
    'rang': 'بژ', 'ashia': 'بیل', 'ghaza': 'باقلوا'})
    calculate_all()
