import click
import re

@click.command()
@click.argument("logfile", type=click.File("r"))
@click.option("--output", type=click.Path(writable=True), default="errors.log", help="File to save errors")
def read_log(logfile, output):
    """Reads log and saves errors to a different file."""
    total_errors = 0
    found_errors = []
    for line in logfile:
        line = line.strip() # Clean it first
        if "ERROR" in line:
            # Need the timestamp so we will use regex to get it [YYYY-MM-DD HH:MM:SS]
            timestamp_match = re.match(r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]", line)
            timestamp = timestamp_match.group(1) if timestamp_match else "UNKNOWN TIME"

            # Format the log entry with the extracted time
            formatted_error = f"{timestamp} - {line}"
            print(formatted_error)  
            found_errors.append(formatted_error)  
            total_errors += 1  

    if found_errors:    #If we have anything we will make the file
        with open(output, "w") as f:
            for error in found_errors:
                f.write(error + "\n")
        print(f"\nErrors saved to {output}")

    print(f"\nTotal Errors is: {total_errors}")

if __name__ == "__main__":
    read_log()