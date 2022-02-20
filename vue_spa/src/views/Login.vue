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

methods: {
    kakaoLogin(){
        windows.kakao.Auth.login({
          scope: 'profile, account_email',
          success: this.getKakaoAccount,
        });
    }
    getKakaoAccount(){
      window.Kakao.API.request({
        url: '/v2/user/me',
        success : res => {
          const kakao_account = res.kakao.account;
          const nickname = kakao_account.profile.nickname;
          const email = kakao_account.email
          console.log("nickname", nickname);
          console.log("email", email);
        },
        fail : error => {
          console.log(error)
        }
      })
    }
}