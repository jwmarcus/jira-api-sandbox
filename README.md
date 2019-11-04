# Connecting to Atlassian Jira APIs

Handy reading:

- https://confluence.atlassian.com/cloud/api-tokens-938839638.html
- https://id.atlassian.com/manage/api-tokens
- https://developer.atlassian.com/cloud/jira/platform/jira-rest-api-basic-authentication/

To run:

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

export JIRA_TOKEN=my-token
export JIRA_EMAIL=me@example.com

python3 main.py
```
