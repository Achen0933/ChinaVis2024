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
          const response = await passInfo('GET', '/back/chart3/');  // 发起请求获取数据
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
        const letters = Object.keys(this.chartData);  // 获取字母数组
        const highQuality = [];
        const mediumQuality = [];
        const lowQuality = [];
  
        letters.forEach(letter => {
          highQuality.push(this.chartData[letter][0]);
          mediumQuality.push(this.chartData[letter][1]);
          lowQuality.push(this.chartData[letter][2]);
        });
  
        // 配置项
        const option = {
          title: {
            text: '各地区需求人才质量分布',
            left: 'center',
            textStyle: {
              color: 'white'
            },
            subtext: '质量：经验-教育等级',
            subtextStyle: {
              color: '#b0c7e7'
            }
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            }
          },
          legend: {
            data: ['弱质量', '中质量', '高质量'],
            bottom: 0,
            textStyle: {
              color: 'white'
            }
          },
          xAxis: {
            type: 'category',
            data: letters,
            axisLine: {
              lineStyle: {
                color: 'white'
              }
            },
            axisLabel: {
              color: 'white'
            }
          },
          yAxis: {
            type: 'value',
            axisLine: {
              lineStyle: {
                color: 'white'
              }
            },
            splitLine: {
              lineStyle: {
                color: 'white'
              }
            },
            axisLabel: {
              color: 'white'
            }
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '10%',
            containLabel: true
          },
          color: ['#516b91', '#59c4e6', '#93b7e3', '#cbef99', '#f6d676'],
          series: [
            {
              name: '高质量',
              type: 'bar',
              stack: '总量',
              data: lowQuality
            },
            {
              name: '中质量',
              type: 'bar',
              stack: '总量',
              data: mediumQuality
            },
            {
              name: '弱质量',
              type: 'bar',
              stack: '总量',
              data: highQuality
            }
          ]
        };
  
        // 使用配置项绘制图表
        this.chartInstance.setOption(option);
  
        // 监听窗口大小变化，使图表自适应
        window.addEventListener('resize', () => {
          this.chartInstance.resize();
        });
      }
    }
  };
  </script>
  


<style scoped>
/* 确保容器有明确的尺寸 */
div[ref="chart"] {
  width: 100%;
  height: 100%;
}
</style>