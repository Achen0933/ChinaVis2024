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
        const response = await passInfo('GET', '/back/info2/');
        this.chartData = response.data;  // 保存数据
        console.log(this.chartData);  // 输出数据以确认获取成功
        this.drawChart(this.selectedLetter);  // 获取数据后立即绘制图表
      } catch (error) {
        console.error('An error occurred:', error);
      }
    },
    calculateQuartiles(min, median, max) {
      const lowerQuartile = min + 0.25 * (median - min);
      const upperQuartile = median + 0.25 * (max - median);
      return [lowerQuartile, upperQuartile];
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
      const xData = Object.keys(data);
      const yData = xData.map(key => {
        const values = data[key];
        const [min, median, max] = values;
        const [q1, q3] = this.calculateQuartiles(min, median, max);
        return [min, q1, median, q3, max];
      });

      const option = {
        title: {
          text: '单指标薪酬分布分析',
          left: 'center',
          top: '2%',  // 增加标题距离顶部的距离
          textStyle: {
            color: '#ffffff'  // 标题颜色
          },
          subtext: '单位:万元',  // 添加副标题示例
          subtextStyle: {
            color: '#b0c7e7'  // 副标题颜色
          }
        },
        grid: {
          left: '8%',  // 增加左边距，向右移动图表
          right: '10%',
          bottom: '10%',
          top: '30%'  // 增加图表顶部与标题的间距
        },
        tooltip: {
          trigger: 'item',
          formatter: (param) => {
            const value = yData[param.value[0]];
            return `${param.name}<br/>
                    最小值: ${value[0]}<br/>
                    下四分位数: ${value[1]}<br/>
                    中位数: ${value[2]}<br/>
                    上四分位数: ${value[3]}<br/>
                    最大值: ${value[4]}`;
          }
        },
        xAxis: {
          type: 'category',
          data: xData,
          boundaryGap: true,
          nameGap: 30,
          splitArea: {
            show: false
          },
          axisLabel: {
            formatter: '{value}',
            color: '#ffffff'  // 坐标轴标签颜色
          },
          splitLine: {
            show: false
          },
          axisLine: {
            lineStyle: {
              color: '#ffffff'  // 坐标轴线颜色
            }
          }
        },
        yAxis: {
          type: 'value', // 普通刻度
          scale: true, // 使用 scale 属性
          min: 'dataMin', // 自适应最小值
          max: 'dataMax', // 自适应最大值
          splitArea: {
            show: true,
            areaStyle: {
              color: 'rgba(255, 255, 255, 0.1)'  // 网格线颜色
            }
          },
          axisLabel: {
            color: '#ffffff'  // 坐标轴标签颜色
          },
          axisLine: {
            lineStyle: {
              color: '#ffffff'  // 坐标轴线颜色
            }
          },
          splitLine: {
            lineStyle: {
              color: '#ffffff'  // 网格线颜色
            }
          }
        },
        series: [{
          name: 'boxplot',
          type: 'boxplot',
          data: yData,
          itemStyle: {
            color: '#59c4e6',  // 系列颜色，针对特定系列
            borderColor: '#516b91'  // 边框颜色
          },
        }],
        color: ['#516b91', '#59c4e6', '#93b7e3', '#cbef99', '#f6d676']  // 主题颜色
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
  padding: 0px;  /* 添加适当的内边距 */
}

.echarts {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
}
</style>
