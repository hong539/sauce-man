# bot

## To-do-list

### working

* uv
```shell
uv pip freeze --project pyproject.toml
#vs
uv pip compile pyproject.toml > requirements.txt
```

* Add 3rd party or implement APIs to fix social media broken prview.
* Add Prometheus metrics
* refactoring
    * ~~move src/** to backend/**~~
    * ~~merge backend/core/settings.py to backend/bot/config.py~~
    ~~* ~/sauce-man$ uv run backend/bot/main.py~~
        ~~* ModuleNotFoundError: No module named 'core'~~
    ~~* ~/sauce-man$ python3 backend/bot/main.py~~
        ~~* ModuleNotFoundError: No module named 'discord'~~
* update Dockerfile
* ~~migrage from pyenv+poetry to uv~~
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
    * ~~search history messages from a specific channel~~
    * find mark messages and store
    * dump history messages from a specific channel
        * calculate the range <= 100 for iterator to append all history to the stored list

### pending

* Container part
    * ~~prepare Dockerfile~~
    * ~~Run with podman~~
    * docekr network DNS resovle error
        * ERROR: failed to solve: docker.io/python:3.11.4-slim-bullseye: failed to do request: Head "https://registry-1.docker.io/v2/library/python/manifests/3.11.4-slim-bullseye": EOF

### done

* ~~separate function load_config from class or not? (Hint: Like django settings.py)~~
* ~~postgresql db init~~