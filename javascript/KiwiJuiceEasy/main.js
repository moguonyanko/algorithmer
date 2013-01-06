/**
 * 参考書籍：
 * 「最強最速アルゴリズマー養成講座 著：高橋直大」
 * P.53 シミュレーション
 **/

load("../unittest.js");

(function(ut){
	"use strict";

	var KiwiJuiceEasy = {
		thePouring : function(capacities, bottles, 
			fromId, toId){
				for(var i = 0, len = fromId.length; i<len; i++){
					var f = fromId[i], 
					t = toId[i],
					vol = Math.min(bottles[f], capacities[t] - bottles[t]);
		
					bottles[f] -= vol;
					bottles[t] += vol;
				}
		
				return bottles;
		}
	};

	this.main = function(){
		var capacities = [30, 20, 10],
		bottles = [10, 5, 5],
		fromId = [0, 1, 2],
		toId = [1, 2, 0];
	
		var result = KiwiJuiceEasy.thePouring(capacities, bottles, fromId, toId),
		answer = [10, 10, 0];
	
		ut.assertEqual(answer, result);
	};

}(unittest));


