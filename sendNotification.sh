#!/bin/bash
curl -sS -H 'Content-type: application/json' -H "Authorization: Bearer $HIPCHAT_TOKEN" -d @message.json $HIPCHAT_URL/v2/room/$HIPCHAT_ROOM_ID/notification
