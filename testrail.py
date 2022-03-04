from testrail_api import TestRailAPI

def testrail_connect():
    api = TestRailAPI('https://stillcolor1029.testrail.io/', 'gerben.chen@pickupp.io', 'Ss0128210')
    return api

def testrail_update_result(case_id,status_code,result):
    api = testrail_connect()
    api.results.add_result_for_case(
            case_id=case_id,
            status_id=status_code,
            comment=result,
            version="1"
        )