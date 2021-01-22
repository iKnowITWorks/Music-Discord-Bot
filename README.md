<img src="https://github.com/Darkempire78/Music-Discord-Bot/blob/main/Banner.png"/>

![](https://img.shields.io/codefactor/grade/github/Darkempire78/Music-Discord-Bot?style=for-the-badge) ![](https://img.shields.io/github/repo-size/Darkempire78/Music-Discord-Bot?style=for-the-badge) ![](https://img.shields.io/badge/SOURCERY-ENABLED-green?style=for-the-badge) <a href="https://discord.gg/FxXQwKvmUY"><img src="https://img.shields.io/discord/798492323860185108?color=%237289DA&label=DISCORD&style=for-the-badge"></a>

**INVITE :** https://discord.com/oauth2/authorize?client_id=796749718217555978&scope=bot&permissions=2147483647

# Music Discord Bot

A Discord bot with more than 20+ commands which allows to play music on your server efficiently. Supports Youtube, Spotify, Deezer and Soundcloud links.

## Installation

* Install all dependencies : ``pip install -r requirements.txt``.
* Download [FFmpeg](https://ffmpeg.org/download.html).
* Put your Discord token that can be found in the [Discord's developers portal](https://discord.com/developers/applications) inside `configuration example.json`.
* **(OPTIONAL : Spotify links support)** Add also your Spotify token and ID.
* Rename it to `configuration.json`.

Finally, host the bot and invite it to your own server.


## Features

* Play music from YouTube
* Support links from YouTube, Spotify, Deezer and Soudcloud 
* Support YouTube lives
* Support playlists from Spotify, Deezer, Soundcloud and YouTube.
* Many commands
* Complex queue commands


## Preview

<img src="https://github.com/Darkempire78/Music-Discord-Bot/blob/main/capture1.png" width="600"/>

<img src="https://github.com/Darkempire78/Music-Discord-Bot/blob/main/capture2.png" width="600"/>


## Commands

```
?play <Url/Query> : Search on youtube and play the music.
?search <Query> : Search a song on youtube.
?nowplaying : Display data about the current song.
?join : Add the bot to your voice channel.
?leave : Remove the bot of your voice channel.
?pause : Pause the current song.
?resume : Resume the current song.
?volume <0-100> : Change the bot's volume.
?queue : Display the queue.
?shuffle : Shuffle the queue.
?move <IndexFrom> <IndexTo> : Move a song in the queue.
?remove <Index> : Remove the song with its index.
?removedupes : Remove all duplicates song from the queue.
?leavecleanup : Remove absent user's songs from the queue.
?clear : Clear the queue.
?replay : Replay the current song.
?reload : Reload the current song.
?loop : Enable or disable the loop mode.

?stats : Display the bot's stats.
?support : Give a link to join the support server.
?invite : Give a link to invite the bot.
?help : Display the help.
```


## Soon
### Command
* Lyrics
* Forward / Rewind
* Skipto
* Loopqueue
* Playfile
* Blindtest

### Other
* DJ system
* Custom playlist system


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Support
<a href="https://discord.gg/FxXQwKvmUY">
  <img src = "https://discordapp.com/api/guilds/798492323860185108/widget.png?style=banner2">
</a>


## License

This project is under [GPLv3](https://github.com/Darkempire78/Raid-Protect-Discord-Bot/blob/master/LICENSE).


# Advice :

You should use [Discord Tools](https://marketplace.visualstudio.com/items?itemName=Darkempire78.discord-tools) to code your Discord bots on Visual Studio Code easier.
Works for Python (Discord.py), Javascript (Discord.js) and Java (JDA). Generate template bot and code (snippets).
- **Download :** https://marketplace.visualstudio.com/items?itemName=Darkempire78.discord-tools
- **Repository :** https://github.com/Darkempire78/Discord-Tools
