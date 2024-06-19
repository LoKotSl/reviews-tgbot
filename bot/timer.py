import time

timers = {}

def timeout(key, seconds):
    global timers

    initial_time = timers[key] if key in timers else None
    if initial_time and time.time() - initial_time < seconds:
        return True
    timers[key] = time.time()

    return False
