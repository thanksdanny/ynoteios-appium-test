
import os

class AppiumServer():

    def startServer(self):
        #start appium
        startcmd='appium --no-reset'
        self.getCmd(startcmd)

    def stopServer(self):
        #stop appium
        stopcmd='sudo killall node'
        self.getCmd(stopcmd)

    def restartServer(self):
        self.stopServer()
        self.startServer()

    def getCmd(self,command):
        #create a cmd
        os.system(command)

if __name__=='__main__':

    o=AppiumServer()
    o.startServer()