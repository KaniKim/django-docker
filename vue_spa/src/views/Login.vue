<template>
  <div>
    <a id="custom-login-button" @click="kakaoLogin()">
      <img
        src="//k.kakaocdn.net/14/dn/btqCn0WEmI3/nijroPfbpCa4at5EIsjyf0/0.jpg"
        width="222"
      />
    </a>
  </div>
</template>
<script>
methods: {
    kakaoLogin() {
        windows.kakao.Auth.login();
    }
}
</script>