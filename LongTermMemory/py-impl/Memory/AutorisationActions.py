


class AutorisationActions():

    def login(self, loginobject):
        if self.checkHash(loginobject.password):
            pass
        else:
            raise Exception

    def changePassword(self, username, password):
        if self.checkHash(password):
            pass
        else:
            raise Exception

    def checkHash(self, password):
        return True