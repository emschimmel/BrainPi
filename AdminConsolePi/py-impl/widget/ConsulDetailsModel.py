
class ConsulDetailsModel(object):

    name = ''
    service_id = ''
    service_name = ''
    service_adres = ''
    service_port = 0
    checks = []

    def __init__(self):
        self.name = ''
        self.service_id = ''
        self.service_name = ''
        self.service_adres = ''
        self.service_port = 0
        self.checks = []


class ConsulChecksModel(object):
    check_id = ''
    name = ''
    status = ''
    output = ''
    service_id = ''
    service_name = ''
    statuscolor = [0, 1, 0.3, 0.2]

    def __init__(self):
        self.check_id = ''
        self.name = ''
        self.status = ''
        self.output = ''
        self.service_id = ''
        self.service_name = ''
        self.statuscolor = [0, 1, 0.3, 0.2]

    def status_color(self, status):
        if status == 'warning':
            self.statuscolor = [1, 0.6, 0, 0.2]
        elif status != 'passing':
            self.statuscolor = [1, 0, 0, 0.2]

