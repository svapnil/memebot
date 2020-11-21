# kill current process before loading code
pm2 kill
sudo git fetch --all
sudo git reset --hard origin/master
pm2 start main.py --interpreter python3