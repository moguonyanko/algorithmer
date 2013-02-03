/**
 * 参考書籍：
 * 	「最強最速アルゴリズマー養成講座 著：高橋直大」
 * P.79 全探索
 **/

load("../unittest.js");

(function(ut){
	"use strict";

	var Cryptography = {
		encrypt : function(numbers){

			/** 
			 * 最小要素に１加えた時の増加量が最大になる。
			 * 完全に正しいが全探索の練習にならないので
			 * コメントアウトしている。
			 */
			/*
			numbers.sort();
			numbers[0] += 1;
			return numbers.reduce(function(a, b){
				return a * b;
			});
			*/
			
			var result = 0,
			mulfn = function(a, b){ return a * b; };
			
			for(var i = 0, len = numbers.length; i<len; i++){
				numbers[i] += 1;
				res = numbers.reduce(mulfn);
				result = Math.max(result, res);
				numbers[i] -= 1;
			}
			
			return result;
		}
	};

	this.main = function(){
		var numbers = [1, 3, 2, 1, 1, 3];
	
		var result = Cryptography.encrypt(numbers),
		answer = 36;
	
		ut.assertEqual(answer, result);
	};
}(unittest));


