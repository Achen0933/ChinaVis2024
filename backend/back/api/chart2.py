from django.http import JsonResponse
 
#这里的函数名称开头必须小写
def passChart2(request):
    # 定义需要返回的数据
    data = {
        "status": "success",
        "message": "Data retrieved successfully",
        "data": {"A": 7.58, "B": 13.7, "C": 7.27, 
 "D": 7.39, "E": 8.46, "F": 14.16,
 "G": 7.17, "H": 10.44, "I": 8.08, 
 "J": 7.37, "K": 16.41, "L": 7.29, "M": 7.16, 
 "N": 12.14, "O": 9.81, "P": 14.79, "Q": 7.28, "R": 10.43, 
 "S": 11.08, "T": 7.12, "U": 7.66, "V": 10.06, "W": 7.14, "X": 8.35,
 "Y": 12.09, "Z": 7.35}
    }
 
    #返回json类型数据
    return JsonResponse(data)