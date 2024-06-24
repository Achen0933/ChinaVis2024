from django.urls import path
 
#通过.做相当路径导入，适用于包内导入
from .api import chart1
from .api import chart2
from .api import chart3
from .api import chart4
from .api import chart5
from .api import chart6
from .api import chart7
from .api import chart8
from .api import box1
from .api import info1
from .api import info2
from .api import info4
from .api import info5
from .api import info6
urlpatterns = [
    #路径http://127.0.0.1:8000/back/chart1，访问即通过函数passChart1返回chart1的json数据
    path("chart1/",chart1.passChart1),
    #添加后续的
    path("chart2/",chart2.passChart2),
    path("chart3/",chart3.passChart3),
    path("chart4/",chart4.passChart4),
    path("chart5/",chart5.passChart5),
    path("chart6/",chart6.passChart6),
    path("chart7/",chart7.passChart7),
    path("chart8/",chart8.passChart8),
    path("box1/",box1.passBox1),
    path("info1/",info1.passInfo1),
    path("info2/",info2.passInfo2),
    path("info4/",info4.passInfo4),
    path("info5/",info5.passInfo5),
    path("info6/",info6.passInfo6),
]