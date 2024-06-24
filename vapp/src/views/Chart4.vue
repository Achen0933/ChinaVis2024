<template>
    <div ref="chart" style="width: 100%; height: 100%;"></div>
  </template>
  
  <script>
import * as echarts from 'echarts';  // 导入 echarts 库
import { passInfo } from '@/api/passinfo';  // 导入 API 请求函数

export default {
  name: 'PassInfo',
  data() {
    return {
      chartData: null,  // 存储从后端获取的数据
      chartInstance: null,  // 存储 ECharts 实例
    };
  },
  mounted() {
    // 页面加载时自动获取数据并绘制图表
    this.getInfo();
  },
  methods: {
    async getInfo() {
      try {
        const response = await passInfo('GET', '/back/chart4/');  // 发起请求获取数据
        this.chartData = response.data;  // 保存数据
        console.log(this.chartData);  // 输出数据以确认获取成功
        this.drawChart();  // 获取数据后立即绘制图表
      } catch (error) {
        console.error('An error occurred:', error);
      }
    },
    drawChart() {
      if (!this.chartData) {
        console.error('Chart data is not available');
        return;
      }

      // 初始化 ECharts 实例
      this.chartInstance = echarts.init(this.$refs.chart);

      // 准备数据
      const processedData = this.chartData.map((item) => [item[0] - 1, item[1] - 1, item[2]]);

      // 配置项
      const option = {
        title: {
          text: '学历-经验相关数分析',
          left: 'center',
          textStyle: {
            color: 'white'
          },
          subtext: '单位：招聘数-条',
          subtextStyle: {
            color: '#b0c7e7'
          }
        },
        tooltip: {
          position: 'top',
          formatter: function (params) {
            return (
              '经验: ' + (params.value[0] + 1) + // 恢复实际值
              '<br>学历: ' + (params.value[1] + 1) + // 恢复实际值
              '<br>数量: ' + params.value[2]
            );
          },
        },
        xAxis: {
          type: 'category',
          data: ['低', '中', '高'],
          name: '经验',
          axisLabel: {
            interval: 0,
            color: 'white'
          },
          axisLine: {
            lineStyle: {
              color: 'white'
            }
          }
        },
        yAxis: {
          type: 'category',
          data: ['低', '中', '高'],
          name: '学历',
          axisLabel: {
            interval: 0,
            color: 'white'
          },
          axisLine: {
            lineStyle: {
              color: 'white'
            }
          }
        },
        visualMap: {
          min: 0,
          max: Math.max(...this.chartData.map((d) => d[2])),
          calculable: true,
          orient: 'horizontal',
          left: 'center',
          bottom: '15%',
          inRange: {
            color: ['#516b91', '#59c4e6', '#93b7e3', '#cbef99', '#f6d676']
          },
          textStyle: {
            color: 'white'
          }
        },
        series: [
          {
            name: '数据',
            type: 'heatmap',
            data: processedData,
            label: {
              show: true,
              formatter: function (params) {
                return params.value[2];
              },
              color: 'white'
            },
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
              },
            },
          },
        ],
      };

      // 使用配置项绘制图表
      this.chartInstance.setOption(option);

      // 监听窗口大小变化，使图表自适应
      window.addEventListener('resize', () => {
        this.chartInstance.resize();
      });
    },
  },
};
</script>


<style scoped>
/* 确保容器有明确的尺寸 */
div[ref="chart"] {
width: 100%;
height: 100%;
}
</style>