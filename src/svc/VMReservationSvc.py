class VMReservationSvc:
    def __init__(self):
        self.hostedVM = 0

    def hostVMs(self, count):
        self.hostedVM = count

    def getAvailableVM(self):
        pass

    def assignVMtoUser(self):
        pass

    def checkOut(self):
        ipaddress = ''
        return ipaddress

    def checkIn(self, ipaddress):
        pass

    def cleanupIncomingVM(self):
        # if state is pendingCleanup - perform cleanup
        ipaddress = ''
        return ipaddress

    def addVM(self, ipaddress):
        pass

    def addVMToAvailablePool(self):
        ipadress = self.cleanupIncomingVM()
        self.addVM(ipadress)

    def getUsageStats(self):
        pass