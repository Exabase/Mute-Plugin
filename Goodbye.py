class Goodbye():

    def getName(self):
        return 'Goodbye'

    def onEnable(self, parser):
        print "Loaded Goodbye Plugin"

    def handleRequirements(self, input):
        response = 0
        if (input.find("bye") != -1 or input.find("goodbye") != -1):
            response += 20
        return response

    def generateResponse(self, input):
        return {"response":"goodbye"}

    def onDisable(self):
        print "Disabling Goodbye"
