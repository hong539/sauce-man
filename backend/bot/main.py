from client import MyClient

def main():

    client = MyClient(load_commands=True)
    client.run(token= client.token)

if __name__ == "__main__":
    main()