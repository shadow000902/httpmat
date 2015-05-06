from cx_Freeze import setup, Executable;
setup(name = "httpmat",
        version = "0.1",
        description = "http api",
        executables =[Executable("E:/httpmat/httpapimat.py")])