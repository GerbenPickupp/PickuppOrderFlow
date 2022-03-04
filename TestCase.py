import unittest
from api_query import*
from db_query import*
from testrail import*
import configparser
class Newconfigparser(configparser.ConfigParser):
    def __init__(self,defaults=None):
        configparser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

class Order_flow(unittest.TestCase):
    def setUp(self):
        self.config = Newconfigparser()
        self.config.read('condition.ini')

    def test_CreateOrder_DA_Accept(self):
        #create an order
        OrderID = create_order(self.config)
        #assign da
        TripID = deliveryAgent(OrderID)
        #Finish delivery
        enroute(TripID)
        #Check the job status in AP
        dropoff(TripID)
        #Get payment

        #Update to testrail
        #testrail_update_result(case_id,status_code,result)


if __name__ == '__main__':
    unittest.main()  
