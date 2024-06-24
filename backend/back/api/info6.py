from django.http import JsonResponse
 
def passInfo6(request):
    data = {
        "status": "success",
        "message": "Data retrieved successfully",
        "data": {
            "小地区低经验中学历": {
                '月薪': 1
            },
            "小地区中经验低学历": {
                '日薪': 19
            },
            "小地区中经验中学历": {
                '月薪': 43121, '绩效制': 819, '日薪': 468, '时薪': 328, '周薪': 11
            },
            "小地区中经验高学历": {
                '月薪': 4198, '绩效制': 284, '时薪': 49, '日薪': 19, '周薪': 2
            },
            "小地区高经验中学历": {
                '月薪': 6052, '绩效制': 256, '时薪': 14, '日薪': 6, '周薪': 1
            },
            "小地区高经验高学历": {
                '月薪': 1868, '绩效制': 241, '时薪': 12, '日薪': 2, '周薪': 1
            },
            "中地区低经验中学历": {
                '月薪': 16
            },
            "中地区低经验高学历": {
                '月薪': 13
            },
            "中地区中经验低学历": {
                '日薪': 87
            },
            "中地区中经验中学历": {
                '月薪': 84558, '绩效制': 5770, '日薪': 2233, '时薪': 469, '周薪': 37
            },
            "中地区中经验高学历": {
                '月薪': 20799, '绩效制': 6272, '时薪': 134, '日薪': 52, '周薪': 5
            },
            "中地区高经验中学历": {
                '月薪': 19009, '绩效制': 2941, '时薪': 31, '日薪': 9, '周薪': 4
            },
            "中地区高经验高学历": {
                '月薪': 17056, '绩效制': 8564, '时薪': 46, '日薪': 9, '周薪': 5
            },
            "大地区低经验低学历": {
                '日薪': 2
            },
            "大地区低经验中学历": {
                '月薪': 8
            },
            "大地区低经验高学历": {
                '月薪': 18
            },
            "大地区中经验低学历": {
                '日薪': 105
            },
            "大地区中经验中学历": {
                '月薪': 105256, '绩效制': 6309, '日薪': 2807, '时薪': 521, '周薪': 29
            },
            "大地区中经验高学历": {
                '月薪': 26708, '绩效制': 6492, '时薪': 213, '日薪': 79, '周薪': 14
            },
            "大地区高经验中学历": {
                '月薪': 23367, '绩效制': 2947, '时薪': 37, '日薪': 21, '周薪': 1
            },
            "大地区高经验高学历": {
                '月薪': 21263, '绩效制': 8215, '时薪': 76, '日薪': 14, '周薪': 4
            }
        }
    }
    
    return JsonResponse(data)

