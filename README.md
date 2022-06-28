# MemoryBlob
A small wrapper around c_type arrays for easier FFI and state persistence in Ren'Py.

Since Ren'Py depends on pickling for its replays and save files, efficient interopability with foreign languages (for example, Lua through LuaJIT) is problematic.

This library helps with this issue by exposing a `MemoryBlob` class, a thin wrapper around c_type arrays that supports pickling while also exposing the raw pointer that can be passed to other languages for further use.

## Example use
```python
from c_types import *

# Create the memory blob. We're passing the length, in elements (not bytes) and the c_type to use.
arr = MemoryBlob(8, c_float)

# For the user in Python, MemoryBlob functions like a normal list.
print("Before: " + str(arr[6]))
arr[6] = 1.2
print("After: " + str(arr[6]))

# Unlike arrays create by multiplication of a c_type and an integer (for example, c_bool * 100), it supports pickling.
import pickle
with open('data.pickle', 'wb') as f:
	pickle.dump(arr, f)
with open('data.pickle', 'rb') as f:
	data = pickle.load(f)
	print("Pickled: " + str(data[6]))

# Since __next__ is implemented for MemoryBlob, it supports `map` and similar functions.
print(list(map(lambda o: int(o), arr)))

# The type is optional (defaults to c_byte)...
arr = MemoryBlob(4) 
# ... and so is the length (defaults to 0)
arr = MemoryBlob()
```

## Additional remarks
This module depends on ctypes. It's intended to be used with Ren'Py, which provides it by default.
