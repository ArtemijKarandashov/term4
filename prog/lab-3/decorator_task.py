from custom_exceptions import JsonDecoratorNonValidPath
import sqlite3
import functools
import sys
import datetime
import warnings
import json
import os

_warn_skips = (os.path.dirname(__file__),)

def trace(func=None, *, handle=sys.stdout):

    if func is None:
        return lambda func: trace(func, handle=handle)
    
    @functools.wraps(func)

    def default_inner(*args, **kwargs):
        handle.write(f"[{datetime.datetime.now()}] func_name : {func.__name__}, args : {args}, kwargs : {kwargs}\n")
    
    def _generate_default_json(filename):
         with open(f"{filename}", "w") as file:
              json.dump({"func_calls":[]}, file, indent= 4)

    def json_inner(*args, **kwargs):
        nonlocal handle
        file_type = handle.rpartition(".")[-1]

        #No directory check because :D 

        #File type check
        if not file_type == "json":
            old_handle = handle
            handle = old_handle.replace(f".{file_type}", ".json")
            warnings.warn(f"Using wrong file type (.{file_type} in {old_handle})! {handle} will be used instead!", skip_file_prefixes=_warn_skips)
        
        #File exists check (And lazy wrong dir exception)
        try:
            if not os.path.isfile(handle):
                warnings.warn(f"File {handle} does not exist! Blank json file created in: {handle}",skip_file_prefixes=_warn_skips)
                _generate_default_json(handle)
        except:
             raise JsonDecoratorNonValidPath
        
        with open(handle, "r+") as file:
            adding_time = str(datetime.datetime.now())
            json_buffer = json.load(file)
            json_buffer["func_calls"].append(
                {"func_name":   f"{func.__name__}",
                 "call_time":   f"{adding_time}", 
                 "args"     :   list(args),
                 "kwargs"   :   kwargs
                })
            file.seek(0)
            json.dump(json_buffer, file, indent = 4)

    def sql_inner(*args, **kwargs):
        cur = handle.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS func_calls(func_name, call_time, args, kwargs)")
        cur.execute("INSERT INTO func_calls VALUES (?,?,?,?)", (str(func.__name__), str(datetime.datetime.now()), str(list(args)), str(kwargs)))
        handle.commit()
    
    if isinstance(handle,type(sys.stdout)):
            return default_inner
    
    if isinstance(handle, str):
            return json_inner
    
    if isinstance(handle, sqlite3.Connection):
            return sql_inner
    
    warnings.warn(f"Decorator {trace} setted to invalid handle type (handle={handle}). Using stdout instead.", skip_file_prefixes=_warn_skips)
    handle = sys.stdout
    return default_inner
        
@trace(handle=sys.stdout)
def a(numer,index,string, a=20, b=10):
    pass

@trace(handle="output/log.json")
def b(numer,index,string, a=20, b=10):
    pass

con = sqlite3.connect("db/workers.db")
@trace(handle=con)
def c(id,name,job, nothing = True):
     pass

@trace(handle=213124)
def d(a,b, c = 10):
    pass

a(1,2,"somestring", a = 2)
b(1,2,'somestring', b = 3)
c(1,'Jhon','The Worker', nothing = False)
d(2,8, c = 100)