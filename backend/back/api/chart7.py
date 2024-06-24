from django.http import JsonResponse

# 这里的函数名称开头必须小写
def passChart7(request):
    # 定义需要返回的数据
    data = {
        "status": "success",
        "message": "Data retrieved successfully",
        "data": {
  "A": {
    "experience": [
      [
        2,
        3870
      ],
      [
        3,
        662
      ]
    ],
    "education": [
      [
        1,
        4
      ],
      [
        2,
        4010
      ],
      [
        3,
        518
      ]
    ],
    "company_level": [
      [
        1,
        1376
      ],
      [
        2,
        1377
      ],
      [
        3,
        1779
      ]
    ],
    "salary": [
      [
        1,
        3159
      ],
      [
        2,
        1095
      ],
      [
        3,
        246
      ],
      [
        4,
        32
      ]
    ],
    'mode': [['周薪', 1], ['日薪', 50], ['时薪', 29], ['月薪', 4367], ['绩效制', 85]], 
  },
  "B": {
    "experience": [
      [
        1,
        4
      ],
      [
        2,
        20523
      ],
      [
        3,
        8273
      ]
    ],
    "education": [
      [
        1,
        21
      ],
      [
        2,
        19187
      ],
      [
        3,
        9592
      ]
    ],
    "company_level": [
      [
        1,
        10144
      ],
      [
        2,
        7783
      ],
      [
        3,
        10873
      ]
    ],
    "salary": [
      [
        1,
        9067
      ],
      [
        2,
        11004
      ],
      [
        3,
        6663
      ],
      [
        4,
        2066
      ]
    ],
    'mode': [['周薪', 9], ['日薪', 464], ['时薪', 114], ['月薪', 23404], ['绩效制', 4809]], 
  },
  "C": {
    "experience": [
      [
        2,
        2670
      ],
      [
        3,
        407
      ]
    ],
    "education": [
      [
        2,
        2776
      ],
      [
        3,
        301
      ]
    ],
    "company_level": [
      [
        1,
        927
      ],
      [
        2,
        950
      ],
      [
        3,
        1200
      ]
    ],
    "salary": [
      [
        1,
        2306
      ],
      [
        2,
        615
      ],
      [
        3,
        125
      ],
      [
        4,
        31
      ]
    ],
    'mode': [['周薪', 1], ['日薪', 23], ['时薪', 19], ['月薪', 2969], ['绩效制', 65]], 
  },
  "D": {
    "experience": [
      [
        2,
        5197
      ],
      [
        3,
        953
      ]
    ],
    "education": [
      [
        1,
        1
      ],
      [
        2,
        5473
      ],
      [
        3,
        676
      ]
    ],
    "company_level": [
      [
        1,
        1892
      ],
      [
        2,
        1810
      ],
      [
        3,
        2448
      ]
    ],
    "salary": [
      [
        1,
        4398
      ],
      [
        2,
        1431
      ],
      [
        3,
        286
      ],
      [
        4,
        35
      ]
    ],
    'mode': [['周薪', 2], ['日薪', 50], ['时薪', 40], ['月薪', 5896], ['绩效制', 162]], 
  },
  "E": {
    "experience": [
      [
        2,
        2986
      ],
      [
        3,
        566
      ]
    ],
    "education": [
      [
        2,
        3050
      ],
      [
        3,
        502
      ]
    ],
    "company_level": [
      [
        1,
        1172
      ],
      [
        2,
        1020
      ],
      [
        3,
        1360
      ]
    ],
    "salary": [
      [
        1,
        2236
      ],
      [
        2,
        986
      ],
      [
        3,
        284
      ],
      [
        4,
        46
      ]
    ],
    'mode': [['周薪', 0], ['日薪', 33], ['时薪', 27], ['月薪', 3320], ['绩效制', 172]],
  },
  "F": {
    "experience": [
      [
        1,
        7
      ],
      [
        2,
        37292
      ],
      [
        3,
        15597
      ]
    ],
    "education": [
      [
        1,
        20
      ],
      [
        2,
        33834
      ],
      [
        3,
        19042
      ]
    ],
    "company_level": [
      [
        1,
        20129
      ],
      [
        2,
        13959
      ],
      [
        3,
        18808
      ]
    ],
    "salary": [
      [
        1,
        16895
      ],
      [
        2,
        20101
      ],
      [
        3,
        11623
      ],
      [
        4,
        4277
      ]
    ],
    'mode': [['周薪', 12], ['日薪', 913], ['时薪', 203], ['月薪', 45821], ['绩效制', 5947]], 
  },
  "G": {
    "experience": [
      [
        2,
        3340
      ],
      [
        3,
        525
      ]
    ],
    "education": [
      [
        1,
        2
      ],
      [
        2,
        3427
      ],
      [
        3,
        436
      ]
    ],
    "company_level": [
      [
        1,
        1151
      ],
      [
        2,
        1062
      ],
      [
        3,
        1652
      ]
    ],
    "salary": [
      [
        1,
        2850
      ],
      [
        2,
        841
      ],
      [
        3,
        150
      ],
      [
        4,
        24
      ]
    ],
    'mode': [['周薪', 1], ['日薪', 34], ['时薪', 22], ['月薪', 3716], ['绩效制', 92]],
  },
  "H": {
    "experience": [
      [
        2,
        2194
      ],
      [
        3,
        480
      ]
    ],
    "education": [
      [
        1,
        1
      ],
      [
        2,
        2161
      ],
      [
        3,
        512
      ]
    ],
    "company_level": [
      [
        1,
        770
      ],
      [
        2,
        827
      ],
      [
        3,
        1077
      ]
    ],
    "salary": [
      [
        1,
        1680
      ],
      [
        2,
        594
      ],
      [
        3,
        253
      ],
      [
        4,
        147
      ]
    ],
    'mode': [['周薪', 1], ['日薪', 23], ['时薪', 23], ['月薪', 2483], ['绩效制', 144]], 
  },
  "I": {
    "experience": [
      [
        1,
        1
      ],
      [
        2,
        3324
      ],
      [
        3,
        668
      ]
    ],
    "education": [
      [
        2,
        3472
      ],
      [
        3,
        521
      ]
    ],
    "company_level": [
      [
        1,
        1281
      ],
      [
        2,
        1163
      ],
      [
        3,
        1549
      ]
    ],
    "salary": [
      [
        1,
        2578
      ],
      [
        2,
        1115
      ],
      [
        3,
        267
      ],
      [
        4,
        33
      ]
    ],
    'mode': [['周薪', 0], ['日薪', 36], ['时薪', 23], ['月薪', 3805], ['绩效制', 129]], 
  },
  "J": {
    "experience": [
      [
        2,
        3309
      ],
      [
        3,
        502
      ]
    ],
    "education": [
      [
        2,
        3351
      ],
      [
        3,
        460
      ]
    ],
    "company_level": [
      [
        1,
        1099
      ],
      [
        2,
        1091
      ],
      [
        3,
        1621
      ]
    ],
    "salary": [
      [
        1,
        2803
      ],
      [
        2,
        809
      ],
      [
        3,
        161
      ],
      [
        4,
        38
      ]
    ],
    'mode': [['周薪', 1], ['日薪', 33], ['时薪', 32], ['月薪', 3675], ['绩效制', 70]], 
  },
  "K": {
    "experience": [
      [
        1,
        8
      ],
      [
        2,
        19083
      ],
      [
        3,
        9311
      ]
    ],
    "education": [
      [
        1,
        14
      ],
      [
        2,
        17200
      ],
      [
        3,
        11188
      ]
    ],
    "company_level": [
      [
        1,
        11071
      ],
      [
        2,
        7701
      ],
      [
        3,
        9630
      ]
    ],
    "salary": [
      [
        1,
        6482
      ],
      [
        2,
        10604
      ],
      [
        3,
        8181
      ],
      [
        4,
        3135
      ]
    ],
    'mode': [['周薪', 11], ['日薪', 711], ['时薪', 133], ['月薪', 22065], ['绩效制', 5482]], 
  },
  "L": {
    "experience": [
      [
        2,
        3810
      ],
      [
        3,
        628
      ]
    ],
    "education": [
      [
        1,
        1
      ],
      [
        2,
        3931
      ],
      [
        3,
        506
      ]
    ],
    "company_level": [
      [
        1,
        1266
      ],
      [
        2,
        1250
      ],
      [
        3,
        1922
      ]
    ],
    "salary": [
      [
        1,
        3179
      ],
      [
        2,
        1017
      ],
      [
        3,
        219
      ],
      [
        4,
        23
      ]
    ],
    'mode': [['周薪', 3], ['日薪', 45], ['时薪', 31], ['月薪', 4275], ['绩效制', 84]], 
  },
  "M": {
    "experience": [
      [
        2,
        3140
      ],
      [
        3,
        429
      ]
    ],
    "education": [
      [
        1,
        1
      ],
      [
        2,
        3245
      ],
      [
        3,
        323
      ]
    ],
    "company_level": [
      [
        1,
        1028
      ],
      [
        2,
        1044
      ],
      [
        3,
        1497
      ]
    ],
    "salary": [
      [
        1,
        2690
      ],
      [
        2,
        708
      ],
      [
        3,
        141
      ],
      [
        4,
        30
      ]
    ],
    'mode': [['周薪', 1], ['日薪', 25], ['时薪', 36], ['月薪', 3450], ['绩效制', 57]], 
  },
  "N": {
    "experience": [
      [
        1,
        3
      ],
      [
        2,
        19554
      ],
      [
        3,
        6920
      ]
    ],
    "education": [
      [
        1,
        17
      ],
      [
        2,
        18894
      ],
      [
        3,
        7566
      ]
    ],
    "company_level": [
      [
        1,
        10426
      ],
      [
        2,
        7423
      ],
      [
        3,
        8628
      ]
    ],
    "salary": [
      [
        1,
        9575
      ],
      [
        2,
        10574
      ],
      [
        3,
        5165
      ],
      [
        4,
        1163
      ]
    ],
    'mode': [['周薪', 7], ['日薪', 271], ['时薪', 123], ['月薪', 21952], ['绩效制', 4124]], 
  },
  "O": {
    "experience": [
      [
        1,
        4
      ],
      [
        2,
        20631
      ],
      [
        3,
        6709
      ]
    ],
    "education": [
      [
        1,
        13
      ],
      [
        2,
        19462
      ],
      [
        3,
        7869
      ]
    ],
    "company_level": [
      [
        1,
        10225
      ],
      [
        2,
        7386
      ],
      [
        3,
        9733
      ]
    ],
    "salary": [
      [
        1,
        14075
      ],
      [
        2,
        9556
      ],
      [
        3,
        3100
      ],
      [
        4,
        613
      ]
    ],
    'mode': [['周薪', 11], ['日薪', 303], ['时薪', 94], ['月薪', 24865], ['绩效制', 2071]], 
  },
  "P": {
    "experience": [
      [
        1,
        4
      ],
      [
        2,
        20927
      ],
      [
        3,
        9233
      ]
    ],
    "education": [
      [
        1,
        9
      ],
      [
        2,
        20772
      ],
      [
        3,
        9383
      ]
    ],
    "company_level": [
      [
        1,
        11967
      ],
      [
        2,
        7936
      ],
      [
        3,
        10261
      ]
    ],
    "salary": [
      [
        1,
        8927
      ],
      [
        2,
        11079
      ],
      [
        3,
        7419
      ],
      [
        4,
        2739
      ]
    ],
    'mode': [['周薪', 9], ['日薪', 327], ['时薪', 104], ['月薪', 25496], ['绩效制', 4228]], 
  },
  "Q": {
    "experience": [
      [
        2,
        2278
      ],
      [
        3,
        364
      ]
    ],
    "education": [
      [
        1,
        1
      ],
      [
        2,
        2324
      ],
      [
        3,
        317
      ]
    ],
    "company_level": [
      [
        1,
        760
      ],
      [
        2,
        737
      ],
      [
        3,
        1145
      ]
    ],
    "salary": [
      [
        1,
        1892
      ],
      [
        2,
        620
      ],
      [
        3,
        117
      ],
      [
        4,
        13
      ]
    ],
    'mode': [['周薪', 1], ['日薪', 20], ['时薪', 20], ['月薪', 2522], ['绩效制', 79]], 
  },
  "R": {
    "experience": [
      [
        1,
        6
      ],
      [
        2,
        19698
      ],
      [
        3,
        7228
      ]
    ],
    "education": [
      [
        1,
        13
      ],
      [
        2,
        19562
      ],
      [
        3,
        7357
      ]
    ],
    "company_level": [
      [
        1,
        9887
      ],
      [
        2,
        7253
      ],
      [
        3,
        9792
      ]
    ],
    "salary": [
      [
        1,
        12542
      ],
      [
        2,
        9809
      ],
      [
        3,
        3892
      ],
      [
        4,
        689
      ]
    ],
    'mode': [['周薪', 4], ['日薪', 314], ['时薪', 112], ['月薪', 23669], ['绩效制', 2833]], 
  },
  "S": {
    "experience": [
      [
        1,
        5
      ],
      [
        2,
        37188
      ],
      [
        3,
        13108
      ]
    ],
    "education": [
      [
        1,
        23
      ],
      [
        2,
        35616
      ],
      [
        3,
        14662
      ]
    ],
    "company_level": [
      [
        1,
        19050
      ],
      [
        2,
        13675
      ],
      [
        3,
        17576
      ]
    ],
    "salary": [
      [
        1,
        20621
      ],
      [
        2,
        20195
      ],
      [
        3,
        7996
      ],
      [
        4,
        1489
      ]
    ],
    'mode': [['周薪', 13], ['日薪', 573], ['时薪', 221], ['月薪', 41991], ['绩效制', 7503]], 
  },
  "T": {
    "experience": [
      [
        2,
        1779
      ],
      [
        3,
        294
      ]
    ],
    "education": [
      [
        1,
        1
      ],
      [
        2,
        1861
      ],
      [
        3,
        211
      ]
    ],
    "company_level": [
      [
        1,
        568
      ],
      [
        2,
        616
      ],
      [
        3,
        889
      ]
    ],
    "salary": [
      [
        1,
        1534
      ],
      [
        2,
        432
      ],
      [
        3,
        99
      ],
      [
        4,
        8
      ]
    ],
    'mode': [['周薪', 1], ['日薪', 10], ['时薪', 18], ['月薪', 1990], ['绩效制', 54]], 
  },
  "U": {
    "experience": [
      [
        2,
        3315
      ],
      [
        3,
        567
      ]
    ],
    "education": [
      [
        1,
        3
      ],
      [
        2,
        3445
      ],
      [
        3,
        434
      ]
    ],
    "company_level": [
      [
        1,
        1105
      ],
      [
        2,
        1160
      ],
      [
        3,
        1617
      ]
    ],
    "salary": [
      [
        1,
        2673
      ],
      [
        2,
        971
      ],
      [
        3,
        212
      ],
      [
        4,
        26
      ]
    ],
     'mode': [['周薪', 0], ['日薪', 40], ['时薪', 40], ['月薪', 3681], ['绩效制', 121]], 
  },
  "V": {
    "experience": [
      [
        1,
        8
      ],
      [
        2,
        36116
      ],
      [
        3,
        12611
      ]
    ],
    "education": [
      [
        1,
        32
      ],
      [
        2,
        34585
      ],
      [
        3,
        14118
      ]
    ],
    "company_level": [
      [
        1,
        18053
      ],
      [
        2,
        13048
      ],
      [
        3,
        17634
      ]
    ],
    "salary": [
      [
        1,
        23713
      ],
      [
        2,
        17766
      ],
      [
        3,
        6146
      ],
      [
        4,
        1110
      ]
    ],
     'mode': [['周薪', 14], ['日薪', 653], ['时薪', 234], ['月薪', 44064], ['绩效制', 3770]], 
  },
  "W": {
    "experience": [
      [
        2,
        2313
      ],
      [
        3,
        320
      ]
    ],
    "education": [
      [
        1,
        2
      ],
      [
        2,
        2376
      ],
      [
        3,
        255
      ]
    ],
    "company_level": [
      [
        1,
        787
      ],
      [
        2,
        736
      ],
      [
        3,
        1110
      ]
    ],
    "salary": [
      [
        1,
        1944
      ],
      [
        2,
        573
      ],
      [
        3,
        96
      ],
      [
        4,
        20
      ]
    ],
    'mode': [['周薪', 0], ['日薪', 24], ['时薪', 10], ['月薪', 2521], ['绩效制', 78]], 
  },
  "X": {
    "experience": [
      [
        2,
        2392
      ],
      [
        3,
        496
      ]
    ],
    "education": [
      [
        2,
        2592
      ],
      [
        3,
        296
      ]
    ],
    "company_level": [
      [
        1,
        864
      ],
      [
        2,
        893
      ],
      [
        3,
        1131
      ]
    ],
    "salary": [
      [
        1,
        1785
      ],
      [
        2,
        858
      ],
      [
        3,
        209
      ],
      [
        4,
        36
      ]
    ],
    'mode': [['周薪', 0], ['日薪', 35], ['时薪', 9], ['月薪', 2756], ['绩效制', 88]], 
  },
  "Y": {
    "experience": [
      [
        1,
        8
      ],
      [
        2,
        37937
      ],
      [
        3,
        14629
      ]
    ],
    "education": [
      [
        1,
        32
      ],
      [
        2,
        37268
      ],
      [
        3,
        15274
      ]
    ],
    "company_level": [
      [
        1,
        20091
      ],
      [
        2,
        14329
      ],
      [
        3,
        18154
      ]
    ],
    "salary": [
      [
        1,
        20374
      ],
      [
        2,
        19903
      ],
      [
        3,
        9865
      ],
      [
        4,
        2432
      ]
    ],
     'mode': [['周薪', 9], ['日薪', 889], ['时薪', 189], ['月薪', 44744], ['绩效制', 6743]], 
  },
  "Z": {
    "experience": [
      [
        2,
        3401
      ],
      [
        3,
        592
      ]
    ],
    "education": [
      [
        1,
        2
      ],
      [
        2,
        3583
      ],
      [
        3,
        408
      ]
    ],
    "company_level": [
      [
        1,
        1138
      ],
      [
        2,
        1148
      ],
      [
        3,
        1707
      ]
    ],
    "salary": [
      [
        1,
        2858
      ],
      [
        2,
        928
      ],
      [
        3,
        182
      ],
      [
        4,
        25
      ]
    ],
    'mode': [['周薪', 2], ['日薪', 33], ['时薪', 24], ['月薪', 3814], ['绩效制', 120]],
  }
}
    }
    # 返回json类型数据
    return JsonResponse(data)
