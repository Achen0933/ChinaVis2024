<template>
  <div ref="chart" style="width: 100%; height: 100%;"></div>
</template>

<script>
import * as echarts from 'echarts';  // 导入 echarts 库
import 'echarts-wordcloud';  // 导入 echarts-wordcloud 插件
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
        const response = await passInfo('GET', '/back/chart7/');  // 发起请求获取数据
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
      const words = [];

      // 处理经验数据
      const experienceMap = { 1: '低经验', 2: '中经验', 3: '高经验' };
      data.experience.forEach(item => {
        words.push({ name: experienceMap[item[0]], value: item[1] });
      });

      // 处理教育数据
      const educationMap = { 1: '低学历', 2: '中学历', 3: '高学历' };
      data.education.forEach(item => {
        words.push({ name: educationMap[item[0]], value: item[1] });
      });

      // 处理公司级别数据
      const companyLevelMap = { 1: '冷门行业', 2: '普通行业', 3: '热门行业' };
      data.company_level.forEach(item => {
        words.push({ name: companyLevelMap[item[0]], value: item[1] });
      });

      // 处理薪资数据
      const salaryMap = { 1: '低薪', 2: '小康', 3: '中产', 4: '高薪' };
      data.salary.forEach(item => {
        words.push({ name: salaryMap[item[0]], value: item[1] });
      });

      // 处理薪酬模式数据
      data.mode.forEach(item => {
        words.push({ name: item[0], value: item[1] });
      });

      // 配置项
      const option = {
        title: {
          text: '该地区关键词词云分析',
          left: 'center',
          textStyle: {
            color: 'white'
          },
          subtext: '',
          subtextStyle: {
            color: '#b0c7e7'
          }
        },
        tooltip: {
          show: true,
        },
        series: [
          {
            type: 'wordCloud',
            gridSize: 10,
            sizeRange: [10, 30],  // 调整词的字号
            rotationRange: [0, 0], // 固定旋转角度为0
            shape: 'circle',  // 使用圆形
            width: '100%',
            height: '100%',
            drawOutOfBound: false,
            textStyle: {
              normal: {
                color: (params) => {
                  const colors = ['#516b91', '#59c4e6', '#93b7e3', '#cbef99', '#f6d676'];
                  return colors[params.dataIndex % colors.length];
                },
              },
              emphasis: {
                shadowBlur: 10,
                shadowColor: '#333'
              }
            },
            data: words
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
