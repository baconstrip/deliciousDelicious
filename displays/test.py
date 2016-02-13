import Display 

class Test(Display):
    name = "test"

    def getLayout():
        testLabel = Label()
        testLabel.text = "delicious"
        return [testLabel,]
