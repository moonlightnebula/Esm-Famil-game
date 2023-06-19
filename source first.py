import csv


def ready_up(PATH):

    with open(PATH, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            result = ', '.join(row)
    return result



def add_participant(participant, answers):
    pass


def calculate_all():
    pass


if __name__ == '__main__':
    print (ready_up("I:\snake\Quera solutions\esm-famil\esm_famil_data.csv"))