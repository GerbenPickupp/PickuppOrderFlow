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

    def result_appened(self,resultList,status_code,response):
        resultJson = {}
        return resultList

    def test_OrderFlow4Hours(self):
        status = True
        resultList = []
        #create an order
        status_code, OrderID, status = create_order(self.config,'4Hours',status)
        print (OrderID)
        resultList = self.result_appened(resultList, status_code, OrderID)
        print ('#assign DA')
        status_code, TripID, status = AssignToDeliveryAgent(OrderID,status)
        resultList = self.result_appened(resultList, status_code, TripID)
        print ('Finish delivery')
        status_code, response, status = enroute(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        #Check the job status in AP
        status_code, response, status = dropoff_process(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        status_code, response, status = dropoff(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        #Get payment

        #Update to testrail
        #testrail_update_result(case_id,status_code,result)

    def test_OrderFlowExchange(self):
        status = True
        resultList = []
        #create an order
        status_code, OrderID, status = create_order(self.config,'Exchange',status)
        resultList = self.result_appened(resultList, status_code, OrderID)
        print ('#assign da')
        status_code, TripID, status = AssignToDeliveryAgent(OrderID,status)
        resultList = self.result_appened(resultList, status_code, TripID)
        print ('Finish delivery')
        status_code, response, status = enroute(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        #Check the job status in AP
        status_code, response, status = dropoff_process(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        status_code, response, status = dropoff(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        #Get payment

        #Update to testrail
        #testrail_update_result(case_id,status_code,result)

    def test_OrderFlowExpress(self):
        status = True
        resultList = []
        #create an order
        status_code, OrderID, status = create_order(self.config,'Express',status)
        resultList = self.result_appened(resultList, status_code, OrderID)
        print ('#assign da')
        status_code, TripID, status = AssignToDeliveryAgent(OrderID,status)
        resultList = self.result_appened(resultList, status_code, TripID)
        print ('Finish delivery')
        status_code, response, status = enroute(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        #Check the job status in AP
        status_code, response, status = dropoff_process(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        status_code, response, status = dropoff(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        #Get payment

        #Update to testrail
        #testrail_update_result(case_id,status_code,result)

    def test_OrderFlowNextDay(self):
        status = True
        resultList = []
        #create an order
        status_code, OrderID, status = create_order(self.config,'NextDay',status)
        resultList = self.result_appened(resultList, status_code, OrderID)
        print ('#assign da')
        status_code, TripID, status = AssignToDeliveryAgent(OrderID,status)
        resultList = self.result_appened(resultList, status_code, TripID)
        print ('Finish delivery')
        status_code, response, status = enroute(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        #Check the job status in AP
        status_code, response, status = dropoff_process(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        status_code, response, status = dropoff(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        #Get payment

        #Update to testrail
        #testrail_update_result(case_id,status_code,result)

    def test_OrderFlowSameDay(self):
        status = True
        resultList = []
        #create an order
        status_code, OrderID, status = create_order(self.config,'SameDay',status)
        resultList = self.result_appened(resultList, status_code, OrderID)
        print ('#assign da')
        status_code, TripID, status = AssignToDeliveryAgent(OrderID,status)
        resultList = self.result_appened(resultList, status_code, TripID)
        print ('Finish delivery')
        status_code, response, status = enroute(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        #Check the job status in AP
        status_code, response, status = dropoff_process(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        status_code, response, status = dropoff(TripID,status)
        resultList = self.result_appened(resultList, status_code, response)
        #Get payment

        #Update to testrail
        #testrail_update_result(case_id,status_code,result)

if __name__ == '__main__':
    unittest.main()  
