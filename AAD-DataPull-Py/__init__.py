import datetime
import logging

import azure.functions as func
from azure.cli.core import get_default_cli

def az_cli (args_str):
    args = args_str.split()
    cli = get_default_cli()
    cli.invoke(args)
    if cli.result.result:
        return cli.result.result
    elif cli.result.error:
        raise cli.result.error
    return True


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    logging.info("Starting the function")
    response = az_cli("login --identity --allow-no-subscriptions")
    logging.info(f'az login --identity --allow-no-subscriptions: ${response}')

    logging.info("Getting groups from aad")
    response = az_cli("ad group list")
    logging.info(f'az ad group list: ${response}')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
