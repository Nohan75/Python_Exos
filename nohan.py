import sys
import logging

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        logging.info("L'année %d est bissextile.", year)
        return True
    else:
        logging.info("L'année %d n'est pas bissextile.", year)
        return False


def main():
    if len(sys.argv) == 2:
        year = int(sys.argv[1])
        is_leap_year(year)
    else:
        logging.error("Usage: %s <year>", sys.argv[0])
        sys.exit(1)

if __name__ == "__main__":
    logging.basicConfig(filename="log.log", level=logging.INFO, format='%(asctime)s [ %(filename)s - l%(lineno)d : %(funcName)s ] - %(message)s')
    main()