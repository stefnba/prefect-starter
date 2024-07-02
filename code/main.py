from flows.hello import hello_world
from prefect import serve


def main():

    hello_world_deploy = hello_world.deploy(name="hello_world")

    serve(hello_world_deploy)  # type: ignore


if __name__ == "__main__":
    main()
