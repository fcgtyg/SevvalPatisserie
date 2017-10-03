#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect("MainDB.db")
data = conn.cursor()
def createOrOpenTable():
    try:
        data.execute("CREATE TABLE AnaKayitlar "
                                  "(tarih DATE PRIMARY KEY, "
                                  "toplam_gelir DOUBLE, "
                                  "toplam_gider DOUBLE, "
                                  "toplam_kar DOUBLE,"
                                  "devreden_kasa DOUBLE,"
                                  "gunluk_mevcut_kasa DOUBLE,"
                                  "toplam_gunluk_kasa DOUBLE,"
                                  "ana_kasa_gider DOUBLE,"
                                  "devreden_toplam_kasa DOUBLE,"
                                  "cikan_urunler VARCHAR(10000),"
                                  "cikan_urun_toplam DOUBLE,"
                                  "anakasa_urunler VARCHAR(10000),"
                                  "anakasa_urun_toplam DOUBLE)")
    except sqlite3.OperationalError:
        pass
    return conn, data

def pushNewDate(date):

    try:
        data.execute("insert into AnaKayitlar "
                 "(tarih,"
                 "toplam_gelir, "
                 "toplam_gider, "
                 "toplam_kar, "
                 "devreden_kasa, "
                 "gunluk_mevcut_kasa, "
                 "toplam_gunluk_kasa, "
                 "ana_kasa_gider, "
                 "devreden_toplam_kasa, "
                 "cikan_urun_toplam, "
                 "anakasa_urun_toplam) "
                 "Values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                 ,(date, 0,0,0,0,0,0,0,0,0,0))
        conn.commit()
    except sqlite3.IntegrityError:
        print "Tarih kaydı bulundu."

def updateData(date, totalIncome=0.0, totalOutcome=0.0, pastVault=0.0, todayVault=0.0, mainVaultOutcome=0.0, dailyOutProducts="",
               dailyOutProductsTotal=0.0, mainVaultProducts="", mainVaultProductsTotal=0.0):
    totalRevenue = totalIncome - totalOutcome
    totalVault = pastVault + todayVault
    totalPastVault=totalVault-mainVaultOutcome

    print date
    data.execute("update AnaKayitlar set "
                 "toplam_gelir=?, "
                 "toplam_gider=?, "
                 "toplam_kar=?, "
                 "devreden_kasa=?, "
                 "gunluk_mevcut_kasa=?, "
                 "toplam_gunluk_kasa=?, "
                 "ana_kasa_gider=?, "
                 "devreden_toplam_kasa=?, "
                 "cikan_urunler=?, "
                 "cikan_urun_toplam=?, "
                 "anakasa_urunler=?, "
                 "anakasa_urun_toplam=? "
                 "where tarih=?"
                 ,(totalIncome, totalOutcome, totalRevenue, pastVault, todayVault, totalVault, mainVaultOutcome,
                   totalPastVault, dailyOutProducts, dailyOutProductsTotal, mainVaultProducts, mainVaultProductsTotal,
                   date))

    conn.commit()

    pass

def loadData(date):
    load = data.execute("select * from AnaKayitlar where tarih=%s" %date).fetchall()
    try:
        return load[0]
    except IndexError:
        return None