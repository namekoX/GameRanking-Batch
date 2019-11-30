import sys
import os
from configparser import ConfigParser
import click
import logging

app_home = os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)) , ".." ))
sys.path.append(os.path.join(app_home,"lib"))

from get_rank import GetRank
from db_util import DbUtil

@click.command()
def cmd():
    prog_name = os.path.splitext(os.path.basename(__file__))[0]
    config = ConfigParser()
    conf_path = os.path.join(app_home,"conf", prog_name + ".conf")
    config.read(conf_path)

    log_format = logging.Formatter("%(asctime)s [%(levelname)8s] %(message)s")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(log_format)
    logger.addHandler(stdout_handler)
    file_handler = logging.FileHandler(os.path.join(app_home,"log", prog_name + ".log"), "a+")
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    try:
        logger.info("start")
        getRank = GetRank()
        getRank.getDmm18()
        getRank.getDmm()
        getRank.getNijiyome()
        getRank.getGooglePlay()
        getRank.getYahoo()

        logger.info("end")

    except Exception as e:
        logger.exception(e)
        sys.exit(1)

if __name__ == '__main__':
    cmd()