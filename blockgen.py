from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
import time
import main

adressList = []
adressListAmount = []
recievingAddress = ""

class iconBlockGen():

    transactionAddress = ""

    def startLoop(self, _instance, object):

        icon_service = IconService(HTTPProvider("https://ctz.solidwallet.io/api/v3"))
        newBlock = []

        while True:
            time.sleep(0.5)

            block = icon_service.get_block("latest")['confirmed_transaction_list']
            if newBlock != block:
                newBlock = block
                endIndex = len(block)
                for i in range(endIndex):
                    if (block[i]['to']) == self.transactionAddress:
                        adressList.append(newBlock[i]['from'])
                        adressListAmount.append(int(newBlock[i]['value'])/1000000000000000000)
                        _instance.addPayment(_instance, main.listIndex, newBlock[i]['from'], int(newBlock[i]['value']) / 1000000000000000000)
                        main.listIndex += 1