from cx_Freeze import setup, Executable

base = None    

executables = [Executable("DOSBoxPy.py", base=base)]

packages = ["idna","time","os","sys","subprocess"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "DOSBoxPy",
    options = options,
    version = "1",
    description = 'UI for DOSBox',
    executables = executables
)