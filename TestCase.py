#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import Final
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
    @classmethod
    def setUpClass(self):
        self.config = Newconfigparser()
        self.config.read('condition.ini')
        self.setting_config = configparser.ConfigParser()
        self.setting_config.read('common_setting.ini')
        self.TestSuiteName = "Order Flow"
        self.runId, self.testIds = AddTestRunAndTest(self.TestSuiteName)

    def CheckTotalStatus(self,resultList):
        for index in resultList:
            if index == False:
                return 5
        return 1   

    def TranslateForStatus(self,resultList):
        FinalResult = []
        for index in resultList:
            if index == True:
                FinalResult.append(1)
            elif index == False:
                FinalResult.append(5)
            else:
                FinalResult.append(index)
        return FinalResult

    def test_OrderFlow4Hours(self):
        totalstatus = True
        resultList = []
        #Step 1 : Get_auth_portal
        response, status = get_auth_portal(self.setting_config)
        resultList.extend((status,response))
        #Step 2 : Get_auth_admin
        response, status = get_auth_admin(self.setting_config)
        resultList.extend((status,response))
        #Step 3 : Get_auth
        response, status = get_auth_admin(self.setting_config)
        resultList.extend((status,response))
        #Step 4 : Create an order
        status_code, OrderID, status = create_order(self.config,'4Hours',totalstatus)
        resultList.extend((status, OrderID))
        #Step 5 : Assign to DA
        status_code, TripID, status = AssignToDeliveryAgent(OrderID,totalstatus)
        resultList.extend((status, TripID))
        #Step 6 : Enroute
        status_code, response, status = enroute(TripID,totalstatus)
        resultList.extend((status, response))
        #Step 7 : Dropoff Process
        status_code, response, status = dropoff_process(TripID,totalstatus)
        resultList.extend((status, response))
        status_code, response, status = dropoff(TripID,totalstatus)
        resultList.extend((status, response))
        #Step 8 : Payrolls
        status = 3
        response = ""
        resultList.extend((status, response))
        #Final : Update result to testrail
        totalstatus = self.CheckTotalStatus(resultList)
        resultList = self.TranslateForStatus(resultList)
        AddResultByStep(totalstatus,self.testIds,"4Hours",resultList,self.runId)

    def test_OrderFlowExchange(self):
        totalstatus = True
        resultList = []
        #Step 1 : Get_auth_portal
        response, status = get_auth_portal(self.setting_config)
        resultList.extend((status,response))
        #Step 2 : Get_auth_admin
        response, status = get_auth_admin(self.setting_config)
        resultList.extend((status,response))
        #Step 3 : Get_auth
        response, status = get_auth_admin(self.setting_config)
        resultList.extend((status,response))
        #Step 4 : Create an order
        status_code, OrderID, status = create_order(self.config,'Exchange',totalstatus)
        resultList.extend((status, OrderID))
        #Step 5 : Assign to DA
        status_code, TripID, status = AssignToDeliveryAgent(OrderID,totalstatus)
        resultList.extend((status, TripID))
        #Step 6 : Enroute
        status_code, response, status = enroute(TripID,totalstatus)
        resultList.extend((status, response))
        #Step 7 : Dropoff Process
        status_code, response, status = dropoff_process(TripID,totalstatus)
        resultList.extend((status, response))
        status_code, response, status = dropoff(TripID,totalstatus)
        resultList.extend((status, response))
        #Step 8 : Payrolls
        status = 3
        response = ""
        resultList.extend((status, response))
        #Final : Update result to testrail
        totalstatus = self.CheckTotalStatus(resultList)
        resultList = self.TranslateForStatus(resultList)
        AddResultByStep(totalstatus,self.testIds,"Exchange",resultList,self.runId)

    def test_OrderFlowExpress(self):
        totalstatus = True
        resultList = []
        #Step 1 : Get_auth_portal
        response, status = get_auth_portal(self.setting_config)
        resultList.extend((status,response))
        #Step 2 : Get_auth_admin
        response, status = get_auth_admin(self.setting_config)
        resultList.extend((status,response))
        #Step 3 : Get_auth
        response, status = get_auth_admin(self.setting_config)
        resultList.extend((status,response))
        #Step 4 : Create an order
        status_code, OrderID, status = create_order(self.config,'Express',totalstatus)
        resultList.extend((status, OrderID))
        #Step 5 : Assign to DA
        status_code, TripID, status = AssignToDeliveryAgent(OrderID,totalstatus)
        resultList.extend((status, TripID))
        #Step 6 : Enroute
        status_code, response, status = enroute(TripID,totalstatus)
        resultList.extend((status, response))
        #Step 7 : Dropoff Process
        status_code, response, status = dropoff_process(TripID,totalstatus)
        resultList.extend((status, response))
        status_code, response, status = dropoff(TripID,totalstatus)
        resultList.extend((status, response))
        #Step 8 : Payrolls
        status = 3
        response = ""
        resultList.extend((status, response))
        #Final : Update result to testrail
        totalstatus = self.CheckTotalStatus(resultList)
        resultList = self.TranslateForStatus(resultList)
        AddResultByStep(totalstatus,self.testIds,"Express",resultList,self.runId)

    def test_OrderFlowNextDay(self):
        totalstatus = True
        resultList = []
        #Step 1 : Get_auth_portal
        response, status = get_auth_portal(self.setting_config)
        resultList.extend((status,response))
        #Step 2 : Get_auth_admin
        response, status = get_auth_admin(self.setting_config)
        resultList.extend((status,response))
        #Step 3 : Get_auth
        response, status = get_auth_admin(self.setting_config)
        resultList.extend((status,response))
        #Step 4 : Create an order
        status_code, OrderID, status = create_order(self.config,'NextDay',totalstatus)
        resultList.extend((status, OrderID))
        #Step 5 : Assign to DA
        status_code, TripID, status = AssignToDeliveryAgent(OrderID,totalstatus)
        resultList.extend((status, TripID))
        #Step 6 : Enroute
        status_code, response, status = enroute(TripID,totalstatus)
        resultList.extend((status, response))
        #Step 7 : Dropoff Process
        status_code, response, status = dropoff_process(TripID,totalstatus)
        resultList.extend((status, response))
        status_code, response, status = dropoff(TripID,totalstatus)
        resultList.extend((status, response))
        #Step 8 : Payrolls
        status = 3
        response = ""
        resultList.extend((status, response))
        #Final : Update result to testrail
        totalstatus = self.CheckTotalStatus(resultList)
        resultList = self.TranslateForStatus(resultList)
        AddResultByStep(totalstatus,self.testIds,"NextDay",resultList,self.runId)

    def test_OrderFlowSameDay(self):
        totalstatus = True
        resultList = []
        #Step 1 : Get_auth_portal
        response, status = get_auth_portal(self.setting_config)
        resultList.extend((status,response))
        #Step 2 : Get_auth_admin
        response, status = get_auth_admin(self.setting_config)
        resultList.extend((status,response))
        #Step 3 : Get_auth
        response, status = get_auth_admin(self.setting_config)
        resultList.extend((status,response))
        #Step 4 : Create an order
        status_code, OrderID, status = create_order(self.config,'SameDay',totalstatus)
        resultList.extend((status, OrderID))
        #Step 5 : Assign to DA
        status_code, TripID, status = AssignToDeliveryAgent(OrderID,totalstatus)
        resultList.extend((status, TripID))
        #Step 6 : Enroute
        status_code, response, status = enroute(TripID,totalstatus)
        resultList.extend((status, response))
        #Step 7 : Dropoff Process
        status_code, response, status = dropoff_process(TripID,totalstatus)
        resultList.extend((status, response))
        status_code, response, status = dropoff(TripID,totalstatus)
        resultList.extend((status, response))
        #Step 8 : Payrolls
        status = 3
        response = ""
        resultList.extend((status, response))
        #Final : Update result to testrail
        totalstatus = self.CheckTotalStatus(resultList)
        resultList = self.TranslateForStatus(resultList)
        AddResultByStep(totalstatus,self.testIds,"SameDay",resultList,self.runId)

if __name__ == '__main__':
    unittest.main()  
