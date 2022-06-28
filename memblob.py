from ctypes import *

class MemoryBlob:
	def __init__(self, size: int = 0, array_type = c_byte):
		self._data = (array_type * size)()
		self._array_type = array_type

	def __reduce__(self) -> list:
		state = []
		state.append(self._array_type)
		state.append(len(self._data))
		for d in self._data:
			state.append(d)
		return (self.__class__, (), state)

	def __setstate__(self, state: list):
		self._data = (state[1] * state[0])()
		for i in range(0, len(self._data)):
			self._data[i] = state[2 + i]

	def __len__(self) -> int:
		return len(self._data)

	def __next__(self) -> int:
		return self._data.__next__()

	def __getitem__(self, index):
		return self._data[index]

	def __setitem__(self, index, value):
		self._data[index] = value
