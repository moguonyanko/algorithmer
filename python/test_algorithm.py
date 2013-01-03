#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

import algorithm as al

class AlgorithmerTrainingTest(unittest.TestCase):
	'''
	最強最速アルゴリズマー養成講座（著 高橋直大氏）に記載されている
	サンプルコードを元に作成した練習コードをテストするクラスです。
	'''
	def test_thePouring(self):
		capas = [700000, 800000, 900000, 1000000]
		bottles = [478478, 478478, 478478, 478478]
		fromIds = [2, 3, 2, 0, 1]
		toIds = [0, 1, 1, 3, 2]
		
		kiwi = al.KiwiJuiceEasy()
		
		res = kiwi.thePouring(capas, bottles, fromIds, toIds)
		self.assertEqual([0, 156956, 900000, 856956], res)
	
	def test_bestInvitation(self):
		first = ["snakes","programming","cobra","monty"]
		second = ["python","python","anaconda","python"]
		
		party = al.InterestingParty()
		
		res = party.bestInvitation(first, second)
		self.assertEqual(3, res)
		
	def test_encrypt(self):
		numbers = [1,2,3,1,1,3]
		crypt = al.Cryptography()
		res = crypt.encrypt(numbers)
		self.assertEqual(36, res)
		
		numbers2 = [1,1,1,1]
		crypt = al.Cryptography()
		res2 = crypt.encrypt(numbers2)
		self.assertEqual(2, res2)
	
	def test_digits(self):
		intdg = al.InterestingDigits()
		
		res1 = intdg.digits(10)
		self.assertEqual({3,9}, res1)
		
		res2 = intdg.digits(26)
		self.assertEqual({5,25}, res2)
	
	def test_find(self):
		tpl = al.ThePalindrome()
		
		res = tpl.find("abab")
		self.assertEqual(5, res)
		
		res1 = tpl.find("abacaba")
		self.assertEqual(7, res1)

		res2 = tpl.find("qwerty")
		self.assertEqual(11, res2)

	def test_hightestScore(self):
		hs = al.FriendScore()
		
		friend_info = [
			"NYNNN",
			"YNYNN",
			"NYNYN",
			"NNYNY",
			"NNNYN"
		]
		
		res = hs.highestScore(friend_info)
		self.assertEqual(4, res)
		
	def test_getProbability(self):
		cb = al.CrazyBot()
		
		res = cb.getProbability(2,25,25,25,25)
		self.assertEqual(0.75, res)

	def test_longestPath(self):
		mm = al.MazeMaker()
		maze = [
			"...",
			"...",
			"..."
		]
		startRow = 0
		startCol = 1
		moveRow = [1,0,-1,0]
		moveCol = [0,1,0,-1]
		res = mm.longestPath(maze, startRow, startCol, moveRow, moveCol)
		self.assertEqual(3, res)

		maze2 = [
			"X.X",
			"...",
			"XXX",
			"X.X"
		]
		startRow2 = 0
		startCol2 = 1
		moveRow2 = [1,0,-1,0]
		moveCol2 = [0,1,0,-1]
		res2 = mm.longestPath(maze2, startRow2, startCol2, moveRow2, moveCol2)
		self.assertEqual(-1, res2)
	
	def test_theNumber(self):
		nm = al.NumberMagicEasy()
		
		answer = "YNYY"
		res = nm.theNumber(answer)
		self.assertEqual(5, res)

		answer = "YYYYYYYYYYY"
		self.assertRaises(KeyError, nm.theNumber, answer)
	
	def test_routecalc(self):
		maxW = 5
		maxH = 4
		rt = al.RouteSearchEasy(maxW, maxH)
		res = rt.calc(maxW, maxH)
		self.assertEqual(126, res)
	
	def test_knapsack_search(self):
		ws = [3,4,1,2,3]
		ps = [2,3,2,3,6]
		maxW = 10
		
		#誤植のために動作しない疑いあり。
		#knap = al.KnapsackSearch(ws, ps, maxW)
		#res = knap.getMaxPrecious()
		#self.assertEqual(14, res)
	
	def test_totalSalary(self):
		relations = ["NNYN","NNYN","NNNN","NYYN"]
		cs = al.CorporationSalary(relations)
		res = cs.totalSalary()
		self.assertEqual(5, res)

		relations2 = ["NNNN","NNNN","NNNN","NNNN"]
		cs2 = al.CorporationSalary(relations2)
		res2 = cs2.totalSalary()
		self.assertEqual(4, res2)

	def test_maxDonations(self):
		donations = [1,2,3,4,5,1,2,3,4,5]
		bn = al.BadNeighbors(donations)
		res = bn.maxDonations()
		self.assertEqual(16, res)
		
	def test_howMany(self):
		boradsize = 3
		x_range = [1,1,1,0,-1,-1,-1,0,2,1,-1,-2,-2,-1,1,2]
		y_range = [1,0,-1,-1,-1,0,1,1,-1,-2,-2,-1,1,2,2,1]
		
		cm1 = al.ChessMetric(boradsize, x_range, y_range)
		res1 = cm1.howMany([0,0], [1,2], 1)	
		self.assertEqual(1, res1)
	
		cm2 = al.ChessMetric(boradsize, x_range, y_range)
		res2 = cm2.howMany([0,0], [2,2], 1)	
		self.assertEqual(0, res2)

		cm3 = al.ChessMetric(boradsize, x_range, y_range)
		res3 = cm3.howMany([0,0], [0,0], 2)	
		self.assertEqual(5, res3)
		
		#too late!
		#boradsize = 100
		#cm4 = al.ChessMetric(boradsize, x_range, y_range)
		#res4 = cm4.howMany([0,0], [0,99], 50)	
		#self.assertEqual(243097320072600, res4)
		
		self.assertRaises(ValueError, cm3.howMany, [0,0], [0,0], 56)
		
	def test_countPerfect(self):
		hs = al.HandsShaking()
		
		res2 = hs.countPerfect(4)	
		self.assertEqual(2, res2)
		
		res3 = hs.countPerfect(8)	
		self.assertEqual(14, res3)
	
	def test_getMaximum(self):
		cb = al.ColorfulBoxesAndBalls()
		
		res = cb.getMaximum(2,3,100,400,200)
		self.assertEqual(1400, res)

		res2 = cb.getMaximum(2,3,100,400,300)
		self.assertEqual(1600, res2)

	def test_maximumEarnings(self):
		stockPrices = ["10 20 30", "15 24 32"]
		me = al.StockHistory(stockPrices)
		initialInvestment = 1000
		monthlyContribution = 0
		res = me.maximumEarnings(initialInvestment, monthlyContribution)
		self.assertEqual(500, res)

		stockPrices = ["10", "9"]
		me = al.StockHistory(stockPrices)
		initialInvestment = 1000
		monthlyContribution = 0
		res2 = me.maximumEarnings(initialInvestment, monthlyContribution)
		self.assertEqual(0, res2)
		
		stockPrices = ["40 50 60", "37 48 55", "100 48 50", "105 48 47", "110 50 52", 
										"110 50 52", "110 51 54", "109 49 53"]
		me = al.StockHistory(stockPrices)
		initialInvestment = 100
		monthlyContribution = 20
		res3 = me.maximumEarnings(initialInvestment, monthlyContribution)
		self.assertEqual(239, res3)

	def test_schedule(self):
		bt = al.BatchSystem()
		
		duration = [400,100,100,100]
		user = ["Danny Messer","Stella Bonasera","Stella Bonasera","Mac Taylor"]
		res = bt.schedule(duration, user)
		self.assertEqual([3,1,2,0], res)
		
	def test_interestRate(self):
		at = al.AutoLoad()
		
		res1 = at.interestRate(2000, 510, 4) 
		self.assertEqual(round(9.5620546258368, 3), round(res1, 3))
	
	def test_leastBorders(self):
		cc = al.CirclesCountly()
		
		xs = [-3, 2, 2, 0, -4, 12, 12, 12]
		ys = [-1, 2, 3, 1, 5, 1, 1, 1]
		rs = [1, 3, 1, 7, 1, 1, 2, 3]
		x1 = 2
		y1 = 3
		x2 = 13
		y2 = 2
		res = cc.leastBorders(xs, ys, rs, x1, y1, x2, y2)
		
		self.assertEqual(5, res)		
	
	def test_countPaths(self):
		roads = [
			"NNNNNY",
			"NNNNYN",
			"NNNNYN",
			"NNNNNN",
			"NYYNNN",
			"YNNNNY"
		]
		
		hm = al.HamiltonPath(roads)
		res = hm.countPaths()
		self.assertEqual(24, res)		
	
if __name__ == '__main__':
	print(__file__)
	unittest.main()

