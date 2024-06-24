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
        const response = await passInfo('GET', '/back/chart2/');  // 发起请求获取数据
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
      const data = Object.keys(this.chartData).map(key => ({
        name: key,
        value: this.chartData[key]
      }));

      // 配置项
      const option = {
        title: {
          text: '各地区年薪热力图',
          left: 'center',
          textStyle: {
            color: 'white'
          },
          subtext: '单位：年薪-万元',
          subtextStyle: {
            color: '#b0c7e7'
          }
        },
        tooltip: {
          formatter: function (info) {
            return `${info.name}: ${info.value}`;
          }
        },
        visualMap: {
          show: false,
          min: Math.min(...Object.values(this.chartData)),
          max: Math.max(...Object.values(this.chartData)),
          inRange: {
            color: ['#e0ffff', '#006edd']
          }
        },
        series: [
          {
            name: 'Letter Heatmap',
            type: 'treemap',
            data: data,
            label: {
              show: true,
              formatter: '{b}',
              color: 'white'
            },
            itemStyle: {
              borderColor: '#fff'
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