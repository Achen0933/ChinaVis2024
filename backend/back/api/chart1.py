from django.http import JsonResponse
 
def passChart1(request):
    data = {
        "status": "success",
        "message": "Data retrieved successfully",
        # A-Z每个区的招聘信息数量
        "data": { 
            'A': 4532, 'B': 28800, 'C': 3077, 'D': 6150, 'E': 3552, 'F': 52896, 'G': 3865, 'H': 2674, 'I': 3993, 
            'J': 3811, 'K': 28402, 'L': 4438, 'M': 3569, 'N': 26477, 'O': 27344, 'P': 30164, 'Q': 2642, 'R': 26932, 
            'S': 50301, 'T': 2073, 'U': 3882, 'V': 48735, 'W': 2633, 'X': 2888, 'Y': 52574, 'Z': 3993,
        }
    }

    return JsonResponse(data)

