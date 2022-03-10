#!/usr/bin/python
# -*- coding: UTF-8 -*-
from testrail_api import TestRailAPI
import configparser
import json

testrail_config = configparser.ConfigParser()
testrail_config.read('testrail.ini')
api = TestRailAPI('https://pickupp.testrail.io/', 'gerben.chen@pickupp.io', 'Ss0128210#')
#list(testrail_config[TestSuiteName]['case_ids'])
def AddTestRunAndTest(TestSuiteName):
    runId = api.runs.add_run(project_id=2,suite_id=1,name=TestSuiteName,include_all=False,case_ids=testrail_config[TestSuiteName]['case_ids'].split(','))
    testIds = api.tests.get_tests(run_id=runId["id"]) 
    return runId["id"],testIds

def CheckTestIDWithCase(testIds,CaseName):
    for i in range(len(testIds['tests'])):
        if CaseName in testIds['tests'][i]['title']:
            return testIds['tests'][i]['id'], testIds['tests'][i]['custom_steps_separated']

def CountContentForResult(resultList,StepCounts):
    result = []
    for i in range(len(StepCounts)):
        body = {
            "content":"Step%s" % (i+1),
            "actual":"%s" % resultList[((i*2)+1)],
            "status_id":"%s" % resultList[((i*2)+2)]
            }
        result.append(body)
    return result

def AddResultByStep(totalstatus,testIds,CaseName,resultList,runId):
    #print (testId)
    testId, StepCounts = CheckTestIDWithCase(testIds,CaseName)
    result = CountContentForResult(resultList,StepCounts)
    api.results.add_results(
    run_id=runId,
    results = [
        {"test_id": testId,
            "status_id": totalstatus,
            "custom_step_results": result
        }]
    )

