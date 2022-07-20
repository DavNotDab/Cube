
import sqlite3 as sql


def get_algorithm(origin, end, table):
    '''Returns the algorithm that the cube has to execute to bring a piece from origin position to end position'''
    conex = sql.connect('cube.db')
    cursor = conex.cursor()
    try:
        querry = f'SELECT algorithm FROM {table} ' \
                 f'WHERE origin = "{str(origin)}" AND end = "{str(end)}";'
        cursor.execute(querry)
        algorithm = cursor.fetchone()

        return algorithm[0] if algorithm else '0'

    except sql.OperationalError:
        print('TABLE NOT FOUND, TRY AGAIN')
    finally:
        conex.close()


def get_LL_algorithm(position, table):
    '''Returns the algorithm that the cube has to execute to orientate the last layer'''
    conex = sql.connect('cube.db')
    cursor = conex.cursor()
    try:
        querry = f'SELECT algorithm FROM {table} ' \
                 f'WHERE position = "{position}";'
        cursor.execute(querry)
        algorithm = cursor.fetchone()

        return algorithm[0] if algorithm else '0'

    except sql.OperationalError:
        print('TABLE NOT FOUND, TRY AGAIN')
    finally:
        conex.close()



if __name__ == '__main__':
    get_algorithm((0, -1, 1), (-1, -1, 0), 'white_cross')       # Just for testing


