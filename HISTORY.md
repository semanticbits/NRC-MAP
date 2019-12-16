# Release History

## 0.1.0 (2020-mm-dd)

**Improvements**

- MAP-115: Added Python package build capability.
    - Updated Docker compose file to have Python, NGINX, and SQL Server 
    containers.
    - Added `nrc_map` source code directory.
    - Added command line interface module `cli.py`
    - Added exceptions module `exceptions.py`
    - Added package global variables module `pkg_globals.py`
    - Added utilities module `utils.py`
    - The `requirements.txt` was updated to show all dependencies and moved to 
    the package root directory. 
- MAP-116: Create a toplevel Makefile with targets for common tasks (start / 
stop Docker, run tests, upgrade Python third party packages, ect...).