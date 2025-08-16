# bot

* bot is a discord bot to make discord app bertter to:
    * advanced search features for who want make some records or fix the broken preview from some outside URLs.
    * Fix Links Previews

## To-do-list

### working

* uv
```shell
uv pip freeze --project pyproject.toml
#output a requirements.txt
uv pip compile pyproject.toml > requirements.txt

#dev with uv
uv run main.py
```

* Add 3rd party or implement APIs to fix social media broken prview.
* Add Prometheus metrics
* refactoring dir layout?
* update Dockerfile
* test discord.py
* ~~find a better and safe way to set env~~
    * pydantic-settings
* implement event handling
    * ~~Discord Twitter Link Handler<br>~~
        ✅ Detect Twitter links in messages<br>
        ✅ Extract Tweet ID from the URL<br>
        ✅ Fetch tweet data using fxtwitter API (fallback to vxtwitter API)<br>
        ✅ Generate a Discord Embed containing tweet details<br>
        ✅ Send tweet media (images/videos) separately<br>
        ✅ Provide a backup link if API calls fail<br>
        ✅ Suppress Discord’s default Twitter preview<br>
* implement channel app commands
    * find mark messages and store
    * dump history messages from a specific channel
        * calculate the range <= 100 for iterator to append all history to the stored list

### others

* [github.com/dylanpdx/BetterTwitFix/tree/main](https://github.com/dylanpdx/BetterTwitFix/tree/main)