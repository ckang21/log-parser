import click

@click.command()
@click.argument("logfile", type=click.File("r"))
def read_log(logfile):
    """Reads log and print only ERRORS."""
    total_errors = 0
    for line in logfile:
        line = line.strip() # Clean it first
        if "ERROR" in line:
            print(line)
            total_errors += 1 # Increment if we find one

    print(f"\nTotal Errors is: {total_errors}")

if __name__ == "__main__":
    read_log()