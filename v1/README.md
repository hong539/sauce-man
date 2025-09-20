# v1

v1: include a bot and an api impl in python3.

* sauce-man is services which includes:
    * bot: a discord bot to make discord app bertter to:        
        * Fix Links Previews
        * reverse image search
        * query user messages
        and also:
        * prometheus metrics
        * opentelemetry instrumentation
    * api: a FastAPI to interact with bot

## quick-start

```shell
#bot
cd bot/
uv run main.py

#api
cd api/
# need to update
# uv run --python=python3.10 backend/manage.py runapi 0.0.0.0 8000 --uv
```

## misc

### Reference implementation

* [github.com/practical-tutorials/project-based-learning?tab=readme-ov-file#python](https://github.com/practical-tutorials/project-based-learning?tab=readme-ov-file#python)
* [modelcontextprotocol.io/introduction](https://modelcontextprotocol.io/introduction)
* [ermiana](https://github.com/canaria3406/ermiana/tree/master)
    * A Discord bot that fixes sites with broken preview by providing more detailed images and webpage content. Supports multiple popular sites in Taiwan, East Asia. 
* [bckbot](https://github.com/hker9527/bckbot)
    * A discord bot powered by discord.js 
* [how-do-i-apply-environment-variables-to-python-interactive](https://stackoverflow.com/questions/73858371/how-do-i-apply-environment-variables-to-python-interactive)
* [pprint](https://docs.python.org/3.11/library/pprint.html)
* [os.environ](https://docs.python.org/3/library/os.html#os.environ)
* [sqlalchemy/postgresql](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html)
* [pandas](https://pandas.pydata.org/)
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
* packaging
    * [packaging.python.org/en/latest/tutorials/packaging-projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
    * [packaging.python.org/en/latest/guides/writing-pyproject-toml/#a-full-example](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#a-full-example)
* setuptools
    * [setuptools.pypa.io/en/latest/userguide/quickstart.html](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)