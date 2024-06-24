<template>
    <div ref="chart" style="width: 100%; height: 100%;"></div>
  </template>
  
<script>
import * as echarts from 'echarts'; // 导入 echarts 库
import { passInfo } from '@/api/passinfo'; // 导入 API 请求函数

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
      chartData: null, // 存储从后端获取的数据
      chartInstance: null, // 存储 ECharts 实例
    };
  },
  watch: {
    selectedLetter(newVal) {
      console.log(newVal); // 确认新的值是否正确传递
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
        const response = await passInfo('GET', '/back/chart6/'); // 发起请求获取数据
        this.chartData = response.data; // 保存数据
        console.log(this.chartData); // 输出数据以确认获取成功
        this.drawChart(this.selectedLetter); // 获取数据后立即绘制图表
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
      const formattedData = Object.keys(data).map(key => [key, ...data[key]]);

      // 配置项
      const option = {
        title: {
          text: '小辖区各指标分析',
          left: 'center',
          textStyle: {
            color: 'white'
          },
          /*subtext: '数据来源: 后端 API',
          subtextStyle: {
            color: '#b0c7e7'
          }*/
        },
        parallelAxis: [
          /*{ dim: 0, name: '名称',  nameLocation: 'start', nameTextStyle: { color: 'white' }, axisLabel: { color: 'white' } },*/
          { dim: 1, name: '年薪/万元', min: 0, nameLocation: 'start', nameTextStyle: { color: 'white' }, axisLabel: { color: 'white' } },
          { dim: 2, name: '经验等级', min: 1, max: 3, nameLocation: 'start', nameTextStyle: { color: 'white' }, axisLabel: { color: 'white' } },
          { dim: 3, name: '教育等级', min: 1, max: 3, nameLocation: 'start', nameTextStyle: { color: 'white' }, axisLabel: { color: 'white' } },
          { dim: 4, name: '行业热门程度', min: 1, max: 3, nameLocation: 'start', nameTextStyle: { color: 'white' }, axisLabel: { color: 'white' } },
        ],
        tooltip: {
          trigger: 'item',
          formatter: function (params) {
            return `${params.data[0]}<br>年薪: ${params.data[1]}<br>经验: ${params.data[2]}<br>教育: ${params.data[3]}<br>行业: ${params.data[4]}`;
          }
        },
        parallel: {
          left: '5%',
          right: '18%',
          bottom: '10%',
          top: '20%',
          parallelAxisDefault: {
            type: 'value',
            nameLocation: 'end',
            nameGap: 5,
            nameTextStyle: {
              fontSize: 12,
              color: 'white'
            },
            axisLine: {
              lineStyle: {
                color: 'white'
              }
            },
            axisTick: {
              lineStyle: {
                color: 'white'
              }
            },
            splitLine: {
              show: false
            }
          }
        },
        series: [
          {
            name: '数据',
            type: 'parallel',
            lineStyle: {
              width: 1,
              opacity: 0.5,
              color: {
                type: 'linear',
                x: 0,
                y: 0,
                x2: 1,
                y2: 1,
                colorStops: [
                  { offset: 0, color: '#f6d676' },
                  { offset: 1, color: '#516b91' }
                ]
              }
            },
            data: formattedData
          }
        ],
        color: ['#516b91', '#59c4e6', '#93b7e3', '#cbef99', '#f6d676']
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
  