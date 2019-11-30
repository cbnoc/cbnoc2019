#!/bin/bash
# 参考: https://blog.dshimizu.jp/article/1133

# * メディアタイプで設定した引数を受け取って、その内容をSlackに通知するスクリプト *

# Slack incoming web-hook URL
SLACK_WEBHOOKSURL=''

# テスト用
# SLACK_WEBHOOKSURL=''


# Slack UserName
SLACK_USERNAME='Zabbix(bot)'


# "Send to" for Zabbix User Media Setting 
NOTIFY_CHANNEL="$1"

# "Default subject" for Action Operations Setting
ALERT_SUBJECT="$2"

# "Default message" for Action Operations Setting
ALERT_MESSAGE="$3"

if [ "${ALERT_SUBJECT%%:*}" == 'Resolved' ]; then
        ICON=':smile:'
        COLOR="good"
elif [ "${ALERT_SUBJECT%%:*}" == 'Problem' ]; then
        ICON=':skull:'
        COLOR="danger"
else
        ICON=':skull:'
        COLOR="danger"
fi

# Create JSON payload
PAYLOAD="payload={
    \"channel\": \"${NOTIFY_CHANNEL//\"/\\\"}\",
    \"username\": \"${SLACK_USERNAME//\"/\\\"}\",
    \"icon_emoji\": \"${ICON}\",
    \"attachments\": [
        {
            \"color\": \"${COLOR}\",
            \"text\": \"${ALERT_MESSAGE//\"/\\\"}\"
        }
    ]
}"

# Send it as a POST request to the Slack incoming webhooks URL
curl -m 5 --data-urlencode "${PAYLOAD}" $SLACK_WEBHOOKSURL
