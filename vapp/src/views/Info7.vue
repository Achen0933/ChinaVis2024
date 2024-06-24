<template>
  <div class="box">
    <div class="chart-title">{{ title }}类</div>
    <div ref="chart" class="echarts"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import { passInfo } from '@/api/passinfo';  // 导入 API 请求函数

export default {
  data() {
    return {
      title: "",
      chartData: null,
      chartInstance: null,  // 存储 ECharts 实例
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
        const response = await passInfo('GET', '/back/info1/');
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
      
      this.title = letter;
      const data = this.chartData[letter];
      const labels = [...data.leftData.label, ...data.rightData.label];
      const values = [...data.leftData.value, ...data.rightData.value];

      const maxVal = Math.max(...values);

      const indicators = labels.map((label) => ({
        name: label,
        max: maxVal
      }));

      const option = {
        tooltip: {
          trigger: 'item',
          z: 10000, // 设置z-index
        },
        radar: {
          indicator: indicators,
          shape: 'polygon', // 改为多边形
          center: ['50%', '50%'], // 中心位置调整，使图表更加居中
          radius: '55%', // 调整半径以确保图表完全显示
          name: {
            textStyle: {
              color: 'white',  // 标签文字白色
              borderRadius: 3,
              padding: [3, 5]
            }
          },
          splitLine: {
            lineStyle: {
              color: 'white'  // 网格线白色
            }
          },
          splitArea: {
            areaStyle: {
              color: ['rgba(255, 255, 255, 0.1)', 'rgba(255, 255, 255, 0)'],
              shadowBlur: 10
            }
          }
        },
        series: [{
          name: letter,
          type: 'radar',
          data: [{
            value: values,
            name: letter
          }],
          areaStyle: {
            opacity: 0.3
          },
          lineStyle: {
            color: this.themeColors[0]  // 使用主题颜色
          },
          itemStyle: {
            color: this.themeColors[1]  // 使用主题颜色
          }
        }],
        textStyle: {
          color: 'white'  // 全局文字颜色
        }
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
  padding: 10px;  /* 添加适当的内边距 */
  position: relative;  /* 保持子元素相对定位 */
  overflow: visible;  /* 确保内容不会被裁剪 */
}

.chart-title {
  text-align: center;
  color: white;
  font-size: 18px;  /* 调整标题大小 */
  font-weight: bold;
  margin-bottom: 10px;  /* 增加标题和图表之间的距离 */
}

.echarts {
  width: 100%;
  height: calc(100% - 40px);  /* 减去标题高度 */
  box-sizing: border-box;
  overflow: visible;  /* 防止内容溢出 */
}
</style>
