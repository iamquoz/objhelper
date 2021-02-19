import matplotlib.pyplot as plt
import sys

class Data:
	year : int
	sd : int
	sto : int
	r : int
	n : int
	np : int
	d : int
	z : float 

	def __init__(self, yr, sdi, stoi, ri, ni, npi, di, zi):
		self.year = yr
		self.sd = sdi
		self.sto = stoi
		self.r = ri
		self.n = ni
		self.np = npi
		self.d = di
		self.z = zi

	def kto(self):
		return self.sto * 100 / self.sd

	def kte(self):
		return self.n / self.sto

	def ktte(self):
		return self.d / self.sto

	def kch(self):
		return self.n * 1000 / self.r

	def kt(self):
		return self.d / self.n

	def kst1(self):
		return self.np * 1000 / self.r

	def kz(self):
		return self.z * 10000 / self.r

	def kpt(self):
		return self.n * 10000 / self.r

	def kst(self):
		return self.np * 10000 / self.r

	def __str__(self):
		return str(round(self.kto(), 1)) + ' ' + str(round(self.kte(), 1)) + ' ' + str(round(self.ktte(), 1)) + ' ' + str(round(self.kch(), 1)) + ' ' + str(round(self.kt(), 1)) + ' ' + str(round(self.kst1(), 1)) + ' ' + str(round(self.kz(), 1)) + ' ' + str(round(self.kpt(), 1)) + ' ' + str(round(self.kst(), 1)) + '\n'


lineIn = sys.stdin.read()

lines = lineIn.split(sep='\n')

nums = []

arr = []
i = 0
for line in lines:
	nums.clear()

	for t in line.split():
		try:
			nums.append(float(t.replace(',', '.')))
		except ValueError:
			pass
	if i != (len(lines) - 1):
		arr.append(Data(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7]))
	i = i + 1

years = []

ktoArr = []
kteArr = []
ktteArr= []
kchArr = []
ktArr  = []
kst1Arr = []
kzArr  = []
kptArr = []
kstArr = []

for datum in arr:
	years.append(int(datum.year))
	ktoArr.append(round(datum.kto(), 1))
	kteArr.append(round(datum.kte(), 1))
	ktteArr.append(round(datum.ktte(), 1))
	kchArr.append(round(datum.kch(), 1))
	ktArr.append(round(datum.kt(), 1))
	kst1Arr.append(round(datum.kst(), 1))
	kzArr.append(round(datum.kz(), 1))
	kptArr.append(round(datum.kpt(), 1))
	kstArr.append(round(datum.kst(), 1))

print("kto change: " + str(round(ktoArr[-1]/ktoArr[0], 2)))
print("kte change: " + str(round(kteArr[-1]/kteArr[0], 2)))
print("ktte change: " + str(round(ktteArr[-1]/ktteArr[0], 2)))
print("kch change: " + str(round(kchArr[-1]/kchArr[0], 1)))
print("kt change: " + str(round(ktArr[-1]/ktArr[0], 2)))
print("kst1 change: " + str(round(kst1Arr[-1]/kst1Arr[0], 2)))
print("kz change: " + str(round(kzArr[-1]/kzArr[0], 2)))
print("kpt change: " + str(round(kptArr[-1]/kptArr[0], 2)))
print("kst change: " + str(round(kstArr[-1]/kstArr[0], 2)))

plt.subplot(3, 3, 1)
plt.scatter(years, ktoArr)
plt.title('Kто')
plt.plot(	range(len(ktoArr)), ktoArr)
plt.xlim(xmin = years[0] - 1, xmax = years[-1] + 1)

plt.subplot(3, 3, 2)
plt.scatter(years, kteArr)
plt.title('Kте')
plt.plot(	range(len(kteArr)), kteArr)
plt.xlim(xmin = years[0] - 1, xmax = years[-1] + 1)


plt.subplot(3, 3, 3)
plt.scatter(years, ktteArr)
plt.title('Kтте')
plt.plot(	range(len(ktteArr)), ktteArr)
plt.xlim(xmin = years[0] - 1, xmax = years[-1] + 1)


plt.subplot(3, 3, 4)
plt.scatter(years, kchArr)
plt.title('Kч')
plt.plot(	range(len(kchArr)), kchArr)
plt.xlim(xmin = years[0] - 1, xmax = years[-1] + 1)


plt.subplot(3, 3, 5)
plt.scatter(years, ktArr)
plt.title('Kт')
plt.plot(	range(len(ktArr)), ktArr)
plt.xlim(xmin = years[0] - 1, xmax = years[-1] + 1)


plt.subplot(3, 3, 6)
plt.scatter(years, kst1Arr)
plt.title('Kст1')
plt.plot(	range(len(kst1Arr)), kst1Arr)
plt.xlim(xmin = years[0] - 1, xmax = years[-1] + 1)


plt.subplot(3, 3, 7)
plt.scatter(years, kzArr)
plt.title('Kз')
plt.plot(	range(len(kzArr)), kzArr)
plt.xlim(xmin = years[0] - 1, xmax = years[-1] + 1)


plt.subplot(3, 3, 8)
plt.scatter(years, kptArr)
plt.title('Kпт')
plt.plot(	range(len(kptArr)), kptArr)
plt.xlim(xmin = years[0] - 1, xmax = years[-1] + 1)


plt.subplot(3, 3, 9)
plt.scatter(years, kstArr)
plt.title('Kст')
plt.plot(	range(len(kstArr)), kstArr)

plt.xlim(xmin = years[0] - 1, xmax = years[-1] + 1)
plt.show()