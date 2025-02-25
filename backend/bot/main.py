from client import MyClient
import commands

def main():

    client = MyClient()
    commands.set_client(client)
    commands.register_commands()
    client.run(token= client.token)

if __name__ == "__main__":
    main()