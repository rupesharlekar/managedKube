class User:
    def __init__(self, name):
        self.name = name

    def checkOut(self):
        ipaddress = ''
        return ipaddress

    def checkIn(self, ipaddress):
        pass

    def queryRequiredVM(self):
        # retry logic till VM is available
        available = True
        if available:
            self.checkOut()
