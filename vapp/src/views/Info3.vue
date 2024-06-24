<template>
  <div class="box">
    <div ref="chart" style="width: 100%; height: 100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  data() {
    return {
      loading: false,
      themeColors: ['#516b91', '#59c4e6', '#cbef99', '#93b7e3', '#f6d676']  // 主题颜色
    }
  },
  methods: {
    getdata() {
      var myChart = echarts.init(this.$refs.chart);

      // 数据
      const data = [
        { name: '地域', value: 0.04209648 },
        { name: '经验', value: 0.48837858 },
        { name: '行业', value: -0.00661575 },
        { name: '学历', value: 0.46290919 }
      ];

      // 配置项
      var option = {
        title: {
          text: '薪酬影响因子占比分析',
          left: 'center',
          top: '10%',  // 进一步上移标题
          textStyle: {
            color: '#ffffff'  // 标题颜色
          },
          subtextStyle: {
            color: '#b0c7e7'  // 副标题颜色
          }
        },
        tooltip: {
          trigger: 'item',
          formatter: (params) => {
            const value = params.value;
            return `${params.name}: ${value == 0.00661575 ? '-' : ''}${Math.abs(value)}`;
          }
        },
        grid: {
          
        },
        series: [
          {
            type: 'treemap',
            data: data.map((item, index) => ({
              name: item.name,
              value: Math.abs(item.value),  // 取绝对值
              itemStyle: {
                color: this.themeColors[index % this.themeColors.length]  // 使用主题颜色
              }
            })),
            label: {
              show: true,
              formatter: '{b}',
              textStyle: {
                color: '#ffffff'  // 标签文字颜色
              }
            },
          }
        ]
      };

      // 使用配置项绘制图表
      myChart.setOption(option);

      // 监听窗口大小变化，使图表自适应
      window.addEventListener('resize', () => {
        myChart.resize();
      });
    }
  },
  mounted() {
    this.getdata();
  },
  beforeDestroy() {
    if (this.chartInstance) {
      window.removeEventListener('resize', this.chartInstance.resize);
    }
  }
}
</script>

<style scoped>

</style>
