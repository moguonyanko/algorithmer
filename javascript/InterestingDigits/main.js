/**
 * 参考書籍：
 * 	「最強最速アルゴリズマー養成講座 著：高橋直大」
 * P.85 全探索
 **/

load("../unittest.js");

(function(ut){
	"use strict";

	var InterestingDigits = {
		digits : function(base){
			v = [];
			
			for(var n = 2; n < base; n++){
				var ok = true;
				for(var k1 = 0; k1 < base; k1++){
					for(var k2 = 0; k2 < base; k2++){
						for(var k3 = 0; k3 < base; k3++){
							if((k1 + k2*base + k3*base*base)%n === 0 && 
							(k1 + k2 + k3)%n !== 0){
								ok = false;
								break;
							}
						}
						if (!ok) break;
					}
					if (!ok) break;
				}
				if (ok) v.push(n);
			}
			
			return v;
		}
	};

	this.main = function(){
		var result = InterestingDigits.digits(10),
		answer = [3, 9];
	
		ut.assertEqual(answer, result);
	};
}(unittest));


