from testrail_api import TestRailAPI

def testrail_connect():
    api = TestRailAPI('https://pickupp.testrail.io/', 'gerben.chen@pickupp.io', 'Ss0128210')
    return api

def testrail_update_result(case_id,status_code,result):
    api = testrail_connect()
    api.results.add_result_for_case(
            case_id=case_id,
            status_id=status_code,
            comment=result,
            version="1"
        )
'''
api = TestRailAPI('https://pickupp.testrail.io', 'gerben.chen@pickupp.io', 'Ss0128210#')
my_test_run = api.runs.add_run(project_id=2,
    suite_id=1,
    name="Order Flow",
    include_all=True,)
print (my_test_run)

api.results.add_result_for_case(
    run_id=my_test_run["id"],
    case_id=57,
    status_id=1,
    comment="Pass",
    version="1"
)

api.results.add_results_for_cases(
    run_id = my_test_run['id'],
    results = [
        57,1,"Pass"]
)
'''
