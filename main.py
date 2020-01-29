from urllib3 import PoolManager
import os, json, base64
from datetime import datetime

jira_token = os.getenv("JIRA_TOKEN")
jira_email = os.getenv("JIRA_EMAIL")
instance_name = "jwmarcus"


base_api = f"https://{instance_name}.atlassian.net/rest/api/3"
base64_token = str(base64.b64encode(f"{jira_email}:{jira_token}".encode()), "utf-8")
headers = {"Authorization": f"Basic {base64_token}", "Content-Type": "application/json"}
http = PoolManager()


def get_issue(issue_name="HW-1"):
    resource_api = f"{base_api}/issue/{issue_name}"

    res = http.request("GET", resource_api, headers=headers,)

    return json.loads(res.data.decode("utf-8"))


def create_issue():
    resource_api = f"{base_api}/issue"
    payload = json.dumps(
        {
            "fields": {
                "summary": f"The time is {datetime.now()}",
                "project": {"key": "HW"},
                "issuetype": {"name": "Task"},
            }
        }
    )

    res = http.request("POST", resource_api, body=payload, headers=headers,)

    return json.loads(res.data.decode("utf-8"))


if __name__ == "__main__":
    # json_res = get_issue("HW-1")
    json_res = create_issue()

    print(json.dumps(json_res, indent=2))
