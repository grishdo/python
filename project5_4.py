with open("text.txt", "r", encoding='utf-8') as f:
    with open("text1.txt", "w", encoding='utf-8') as f_1:
        for line in f:
            if line.find('One') != -1:
                f_1.write(line.replace('One', 'Один'))
            elif line.find('Two') != -1:
                f_1.write(line.replace('Two', 'Два'))
            elif line.find('Three') != -1:
                f_1.write(line.replace('Three', 'Три'))
            elif line.find('Four') != -1:
                f_1.write(line.replace('Four', 'Четыре'))

