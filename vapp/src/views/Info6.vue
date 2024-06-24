<template>
  <div class="box">
    <div ref="chart" style="width: 100%; height: 100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import { passInfo } from '@/api/passinfo';  // 导入 API 请求函数

export default {
  data() {
    return {
      chartData: null,
      chartInstance: null,  // 存储 ECharts 实例
      resizeHandler: null,  // 保存 resize 事件处理器引用
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
  beforeDestroy() {
    // 组件销毁前移除 resize 事件监听器
    if (this.resizeHandler) {
      window.removeEventListener('resize', this.resizeHandler);
    }
  },
  methods: {
    async getInfo() {
      try {
        const response = await passInfo('GET', '/back/info6/');
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
      const xdata = Object.keys(data);
      const ydata = Object.values(data);

      const option = {
        title: {
          text: '画像薪酬模式统计',
          left: 'center',
          textStyle: {
            color: '#ffffff'  // 标题颜色
          },
          subtext: '单位:个',  // 添加副标题示例
          subtextStyle: {
            color: '#b0c7e7'  // 副标题颜色
          }
        },
        grid: {
          left: '20%',  // 增加左边距以保证纵坐标数值显示
          right: '10%', // 调整右边距
          bottom: '20%', // 调整下边距
          top: '20%' // 调整上边距
        },
        tooltip: {
          trigger: 'item',  // 触发类型，'item' 表示数据项触发
          formatter: '{b}: {c}'  // 标签显示格式，这里表示“类别: 值”
        },
        xAxis: {
          data: xdata,
          axisTick: { show: false },
          axisLine: { show: false },
          axisLabel: {
            color: '#ffffff'  // 坐标轴文字颜色
          }
        },
        yAxis: {
          type: 'log', // 使用对数刻度
          logBase: 10, // 对数底数
          splitLine: { show: false },
          axisTick: { show: false },
          axisLine: { show: false },
          axisLabel: { 
            color: '#ffffff',  // 坐标轴文字颜色
            fontSize: 12, // 增加字体大小
            rotate: 45, // 旋转角度
          }
        },
        color: this.themeColors, // 设置主题颜色
        series: [
          {
            name: 'hill',
            type: 'pictorialBar',
            barCategoryGap: '-130%',
            symbol: 'path://M0,10 L10,10 C5.5,10 5.5,5 5,0 C4.5,5 4.5,10 0,10 z',
            itemStyle: {
              color: (params) => {
                return this.themeColors[params.dataIndex % this.themeColors.length];
              },
              opacity: 0.5
            },
            emphasis: {
              itemStyle: {
                opacity: 1
              }
            },
            data: ydata
          }
        ],
        textStyle: {
          color: '#ffffff'  // 全局文字颜色
        }
      };

      // 使用配置项绘制图表
      this.chartInstance.setOption(option);

      // 监听窗口大小变化，使图表自适应
      this.resizeHandler = () => {
        this.chartInstance.resize();
      };
      window.addEventListener('resize', this.resizeHandler);
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
  padding: 20px;  /* 添加适当的内边距 */
}

.echarts {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
}
</style>
