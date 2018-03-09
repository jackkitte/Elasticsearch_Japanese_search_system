# -*- coding: utf-8 -*-

with open("synonym.txt", "r") as fr:
    lines = fr.readlines()
    with open("synonym_r.txt", "a") as fa:
        for line in lines:
            line = line.replace("\n", "")
            fa.write("{} => {}".format(line, line))
            fa.write("\n")
