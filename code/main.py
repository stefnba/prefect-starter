from flows.hello import hello_world
from prefect import serve


def main():

    hello_world_deploy = hello_world.to_deployment(name="hello_world", interval=60)

    serve(hello_world_deploy)  # type: ignore


if __name__ == "__main__":
    main()
