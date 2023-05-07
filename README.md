# sauce_man
sauce_man is a discord bot to analysis your images in discord channel

## dev

```shell
#setting up python version
pyenv local 3.8.16

#Specify which version of Python virtualenv should use.
pipenv --python 3.8.16

#Spawns a shell within the virtualenv.
pipenv shell

#packages
pipenv install discord.py
pipenv install PyYAML
```

## packages/tips/docs

* [discord.py/intro](https://discordpy.readthedocs.io/en/latest/intro.html)
* [events](https://discordpy.readthedocs.io/en/latest/api.html#event-reference)
    * [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine)
        * [asyncio](https://docs.python.org/3.8/library/asyncio.html)