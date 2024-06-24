<template>
  <dv-full-screen-container style="background-color: rgb(3, 17, 43);">
    <dv-border-box-11 title="「职定天下」职位导向大屏">
      <div class="grid-container">
        <!-- 第一列 -->
        <div class="column">
          <div class="box box1-1 decorated-box">
              <div class="dropdown">
                <label for="region">地域大小：</label>
                <select id="region" v-model="region" @change="updateSelection">
                  <option value="1">小</option>
                  <option value="2">中</option>
                  <option value="3">大</option>
                </select>
              </div>
              <div class="dropdown">
                <label for="experience">经验要求选择：</label>
                <select id="experience" v-model="experience" @change="updateSelection">
                  <option value="1">低要求</option>
                  <option value="2">中要求</option>
                  <option value="3">高要求</option>
                </select>
              </div>
              <div class="dropdown">
                <label for="education">学历要求选择：</label>
                <select id="education" v-model="education" @change="updateSelection">
                  <option value="1">低要求</option>
                  <option value="2">中要求</option>
                  <option value="3">高要求</option>
                </select>
              </div>
          </div>
          <div class="box box2-1">
              <Info2 :selectedLetter="selectedLetter" />
          </div>
          <div class="box box3-1">
              <Info3 />
          </div>
        </div>
        <!-- 第二列 -->
        <div class="column">
          <div class="box box1-2">
                <Info1 :selectedLetter="selectedLetter" />
          </div>
          <div class="box box2-2">
            <div class="inner-box-container">
              <div class="inner-box">
                 <Info7 :selectedLetter="prevLetter" />
              </div>
              <div class="inner-box">
                  <Info7 :selectedLetter="selectedLetter" />
              </div>
              <div class="inner-box">
                  <Info7 :selectedLetter="nextLetter" />
              </div>
            </div>
          </div>
        </div>
        <!-- 第三列 -->
        <div class="column">
          <div class="box box1-3">
              <Info4 :selectedLetter="selectedLetter" />
          </div>
          <div class="box box2-3">
              <Info5 :selectedLetter="selectedLetter" />
          </div>
          <div class="box box3-3">
              <Info6 :selectedLetter="selectedLetter" />
          </div>
        </div>
      </div>
    </dv-border-box-11>
  </dv-full-screen-container>
</template>

<script>
import Info1 from "./Info1.vue";
import Info2 from "./Info2.vue";
import Info3 from "./Info3.vue";
import Info4 from "./Info4.vue";
import Info5 from "./Info5.vue";
import Info6 from "./Info6.vue";
import Info7 from "./Info7.vue";

export default {
  data() {
    return {
      region: "3",
      experience: "3",
      education: "3",
      selectedLetter: "大地区高经验高学历",
      prevLetter: "大地区高经验高学历",
      nextLetter: "大地区高经验高学历",
      mapping: {/*no 1-1-1,1-1-3,1-3-1,2-1-1,2-3-1,3-3-1*/
        
        "1-1-2": "小地区低经验中学历",
        
        "1-2-1": "小地区中经验低学历",
        "1-2-2": "小地区中经验中学历",
        "1-2-3": "小地区中经验高学历",
        
        "1-3-2": "小地区高经验中学历",
        "1-3-3": "小地区高经验高学历",
        
        "2-1-2": "中地区低经验中学历",
        "2-1-3": "中地区低经验高学历",
        "2-2-1": "中地区中经验低学历",
        "2-2-2": "中地区中经验中学历",
        "2-2-3": "中地区中经验高学历",
        
        "2-3-2": "中地区高经验中学历",
        "2-3-3": "中地区高经验高学历",
        "3-1-1": "大地区低经验低学历",
        "3-1-2": "大地区低经验中学历",
        "3-1-3": "大地区低经验高学历",
        "3-2-1": "大地区中经验低学历",
        "3-2-2": "大地区中经验中学历",
        "3-2-3": "大地区中经验高学历",
        
        "3-3-2": "大地区高经验中学历",
        "3-3-3": "大地区高经验高学历"
      }
    };
  },
  components: {
    Info1, Info2, Info3, Info4, Info5, Info6, Info7
  },
  methods: {
    updateSelection() {
      const key = `${this.region}-${this.experience}-${this.education}`;
      this.selectedLetter = this.mapping[key];
      this.calculateAdjacentLetters(key);
    },
    calculateAdjacentLetters(key) {
      const keys = Object.keys(this.mapping);
      const currentIndex = keys.indexOf(key);

      if (currentIndex !== -1) {
        this.prevLetter = currentIndex > 0 ? this.mapping[keys[currentIndex - 1]] : this.mapping[keys[keys.length - 1]];
        this.nextLetter = currentIndex < keys.length - 1 ? this.mapping[keys[currentIndex + 1]] : this.mapping[keys[0]];
      }
    }
  },
  mounted() {
    const key = `${this.region}-${this.experience}-${this.education}`;
    this.calculateAdjacentLetters(key);
  }
};
</script>

<style scoped>
.dv-border-box-11 {
font-weight: bold;
}
.dv-full-screen-container {
  height: 100vh;
  overflow-y: auto;
  z-index: 0;
}

.grid-container {
  display: grid;
  grid-template-columns: 25% 50% 25%; /* 调整列宽 */
  column-gap: 10px; /* 控制列间距 */
  padding: 60px;
}

.column {
  display: flex;
  flex-direction: column;
  row-gap: 10px; /* 控制列内元素间距 */
}

.box1-1, .box2-1, .box3-1,
.box1-2 {
  box-sizing: border-box;
  padding: 10px;
}

.box1-1 {
  height: 300px; /* 调整高度适应内容 */
}

.box2-1 {
  height: 210px;
}

.box3-1 {
  height: 180px;
}

.box1-3 {
  height: 240px;
}

.box2-3 {
  height: 200px;
}

.box3-3 {
  height: 170px;
}
.box1-2 {
  height: 395px;
}

.box2-2 {
  display: flex;
  flex-direction: column;
  gap: 10px; /* 控制内元素间距 */
  overflow: visible;
}

.inner-box-container {
  display: flex;
  width: 100%;
  overflow: visible;
}

.inner-box {
  height: 235px;
  flex: 1; /* 等分宽度 */
  box-sizing: border-box;
  overflow: visible;
  z-index: 10;  /* 设置较高的z-index */
}

/* 新增装饰和特效 */
.decorated-box {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 0.5));
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  transition: transform 0.3s;
  padding: 20px; /* 增加内边距 */
  overflow: hidden; /* 防止内容溢出 */
}

.decorated-box:hover {
  transform: translateY(-10px);
}

.dropdown {
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
}

.dropdown label {
  color: white;
  font-weight: bold;
  display: block;
  margin-bottom: 5px;
  max-width: 100%; /* 防止溢出 */
  margin-left: 10px; /* 右移 */
}

.dropdown select {
  width: calc(100% - 20px); /* 调整宽度以防止溢出 */
  padding: 8px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  background-color: rgba(255, 255, 255, 0.2);
  color: white;
  outline: none;
  transition: background-color 0.3s;
  margin-left: 10px; /* 右移 */
  margin-top: 5px; /* 下移 */
}

.dropdown select:hover {
  background-color: rgba(255, 255, 255, 0.3);
}

.dropdown select option {
  background-color: rgb(3,17,43);; /* 设置选项背景为黑色 */
  color: white; /* 设置选项文字为白色 */
}

.dropdown select:focus {
  background-color: rgba(255, 255, 255, 0.3);
}
</style>