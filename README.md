echo "export HIPCHAT_TOKEN=<YOUR_HIPCHAT_API_TOKEN>" > hipchat.sh
echo "export HIPCHAT_ROOM_ID=<YOUR_HIPCHAT_ROOM_ID>" >> hipchat.sh
echo "export HIPCHAT_URL=<YOUR_HIPCHAT_URL>" >> hipchat.sh
chmod 755 hipchat.sh
./hipchat.sh

