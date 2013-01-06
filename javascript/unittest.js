/**
 * Unittest utility functions.
 * This is tested on SpiderMonkey 1.8.0.
 **/

if(!this.assert){
	var assert = function(b){
		if(b){
			return;
		}
		
		throw new Error("failed");
	}
}

var unittest = {
	assertEqual : function(ans, res){
		try{
			if(ans.length != null && res.length != null){/* TODO:Not enough array checking. */
				for(var i = 0, len = res.length; i<len; i++){
					assert(res[i] === ans[i]);
				}
			}else{
				assert(ans === res);
			}
			
			print("OK");
		}catch(e){
			print(e.message);
			print("ANSWER:" + ans);
			print("RESULT:" + res);
		}
	}
};
