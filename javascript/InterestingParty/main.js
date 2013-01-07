/**
 * 参考書籍：
 * 「最強最速アルゴリズマー養成講座 著：高橋直大」
 * P.71 全探索
 **/

load("../unittest.js");

(function(ut){
	"use strict";

	var InterestingParty = {
		bestInvestigation : function(first, second){
			
			var dic = {},
			answer = 0;
			
			var _prepare = function(kwd){
				if(dic[kwd] != null){
					dic[kwd]++;
				}else{
					dic[kwd] = 1;	
				}
			};
			
			for(var i = 0, len = first.length; i<len; i++){
				var a = first[i], 
				b = second[i];
				
				_prepare(a);
				_prepare(b);
				
				answer = dic[a] < dic[b] ? dic[b] : dic[a];
			}
			
			return answer;
		}
	};

	this.main = function(){
		var first = ["snakes", "programming", "cobra", "monty"],
		second = ["python", "python", "anaconda", "python"];
	
		var result = InterestingParty.bestInvestigation(first, second),
		answer = 3;
	
		ut.assertEqual(answer, result);
	};

}(unittest));


