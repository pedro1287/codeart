import os
import json
import time
import io
import telegram

class JsonDatabase(object):
    def __init__(self,path='newdb'):
        self.path = f'{path}.jdb'
        self.items = {}

    def check_create(self):
        exist = os.path.isfile(self.path)
        if not exist:
            db = open(str(self.path), 'w')
            db.write('')
            db.close()

    def save(self):
        dbfile = open(self.path, 'w')
        i = 0
        for user in self.items:
            separator = ''
            if i < len(self.items) - 1:
                separator = '\n'
            dbfile.write(user + '=' + str(self.items[user]) + separator)
            i += 1
        dbfile.close()



    def create_user(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': '---',
                     'moodle_repo_id': 4,
                     'moodle_user': '---',
                     'moodle_password': '---',
                     'isadmin': 0,
                     'zips': 100,
                     'uploadtype':'evidence',
                     'proxy':'',
                     'tokenize':0,
                     'preview':0,
                     'brodcast':0}

    def create_admin(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': '---',
                     'moodle_repo_id': 4,
                     'moodle_user': '---',
                     'moodle_password': '---',
                     'isadmin': 1,
                     'zips': 100,
                     'uploadtype':'evidence',
                     'proxy':'',
                     'tokenize':0,
                     'preview':0,
                     'brodcast':0}
                     
    def create_user_eduvirtual(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://eduvirtual.uho.edu.cu/',
                     'moodle_repo_id': 3,
                     'moodle_user': '-', #user aqui
                     'moodle_password': '-', #pass aqui
                     'isadmin': 0,
                     'zips': 1999,
                     'uploadtype':'draft',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}

    def create_user_cursos(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://cursos.uo.edu.cu/',
                     'moodle_repo_id': 4,
                     'moodle_user': '-', #user aqui
                     'moodle_password': '-', #pass aqui
                     'isadmin': 0,
                     'zips': 99,
                     'uploadtype':'calendar',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}
                     
    def create_user_eva(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://eva.uo.edu.cu/',
                     'moodle_repo_id': 4,
                     'moodle_user': '-', #user aqui
                     'moodle_password': '-', #pass aqui
                     'isadmin': 0,
                     'zips': 99,
                     'uploadtype':'draft',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}
                     
    def create_user_aulacened(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://aulacened.uci.cu/',
                     'moodle_repo_id': 5,
                     'moodle_user': '-', #user aqui
                     'moodle_password': '-', #pass aqui
                     'isadmin': 0,
                     'zips': 249,
                     'uploadtype':'draft',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}

    def create_user_uclv(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://moodle.uclv.edu.cu/',
                     'moodle_repo_id': 4,
                     'moodle_user': '-', #user aqui
                     'moodle_password': '-', #pass aqui
                     'isadmin': 0,
                     'zips': 350,
                     'uploadtype':'calendar',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}

    def create_user_evea(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://evea.uh.cu/',
                     'moodle_repo_id': 4,
                     'moodle_user': '-', #user aqui
                     'moodle_password': '-', #pass aqui
                     'isadmin': 0,
                     'zips': 250,
                     'uploadtype':'blog',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}

    def create_user_aula_sld(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://aulavirtual.sld.cu/',
                     'moodle_repo_id': 3,
                     'moodle_user': '-', #user aqui
                     'moodle_password': '-', #pass aqui
                     'isadmin': 0,
                     'zips': 5,
                     'uploadtype':'calendar',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}

    def create_user_aula_art(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'http://www.aulavirtual.art.sld.cu/',
                     'moodle_repo_id': 5,
                     'moodle_user': '-', #user aqui
                     'moodle_password': '-', #pass aqui
                     'isadmin': 0,
                     'zips': 99,
                     'uploadtype':'calendar',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}

    def create_user_aula_grm(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://aula.ucm.grm.sld.cu/',
                     'moodle_repo_id': 5,
                     'moodle_user': '-', #user aqui
                     'moodle_password': '-', #pass aqui
                     'isadmin': 0,
                     'zips': 19,
                     'uploadtype':'draft',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}

    def create_user_reduc(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://moodle.reduc.edu.cu/',
                     'moodle_repo_id': 5,
                     'moodle_user': '-', #user aqui
                     'moodle_password': '-', #pass aqui
                     'isadmin': 0,
                     'zips': 20,
                     'uploadtype':'draft',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}

    def create_user_aula_scu(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://www.aula.scu.sld.cu/',
                     'moodle_repo_id': 4,
                     'moodle_user': '-', #user aqui
                     'moodle_password': '-', #pass aqui
                     'isadmin': 0,
                     'zips': 49,
                     'uploadtype':'calendar',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}

    def create_user_aula_hlg(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://aulavirtual.hlg.sld.cu/',
                     'moodle_repo_id': 5,
                     'moodle_user': '-', #user aqui
                     'moodle_password': '-', #pass aqui
                     'isadmin': 0,
                     'zips': 10,
                     'uploadtype':'calendar',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}

    def create_user_posgrado(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://posgrado.unica.cu/',
                     'moodle_repo_id': 3,
                     'moodle_user': '-', #user aqui
                     'moodle_password': '-', #pass aqui
                     'isadmin': 0,
                     'zips': 49,
                     'uploadtype':'calendar',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}


    def create_user_reset(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': '---',
                     'moodle_repo_id': 4,
                     'moodle_user': '---',
                     'moodle_password': '---',
                     'isadmin': 0,
                     'zips': 100,
                     'uploadtype':'evidence',
                     'proxy':'',
                     'tokenize':0,
                     'preview':0,
                     'brodcast':0}

    def remove(self,name):
        try:
            del self.items[name]
        except:pass

    def get_user(self,name):
        try:
            return self.items[name]
        except:
            return None

    def save_data_user(self,user, data):
        self.items[user] = data

    def is_admin(self,user):
        User = self.get_user(user)
        if User:
            return User['isadmin'] == 1
        return False

    def preview(self,user):
        User = self.get_user(user)
        if User:
            return User['preview'] == 1
        return False

    def load(self):
        dbfile = open(self.path, 'r')
        lines = dbfile.read().split('\n')
        dbfile.close()
        for lin in lines:
            if lin == '': continue
            tokens = lin.split('=')
            user = tokens[0]
            data = json.loads(str(tokens[1]).replace("'", '"'))
            self.items[user] = data
