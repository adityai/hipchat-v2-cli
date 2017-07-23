#!/bin/bash
curl -sS -H 'Content-type: application/json' -H "Authorization: Bearer $HIPCHAT_TOKEN" -d @message.json https://api.hipchat.com/v2/room/3076684/notification
