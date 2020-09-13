import  regex as re
import csv

k_log=0
log_files=open('log_name.csv','r',encoding='utf_8_sig')
#读取文件内容
log_file=csv.reader(log_files)
#设置文件对象
for log in log_file:

    log_str = ""
    f1 = open(log[0], "r", encoding='utf_8_sig')
    # 将txt文件的所有内容读入到字符串str中
    str_txt1 = f1.read()
    f1.close()
    str1 = ""
    result_name1 = re.compile(r'.*Author: (.*?) <.*').findall(str_txt1)
    result_name1 = list(set(result_name1))
    for i in result_name1:
        str1 = str1 + i + "\n"
    with open(log[0]+'Author.csv', 'w', encoding='utf_8_sig') as fw1:
        fw1.writelines(str1)
    f2 = open(log[0], "r", encoding='utf_8_sig')
    # 将txt文件的所有内容读入到字符串str中
    str_txt2 = f2.read()
    f2.close()
    # 将文件按照commit分割
    str2 = 'commit '
    find_java2 = ""
    result2 = str_txt2.split(str2)
    # 打开文件
    file2 = open(log[0]+'Author.csv', 'r', encoding='utf_8_sig')
    # 读取文件内容
    author_file2 = csv.reader(file2)
    # 遍历csv文件
    for author2 in author_file2:

        if len(author2) == 0:
            continue
        flag2 = 0
        for i2 in result2:
            java_2 = ""
            res = []
            if re.search("Author: " + author2[0], i2):
                find_num2 = re.search(author2[0], i2).group()
                result_java2 = re.findall('\d+[\t]\d+[\t][ >={}/\w-]*[.]java[}]?', i2)
                if result_java2:
                    if flag2 == 0:
                        flag2 = 1
                        java_2+=author2[0]+'\n'
                    for j2 in result_java2:
                        x2 = list(reversed(j2.split('\t')))
                        res.append(x2[0].strip())
                        java_2 = java_2 + x2[0].strip() + "\n"
                    if len(res) <= 50:
                        find_java2= find_java2 + java_2
    with open(log[0]+'Author_revised_files.csv', 'w', encoding='utf_8_sig') as fw2:
        fw2.writelines(find_java2)
    file3 = open(log[0]+'Author_revised_files.csv', 'r', encoding='utf_8_sig')
    # 读取文件内容
    author_revised_files3 = csv.reader(file3)
    java_file3 = []
    for file3 in author_revised_files3:
        result_java3 = re.findall('.*[.]java[}]?', file3[0])
        if result_java3:
            java_file3.append(file3[0])
    len1 = len(java_file3)
    len2 = len(list(set(java_file3)))
    COR = len1 / len2
    print("len1", len1)
    print("len2", len2)
    print("COR", COR)
    file4 = open(log[0]+'Author_revised_files.csv', 'r', encoding='utf_8_sig')
    # 读取文件内容
    author_revised_files4 = csv.reader(file4)
    str_txt4 = ""
    java_files4 = []
    flag4 = 0
    for file4 in author_revised_files4:
        result_java4 = re.findall('.*[.]java[}]?', file4[0])
        if result_java4:
            java_files4.append(file4[0])
        else:
            if flag4 == 0:
                str_txt4 += file4[0] + "\n"
                flag4 = 1
                continue
            for i4 in list(set(java_files4)):
                str_txt4 += i4 + "\n"
            str_txt4 += file4[0] + "\n"
            java_files4 = []
    for i4 in list(set(java_files4)):
        str_txt4 += i4 + "\n"
    with open(log[0]+'Author_revised_setfiles.csv', 'w', encoding='utf_8_sig') as fw:
        fw.writelines(str_txt4)
    # 计算CFOR
    file4 = open(log[0]+'Author_revised_setfiles.csv', 'r', encoding='utf_8_sig')
    # 读取文件内容
    author_revised_files4 = csv.reader(file4)
    java_file4 = []
    for file4 in author_revised_files4:
        result_java4 = re.findall('.*[.]java[}]?', file4[0])
        if result_java4:
            java_file4.append(file4[0])
    len3 = len(java_file4)
    len4 = len(list(set(java_file4)))
    CFOR = len3 / len4
    print("len3", len3)
    print("len4", len4)
    print("CFOR", CFOR)
    file5 = open(log[0]+'Author_revised_setfiles.csv', 'r', encoding='utf_8_sig')
    # 读取文件内容
    files5 = csv.reader(file5)
    list_javafiles5 = []
    flag5 = 0
    java_files5 = []
    CO_5 = 0
    # 将每个提交者的文件保存在一个列表里,每个作者的列表在保存在同一个列表里
    for file5 in files5:
        result_java5 = re.findall('.*[.]java[}]?', file5[0])
        if flag5 == 0:
            flag5 = 1
            continue
        if result_java5:
            java_files5.append(file5[0])
        else:
            list_javafiles5.append(java_files5)
            java_files5 = []
    list_javafiles5.append(java_files5)

    num_author5 = 0
    for z in list_javafiles5:
        if len(z) != 0:
            num_author5 += 1
    for m in range(len(list_javafiles5)):
        for n in range(len(list_javafiles5)):
            if (m == n or len(list_javafiles5[m]) == 0 or len(list_javafiles5[n]) == 0):
                continue
            list_inter = list(set(list_javafiles5[m]).intersection(set(list_javafiles5[n])))
            list_union = list(set(list_javafiles5[m]).union(set(list_javafiles5[n])))
            len5 = len(list_inter)
            len6 = len(list_union)
            CO_5 += (len5 / len6)
    print("CO_5", CO_5)
    print(num_author5)
    PCO = CO_5 / num_author5
    print(PCO)
    log_str+=str(COR)+','+str(CFOR)+','+str(PCO)+'\n'
    with open('measure1.csv', 'a+', encoding='utf_8_sig') as fw:
        fw.writelines(log_str)
    k_log+=1
    print(k_log)

