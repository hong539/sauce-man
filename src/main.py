from bot.client import MyClient
import bot.commands

def main():

    client = MyClient()
    bot.commands.set_client(client)
    bot.commands.register_commands()
    client.run(token= client.token)

if __name__ == "__main__":
    main()