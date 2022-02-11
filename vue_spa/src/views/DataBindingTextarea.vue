<template>
  <div>
    <textarea v-model="message"></textarea>
  </div>
</template>
<script>
export default {
  data() {
    return {
      message: "여러 줄을 입력할 수 있는 textarea입니다.",
    };
  },
};
</script>