from promptflow import tool
import json


@tool
def convert_to_dict(
    application_form_risk: str,
    certificate_of_all_matters_risk: str,
    web_page_risk: str,
    distance_risk: str
    ):
    try:
        application_form_risk = json.loads(application_form_risk)
        certificate_of_all_matters_risk = json.loads(certificate_of_all_matters_risk)
        web_page_risk = json.loads(web_page_risk)
        distance_risk = json.loads(distance_risk)
        
        results={}
        results['Risk'] = application_form_risk['Risk'] \
            + certificate_of_all_matters_risk['Risk'] \
            + web_page_risk['Risk'] \
            + distance_risk['Risk']

        results['reason'] = application_form_risk['reason'] \
            + certificate_of_all_matters_risk['reason'] \
            + web_page_risk['reason'] \
            + distance_risk['reason']
        return results

    except Exception as e:
        print("input is not valid, error: {}".format(e))
        return {
            "Risk": "None",
            "reason": "None"
        }
