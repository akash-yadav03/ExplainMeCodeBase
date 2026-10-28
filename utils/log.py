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

def used_in():
    pass

def log_content(file):
    with open("log.txt","a") as log_file:
        with open(file,"r") as f:
            filename = str(file)
            log_file.write(f"   {100*"-"}\n")
            log_file.write(f"   {"TYPE":<15} |  {"NAME":<15} |  {"ORIGIN":<30} |  {"USED BY":<15}\n")
            log_file.write(f"   {100*"-"}\n")
            for line in f:
                if "=" in line:
                    words = line.split("=")
                    log_file.write(f"   {"Variable":<15} |  {words[0].strip():<15} |  {filename:<30} |  {used_in(words[0])}\n")
                    log_file.write(f"   {100*"-"}\n")
                elif line.strip().startswith("def"):
                    fun_name = line.split("def ")[1].split("(")[0] 
                    log_file.write(f"   {"Function":<15} |  {fun_name.strip():<15} |  {filename:<30} |  {used_in(fun_name)}\n")
                    log_file.write(f"   {100*"-"}\n")
                elif line.strip().startswith("class"):
                    class_name = line.split("class ")[1].split("(")[0].split(":")[0].strip()
                    log_file.write(f"   {"Class":<15} |  {class_name.strip():<15} |  {filename:<30} |  {used_in(class_name)}\n")
                    log_file.write(f"   {100*"-"}\n")

            log_file.write("\n")
