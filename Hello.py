class Hello():

    def getName(self):
        return 'Hello'

    def onEnable(self, parser):
        print "Loaded Hello Plugin"

    def handleRequirements(self, input):
        response = 0
        if (input.find("hi") != -1 or input.find("hello") != -1):
            response += 20
        return response

    def generateResponse(self, input):
        return {"response":"hello"}

    def onDisable(self):
        print "Disabling Hello"
