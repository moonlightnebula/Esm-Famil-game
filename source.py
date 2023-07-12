import csv

all_data = {}
headers = ['esm' , 'famil' , 'keshvar' , 'rang' , 'ashia' , 'ghaza']
for head in headers :
    all_data[head] = []

data_participants = []

def remove_space(word):
    return (word.replace(' ', ''))

def ready_up():
    with open ('esm_famil_data.csv' , newline='' , encoding='utf-8') as csv_file:
        game_data = csv.reader(csv_file , delimiter=',')
        next(game_data)
        for row in game_data:
            all_data['esm'].append(remove_space(row[0]))
            all_data['famil'].append(remove_space(row[1]))
            all_data['keshvar'].append(remove_space(row[2]))
            all_data['rang'].append(remove_space(row[3]))
            all_data['ashia'].append(remove_space(row[4]))
            all_data['ghaza'].append(remove_space(row[5]))

def add_participant(participant, answers):
    participants_dict = {participant : answers}
    data_participants.append(participants_dict)
    return data_participants
    # print(data_participants)

def calculate_all():
    scores = {}

    for participant in data_participants:
        for people in participant:
            scores[people] = 0
            for head in headers:
                javab = remove_space(participant[people][head])
                if javab not in all_data[head] or not javab :
                    score = 0
                else:
                    duplicate = False
                    all_answered = True
                    for other in data_participants:
                        for name in other:
                            if name == people:
                                continue
                            if remove_space(other[name][head]) == javab :
                                duplicate = True
                            if remove_space(other[name][head]) == '' :
                                all_answered = False
                    if duplicate and all_answered:
                        score = 5
                    if not all_answered and duplicate :
                        score = 10
                    if not duplicate and all_answered:
                        score = 10
                    if not all_answered and not duplicate:
                        score = 15
                scores[people] = scores[people] + score
                # print(people , javab , score)
    return scores        

if __name__ == '__main__':
    ready_up()

    add_participant(participant = 'salib', answers = {'esm': 'بردیا', 'famil': 'بابایی',
     'keshvar': 'باربادوس', 'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
    add_participant(participant = 'kianoush', answers = {'esm': 'بهرام', 'famil': 'بهرامی', 
    'keshvar': 'برزیل', 'rang': 'بلوطی', 'ashia': 'بیل', 'ghaza': 'به   پلو'})
    add_participant(participant = 'sajjad', answers = {'esm': 'بابک', 'famil': 'بهشتی', 
    'keshvar': 'باهاما', 'rang': 'بژ', 'ashia': '        ', 'ghaza': 'برنج خورشت'})
    add_participant(participant = 'farhad', answers = {'esm': 'بهرام', 'famil': 'براتی',
     'keshvar': 'بببببب', 'rang': 'بژ', 'ashia': 'بیل', 'ghaza': 'باقلوا'})

    print(calculate_all())
