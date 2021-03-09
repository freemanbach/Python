#!/bin/env python3
# Author  : freeman
# Date    : 2021.03.09
# Desc    :
#         : 
# Version : 0.0.1
###################################################################

import sys
import os.path
from os import path


cd, dd, hd, td, vd = "case_data.csv", "death_data.csv", "hosp_data.csv", "test_data.csv", "vacc_data.csv"
m,n,o,p,q = "dates,case\n", "dates,death\n", "dates,hosp\n", "dates,test\n", "dates,vacc\n" 

def australia():
    aut = []
    with open('./australia/aut_case_data.csv') as f:
        for i in f:
            aut.append(i)
    aut.reverse()

    aut.insert(0, m)
    t = "./australia/aut_" + str(cd.split('.')[0]) + "_rev" + "." + str(cd.split('.')[1])
    with open(t, "w") as f:
        for i in aut:
            f.write(i)

    aut = []
    with open('./australia/aut_death_data.csv') as f:
        for i in f:
            aut.append(i)
    aut.reverse()

    aut.insert(0, n)
    t = "./australia/aut_" + str(dd.split('.')[0]) + "_rev" + "." + str(dd.split('.')[1])
    with open(t, "w") as f:
        for i in aut:
            f.write(i)

    aut = []
    with open('./australia/aut_hosp_data.csv') as f:
        for i in f:
            aut.append(i)
    aut.reverse()

    aut.insert(0, o)
    t = "./australia/aut_" + str(hd.split('.')[0]) + "_rev" + "." + str(hd.split('.')[1])
    with open(t, "w") as f:
        for i in aut:
            f.write(i)

    aut = []
    with open('./australia/aut_test_data.csv') as f:
        for i in f:
            aut.append(i)
    aut.reverse()

    aut.insert(0, p)
    t = "./australia/aut_" + str(td.split('.')[0]) + "_rev" + "." + str(td.split('.')[1])
    with open(t, "w") as f:
        for i in aut:
            f.write(i)

    aut = []
    with open('./australia/aut_vacc_data.csv') as f:
        for i in f:
            aut.append(i)
    aut.reverse()

    aut.insert(0, q)
    t = "./australia/aut_" + str(vd.split('.')[0]) + "_rev" + "." + str(vd.split('.')[1])
    with open(t, "w") as f:
        for i in aut:
            f.write(i)

def austria():
    ast = []
    with open('./austria/ast_case_data.csv') as f:
        for i in f:
            ast.append(i)
    ast.reverse()

    ast.insert(0, m)
    t = "./austria/ast_" + str(cd.split('.')[0]) + "_rev" + "." + str(cd.split('.')[1])
    with open(t, "w") as f:
        for i in ast:
            f.write(i)

    ast = []
    with open('./austria/ast_death_data.csv') as f:
        for i in f:
            ast.append(i)
    ast.reverse()

    ast.insert(0, n)
    t = "./austria/ast_" + str(dd.split('.')[0]) + "_rev" + "." + str(dd.split('.')[1])
    with open(t, "w") as f:
        for i in ast:
            f.write(i)

    ast = []
    with open('./austria/ast_hosp_data.csv') as f:
        for i in f:
            ast.append(i)
    ast.reverse()

    ast.insert(0, o)
    t = "./austria/ast_" + str(hd.split('.')[0]) + "_rev" + "." + str(hd.split('.')[1])
    with open(t, "w") as f:
        for i in ast:
            f.write(i)

    ast = []
    with open('./austria/ast_test_data.csv') as f:
        for i in f:
            ast.append(i)
    ast.reverse()

    ast.insert(0, p)
    t = "./austria/ast_" + str(td.split('.')[0]) + "_rev" + "." + str(td.split('.')[1])
    with open(t, "w") as f:
        for i in ast:
            f.write(i)

    ast = []
    with open('./austria/ast_vacc_data.csv') as f:
        for i in f:
            ast.append(i)
    ast.reverse()

    ast.insert(0, q)
    t = "./austria/ast_" + str(vd.split('.')[0]) + "_rev" + "." + str(vd.split('.')[1])
    with open(t, "w") as f:
        for i in ast:
            f.write(i)

def france():
    fra = []
    with open('./france/fra_case_data.csv') as f:
        for i in f:
            fra.append(i)
    fra.reverse()

    fra.insert(0, m)
    t = "./france/fra_" + str(cd.split('.')[0]) + "_rev" + "." + str(cd.split('.')[1])
    with open(t, "w") as f:
        for i in fra:
            f.write(i)

    fra = []
    with open('./france/fra_death_data.csv') as f:
        for i in f:
            fra.append(i)
    fra.reverse()

    fra.insert(0, n)
    t = "./france/fra_" + str(dd.split('.')[0]) + "_rev" + "." + str(dd.split('.')[1])
    with open(t, "w") as f:
        for i in fra:
            f.write(i)

    fra = []
    with open('./france/fra_hosp_data.csv') as f:
        for i in f:
            fra.append(i)
    fra.reverse()

    fra.insert(0, o)
    t = "./france/fra_" + str(hd.split('.')[0]) + "_rev" + "." + str(hd.split('.')[1])
    with open(t, "w") as f:
        for i in fra:
            f.write(i)

    fra = []
    with open('./france/fra_test_data.csv') as f:
        for i in f:
            fra.append(i)
    fra.reverse()

    fra.insert(0, p)
    t = "./france/fra_" + str(td.split('.')[0]) + "_rev" + "." + str(td.split('.')[1])
    with open(t, "w") as f:
        for i in fra:
            f.write(i)

    fra = []
    with open('./france/fra_vacc_data.csv') as f:
        for i in f:
            fra.append(i)
    fra.reverse()

    fra.insert(0, q)
    t = "./france/fra_" + str(vd.split('.')[0]) + "_rev" + "." + str(vd.split('.')[1])
    with open(t, "w") as f:
        for i in fra:
            f.write(i)

def germany():
    deu = []
    with open('./germany/deu_case_data.csv') as f:
        for i in f:
            deu.append(i)
    deu.reverse()

    deu.insert(0, m)
    t = "./germany/deu_" + str(cd.split('.')[0]) + "_rev" + "." + str(cd.split('.')[1])
    with open(t, "w") as f:
        for i in deu:
            f.write(i)

    deu = []
    with open('./germany/deu_death_data.csv') as f:
        for i in f:
            deu.append(i)
    deu.reverse()

    deu.insert(0, n)
    t = "./germany/deu_" + str(dd.split('.')[0]) + "_rev" + "." + str(dd.split('.')[1])
    with open(t, "w") as f:
        for i in deu:
            f.write(i)

    deu = []
    with open('./germany/deu_hosp_data.csv') as f:
        for i in f:
            deu.append(i)
    deu.reverse()

    deu.insert(0, o)
    t = "./germany/deu_" + str(hd.split('.')[0]) + "_rev" + "." + str(hd.split('.')[1])
    with open(t, "w") as f:
        for i in deu:
            f.write(i)

    deu = []
    with open('./germany/deu_test_data.csv') as f:
        for i in f:
            deu.append(i)
    deu.reverse()

    deu.insert(0, p)
    t = "./germany/deu_" + str(td.split('.')[0]) + "_rev" + "." + str(td.split('.')[1])
    with open(t, "w") as f:
        for i in deu:
            f.write(i)

    deu = []
    with open('./germany/deu_vacc_data.csv') as f:
        for i in f:
            deu.append(i)
    deu.reverse()

    deu.insert(0, q)
    t = "./germany/deu_" + str(vd.split('.')[0]) + "_rev" + "." + str(vd.split('.')[1])
    with open(t, "w") as f:
        for i in deu:
            f.write(i)


def hungary():
    hun = []
    with open('./hungary/hun_case_data.csv') as f:
        for i in f:
            hun.append(i)
    hun.reverse()

    hun.insert(0, m)
    t = "./hungary/hun_" + str(cd.split('.')[0]) + "_rev" + "." + str(cd.split('.')[1])
    with open(t, "w") as f:
        for i in hun:
            f.write(i)

    hun = []
    with open('./hungary/hun_death_data.csv') as f:
        for i in f:
            hun.append(i)
    hun.reverse()

    hun.insert(0, n)
    t = "./hungary/hun_" + str(dd.split('.')[0]) + "_rev" + "." + str(dd.split('.')[1])
    with open(t, "w") as f:
        for i in hun:
            f.write(i)

    hun = []
    with open('./hungary/hun_hosp_data.csv') as f:
        for i in f:
            hun.append(i)
    hun.reverse()

    hun.insert(0, o)
    t = "./hungary/hun_" + str(hd.split('.')[0]) + "_rev" + "." + str(hd.split('.')[1])
    with open(t, "w") as f:
        for i in hun:
            f.write(i)

    hun = []
    with open('./hungary/hun_test_data.csv') as f:
        for i in f:
            hun.append(i)
    hun.reverse()

    hun.insert(0, p)
    t = "./hungary/hun_" + str(td.split('.')[0]) + "_rev" + "." + str(td.split('.')[1])
    with open(t, "w") as f:
        for i in hun:
            f.write(i)

    hun = []
    with open('./hungary/hun_vacc_data.csv') as f:
        for i in f:
            hun.append(i)
    hun.reverse()

    hun.insert(0, q)
    t = "./hungary/hun_" + str(vd.split('.')[0]) + "_rev" + "." + str(vd.split('.')[1])
    with open(t, "w") as f:
        for i in hun:
            f.write(i)

def italy():
    ita = []
    with open('./italy/ita_case_data.csv') as f:
        for i in f:
            ita.append(i)
    ita.reverse()

    ita.insert(0, m)
    t = "./italy/ita_" + str(cd.split('.')[0]) + "_rev" + "." + str(cd.split('.')[1])
    with open(t, "w") as f:
        for i in ita:
            f.write(i)

    ita = []
    with open('./italy/ita_death_data.csv') as f:
        for i in f:
            ita.append(i)
    ita.reverse()

    ita.insert(0, n)
    t = "./italy/ita_" + str(dd.split('.')[0]) + "_rev" + "." + str(dd.split('.')[1])
    with open(t, "w") as f:
        for i in ita:
            f.write(i)

    ita = []
    with open('./italy/ita_hosp_data.csv') as f:
        for i in f:
            ita.append(i)
    ita.reverse()

    ita.insert(0, o)
    t = "./italy/ita_" + str(hd.split('.')[0]) + "_rev" + "." + str(hd.split('.')[1])
    with open(t, "w") as f:
        for i in ita:
            f.write(i)

    ita = []
    with open('./italy/ita_test_data.csv') as f:
        for i in f:
            ita.append(i)
    ita.reverse()

    ita.insert(0, p)
    t = "./italy/ita_" + str(td.split('.')[0]) + "_rev" + "." + str(td.split('.')[1])
    with open(t, "w") as f:
        for i in ita:
            f.write(i)

    ita = []
    with open('./italy/ita_vacc_data.csv') as f:
        for i in f:
            ita.append(i)
    ita.reverse()

    ita.insert(0, q)
    t = "./italy/ita_" + str(vd.split('.')[0]) + "_rev" + "." + str(vd.split('.')[1])
    with open(t, "w") as f:
        for i in ita:
            f.write(i)

def newzealand():
    nza = []
    with open('./newzealand/nza_case_data.csv') as f:
        for i in f:
            nza.append(i)
    nza.reverse()

    nza.insert(0, m)
    t = "./newzealand/nza_" + str(cd.split('.')[0]) + "_rev" + "." + str(cd.split('.')[1])
    with open(t, "w") as f:
        for i in nza:
            f.write(i)

    nza = []
    with open('./newzealand/nza_death_data.csv') as f:
        for i in f:
            nza.append(i)
    nza.reverse()

    nza.insert(0, n)
    t = "./newzealand/nza_" + str(dd.split('.')[0]) + "_rev" + "." + str(dd.split('.')[1])
    with open(t, "w") as f:
        for i in nza:
            f.write(i)

    nza = []
    with open('./newzealand/nza_hosp_data.csv') as f:
        for i in f:
            nza.append(i)
    nza.reverse()

    nza.insert(0, o)
    t = "./newzealand/nza_" + str(hd.split('.')[0]) + "_rev" + "." + str(hd.split('.')[1])
    with open(t, "w") as f:
        for i in nza:
            f.write(i)

    nza = []
    with open('./newzealand/nza_test_data.csv') as f:
        for i in f:
            nza.append(i)
    nza.reverse()

    nza.insert(0, p)
    t = "./newzealand/nza_" + str(td.split('.')[0]) + "_rev" + "." + str(td.split('.')[1])
    with open(t, "w") as f:
        for i in nza:
            f.write(i)

    nza = []
    with open('./newzealand/nza_vacc_data.csv') as f:
        for i in f:
            nza.append(i)
    nza.reverse()

    nza.insert(0, q)
    t = "./newzealand/nza_" + str(vd.split('.')[0]) + "_rev" + "." + str(vd.split('.')[1])
    with open(t, "w") as f:
        for i in nza:
            f.write(i)

def poland():
    pol = []
    with open('./poland/pol_case_data.csv') as f:
        for i in f:
            pol.append(i)
    pol.reverse()

    pol.insert(0, m)
    t = "./poland/pol_" + str(cd.split('.')[0]) + "_rev" + "." + str(cd.split('.')[1])
    with open(t, "w") as f:
        for i in pol:
            f.write(i)

    pol = []
    with open('./poland/pol_death_data.csv') as f:
        for i in f:
            pol.append(i)
    pol.reverse()

    pol.insert(0, n)
    t = "./poland/pol_" + str(dd.split('.')[0]) + "_rev" + "." + str(dd.split('.')[1])
    with open(t, "w") as f:
        for i in pol:
            f.write(i)

    pol = []
    with open('./poland/pol_hosp_data.csv') as f:
        for i in f:
            pol.append(i)
    pol.reverse()

    pol.insert(0, o)
    t = "./poland/pol_" + str(hd.split('.')[0]) + "_rev" + "." + str(hd.split('.')[1])
    with open(t, "w") as f:
        for i in pol:
            f.write(i)

    pol = []
    with open('./poland/pol_test_data.csv') as f:
        for i in f:
            pol.append(i)
    pol.reverse()

    pol.insert(0, p)
    t = "./poland/pol_" + str(td.split('.')[0]) + "_rev" + "." + str(td.split('.')[1])
    with open(t, "w") as f:
        for i in pol:
            f.write(i)

    pol = []
    with open('./poland/pol_vacc_data.csv') as f:
        for i in f:
            pol.append(i)
    pol.reverse()

    pol.insert(0, q)
    t = "./poland/pol_" + str(vd.split('.')[0]) + "_rev" + "." + str(vd.split('.')[1])
    with open(t, "w") as f:
        for i in pol:
            f.write(i)

def portugal():
    por = []
    with open('./portugal/por_case_data.csv') as f:
        for i in f:
            por.append(i)
    por.reverse()

    por.insert(0, m)
    t = "./portugal/por_" + str(cd.split('.')[0]) + "_rev" + "." + str(cd.split('.')[1])
    with open(t, "w") as f:
        for i in por:
            f.write(i)

    por = []
    with open('./portugal/por_death_data.csv') as f:
        for i in f:
            por.append(i)
    por.reverse()

    por.insert(0, n)
    t = "./portugal/por_" + str(dd.split('.')[0]) + "_rev" + "." + str(dd.split('.')[1])
    with open(t, "w") as f:
        for i in por:
            f.write(i)

    por = []
    with open('./portugal/por_hosp_data.csv') as f:
        for i in f:
            por.append(i)
    por.reverse()

    por.insert(0, o)
    t = "./portugal/por_" + str(hd.split('.')[0]) + "_rev" + "." + str(hd.split('.')[1])
    with open(t, "w") as f:
        for i in por:
            f.write(i)

    por = []
    with open('./portugal/por_test_data.csv') as f:
        for i in f:
            por.append(i)
    por.reverse()

    por.insert(0, p)
    t = "./portugal/por_" + str(td.split('.')[0]) + "_rev" + "." + str(td.split('.')[1])
    with open(t, "w") as f:
        for i in por:
            f.write(i)

    por = []
    with open('./portugal/por_vacc_data.csv') as f:
        for i in f:
            por.append(i)
    por.reverse()

    por.insert(0, q)
    t = "./portugal/por_" + str(vd.split('.')[0]) + "_rev" + "." + str(vd.split('.')[1])
    with open(t, "w") as f:
        for i in por:
            f.write(i)

def spain():
    spa = []
    with open('./spain/spa_case_data.csv') as f:
        for i in f:
            spa.append(i)
    spa.reverse()

    spa.insert(0, m)
    t = "./spain/spa_" + str(cd.split('.')[0]) + "_rev" + "." + str(cd.split('.')[1])
    with open(t, "w") as f:
        for i in spa:
            f.write(i)

    spa = []
    with open('./spain/spa_death_data.csv') as f:
        for i in f:
            spa.append(i)
    spa.reverse()

    spa.insert(0, n)
    t = "./spain/spa_" + str(dd.split('.')[0]) + "_rev" + "." + str(dd.split('.')[1])
    with open(t, "w") as f:
        for i in spa:
            f.write(i)

    spa = []
    with open('./spain/spa_hosp_data.csv') as f:
        for i in f:
            spa.append(i)
    spa.reverse()

    spa.insert(0, o)
    t = "./spain/spa_" + str(hd.split('.')[0]) + "_rev" + "." + str(hd.split('.')[1])
    with open(t, "w") as f:
        for i in spa:
            f.write(i)

    spa = []
    with open('./spain/spa_test_data.csv') as f:
        for i in f:
            spa.append(i)
    spa.reverse()

    spa.insert(0, p)
    t = "./spain/spa_" + str(td.split('.')[0]) + "_rev" + "." + str(td.split('.')[1])
    with open(t, "w") as f:
        for i in spa:
            f.write(i)

    spa = []
    with open('./spain/spa_vacc_data.csv') as f:
        for i in f:
            spa.append(i)
    spa.reverse()

    spa.insert(0, q)
    t = "./spain/spa_" + str(vd.split('.')[0]) + "_rev" + "." + str(vd.split('.')[1])
    with open(t, "w") as f:
        for i in spa:
            f.write(i)
            
def main():
    australia()
    austria()
    france()
    germany()
    hungary()
    italy()
    newzealand()
    poland()
    portugal()
    spain()


main()