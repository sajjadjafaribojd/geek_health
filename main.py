from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

#app=Flask(__name__)
#CORS(app, support_credentials=True)

entranceـtime='09.13'
workـtime='07.30'


def exit_time_calulator_string(entrance_time,work_time):
    try:
        if int(entrance_time.split(".",-1)[0]) > 23 or int(work_time.split(".",-1)[0]) > 23 or  int(entrance_time.split(".",-1)[1]) > 59 or  int(work_time.split(".",-1)[1]) > 59:
             return "The entered data is not valid!"  
        else:
            exit_time_hour=int(entrance_time.split(".",-1)[0])+int(work_time.split(".",-1)[0]) 
            all_minute=int(entrance_time.split(".",-1)[1])+int(work_time.split(".",-1)[1]) 

        if all_minute >= 60:
            if abs(60-all_minute) < 10 :
                result=str(exit_time_hour+1)+".0"+str(all_minute-60)
            else:
                result=str(exit_time_hour+1)+"."+str(all_minute-60)    

        else:
            if  abs(all_minute-60) == 0: #entranceـtime '8.00' workـtime='8.00'
                result=str(exit_time_hour)+".00"+str(all_minute)
            elif all_minute <10:
                result=str(exit_time_hour)+".0"+str(all_minute)
            else:
                result=str(exit_time_hour)+"."+str(all_minute)
        return result 
    except Exception as e:
        return "Unknown error"           


# @app.route('/api/v1/gettime',methods=['GET'])
# @cross_origin(supports_credentials=True)
# def gettime(): 
#     try:
#        entranceـtime=request.values["e"]
#        workـtime=request.values["w"]
#        exit_time=exit_time_calulator_string(entranceـtime,workـtime)
       
#        ouput= {"exit_time":exit_time}
#        return jsonify(ouput)
    
#     except Exception as e:
#         return "Unknown error1"   

# if __name__ == '__main__':
#    app.run(debug=True,host="0.0.0.0",port=80)

print(exit_time_calulator_string(entranceـtime,workـtime))











def error_result(status,message):
    """" copilt from https://stackoverflow.com/questions/415511/how-to-get-further-information-about-python-exceptions 
    return {
        "status": status,
        "message": message,
        "traceback": traceback.format_exc()
    }
    return {
        "status":status,
        "message":message,
        "error":str(e)
    }
    return {
        "status":status,
        "message":message
    }
    """
   
def error_result2(status,message):
    results={}
    results["error"]={}
    results["error"]["status"]=status
    results["error"]['message']=message
    #return jsonify(results)




def toolbox_code():
    print(118//60) # 1
    print(118/60)  #1.966666666666667
    print(118%60)  #58  remainder of dividing
