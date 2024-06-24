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
        const response = await passInfo('GET', '/back/chart5/');  // 发起请求获取数据
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
      const formattedData = Object.keys(data).map(key => ({ name: key, value: data[key] }));

      // 配置项
      const option = {
        title: {
          text: '相似地域分析',
          left: 'center',
          textStyle: {
            color: 'white'
          },
          subtext: '单位：相似系数',
          subtextStyle: {
            color: '#b0c7e7'
          }
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)',
        },
        series: [
          {
            name: '数据',
            type: 'pie',
            radius: '55%',
            center: ['50%', '60%'],
            data: formattedData,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
              },
            },
            label: {
              show: true,
              position: 'inside',
              formatter: '{b}',
              color: 'white'
            },
            labelLine: {
              show: false
            },
          },
        ],
        color: ['#516b91', '#59c4e6', '#93b7e3', '#cbef99', '#f6d676']
      };

      // 使用配置项绘制图表
      this.chartInstance.setOption(option);
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
