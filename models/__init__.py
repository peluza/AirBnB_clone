#!/usr/bin/python3
"""
    module: __init__
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
