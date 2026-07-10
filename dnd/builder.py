import os
import json
import sys
from pathlib import Path
import random
import re


class Builder:

    def __init__(self):
        self.TABLES_FOLDER = os.path.join("static", "tables")
        self.vars = {}

    def get_manifest(self):
        rtn = []
        mtxtf = os.path.join(self.TABLES_FOLDER,"manifest.txt")
        with open(mtxtf, 'r') as f:
            return [line.rstrip('\n\r') for line in f]
        return rtn

    def find_table(self,title:str, race:str, clazz:str):
        rtn = {}
        # closest match is title-class-race.json
        # next is title-class.json
        # next is title-race.json
        # next is title.json
        checks = [f"{title}-{clazz}-{race}.json", f"{title}-{clazz}.json", f"{title}-{race}.json", f"{title}.json"]
        for c in checks:
            fn = os.path.join(self.TABLES_FOLDER,c)
            pfn = Path(fn)
            if pfn.is_file():
                #print(f"found table file {fn}")
                with open(fn, 'r', encoding='utf-8') as file:
                    data_dict = json.load(file)
                    return data_dict
        #print(f"found no matches for {title} {race} {clazz}")
        return rtn
    
    def is_die_roll(self,s):
        rtn = False
        if type(s) is str:
            match = re.fullmatch(r'(\d+)d(\d+)([+-]\d+)?', s.strip().lower())
            if match != None:
                rtn = True
        return rtn

    def set_vars(self, vars:dict):
        for key, value in vars.items():
            if type(value) is str:
                # check if it's a roll
                #match = re.fullmatch(r'(\d+)d(\d+)([+-]\d+)?', value.strip().lower())
                if self.is_die_roll(value):
                    value = self.roll_dice(value)["total"]
            #print(f"vars[{key} = {value}]")
            self.vars[key] = value

    def roll_dice(self,notation:str):
      
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
        #print(f"my roll {rtn['total']}")
        return rtn

    def randrom_select_from_list(self,mylist:list):
        mll = len(mylist)
        idx = random.randrange(mll)
        return mylist[idx]

    def process_text(self,entry:dict):
        def replace_match(match):
            keyword = match.group(1)
            if keyword in entry:
                value = entry[keyword]
                #if isinstance(value, str) and re.fullmatch(r'\d*d\d+([+-]\d+)?', value):
                if isinstance(value,str) and self.is_die_roll(value):
                    value = self.roll_dice(value)['total']
                elif type(value) is list:
                    value = self.randrom_select_from_list(value)
                return str(value)
            return match.group(0)
        pattern = r'<(\w+)>'
        return re.sub(pattern, replace_match, entry["text"])

    def get_unique_value(self, table):
        unique = False
        if "unique" in table:
            unique = table['unique'].strip().lower() == "true"
        return unique
    
    def get_loop_value(self, table):
        rtn = 1
        if "loop" in table:
            rtn = table['loop']
            if type(rtn) is str:
                rtn = self.vars[rtn]
        return rtn
    def get_choice_hash(self,c):
        rtn = f"{c['from']}{c['to']}"
        return rtn
    
    def get_choice(self,table,myroll):
        for c in table['choices']:
            if c['from'] <= myroll and c['to'] >= myroll:
                return c
        return None

    
    def roll_table(self,tableName:str, params:dict, override = None):
        #print(f"roll_table({tableName}, {params['race']}, {params['clazz']})")
        rtn = {"title":"","text":"","dice":{}}
        table = self.find_table(tableName,params['race'],params['clazz'])
        
        if table != {} :
            table_mod_value = 0
            previous = []
            
            if "table_mod" in table:
                table_mod = table['table_mod']
                if table_mod in self.vars:
                    table_mod_value = self.vars[table_mod]
            txt = ""
            loop = self.get_loop_value(table)
            unique = self.get_unique_value(table)
            #print(f"looping {loop} {unique}")
            if override != None:
                if self.is_die_roll(override):
                    loop = self.roll_dice(override)
                else:
                    loop = int(override)
                #print(f"Override changes loop to {loop}")
            
            i = 0
            while i < loop:
                mydice = self.roll_dice(table['roll'])
                myroll = mydice["total"] + table_mod_value
                mydice["table_mod_value"] = table_mod_value

                #debugging
                
                #print(f"tableName={tableName} i={i}")
                #if tableName == "SupernaturalEvent" and i == 0:
                #    myroll = 12
                #if tableName == "LifeEvent" and i == 0:
                #    myroll = 82
                

                c = self.get_choice(table,myroll)
                if c != None:
                    chash = self.get_choice_hash(c)
                    if unique == False or chash not in previous:
                        ptxt = self.process_text(c)
                        if "vars" in c:
                            self.set_vars(c['vars'])
                        if "goto" in c:
                            o = None
                            if "override" in c:
                                o = int(c['override'])
                            tbl = c['goto']
                            gtr = self.roll_table(tbl,params,o)
                            ptxt = f"{ptxt} {gtr['title']} {gtr['text']}"
                        txt = f"{txt}{ptxt}"
                        i = i + 1
                        previous.append(chash)
            rtn = {"title":table['title'],"text":txt,"dice":mydice}
        return rtn



    def build_back_story(self,params:dict):
        rtn = {}
        rtn['title'] = f"The back story of your {params['race']} {params['clazz']}"
        self.vars["CHA"] = int(params['cha'])
        self.vars["WIS"] = int(params['wis'])
        manifest = self.get_manifest()
        for m in manifest:
            rtn[m] = self.roll_table(m,params)
            
        rtn['vars'] = self.vars
        return rtn