import click

@click.command()
@click.argument("logfile", type=click.File("r"))
def read_log(logfile):
    """Reads log and print all lines."""
    for line in logfile:
        print(line.strip())

if __name__ == "__main__":
    read_log()