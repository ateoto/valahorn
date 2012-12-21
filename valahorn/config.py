import os
import json

DATABASES = {'mysql' : 'mysql://%(username)s:%(password)s@%(host)s/%(database)s',
            'postgresql' : 'postgresql://%(username)s:%(password)s@%(host)s/%(database)s',
            'sqlite' : 'sqlite:///%(database)s'
}

class NNTPServerConfig(object):
    def __init__(self, address = None, username = None, password = None, use_ssl = False):
        self.address = address
        self.username = username
        self.password = password
        self.use_ssl = use_ssl
        
    def __repr__(self):
        return "<NNTPServerConfig('%s','%s')>" % (self.address, self.username)

class DatabaseConfig(object):
    def __init__(self, type = None, name = None, username = None, password = None, host = "localhost"):
        if type in DATABASES.keys():
            self.connect_string = DATABASES[type]

        self.name = name
        self.username = username
        self.password = password
        self.host = host
        self.connect_string = self.connect_string % {"username" : self.username,
                                                    "password" : self.password,
                                                    "host": self.host,
                                                    "database" : self.name}

class Config(object):
    
    def __init__(self, path = os.path.join(os.getenv('XDG_CONFIG_HOME'), 
                                                        'valahorn', 
                                                        'valahorn.conf')):
        self.path = path

        if not os.path.exists(self.path):
            pass # TODO: Run Setup

        else:
            raw_config = json.load(open(self.path))
            self.nntp_server = NNTPServerConfig(raw_config['nntp_server']['address'],
                                                raw_config['nntp_server']['username'],
                                                raw_config['nntp_server']['password'],
                                                raw_config['nntp_server']['use_ssl'])
            self.database = DatabaseConfig(raw_config['database']['type'],
                                            raw_config['database']['name'],
                                            raw_config['database']['username'],
                                            raw_config['database']['password'])
