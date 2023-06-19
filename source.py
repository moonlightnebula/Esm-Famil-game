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
        result = None
        o_status = False
    elif stripped_answer in stripped_name_data:
        result = 10
        o_status = True
    else:
        result = 0
        o_status = True
    return result , o_status

particants_esm = {}
status_answer_esm = {}
particants_famil = {}
status_answer_famil = {}
particants_keshvar = {}
status_answer_keshvar ={}
particants_rang = {}
status_answer_rang = {}
particants_ashia = {}
status_answer_ashia = {}
particants_ghaza = {}
status_answer_ghaza = {}

def compare_participants(o_compare_list , o_initial_score , o_status_answer):
    value_count = Counter(o_compare_list.values())
    status_count = Counter(o_status_answer)
    for people, value in o_compare_list.items():
        if False not in status_count.values() :
            if value_count[value] > 1:
                o_initial_score[people] = o_initial_score[people] - 5
                continue
        else:
            if o_status_answer[people] is False :
                o_initial_score[people] = o_initial_score[people]
            if value_count[value] > 1:
                o_initial_score[people] = o_initial_score[people]
            elif value_count[value] == 1 and o_status_answer[people] is True :
                o_initial_score[people] = o_initial_score[people] + 5


def score_calculator(score_dict):
    sum_score=0
    for value in score_dict:
        if score_dict[value] is None:
            score_dict[value] = 0
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
                    score_esm , o_status_answer = check_in_list((esm_data), answer)
                    score_dict[item] = score_esm
                    particants_esm [participant] = answer
                    status_answer_esm[participant] = o_status_answer
                elif item == 'famil':
                    score_famil , o_status_answer = check_in_list((famil_data), answer )
                    score_dict[item] = score_famil
                    particants_famil [participant] = answer
                    status_answer_famil[participant] = o_status_answer
                elif item == 'keshvar':
                    score_keshvar , o_status_answer = check_in_list((Keshvar_data), answer )
                    score_dict[item] = score_keshvar
                    particants_keshvar [participant] = answer
                    status_answer_keshvar[participant] = o_status_answer
                elif item == 'rang':
                    score_rang , o_status_answer = check_in_list((rang_data), answer )
                    score_dict[item] = score_rang
                    particants_rang [participant] = answer
                    status_answer_rang[participant] = o_status_answer
                elif item == 'ashia':
                    score_ashia , o_status_answer = check_in_list((ashia_data), answer )
                    score_dict[item] = score_ashia
                    particants_ashia [participant] = answer
                    status_answer_ashia[participant] = o_status_answer
                elif item == 'ghaza':
                    score_ghaza , o_status_answer = check_in_list((ghaza_data), answer )
                    score_dict[item] = score_ghaza
                    particants_ghaza [participant] = answer
                    status_answer_ghaza[participant] = o_status_answer
            initial_score[participant] = score_calculator(score_dict)

    compare_participants(particants_esm , initial_score , status_answer_esm)
    compare_participants(particants_famil , initial_score , status_answer_famil)
    compare_participants(particants_keshvar , initial_score , status_answer_keshvar)
    compare_participants(particants_rang , initial_score , status_answer_rang)
    compare_participants(particants_ashia , initial_score , status_answer_ashia)
    compare_participants(particants_ghaza , initial_score , status_answer_ghaza)
    return initial_score

if __name__=='__main__':
    ready_up()

    add_participant(participant = 'salib',
    answers = {'esm': 'ایدا', 'famil': 'اسدی', 'keshvar': 'المان', 'rang': 'ابی',
    'ashia': 'اره', 'ghaza': 'اش'})
    add_participant(participant = 'kianoush',
    answers = {'esm': 'امیر', 'famil': 'اکبری', 'keshvar': 'انگولا', 'rang': 'اجری',
    'ashia': 'اره برقی', 'ghaza': 'اب گوشت'})
    add_participant(participant = 'sajjad',
    answers = {'esm': 'ارمان', 'famil': 'ارمانی', 'keshvar': 'ایتالیا', 'rang': 'ارغوانی',
    'ashia': 'اب پاش', 'ghaza': 'اب گوشت'})
    add_participant(participant = 'ali',
    answers = {'esm': 'ارش', 'famil': 'اعظمی', 'keshvar': 'ارژانتین', 'rang': 'ارکیده',
    'ashia': 'ایینه', 'ghaza': 'اب گوشت'})
    add_participant(participant = 'mamad',
    answers = {'esm': 'امنه', 'famil': 'ازادی', 'keshvar': 'ارمنستان', 'rang': 'البالویی',
    'ashia': 'استکان', 'ghaza': 'اب گوشت'})

    # add_participant(participant = 'salib',
    # answers = {'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش',
    # 'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
    # add_participant(participant = 'kianoush',
    # answers = {'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی',
    # 'ashia': 'بیل', 'ghaza': 'به   پلو'})
    # add_participant(participant = 'sajjad',
    # answers = {'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ',
    # 'ashia': '        ', 'ghaza': 'برنج خورشت'})
    # add_participant(participant = 'farhad',
    # answers = {'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ',
    # 'ashia': 'بیل', 'ghaza': 'باقلوا'})

    calculate_all()
    print (calculate_all())
