from tornado import ioloop
from tornado import netutil

class EchoServer(netutil.TCPServer):

	def handle_stream(self, stream, address):
		self._stream = stream
		self._read_line()

	def _handle_read(self, data_in):
		self._stream.write('You send: %s' % data_in)
		self._read_line()

	def _read_line(self):
		self._stream.read_until('\n', self._handle_read)



if __name__ == '__main__':
	sever = EchoServer()
	sever.listen(2007)
	ioloop.IOLoop.instance().start()