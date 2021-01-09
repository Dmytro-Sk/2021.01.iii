import csv


def create_file(spider_name):
    with open(f'../../iii_results/01-{spider_name}.csv') as old_f:
        reader = csv.reader(old_f)
        for line in reader:
            headers = line
            break
        with open(f'../../iii_results/{spider_name}.csv', 'w', newline='') as new_f:
            writer = csv.DictWriter(new_f, fieldnames=headers)
            writer.writeheader()


def combine_csv(spider_name, file_amount):
    create_file(spider_name)
    for i in range(1, file_amount + 1):
        with open(f'../../iii_results/0{i}-{spider_name}.csv', encoding='utf-8') as old_f:
            reader = csv.reader(old_f)
            next(reader)
            with open(f'../../iii_results/{spider_name}.csv', 'a', newline='', encoding='utf-8') as new_f:
                writer = csv.writer(new_f)
                for line in reader:
                    writer.writerow(line)


combine_csv(spider_name='glovoapp_com_restaurants', file_amount=4)
