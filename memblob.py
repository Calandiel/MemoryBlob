from ctypes import *

class MemoryBlob:
	def __init__(self, size: int = 0, array_type = c_ubyte):
		self._array_type = array_type
		self._data = (array_type * size)()

	def binary_length(self):
		return len(self._data) * sizeof(self._array_type)

	def __reduce__(self) -> list:
		state = []
		state.append(self._array_type)
		state.append(len(self._data))
		state_bytes = bytearray(self._data)
		state.append(state_bytes)
		return (self.__class__, (), state)

	def __setstate__(self, state: list):
		self._array_type = state[0]
		data_type = state[0] * state[1]
		input_binary = state[2]
		self._data = data_type.from_buffer(input_binary)

	def __len__(self) -> int:
		return len(self._data)

	def __next__(self) -> int:
		return self._data.__next__()

	def __getitem__(self, index):
		return self._data[index]

	def __setitem__(self, index, value):
		self._data[index] = value
