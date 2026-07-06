import os
import json
import sys
from pathlib import Path
import random
import re

TABLES_FOLDER = os.path.join("static", "tables")

def find_table(title:str, race:str, clazz:str):
    rtn = {}
    # closest match is title-class-race.json
    # next is title-class.json
    # next is title-race.json
    # next is title.json
    checks = [f"{title}-{clazz}-{race}.json", f"{title}-{clazz}.json", f"{title}-{race}.json", f"{title}.json"]
    for c in checks:
        fn = os.path.join(TABLES_FOLDER,c)
        pfn = Path(fn)
        if pfn.is_file():
            print(f"found table file {fn}")
            with open(fn, 'r', encoding='utf-8') as file:
                data_dict = json.load(file)
                return data_dict
    print(f"found no matches for {title} {race} {clazz}")
    return rtn



def roll_dice(notation):
    """
    Roll dice using D&D notation like '2d8+1', '4d6', '1d20-2'.
    
    Returns a dict with the total and individual rolls.
    """
    match = re.fullmatch(r'(\d+)d(\d+)([+-]\d+)?', notation.strip().lower())
    if not match:
        raise ValueError(f"Invalid dice notation: {notation!r}")
    
    num_dice, num_sides, modifier = match.groups()
    num_dice = int(num_dice)
    num_sides = int(num_sides)
    modifier = int(modifier) if modifier else 0
    
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    total = sum(rolls) + modifier
    
    rtn = {
        "total": total,
        "rolls": rolls,
        "modifier": modifier,
        "notation": notation
    }
    print(f"my roll {rtn['total']}")
    return rtn


def roll_table(tableName:str, race:str, clazz:str):
    rtn = ""
    table = table = find_table(tableName,race,clazz)
    if table != {} :
        mydice = roll_dice(table['roll'])
        myroll = mydice["total"]
        for c in table['choices']:
            if c['from'] <= myroll and c['to'] >= myroll:
                rtn = f"{table['title']} {c['text']}"
    return rtn



def build_back_story(race:str, clazz:str):
    rtn = {}
    rtn['title'] = f"The back story of your {race} {clazz}"
    rtn['parents'] = roll_table("Parents",race,clazz)
    rtn['birthplace'] = roll_table("Birthplace",race,clazz)
        

    return rtn