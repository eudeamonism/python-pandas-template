# Environment Setup

## Create a Virtual environment

at terminal

```bash
python -m venv venv
```

## Activate Virtual Environment

Let's try the excecutable or just the manual process

```bash
venv/Scripts/Activate
```

Or, we can use type

`ctrl shft p`

And, access Python: Selector, choosing the environment with venv

## Install Modules

```bash
pip install openpyxl requests pandas
```

## Folder Structure

Include

- app folder that has
  - `__init__.py` file

### module import standardization

```bash
import openpyxl as px
import requests
import pandas as pd
```

### Confirm Modules

```bash
pip list
```

## Git init (optional)

```bash
git init
```

### Verify venv not commitable

Within root level, add .gitignore that includes the following:

```python
venv
env
.env
output
```
