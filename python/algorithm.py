#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import math
import copy
import sys
import queue as qu

##
# 最強最速アルゴリズマー養成講座（著 高橋直大氏）を参考にした，
# Pythonによる練習コード
##

def makeArray(column, row, initValue=None):
	'''
	Make two-dimensional array.
	'''
	#TODO: Two dimentional array only.
	
	if column == 0 or row == 0:
		raise ValueError("This function need size value that greater than zero.")
	
	marr = [None]*column
	
	for i in range(column):
		marr[i] = [copy.deepcopy(initValue) for dummy in range(row)]
		
	return marr

class KiwiJuiceEasy():
	'''
	P.53 シミュレーション
	'''
	def thePouring(self, capas, bottles, fromIds, toIds):
		size = len(fromIds)
		for i in range(size):
			fromId = fromIds[i]
			toId = toIds[i]
		
			move_vol = min(bottles[fromId], capas[toId]-bottles[toId])

			bottles[fromId] -= move_vol
			bottles[toId] += move_vol
	
		return bottles

class InterestingParty():
	'''
	P.71 全探索
	'''
	def bestInvitation(self, first, second):
		dic = {}
		rng = range(len(first))
		
		for i in rng:
			dic[first[i]] = 0	
			dic[second[i]] = 0	
		
		for i in rng:
			dic[first[i]] = dic[first[i]]+1	
			dic[second[i]] = dic[second[i]]+1
		
		ans = 0
		for key in dic:
			if ans < dic[key]: ans = dic[key]
	
		return ans

class Cryptography():
	'''
	P.77 全探索
	'''
	def encrypt_V1(self, numbers):
		ans = 0
		rng = range(len(numbers))
		for i in rng:
			seki = 1
			for j in rng:
				if i == j: #自分のターンなら自分に1足して掛ける。つまりここは1足す項を探すためのループ。
					seki *= (numbers[j]+1)
				else:
					seki *= numbers[j]
			
			ans = max(ans, seki)
		
		return ans

	def encrypt(self, numbers):
		rng = range(len(numbers))
		nums = sorted(numbers)
		seki = 1
		nums[0] = nums[0]+1 #最小値+1が最大の増加率を導く。
		for i in rng: seki *= nums[i]
		
		return seki

class InterestingDigits():
	'''
	P.88 全探索
	'''
	def digits(self, base):
		res = set()
		rng = range(base)
		
		n = 2
		while n < base:
			ok = True
			for k1 in rng:
				for k2 in rng:
					for k3 in rng:
						#10進数表記に変換して，nの倍数かどうかと各桁の和がnの倍数でないかどうかを確認する。
						if (k1 + k2*base + k3*base*base) % n == 0 and (k1 + k2 + k3) % n != 0:
							ok = False
							break
					if ok == False: break
				if ok == False: break
			if ok == True: res.add(n)
			n += 1
			
		return res

	def digits_V2(self, base):
		'''
		求めるnはbaseを法として1と合同な数字である。
		従って，
			1≡n(mod base)
		ここで左辺を右辺に移行して
			0≡n-1(mod base)
		となる。n-1はbaseを法として0と合同なので
		n-1はbaseの倍数だと分かる。
		'''
		res = set()
		n = 2
		while n < base:
			if (base-1) % n == 0: res.add(n) #TODO: 何故nで割るのか？
			n += 1
		
		return res

class ThePalindrome():
	'''
	P.95 全探索
	回文になる場合の，最小の文字数を返します。
	'''
	def find(self, s):
		size = len(s)
		rng = range(size)
		
		for i in rng:
			matchflag = True
			for j in rng:
				opposite_index = i - j - 1
				#比較する文字を1つずつずらすことで「1文字追加される」という処理を表現している。
				#「1文字追加される」ことで反対側の文字が存在するようになる。
				if opposite_index < size and s[j] != s[opposite_index]:
					matchflag = False
					break
			
			if matchflag == True: return i+size
		
		return size*2-1 #両端から突き合わせたが全く一致しなかった。最長の回文の文字数を返す。

class FriendScore():
	'''
	P.104
	全探索
	'''
	def highestScore_V1(self, friends):
		rng = range(len(friends[0]))
		friend_key = "Y"
		
		max_friend_count = 0
		for i in rng:
			cnt = 0
			
			for j in rng:
				if i == j: continue #自分自身を友人として数えない。
				
				if friends[i][j] == friend_key:
					cnt += 1
				else:
					for k in rng:
						if friends[j][k] == friend_key and friends[k][i] == friend_key:
							cnt += 1
							break
							
			max_friend_count = max(max_friend_count, cnt)
		
		return max_friend_count

	def highestScore(self, friends):
		is_friends = "Y"
		
		max_friend_count = 0
		for i, user_i in enumerate(friends):
			cnt = 0
			
			for j, user_j in enumerate(friends):
				if user_i == user_j: continue #自分自身を友人として数えない。
				
				if user_i[j] == is_friends:
					cnt += 1
				else:
					for k, user_k in enumerate(friends):
						if user_i[k] == user_k[i] == is_friends:
							cnt += 1
							break
							
			max_friend_count = max(max_friend_count, cnt)
		
		return max_friend_count

class CrazyBot():
	'''
	P.129 全探索
	'''
	def __init__(self):
		self.direct = 4
		capacity = 100
	
		self.grid = {}
		for column_num in range(capacity): #正方形という設定
			column = [False]*capacity
			self.grid[column_num] = column
		
		self.vx = [1, -1, 0, 0]
		self.vy = [0, 0, 1, -1]
		self.prob = [0.0]*self.direct
		
	def getProbability(self, n, east, west, south, north):
		directs = [east, west, south, north]

		for i, d in enumerate(directs):
			self.prob[i] = d/100.0
		
		firstx = firsty = 50
		
		return self.__dfs(firstx, firsty, n)
	
	def __dfs(self, x, y, n):
		if self.grid[x][y] == True: return 0 #1度通った場所なので確率0を返す。
		if n == 0: return 1 #もう歩けない。TODO: ここで1を返して良い理屈は？
		
		self.grid[x][y] = True
		ret = 0
		
		for i in range(self.direct):#4方向にロボットを動かしてそれぞれの確率を足し込んでいく。
			ret += self.__dfs(x+self.vx[i], y+self.vy[i], n-1) * self.prob[i]
		
		self.grid[x][y] = False #別のルート探索で通れるよう，より浅いところに上がってくるときにフラグを戻しておく。
		
		return ret
		
class MazeMaker():
	'''
	P.139 全探索
	'''
	def isStep(self, nextX, nextY, width, height, board, maze):
		'''
		Check valid step.
		'''
		if 0 <= nextX and nextX < width and 0 <= nextY and nextY < height and board[nextY][nextX] == -1 and maze[nextY][nextX] == ".": 	
			return False
		
		return True

	def longestPath(self, maze, startRow, startCol, moveRow, moveCol):
		width = len(maze[0])
		height = len(maze)
		board = makeArray(height, width, initValue=-1)
		
		board[startRow][startCol] = 0
		
		queueX = qu.Queue()
		queueY = qu.Queue()
		queueX.put(startCol)
		queueY.put(startRow)
		
		rowrng = range(len(moveRow))
		while queueX.empty() == False:
			x = queueX.get()
			y = queueY.get()
		
			for i in rowrng:
				nextX = x + moveCol[i]
				nextY = y + moveRow[i]
				
				if 0 <= nextX and nextX < width and 0 <= nextY and \
				nextY < height and board[nextY][nextX] == -1 and maze[nextY][nextX] == ".": 	
					board[nextY][nextX] = board[y][x] + 1 #有効なステップならば歩数として数えてboradに追加する。
					queueX.put(nextX)
					queueY.put(nextY)
			
		max_step = 0

		for i in range(height):
			for j in range(width):
				if maze[i][j] == "." and board[i][j] == -1: #通れるが−1，つまり到達できないマスがあった。
					return -1
				max_step = max(max_step, board[i][j])			
		
		return max_step

class NumberMagicEasy():
	'''
	P.151 全探索
	'''
	def __init__(self):
		limit = 16
		soldict = {}
		solvalues = [
			"YYYY",
			"YYYN",
			"YYNY",
			"YYNN",
			"YNYY",
			"YNYN",
			"YNNY",
			"YNNN",
			"NYYY",
			"NYYN",
			"NYNY",
			"NYNN",
			"NNYY",
			"NNYN",
			"NNNY",
			"NNNN"
		]
		
		for i in range(limit):
			soldict[solvalues[i]] = i+1
		
		self.solution = soldict
	
	def theNumber(self, answer):
		try:
			return self.solution[answer]
		except KeyError as ex:
			raise KeyError("Cannot find your number.")
			
class RouteSearchEasy():
	'''
	P.177 動的計画法・メモ化
	'''
	def __init__(self, h, w):
		sizeW = w+1
		sizeH = h+1
		dp = makeArray(sizeH, sizeW, 0)
		dp[0][0] = 1
		for i in range(sizeH):
			for j in range(sizeW): 
				if i != 0: #上に進む
					dp[i][j] += dp[i-1][j]
				if j != 0: #右に進む
					dp[i][j] += dp[i][j-1]
		
		self.dp = dp
	
	def calc(self, h, w):
		return self.dp[h][w]

class KnapsackSearch():
	'''
	P.184 動的計画法・メモ化
	'''
	def __init__(self, ws, ps, maxW):
		weightSize = len(ws)+1
		maxSize = maxW+1
		dp = makeArray(weightSize, maxSize, 0)
		
		ret = 0
		for i in range(weightSize):
			for j in range(maxSize):
				if j+ws[i] <= maxW:
					dp[i+1][j+ws[i]] = max(dp[i+1][j+ws[i]], dp[i][j] + ps[j]) #ps[j]は確実にエラー。誤植？
					ret = max(dp[i+1][j+ws[i]], ret)
		
		self.maxPrecious = ret
		self.dp = dp
	
	def getMaxPrecious(self):
		return self.maxPrecious

class CorporationSalary():
	'''
	P.193 動的計画法・メモ化
	'''
	def __init__(self, relations):
		self.relations = relations
		self.salaries = [0]*len(self.relations)

	def totalSalary(self):
		total = 0
		for i, emp in enumerate(self.relations):
			total += self.__getSalary(i)

		return total

	def __getSalary(self, i):
		if self.salaries[i] == 0:
			salary = 0
			relation = self.relations[i]
			
			for j, char in enumerate(relation):
				if relation[j] == "Y":
					salary += self.__getSalary(j)
			
			if salary == 0: salary = 1
			
			self.salaries[i] = salary
		
		return self.salaries[i]
	
class BadNeighbors():
	'''
	P.204 動的計画法・メモ化
	'''
	def __init__(self, donations):
		self.donations = donations
		self.dp = [0]*len(donations)

	def __calcDonation(self, donation, i, ans):
		self.dp[i] = donation
		if i > 0:
			self.dp[i] = max(self.dp[i], self.dp[i-1])
		if i > 1:
			self.dp[i] = max(self.dp[i], self.dp[i-2]+donation)
		
		return max(ans, self.dp[i])
	
	def maxDonations(self):
		ans0 = 0
		ans1 = 0
	
		for i in range(len(self.donations)-1):
			ans0 = self.__calcDonation(self.donations[i], i, ans0)
			ans1 = self.__calcDonation(self.donations[i+1], i, ans1)
				
		return max(ans0, ans1)

class ChessMetric():
	'''
	P.213 動的計画法・メモ化
	'''
	def __init__(self, boardsize, x_range, y_range, max_movenum=55):
		self.size = boardsize
		ways = makeArray(boardsize, boardsize, 0)	
		for i in range(len(ways)):
			for j in range(len(ways[i])):
				ways[i][j] = [0]*max_movenum
		self.ways = ways
		self.dx = x_range
		self.dy = y_range

	def howMany(self, start, end, numMoves):
		if numMoves > len(self.ways[0][0]):
			raise ValueError("Exceed max move limit!")
	
		sx = start[0]
		sy = start[1]
		ex = end[0]
		ey = end[1]
		
		self.ways[sy][sx][0] = 1 #スタート地点の到達パターン数は1通り
		boardrange = range(self.size) 
		wayrange = range(len(self.dx))

		for i in range(numMoves+1):
			i += 1
			for x in boardrange:
				for y in boardrange:
					for j in wayrange:
						nx = x + self.dx[j]
						ny = y + self.dy[j]
						
						if nx < 0 or ny < 0 or nx >= self.size or ny >= self.size: 
							continue
						else: #1つ前のマスまでの到達パターン数を足し込む。
							self.ways[ny][nx][i] += self.ways[y][x][i-1]
		
		return self.ways[ex][ey][numMoves]

class HandsShaking():
	'''
	P.218 動的計画法・メモ化
	'''
	def countPerfect(self, n):
		size = int(n/2)+1
		dp = [0]*(size+1)
		dp[0] = 1
		
		for i in range(size):
			i += 1
			for j in range(i):
				dp[i] += dp[j] * dp[i-j-1] #カタラン数
		
		return dp[int(n/2)]		

class ColorfulBoxesAndBalls():
	'''
	P.230 カラフルボックス＆ボール
	'''
	def getMaximum(self, numRed, numBlue, onlyRed, onlyBlue, bothColors):
		ans = -sys.maxsize-1
		comsize = min(numRed, numBlue)+1
		
		for i in range(comsize):
			myscore = (numRed-i)*onlyRed + (numBlue-i)*onlyBlue + 2*i*bothColors
			ans = max(ans, myscore)
		
		return ans	

class StockHistory():
	'''
	P.244 株式投資シミュレーション
	'''
	def __init__(self, stockPrices):
		separator = " "
		self.month = len(stockPrices)
		self.corp = len(stockPrices[0].split(separator))
		self.prices = makeArray(self.month, self.corp, 0)
		
		for i in range(self.month):
			s = stockPrices[i].split(separator)
			for j in range(self.corp):
				self.prices[i][j] = int(s[j])
	
	def maximumEarnings(self, initialInvestment, monthlyContribution):
		money = initialInvestment
		maxVal = 0
		proportion = [0.0]*(self.month-1)
		buy = [False]*(self.month-1) #買う月に対応する要素はTrueになる。
		
		i = self.month-2 #最後の月から最初の月まで，利益の得られる月を探りながら遡っていく。
		while 0 <= i:
			for j in range(self.corp):
				p = 1.0 * self.prices[self.month-1][j] / self.prices[i][j] - 1
				
				if 0 < p and maxVal < p: #利益の増加率が更新される月だけ買う。しかし 0 < p は不要では？
					buy[i] = True
					maxVal = p
					proportion[i] = p
			i -= 1 #最後の月から遡っていくのでデクリメントする。

		profit = 0
		for i, isBuy in enumerate(buy):
			if isBuy == True: #買うと決めた月に現在の所持金を全額つぎ込む。
				profit += money * proportion[i]
				money = 0
							
			money += monthlyContribution
		
		return round(profit)

class BatchSystem():
	'''
	P.252 バッチシステム
	'''
	def schedule(self, duration, user):
		taskSize = len(duration)
		
		jobTime = {user[n]:0 for n, userName in enumerate(user) if n < taskSize}
		
		for n in range(taskSize):
			jobTime[user[n]] = jobTime[user[n]]+duration[n]	
		
		#jobTime = {user[n]:jobTime[user[n]]+duration[n] for n in range(taskSize)}
		
		done = [False]*taskSize
		ans = [0]*taskSize
		ansCount = 0
		
		while ansCount < taskSize:
			next = ""
			
			for n in range(taskSize):
				#未完了かつ次のユーザーのタスクより今のユーザーの残りタスクの方が
				#待ち時間が短いならば今のユーザーをnextに設定しタスク処理を継続する。
				if done[n] == False and (next == "" or jobTime.get(user[n]) < jobTime.get(next)):
					next = user[n]
			
			for n in range(taskSize):
				if user[n] == next:
					done[n] = True
					ans[ansCount] = n
					ansCount += 1
		
		return ans	

class AutoLoad():
	'''
	P.264 自動車ローン
	'''
	def interestRate(self, price, montlyPayment, loanTerm):
		balance = 0.0
		high = 100
		low = 0
		mid = 0
		
		error_range = 1E-9
		
		while error_range < high-low and error_range < (high-low)/high:
			balance = price
			mid = (high + low) / 2 
			
			for j in range(loanTerm):
				balance *= mid / 1200 + 1
				balance -= montlyPayment
				
			if 0 < balance: high = mid
			else: low = mid
		
		return mid

class CirclesCountly():
	'''
	P.272 円の国家群
	'''
	def __inside(self, x1, y1, x2, y2, r):
		return (x1-x2)**2 + (y1-y2)**2 <= r**2
	
	def leastBorders(self, X, Y, R, x1, y1, x2, y2):
		crossCount = 0
		
		for i, x in enumerate(X):
			if self.__inside(X[i], Y[i], x1, y1, R[i]) != self.__inside(X[i], Y[i], x2, y2, R[i]):
				crossCount += 1
		
		return crossCount
		
class HamiltonPath():

	TEST_MOD = 1000000007

	'''
	P.285 ハミルトン路
	'''
	def __init__(self, roads):
		self.roads = roads
		self.visited = [False]*len(roads)

	def countPaths(self):
		group = 0
		free = 0
		roadsize = len(self.roads)
		
		connect = [0]*roadsize
		sumu = 1
		
		for i in range(roadsize):
			y = 0
			for j in range(len(self.roads[i])):
				if self.roads[i][j] == "Y":
					y += 1
					if 2 < y:	return 0
			connect[i] = y #接続数を保存する。
			
		for i in range(len(connect)):
			if connect[i] == 0: #接続数がゼロであれば自由に回れる。
				self.visited[i] = True
				free += 1
			elif connect[i] == 1 and self.visited[i] == False:
				group += 1
				self.dfs(i) #深さ優先探索で必ず回らなければならない都市を探す。
		
		for i in range(len(self.visited)):
			if self.visited[i] == False: return 0 #回りきれなかった都市が存在した。
		for i in range(group + free):
			sumu = sumu * (i + 1) % self.TEST_MOD
		for i in range(group):
			sumu = sumu * 2 % self.TEST_MOD
		
		return int(sumu)
	
	def dfs(self, city):
		self.visited[city] = True
		for i in range(len(self.roads[city])):
			if self.roads[city][i] == "Y" and self.visited[i] == False:
				self.dfs(i)
		
#Entry point
if __name__ == '__main__':
	print("PracticeAlgorithmer running.")

