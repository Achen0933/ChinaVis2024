from django.http import JsonResponse
 
#这里的函数名称开头必须小写
def passChart4(request):
    # 定义需要返回的数据
    data = {
        "status": "success",
        "message": "Data retrieved successfully",
        "data":  [[1, 1, 2], [1, 2, 25], [1, 3, 31], [2, 1, 211], [2, 2, 252736],  
                  [2, 3, 65320], [3, 1, 0],[3, 2, 54696], [3, 3, 57376]]
    }
 
    #返回json类型数据
    return JsonResponse(data)