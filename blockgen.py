from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
import time
import main

adressList = []
adressListAmount = []

class iconBlockGen():


    def getGuiInstance(self, _instance):
        print("adding payment now")

    def startLoop(self, _instance, object):

        icon_service = IconService(HTTPProvider("https://ctz.solidwallet.io/api/v3"))
        newBlock = []

        while True:
            time.sleep(2)

            block = icon_service.get_block("latest")['confirmed_transaction_list']
            if newBlock != block:
                newBlock = block
                print(block)
                print("we got a new block!!")
                if (block[0]['to']) == "hx6601d72a45f173681a9122b74352d46cf8d00e87":
                    print("main address found, Value conversion: ", int(newBlock[0]['value']/1000000000000000000))
#                    main.recieverListAdress.append(newBlock[0]['from'])
#                    main.recieverListAmount.append(int(newBlock[0]['value'])/1000000000000000000)
                    adressList.append(newBlock[0]['from'])
                    adressListAmount.append(int(newBlock[0]['value'])/1000000000000000000)
                    _instance.addPayment(main.listIndex, newBlock[0]['from'], int(newBlock[0]['value']) / 1000000000000000000)
                    main.listIndex += 1
#                    _instance.addPayment()