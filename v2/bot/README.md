# v2/bot

* A Discord bot written in Rust.
* bot is a discord bot to make discord app bertter to:
    * advanced search features for who want make some records or fix the broken preview from some outside URLs.
    * Fix Links Previews

## To-do-list

* Refactoring v1/bot to v2/bot
    * slash commands
    * event handling
* Discord Twitter Link Handler with mutli 3rd-pary APIs

### quick start

* cargo
```shell
cd bot
export DISCORD_TOKEN=your-discord-token
cargo run
```

### Reference

* Rust
    * [github.com/hong539/rust-101](https://github.com/hong539/rust-101)
    * [github.com/serenity-rs/serenity](https://github.com/serenity-rs/serenity)
* 3rd-party for Fix twitter/x.com broken preview metadata
    * [github.com/canaria3406/ermiana/blob/master/src/regex/handleTwitterRegexV2.js](https://github.com/canaria3406/ermiana/blob/master/src/regex/handleTwitterRegexV2.js)
    * [github.com/dylanpdx/BetterTwitFix](https://github.com/dylanpdx/BetterTwitFix)
    * [github.com/FxEmbed/FxEmbed](https://github.com/FxEmbed/FxEmbed)
    * [github.com/Wikidepia/InstaFix](https://github.com/Wikidepia/InstaFix)
