with open('report.txt', encoding='utf-8') as grades_class:
    students_lines_whole = []
    students_grade_whole = []
    students_grade_last = []
    list_finish = []
    count_num = 1
    Chinese = 0
    Math = 0
    English = 0
    Physics = 0
    Chemistry = 0
    Biology = 0
    Polity = 0
    History = 0
    Geography = 0
    sum_num = 0
    average_num = 0
    for grades_per_line in grades_class:
        students_lines_whole.append([grades_per_line.strip()])
    students_lines_whole.insert(0, "姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理")
    for search_per_index in students_lines_whole[1:]:
        search_per_index = ','.join(search_per_index)
        search_per_index = search_per_index.split(' ')
        search_per_index = ' '.join(search_per_index)
        search_per_index = search_per_index.split()
        sum_grade = sum(int(x) for x in search_per_index[1:])
        average_grade = round(sum_grade / len(search_per_index[1:]), 1)
        search_per_index.append(str(sum_grade))
        search_per_index.append(str(average_grade))
        students_grade_whole.append(search_per_index)
        students_grade_whole = sorted([x for x in students_grade_whole], reverse=True, key=lambda x: x[-1])
    for x in students_grade_whole:
        x.insert(0, str(count_num))
        count_num += 1
        students_grade_last.append(x)
    for search_per_index_next in students_grade_last:
        Chinese += int(search_per_index_next[2])
        Math += int(search_per_index_next[3])
        English += int(search_per_index_next[4])
        Physics += int(search_per_index_next[5])
        Chemistry += int(search_per_index_next[6])
        Biology += int(search_per_index_next[7])
        Polity += int(search_per_index_next[8])
        History += int(search_per_index_next[9])
        Geography += int(search_per_index_next[10])
        sum_num += int(search_per_index_next[11])
        average_num += eval(search_per_index_next[12])
    list_finish.insert(0, "名次 姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理 总分 平均分")
    list_finish.insert(1, "0 平均 %.1f %.1f %.1f %.1f %.1f""%.1f %.1f %.1f %.1f %.1f %.1f"
                       % (Chinese / 30, Math / 30, English / 30,
                          Physics / 30, Chemistry / 30, Biology / 30,
                          Polity / 30, History / 30, Geography / 30, sum_num / 30,
                          average_num / 30))
    for m in students_grade_last:
        for j in m[2:-2]:
            if int(j) < 60:
                m[m.index(j)] = '不及格'
        m = ' '.join(m)
        list_finish.append(m)
    with open('output.txt', 'w', encoding='utf-8') as output:
        output.write('\n'.join(list_finish))
