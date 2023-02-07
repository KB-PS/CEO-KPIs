# CEO KPIs

## About
The application has been designed for the Keboola Empower conference (March 2023). 
It connects to a Keboola bucket and reads a table. 

Table is split into multiple widgets, each of which tracks its own metric. The metric
is then compared against the target. 

## Keboola dependency
The data is read from https://connection.north-europe.azure.keboola.com/admin/projects/10708/storage/in.c-empower_kpis

## Notifications
### Slack
Slack notification is performed using an orchestration in Keboola (https://connection.north-europe.azure.keboola.com/admin/projects/10708/flows/33397273)

### Jira
Jira notification is sent directly from streamlit. New issue is then created under the TEST-Streamlit project (https://keboola.atlassian.net/jira/software/projects/STR/boards/210)

