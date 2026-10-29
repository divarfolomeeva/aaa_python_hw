outputfile = 'department_summary.csv'


def read_csv(path):
    employees = []

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    headers = lines[0].strip().split(';')

    for line in lines[1:]:
        values = line.strip().split(';')
        if len(values) == len(headers):
            employee = {}
            for i in range(len(headers)):
                employee[headers[i]] = values[i]
            employees.append(employee)

    return employees


def report_hierarchy(employees):
    hierarchy = {}

    for emp in employees:
        dept = emp['Департамент']
        team = emp['Отдел']

        if dept not in hierarchy:
            hierarchy[dept] = []

        if team not in hierarchy[dept]:
            hierarchy[dept].append(team)

    print("иерархия департаментов")
    for dept in hierarchy:
        print(f"\n{dept}:")
        for team in hierarchy[dept]:
            print(f"  - {team}")


def report_department_summary(employees):
    dept_data = {}

    for emp in employees:
        dept = emp['Департамент']
        salary = float(emp['Оклад'])

        if dept not in dept_data:
            dept_data[dept] = []

        dept_data[dept].append(salary)

    print("сводка по департаментам")
    print(f"{'департамент':<20} {'кол-во':<8} {'мин':<12} {'макс':<12} {'средняя':<12}")
    print("-" * 70)

    for dept in dept_data:
        salaries = dept_data[dept]
        count = len(salaries)
        min_sal = min(salaries)
        max_sal = max(salaries)
        avg_sal = sum(salaries) / count

        print(f"{dept:<20} {count:<8} {min_sal:<12.0f} {max_sal:<12.0f} {avg_sal:<12.2f}")


def report_department_summary_csv(employees, output_file=outputfile):
    dept_data = {}

    for emp in employees:
        dept = emp['Департамент']
        salary = float(emp['Оклад'])

        if dept not in dept_data:
            dept_data[dept] = []

        dept_data[dept].append(salary)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('департамент;кол-во человек;минимальная зарплата;максимальная зарплата;средняя зарплата\n')

        for dept in dept_data:
            salaries = dept_data[dept]
            count = len(salaries)
            min_sal = int(min(salaries))
            max_sal = int(max(salaries))
            avg_sal = sum(salaries) / count

            line = f"{dept};{count};{min_sal};{max_sal};{avg_sal:.2f}\n"
            f.write(line)

    print(f"итоговый csv-файл: {output_file}")


def main(option):
    if type(option) is not int:
        raise TypeError("номер варианта должен быть целым числом (1, 2 или 3")

    filepath = 'Corp_Summary.csv'
    employees = read_csv(filepath)

    if option == 1:
        report_hierarchy(employees)
    elif option == 2:
        report_department_summary(employees)
    elif option == 3:
        report_department_summary_csv(employees)
    else:
        raise ValueError(f"допустимые варианты: 1, 2, 3")


if __name__ == '__main__':
    main(3) #здесь менять номер варианта