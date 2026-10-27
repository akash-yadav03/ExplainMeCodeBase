from functools import wraps

def logger_file(func):
    @wraps(func)
    def wrapper(file):
        with open("log.txt", "a") as log_file:
            log_file.write(f"{file}\r\n")
        return func(file)
    return wrapper

@logger_file
def log(file):
    print(file)

def log_content(file):
    with open("log.txt","a") as log_file:
        with open(file,"r") as f:
            for index , line in enumerate(f,start = 1):
                log_file.write(f"   {index}    {line}\r\n")
