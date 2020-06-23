<template>
  <div style="margin: 0 auto;width: 80%">
    <b-tabs type="is-toggle" expanded>
      <b-tab-item label="登录" icon="lock-open">
        <section>
          <b-field label="用户名">
            <b-input v-model="username"></b-input>
          </b-field>

          <b-field label="密码">
            <b-input type="password"
              v-model="password"
              password-reveal
            ></b-input>
          </b-field>

          <div class="has-text-centered">
            <b-button type="is-success">登录</b-button>
          </div>
        </section>
      </b-tab-item>

      <b-tab-item label="注册" icon="account-box">
        <section>
          <b-field label="用户名">
            <b-input v-model="newUsername"></b-input>
          </b-field>

          <b-field label="密码">
            <b-input type="password"
              v-model="newPassword"
              password-reveal
            ></b-input>
          </b-field>

          <div class="has-text-centered">
            <b-button type="is-danger">注册</b-button>
          </div>
        </section>
      </b-tab-item>
    </b-tabs>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      newUsername: '',
      newPassword: ''
    }
  }
}
</script>
