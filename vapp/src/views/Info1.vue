<template>
  <div id="main">
    <div class="title">当前: {{ title }}类</div>
    <div class="container">
      <div class="left-panel">
        <div v-for="(label, index) in leftData.label" :key="index" class="info-box">
          <img :src="require('@/assets/icons/icon1.png')" alt="icon" class="icon">
          <span>{{ label }}</span>
          <span>{{ leftData.value[index] }}</span>
        </div>
      </div>

      <div ref="container" class="central-container">
        <img :src="require('@/assets/icons/icon2.png')" alt="central image" class="central-image">
      </div>

      <div class="right-panel">
        <div v-for="(label, index) in rightData.label" :key="index" class="info-box">
          <img :src="require('@/assets/icons/icon1.png')" alt="icon" class="icon">
          <span>{{ label }}</span>
          <span>{{ rightData.value[index] }}</span>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { passInfo } from '@/api/passinfo';  // 导入 API 请求函数

export default {
  data() {
    return {
      chartData: null,
      title: "",
      leftData:null,
      rightData:null,
      themeColors: ['#516b91', '#59c4e6', '#93b7e3', '#cbef99', '#f6d676']  // 主题颜色
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
      } 
      catch (error) {
        console.error('An error occurred:', error);
      }
    },
    drawChart(letter) {
      if (!this.chartData || !this.chartData[letter]) {
        console.error('Chart data is not available');
        return;
      }
      
      this.title = letter;
      const data = this.chartData[letter];
      this.leftData = data.leftData;
      this.rightData = data.rightData;

      // 如果有ECharts图表数据，可以在此处配置主题颜色
      const option = {
        color: this.themeColors,
        textStyle: {
          color: '#ffffff'  // 标题、文字颜色
        },
        title: {
          textStyle: {
            color: '#ffffff'  // 主标题颜色
          },
          subtextStyle: {
            color: '#b0c7e7'  // 副标题颜色
          }
        },
        xAxis: {
          axisLine: {
            lineStyle: {
              color: '#ffffff'  // 坐标轴颜色
            }
          },
          axisLabel: {
            color: '#ffffff'  // 坐标轴标签颜色
          }
        },
        yAxis: {
          axisLine: {
            lineStyle: {
              color: '#ffffff'  // 坐标轴颜色
            }
          },
          axisLabel: {
            color: '#ffffff'  // 坐标轴标签颜色
          },
          splitLine: {
            lineStyle: {
              color: '#ffffff'  // 网格线颜色
            }
          }
        }
      };
      // this.chart.setOption(option);  // 如果你有ECharts图表配置，可以在这里应用option
    },
    updateChart(letter) {
      this.drawChart(letter);
    }
  }
};
</script>
<style scoped>
#main {
  width: 100%;
  height: 100%;
  color: white; /* 统一文字颜色 */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.title {
  font-size: 24px;
  margin-bottom: 10px;
  color: white; /* 标题颜色 */
}

.container {
  display: flex;
  justify-content: space-between;
  width: 80%;
  height: 80%;
}

.left-panel, .right-panel {
  width: 20%; /* 分配合理的宽度 */
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  height: 100%;
}

.info-box {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(255, 255, 255, 0.1);
  padding: 10px;
  border-radius: 10px;
  margin: 10px 0;
  color: white; /* 文字颜色 */
}

.icon {
  width: 40px;
  height: 40px;
}

.central-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 60%; /* 中间容器的宽度 */
  height: 100%;
}

.central-image {
  width: 350px; /* 修正为正确的宽度 */
  height: 300px; /* 根据需要调整高度 */
}

.control-panel {
  margin-top: 20px;
}

.control-panel label {
  font-size: 16px;
  margin-right: 10px;
  color: white; /* 控制面板标签颜色 */
}
</style>
