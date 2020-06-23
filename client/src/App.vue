<template>
  <div>
    <b-navbar>
      <template slot="brand">
        <b-navbar-item tag="router-link" :to="{ path: '/' }">
          <img src="./assets/Arsenal_FC.svg">
          <strong>阿 森 纳 球 员 信 息 查 询 系 统</strong>
        </b-navbar-item>
      </template>
    </b-navbar>

    <router-view/>
  </div>
</template>
