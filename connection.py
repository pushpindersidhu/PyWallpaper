import socket

def isConnected():
    try:
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            sock.close
        return True
    except OSError:
        pass
    return False

if __name__=='__main__':
    import time
    start = time.perf_counter()
    print(isConnected())
    finish = time.perf_counter()
    print(f'Finished in { finish - start } secs.')