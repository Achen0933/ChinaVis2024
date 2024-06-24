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
        const response = await passInfo('GET', '/back/info5/');
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
          text: '画像地区招聘数排名',
          left: 'center',
          top: '5%',  // 增加标题距离顶部的距离，确保不被遮挡
          textStyle: {
            color: '#ffffff',  // 标题颜色
            fontSize: 18       // 可以适当减小标题字体大小
          },
          /*subtext: '单位:个',
          subtextStyle: {
            color: '#b0c7e7',  // 副标题颜色
            fontSize: 14       // 可以适当减小副标题字体大小
          }*/
        },
        grid: {
          left: '20%',  // 调整左边距
          right: '10%', // 调整右边距
          bottom: '15%', // 调整下边距不必要太大
          top: '28%'    // 进一步增加图表顶部与标题的间距
        },
        tooltip: {
          trigger: 'item',  // 触发类型，'item' 表示数据项触发
          formatter: '{b}: {c}'  // 标签显示格式，这里表示“类别: 值”
        },
        xAxis: {
          data: xdata,
          axisLabel: {
            inside: true,
            color: '#ffffff'  // 坐标轴文字颜色
          },
          axisTick: {
            show: false
          },
          axisLine: {
            show: false
          },
          z: 10
        },
        yAxis: {
          axisLine: {
            show: false
          },
          axisTick: {
            show: false
          },
          axisLabel: {
            color: '#ffffff'  // 坐标轴文字颜色
          }
        },
        dataZoom: [
          {
            type: 'inside'
          }
        ],
        series: [
          {
            type: 'bar',
            showBackground: true,
            backgroundStyle: {
              color: 'rgba(180, 180, 180, 0.2)'
            },
            itemStyle: {
              color: (params) => {
                return this.themeColors[params.dataIndex % this.themeColors.length];
              }
            },
            label: {
              show: true,
              position: 'insideTop',
              color: '#ffffff' // 数据值文字颜色
            },
            emphasis: {
              itemStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  { offset: 0, color: '#2378f7' },
                  { offset: 0.7, color: '#2378f7' },
                  { offset: 1, color: '#83bff6' }
                ])
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
  padding: 20px 20px 0 20px;  /* 添加适当的内边距，增加顶部空间 */
  box-sizing: border-box;
}

.echarts {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
}
</style>
