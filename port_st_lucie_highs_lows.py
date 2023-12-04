import csv
from datetime import datetime

import matplotlib.pyplot as plt


FILENAME = 'data/port_st_lucie_2013_2020.csv'

with open(FILENAME) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    dates, precipitations = [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        try:
            precipitation = float(row[10])
        except ValueError:
            continue
        else:
            dates.append(current_date)
            precipitations.append(precipitation)

    plt.style.use(style='default')
    fig, ax = plt.subplots()
    ax.plot(dates, precipitations, c='red')

    title = 'Daily precipitation 2013 - 2020\nPort ST. Lucie, FL US'
    ax.set_title(title, fontsize=20)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('Precipitation', fontsize=16)

    plt.savefig('img/port_st_lucie_2013_2020.png', bbox_inches='tight')