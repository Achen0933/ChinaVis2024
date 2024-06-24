<template>
    <div ref="chart" style="width: 100%; height: 100%;"></div>
  </template>
  
  <script>
  import * as echarts from 'echarts';  // 导入 echarts 库
  import { passInfo } from '@/api/passinfo';  // 导入 API 请求函数
  
  export default {
    name: 'PassInfo',
    props: {
      selectedLetter: {
        type: String,
        default: 'A',
      },
    },
    data() {
      return {
        chartData: null,  // 存储从后端获取的数据
        chartInstance: null,  // 存储 ECharts 实例
      };
    },
    watch: {
      selectedLetter(newVal) {
        console.log(newVal);  // 确认新的值是否正确传递
        this.updateChart(newVal);
      },
    },
    mounted() {
      // 页面加载时自动获取数据并绘制图表
      this.getInfo();
    },
    methods: {
      async getInfo() {
        try {
          const response = await passInfo('GET', '/back/box1/');  // 发起请求获取数据
          this.chartData = response.data;  // 保存数据
          console.log(this.chartData);  // 输出数据以确认获取成功
          this.drawChart(this.selectedLetter);  // 获取数据后立即绘制图表
        } catch (error) {
          console.error('An error occurred:', error);
        }
      },
      drawChart(letter) {
        if (!this.chartData || !this.chartData[letter]) {
          console.error('Chart data is not available');
          return;
        }
  
        // 初始化 ECharts 实例
        if (!this.chartInstance) {
          this.chartInstance = echarts.init(this.$refs.chart);
        }
  
        // 准备数据
        const data = this.chartData[letter];
        const districtCount = data[0];
        const recruitmentCount = data[1];
  
        // 配置项
        const option = {
          graphic: [
            {
              type: 'text',
              left: 'center',
              top: '10%',
              style: {
                text: `辖区数：${districtCount}`,
                font: 'bold 24px sans-serif',
                fill: 'white',
              }
            },
            {
              type: 'text',
              left: 'center',
              top: '50%',
              style: {
                text: `招聘数：${recruitmentCount}`,
                font: 'bold 24px sans-serif',
                fill: 'white',
              }
            }
          ]
        };
  
        // 使用配置项绘制图表
        this.chartInstance.setOption(option);
  
        // 监听窗口大小变化，使图表自适应
        window.addEventListener('resize', () => {
          this.chartInstance.resize();
        });
      },
      updateChart(letter) {
        this.drawChart(letter);
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
  