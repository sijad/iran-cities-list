#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# see: https://en.wikipedia.org/wiki/ISO_3166-2:IR
PROVINCE_MAP = {
    u'آذربایجان شرقی': 1,
    u'آذربایجان غربی': 2,
    u'اردبیل': 3,
    u'اصفهان': 4,
    u'ایلام': 5,
    u'بوشهر': 6,
    u'تهران': 7,
    u'چهار محال و بختیاری': 8,
    u'خوزستان': 10,
    u'زنجان': 11,
    u'سمنان': 12,
    u'سیستان و بلوچستان': 13,
    u'فارس': 14,
    u'کرمان': 15,
    u'کردستان': 16,
    u'کرمانشاه': 17,
    u'کهگیلویه و بویراحمد': 18,
    u'گیلان': 19,
    u'لرستان': 20,
    u'مازندران': 21,
    u'مرکزی': 22,
    u'هرمزگان': 23,
    u'همدان': 24,
    u'یزد': 25,
    u'قم': 26,
    u'گلستان': 27,
    u'قزوین': 28,
    u'خراسان جنوبی': 29,
    u'خراسان رضوی': 30,
    u'خراسان شمالی': 31,
    u'البرز': 32,
}

def get_province_id(name):
    """return province id by its name"""
    if name in PROVINCE_MAP:
        return PROVINCE_MAP[name]
    else:
        return 0


with open('./iran/dist/iran.json') as opened:
    iran = json.load(opened)

data = {}

for city in iran:
    pid = get_province_id(city['province_name']);
    if pid > 0:
        if not pid in data.keys():
            data[pid] = []
        data[pid].append(city['city_name'])

for pid in data.keys():
    with open('./dist/' + str(pid) + '.json', 'w', encoding='utf8') as out:
        json.dump(data[pid], out, ensure_ascii=False)
