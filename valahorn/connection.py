import nntplib

import config

class Connection(object):
    
    def __init__(self):
        self.nntp_server = config.Config().nntp_server
        if self.nntp_server.use_ssl:
            self.connection = nntplib.NNTP_SSL(self.nntp_server.address,
                                                user = self.nntp_server.username,
                                                password = self.nntp_server.password)
        else:
            self.connection = nntplib.NNTP(self.nntp_server.addres,
                                            user = self.nntp_server.username,
                                            password = self.nntp_server.password)
