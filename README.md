# Bullseye Py
a py library for connecting to the bullseye monitor web socket.

# Usage
```py
from bullseye.monitor import Monitor

def handler(product):
    print(f'{product}')

if __name__ == '__main__':
    mon = Monitor("API_KEY", "DECRYPT_KEY", ["amazon"], handler)
    mon.connect()
```
