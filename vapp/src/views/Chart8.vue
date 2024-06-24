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
        const response = await passInfo('GET', '/back/chart8/');  // 发起请求获取数据
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
      const labels = ['年薪', '经验水平', '教育水平', '行业热门程度'];
      const colors = ['#516b91', '#59c4e6', '#93b7e3', '#cbef99', '#f6d676'];
      const pointerColors = ['#cbef99', '#f6d676'];

      // 配置项
      const option = {
        title: {
          text: '该地区指标分析',
          left: 'center',
          textStyle: {
            color: 'white'
          },
          subtext: '单位：万元-等级-等级-等级',
          subtextStyle: {
            color: '#b0c7e7'
          }
        },
        tooltip: {
          show: true,
        },
        series: [
          {
            name: '年薪',
            type: 'gauge',
            center: ['25%', '45%'],
            radius: '50%',
            min: 0,
            max: 50,
            startAngle: 180,
            endAngle: 0,
            splitLine: {
              show: false,
              length: 10,
              lineStyle: {
                width: 2,
                color: 'white'
              }
            },
            axisLine: {
              lineStyle: {
                width: 10,
                color: [[0.3, colors[0]], [0.7, colors[1]], [1, colors[2]]]
              }
            },
            pointer: {
              color: pointerColors[0]
            },
            axisLabel: {
              show: false,
              color: 'white'
            },
            detail: {
              fontSize: 20,
              formatter: '{value}',
              color: 'white'
            },
            data: [{ value: data[0], name: '年薪', textStyle: { color: 'white' } }]
          },
          {
            name: '经验水平',
            type: 'gauge',
            center: ['75%', '45%'],
            radius: '50%',
            min: 0,
            max: 5,
            startAngle: 180,
            endAngle: 0,
            splitLine: {
              show: false,
              length: 10,
              lineStyle: {
                width: 2,
                color: 'white'
              }
            },
            axisLine: {
              lineStyle: {
                width: 10,
                color: [[0.3, colors[0]], [0.7, colors[1]], [1, colors[2]]]
              }
            },
            pointer: {
              color: pointerColors[1]
            },
            axisLabel: {
              show: false,
              color: 'white'
            },
            detail: {
              fontSize: 20,
              formatter: '{value}',
              color: 'white'
            },
            data: [{ value: data[1], name: '经验水平', textStyle: { color: 'white' } }]
          },
          {
            name: '教育水平',
            type: 'gauge',
            center: ['25%', '85%'],
            radius: '50%',
            min: 0,
            max: 5,
            startAngle: 180,
            endAngle: 0,
            splitLine: {
              show: false,
              length: 10,
              lineStyle: {
                width: 2,
                color: 'white'
              }
            },
            axisLine: {
              lineStyle: {
                width: 10,
                color: [[0.3, colors[0]], [0.7, colors[1]], [1, colors[2]]]
              }
            },
            pointer: {
              color: pointerColors[0]
            },
            axisLabel: {
              show: false,
              color: 'white'
            },
            detail: {
              fontSize: 20,
              formatter: '{value}',
              color: 'white'
            },
            data: [{ value: data[2], name: '教育水平', textStyle: { color: 'white' } }]
          },
          {
            name: '行业热门程度',
            type: 'gauge',
            center: ['75%', '85%'],
            radius: '50%',
            min: 0,
            max: 5,
            startAngle: 180,
            endAngle: 0,
            splitLine: {
              show: false,
              length: 10,
              lineStyle: {
                width: 2,
                color: 'white'
              }
            },
            axisLine: {
              lineStyle: {
                width: 10,
                color: [[0.3, colors[0]], [0.7, colors[1]], [1, colors[2]]]
              }
            },
            pointer: {
              color: pointerColors[1]
            },
            axisLabel: {
              show: false,
              color: 'white'
            },
            detail: {
              fontSize: 20,
              formatter: '{value}',
              color: 'white'
            },
            data: [{ value: data[3], name: '行业热门程度', textStyle: { color: 'white' } }]
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
