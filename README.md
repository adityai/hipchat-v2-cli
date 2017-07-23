echo "export HIPCHAT_TOKEN=<YOUR_HIPCHAT_API_TOKEN>" > hipchat.sh
echo "export HIPCHAT_ROOM_ID=<YOUR_HIPCHAT_ROOM_ID>" >> hipchat.sh
echo "export HIPCHAT_URL=<YOUR_HIPCHAT_URL>" >> hipchat.sh
echo "export HIPCHAT_URI=$HIPCHAT_URL/v2/room/$HIPCHAT_ROOM_ID/notification" >> hipchat.sh

chmod 755 hipchat.sh
cp hipchat.sh ~/.hipchat
source ~/.hipchat
./sendNotification.sh
source venv/bin/activate
python sendNotification.py

