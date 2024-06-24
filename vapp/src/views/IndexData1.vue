<template>
  <dv-full-screen-container style="background-color:rgb(3,17,43)">
    <dv-border-box-11 title="「地定乾坤」地域导向大屏">
      <div class="grid-container">
        <!-- 第一列 -->
        <div class="column">
          <div class="box box1-1">
              <div class="box column-box">
                <div class="box box1-1-1 decorated-box">
                  <div class="dropdown">
                    <label for="region">请选择地区：</label>
                    <select v-model="selectedLetter">
                    <option v-for="letter in letters" :key="letter" :value="letter">
                     {{ letter }}
                    </option>
                    </select>
                  </div>
                </div>
                <div class="box box1-1-2">
                  <Box1 :selected-letter="selectedLetter"/>
                </div>
              </div>
          </div>
          <div class="box box2-1">
            <Chart8 :selected-letter="selectedLetter"/>
          </div>
          <div class="box box3-1">
              <Chart7 :selected-letter="selectedLetter"/>
          </div>
        </div>
        <!-- 第二列 -->
        <div class="column">
          <div class="box box1-2">
              <Chart2 />
          </div>
          <div class="row-box-low">
            <div class="box box2-2">
                <Chart6 :selected-letter="selectedLetter"/>
            </div>
            <div class="box box3-2">
                <Chart5 :selected-letter="selectedLetter"/>
            </div>
          </div>
        </div>
        <!-- 第三列 -->
        <div class="column">
          <div class="box box1-3">
              <Chart1 />
          </div>
          <div class="row-box-low">
            <div class="box box2-3">
              <Chart3 />
            </div>
            <div class="box box3-3">
              <Chart4 />
            </div>
          </div>
        </div>
      </div>
    </dv-border-box-11>
  </dv-full-screen-container>
</template>

<script>
import Chart1 from "./Chart1.vue";
import Chart2 from "./Chart2.vue";
import Chart3 from "./Chart3.vue";
import Chart4 from "./Chart4.vue";
import Chart5 from "./Chart5.vue";
import Chart6 from "./Chart6.vue";
import Chart7 from "./Chart7.vue";
import Chart8 from "./Chart8.vue";
import Box1 from "./Box1.vue";
export default {
  components: { //注册组件
    Chart1, Chart2, Chart3, Chart4,Chart5,Chart6,Chart7,Chart8,Box1,
  },
  data() {
    return {
      selectedLetter: 'A',
      letters: Array.from(Array(26)).map((e, i) => String.fromCharCode(i + 65)), // A-Z
    };
  },
};
</script>

<style scoped>
.dv-border-box-11 {
        font-weight: bold;
         /* 设置文字加粗 */
    }

.dv-full-screen-container {
  height: 100vh;
  overflow-y: auto;
  z-index: 0;
}

.grid-container {
  display: grid;
  grid-template-columns: 20% 40% 40%; /* 初始三列宽度均分 */
  gap: 10px; /* 控制列间距 */
  padding: 60px;
}

.column {
  display: flex;
  flex-direction: column;
  gap: 5px; /* 控制列内元素间距 */
}

.box1-1 {
  height: 215px;
}

.box1-1-1{
 padding: 10px;
 height: 80px;
}
.box1-1-2{
  padding: 0px;
}
.box2-1 {
  height: 215px;
}
.box3-1 {
  height: 200px;
}

.box1-2 {
  height: 430px;
}
.row-box-low {
  display: flex;
  height: 200px;
}
.box2-2 {
  width: 66%;
}
.box3-2 {
  width: 34%;
}

.box1-3 {
  height: 430px;
}
.box2-3 {
  width: 60%;
}
.box3-3 {
  width: 40%;
}
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
background-color:rgb(3,17,43); /* 设置选项背景色 */
color: white; /* 设置选项文字为白色 */
}

.dropdown select:focus {
background-color: rgba(255, 255, 255, 0.3);
}
</style>
