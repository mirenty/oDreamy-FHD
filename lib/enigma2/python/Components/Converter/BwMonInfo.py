from Components.Converter.Converter import Converter
from Components.Element import cached

class BwMonInfo(Converter, object):
	RCL = 0
	TML = 1
	RCW = 2
	TMW = 3
	RCLT = 4
	TMLT = 5
	RCWT = 6
	TMWT = 7

	def __init__(self, type):
		Converter.__init__(self, type)
		if type == "RCL":
			self.type = self.RCL
		elif type == "TML":
			self.type = self.TML
		elif type == "RCW":
			self.type = self.RCW
		elif type == "TMW":
			self.type = self.TMW
		elif type == "RCLT":
			self.type = self.RCLT
		elif type == "TMLT":
			self.type = self.TMLT
		elif type == "RCWT":
			self.type = self.RCWT
		else :
			self.type = self.TMWT

	@cached
	def getText(self):
		if self.type == self.RCL:
			return "%d" % self.source.lanreceive + " KB/s"
		elif self.type == self.TML:
			return "%d" % self.source.lantransmit
		elif self.type == self.RCW:
			return "%d" % self.source.wlanreceive + " KB/s"
		elif self.type == self.TMW:
			return "%d" % self.source.wlantransmit
		elif self.type == self.RCLT:
			return "%d" % self.source.lanreceivetotal
		elif self.type == self.TMLT:
			return "%d" % self.source.lantransmittotal
		elif self.type == self.RCWT:
			return "%d" % self.source.wlanreceivetotal
		else:
			return "%d" % self.source.wlantransmittotal


	@cached
	def getBool(self):
		return False

	text = property(getText)

	boolean = property(getBool)

	@cached
	def getValue(self):
		if self.type == self.RCL:
			return int(self.source.lanreceive)
		elif self.type == self.TML:
			return int(self.source.lantransmit)
		elif self.type == self.RCW:
			return int(self.source.wlanreceive)
		elif self.type == self.TMW:
			return int(self.source.wlantransmit)
		if self.type == self.RCLT:
			return int(self.source.lanreceivetotal)
		elif self.type == self.TMLT:
			return int(self.source.lantransmittotal)
		elif self.type == self.RCWT:
			return int(self.source.wlanreceivetotal)
		else:
			return int(self.source.wlantransmittotal)

	range = 100000
	value = property(getValue)

