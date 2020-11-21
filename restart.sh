# kill current process before loading code
echo "Killing all current PM2 processes"
pm2 kill
echo "Fetching and resetting from origin/master"
sudo git fetch --all
sudo git reset --hard origin/master
echo "Launching Memebot process on PM2"
pm2 start main.py --interpreter python3