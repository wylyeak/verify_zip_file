from distutils.core import setup
import py2exe

py2exe_options = {
    "includes": ["sip"],
    "dll_excludes": ["MSVCP90.dll", ],
    "compressed": 1,
    "optimize": 2,
    "ascii": 0,
    "bundle_files": 1,
}

setup(name='Verify Tool',
      version='1.0',
      windows=["main.py"],
      options={'py2exe': py2exe_options}
)