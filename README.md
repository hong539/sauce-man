# sauce_man

sauce_man is a discord bot to wrapper the search feature for who want make some records.

## To-do-list

* test discord.py
* ~~separate function load_config from class or not? (Hint: Like django settings.py)~~
* make app_commands
    * search history messages from a specific channel    
    * save history messages from a specific channel

## quick-start

```shell
#setting up python version
pyenv local 3.11.4

#Specify which version of Python virtualenv should use.
pipenv --python 3.11.4

#Spawns a shell within the virtualenv.
pipenv shell

#packages
pipenv install discord.py
pipenv install PyYAML

#run this bot
cd src/
python3 main.py
```

## misc

* [decorator](https://docs.python.org/3/glossary.html#term-decorator)
* [await fetch_message](https://discordpy.readthedocs.io/en/latest/api.html#discord.TextChannel.fetch_message)
* [read_message_history](https://discordpy.readthedocs.io/en/latest/api.html?highlight=history#discord.Permissions.read_message_history)
* [async for ... in history](https://discordpy.readthedocs.io/en/latest/api.html?highlight=history#discord.User.history)
* [discord.py/examples/](https://github.com/Rapptz/discord.py/tree/master/examples)
* [How to retrieve previous messages with discord.py](https://stackoverflow.com/questions/64995479/how-to-retrieve-previous-messages-with-discord-py)
* [How could I grab all chat messages in a specific channel in a discord server using discord.py?](https://stackoverflow.com/questions/64211658/how-could-i-grab-all-chat-messages-in-a-specific-channel-in-a-discord-server-usi)
* [Community Resources](https://discord.com/developers/docs/topics/community-resources#community-resources)
* [discord.com/developers/docs/getting-started](https://discord.com/developers/docs/getting-started)
* [Discord bot that automatically download images from a channel.](https://www.reddit.com/r/Discord_Bots/comments/pdz8kp/discord_bot_that_automatically_download_images/)
    * [d-logger.py](https://github.com/therealOri/d-logger/blob/main/d-logger.py)
* [discord.py/intro](https://discordpy.readthedocs.io/en/latest/intro.html)
* [events](https://discordpy.readthedocs.io/en/latest/api.html#event-reference)
    * [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine)
        * [asyncio](https://docs.python.org/3.8/library/asyncio.html)

## Important!!!

== We're Using GitHub Under Protest ==

This project is currently hosted on GitHub.  This is not ideal; GitHub is a
proprietary, trade-secret system that is not Free and Open Souce Software
(FOSS).  We are deeply concerned about using a proprietary system like GitHub
to develop our FOSS project.  We have an
[open {bug ticket, mailing list thread, etc.} ](INSERT_LINK) where the
project contributors are actively discussing how we can move away from GitHub
in the long term.  We urge you to read about the
[Give up GitHub](https://GiveUpGitHub.org) campaign from
[the Software Freedom Conservancy](https://sfconservancy.org) to understand
some of the reasons why GitHub is not a good place to host FOSS projects.

If you are a contributor who personally has already quit using GitHub, please
[check this resource](INSERT_LINK) for how to send us contributions without
using GitHub directly.

Any use of this project's code by GitHub Copilot, past or present, is done
without our permission.  We do not consent to GitHub's use of this project's
code in Copilot.

![Logo of the GiveUpGitHub campaign](https://sfconservancy.org/img/GiveUpGitHub.png)