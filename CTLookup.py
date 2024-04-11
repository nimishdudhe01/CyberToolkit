from sqlalchemy import create_engine, text

def reverse_lookup(hash_value):
    # Create engine and session
    engine = create_engine('sqlite:///hashes.sqlite')
    conn = engine.connect()

    if len(hash_value) == 32:
        hashes = ['md4', 'md5']
        result = conn.execute(text("SELECT string FROM hashes WHERE {} = :hash_value1 OR {} = :hash_value2".format(hashes[0], hashes[1])), {'hash_value1': hash_value, 'hash_value2': hash_value})
    elif len(hash_value) == 40:
        hashes = ['rmd160', 'sha1']
        result = conn.execute(text("SELECT string FROM hashes WHERE {} = :hash_value1 OR {} = :hash_value2".format(hashes[0], hashes[1])), {'hash_value1': hash_value, 'hash_value2': hash_value})
    elif len(hash_value) == 64:
        hashes = ['sha256']
        result = conn.execute(text("SELECT string FROM hashes WHERE {} = :hash_value".format(hashes[0])), {'hash_value': hash_value})
    elif len(hash_value) == 128:
        hashes = ['sha512']
        result = conn.execute(text("SELECT string FROM hashes WHERE {} = :hash_value".format(hashes[0])), {'hash_value': hash_value})

    row = result.fetchone()

    # Close the connection
    conn.close()

    # Return the result string or None if not found
    return row[0] if row else None