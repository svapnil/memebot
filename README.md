# Memebot

A discord bot that plays memes in the chat based off messages that happen in the discord server.

Some of these are inside jokes, others are memes that exist on tiktok, etc. 

## Adding a Meme

Memes can be added to the `meme_config.py` file on the `REGEX_TO_MEME` variable.

## Dependencies

These programs are necessary to do audio encoding that we display in Discord:
`opus`
`ffmpeg`

Follow this tutorial to get discord *and it's related voice commands* based off this documentation:
https://pypi.org/project/discord.py/


You will need two environment variables:

`DISCORD_BOT_TOKEN`

`RIOT_API_KEY`

### Mac Guide:

`python3 -m pip install -U "discord.py[voice]"`

`brew install opus`

`brew install ffmpeg`

`brew install youtube-dl`

`pip3 install cassiopeia`


If certificate error: 
Navigate to you Python folder and run this command:
`./Install Certificates.command`

### Launching on AMAZON-EC2 Linux Guide: 

`sudo python3 -m pip install -U "discord.py[voice]"`

`sudo yum install opus`

Follow Instructions here to install `ffmpeg`:

https://maskaravivek.medium.com/how-to-install-ffmpeg-on-ec2-running-amazon-linux-451e4a8e2694

Install `youtube-dl`:

sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl

`pip3 install cassiopeia`

`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash`

`. ~/.nvm/nvm.sh`

`nvm install node`

`npm install pm2@latest -g`

`pm2 start main.py -interprete python3`



