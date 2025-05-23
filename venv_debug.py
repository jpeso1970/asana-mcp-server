import sys
print('sys.path:', sys.path)
try:
    import modelcontextprotocol
    print('modelcontextprotocol imported successfully')
    print('modelcontextprotocol file:', modelcontextprotocol.__file__)
except Exception as e:
    print('IMPORT ERROR:', e)
