<template>
  <div class="box">
    <div ref="chart" style="width: 100%; height: 100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import { passInfo } from '@/api/passinfo';

export default {
  data() {
    return {
      chartData: null,
      chartInstance: null,
      themeColors: ['#516b91', '#59c4e6', '#93b7e3', '#cbef99', '#f6d676'] // 主题颜色
    }
  },
  props: {
    selectedLetter: {
      type: String,
      default: '大地区高经验高学历',
    },
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
        const response = await passInfo('GET', '/back/info4/');
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

      const data = this.chartData[letter];
      const formattedData = Object.keys(data).map((key) => ({
        name: key,
        value: data[key],
        itemStyle: {
          color: this.themeColors[Object.keys(data).indexOf(key) % this.themeColors.length]
        }
      }));

      const option = {
        title: {
          text: '画像行业热门程度分布',
          left: 'center',
          textStyle: {
            color: '#ffffff'  // 标题颜色
          },
          subtext: '单位:个',  // 添加副标题示例
          subtextStyle: {
            color: '#b0c7e7'  // 副标题颜色
          }
        },
        tooltip: {
          trigger: 'item',
          formatter: '{b}: {c}'
        },
        series: [
          {
            name: '热门程度',
            type: 'funnel',
            sort: 'descending',  // 倒三角形
            height: "70%",
            label: {
              show: true,
              position: 'inside',
              formatter: '{b}: {c}',
              color: '#ffffff'  // 标签文字颜色
            },
            data: formattedData,
          }
        ],
        textStyle: {
          color: '#ffffff',  // 文字颜色
        },
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
  }
};
</script>

<style scoped>
.box {
  width: 100%;
  height: 100%;
}

</style>
